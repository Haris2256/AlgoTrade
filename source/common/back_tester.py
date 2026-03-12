import copy
import statistics as stat
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


class BacktestMetrics:
    def __init__(self):
        """Backtesting performance metrics"""
        self.total_pnl: float = 0
        """Final net value / Initial net value"""
        self.sharpe_ratio: float = 0
        """Sharpe ratio"""
        self.states: list[State] = []

    @staticmethod
    def _calculate_total_pnl(pre: State, post: State) -> float:
        return post.net_value() / pre.net_value()

    def add_state(self, state: State):
        self.states.append(state)

    def _calculate_sharpe_ratio(self) -> float:
        returns: list[(float,float)]  =[]
        for state in self.states:
            returns.append((state.net_value(), state.tbill()))
        prev_net_value, prev_risk_free_rate = returns[0]
        excess_returns: list[float] = []
        for (net_value, risk_free) in returns[1:]:
            curr_return = net_value / prev_net_value - 1
            curr_risk_free_rate = risk_free / prev_risk_free_rate - 1
            excess_return = curr_return - curr_risk_free_rate
            excess_returns.append(excess_return)
        standard_deviation_excess = stat.stdev(excess_returns)
        mean_excess_return = sum(excess_returns) / len(excess_returns)
        sharpe_daily = mean_excess_return / standard_deviation_excess if standard_deviation_excess != 0 else 0
        return sharpe_daily * (252 ** 0.5)

    def performance_metrics(self, pre: State, post: State):
        """Calculates performance metrics based on performance from 'pre' to 'post'"""
        self.total_pnl = self._calculate_total_pnl(pre, post)
        self.sharpe_ratio = self._calculate_sharpe_ratio()


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
        state = copy.deepcopy(initial_state)

        step_count: int = 0
        metrics = BacktestMetrics()
        for t in timestamps:
            step_count += 1

            state.cur_time = t
            self._handle_actions(bot.act(state), state)
            metrics.add_state(copy.deepcopy(state))

        metrics.performance_metrics(initial_state, state)
        print(f"Ran backtest over {step_count} steps, interval: {self._interval.value}")
        print(f"Initial net: {initial_state.net_value()}")
        print(f"Final net: {state.net_value()}")
        print(f"Total P&L: {round((metrics.total_pnl - 1) * 100, 2)}%")
        print(f"Sharpe Ratio {metrics.sharpe_ratio}")


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
            raise InvalidActionError(f"Insufficient holdings to perform sell action {sell}")

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

    bot2 = SNP500()
    back_tester.run(bot2, 100000, {"VOO": 0})


if __name__ == "__main__":
    _main()