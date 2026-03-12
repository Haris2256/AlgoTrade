import copy
from dataclasses import dataclass

from source.bots.bot import Bot
from source.bots.dumbass import Dumbass
from source.bots.snp500bot import SNP500
from source.common.action import Action, Buy, Sell
from source.common.history.ahistory import AHistory, Interval
from source.common.history.history import History, HistoryError
from source.common.portfolio import Symbol
from source.deprecated import variables
from source.bots import dumbass
from datetime import datetime, date
from source.common.state import State

class InvalidActionError(Exception):
    pass

@dataclass
class BacktestMetrics:
    """Backtesting performance metrics"""
    total_pnl: float
    """Final net value / Initial net value"""

class BackTester:
    """Backtests a bot over a defined time period"""

    def __init__(self, start_date: date, end_date: date, interval: Interval = Interval.ONE_DAY):
        self._start_date = start_date
        """Backtest start date"""
        self._end_date = end_date
        """Backtest end date"""
        self._interval = interval
        """Time interval between bot actions during the backtest"""


    def run(self, bot: Bot, cash: float, holdings: dict[Symbol, float]):
        """Backtests the given bot"""
        history = AHistory(list(holdings.keys()), self._start_date, self._end_date, self._interval)
        timestamps = history.get_timestamps()
        initial_state = State(cash, holdings.copy(), history.first_timestamp(), history)
        state = copy.copy(initial_state)

        step_count: int = 0
        for t in timestamps:
            step_count += 1

            state.cur_time = t
            self._handle_actions(bot.act(state), state)

        metrics = self._performance_metrics(initial_state, state)
        print(f"Ran backtest over {step_count} steps, interval: {self._interval.value}")
        print(f"Initial net: {initial_state.net_value()}")
        print(f"Final net: {state.net_value()}")
        print(f"Total P&L: {round((metrics.total_pnl - 1) * 100, 2)}%")


    @staticmethod
    def _performance_metrics(pre: State, post: State) -> BacktestMetrics:
        """Calculates performance metrics based on performance from 'pre' to 'post'"""
        total_pnl: float = post.net_value() / pre.net_value()
        return BacktestMetrics(
            total_pnl=total_pnl
        )


    @staticmethod
    def _handle_buy(buy: Buy, state: State) -> None:
        """Handles the 'buy' action"""
        try:
            cur_price = state.history.market_price(buy.symbol, state.cur_time)
        except HistoryError as e:
            raise InvalidActionError(repr(e))

        value = cur_price * buy.amount
        if not state.cash >= value:
            raise InvalidActionError(f"Insufficient cash to perform buy action {Buy}")

        state.cash -= value
        try:
            state.holdings[buy.symbol] += buy.amount
        except KeyError:
            state.holdings[buy.symbol] = buy.amount


    @staticmethod
    def _handle_sell(sell: Sell, state: State) -> None:
        if not sell.symbol in state.holdings and state.holdings[sell.symbol] > sell.amount:
            raise InvalidActionError(f"Insufficient holdings to perform sell action {Sell}")

        try:
            cur_price = state.history.market_price(sell.symbol, state.cur_time)
        except HistoryError as e:
            raise InvalidActionError(repr(e))

        state.cash += cur_price * sell.amount
        state.holdings[sell.symbol] -= sell.amount


    @staticmethod
    def _handle_actions(actions: list[Action], state: State) -> None:
        """Executes the given action, if possible"""
        for a in actions:
            if isinstance(a, Buy):
                BackTester._handle_buy(a, state)
            elif isinstance (a, Sell):
                BackTester._handle_sell(a, state)


def _main():
    bot = Dumbass()
    back_tester = BackTester(date(2025,1,1), date(2025,12,31))
    back_tester.run(bot, 100000, {"AAPL": 0})

    bot = SNP500()
    back_tester.run(bot, 100000, {"VOO": 0})


if __name__ == "__main__":
    _main()