
from source.common.action import Action, Buy, Sell
from source.common.history.ahistory import AHistory
from source.common.portfolio import Symbol, Holding
from source.deprecated import variables
from source.bots import bot
from source.bots import dumbass
from datetime import datetime
from source.common.state import State

start_date = "2020-07-03"
end_date = "2025-08-05"
date_format = variables.date_format

start = datetime.strptime(start_date, date_format)
end = datetime.strptime(end_date, date_format)

num_days = (end - start).days
money = 100000

b = dumbass.Dumbass()

holdings: dict[Symbol, Holding] = {}
history = AHistory(["AAPL"], start, end)
state = State(money, {}, start, history)


def _handle_buy(buy: Buy, state: State) -> None:
    """Handles the 'buy' action"""
    try:
        cur_price = history.market_price(Buy.symbol, State.cur_time)
    except KeyError:
        raise f"Security not found in history: {buy.symbol}"
    if state.cash >= buy.amount * cur_price:
        try:
            holdings[buy.symbol].amount += buy.amount
            # change value?
        except KeyError:
            raise f"Security not found in holdings: {buy.symbol}"
    else: # Is raising in an else ok...
        raise f"Not enough cash to buy {buy.symbol} (Have: {state.cash}, Need: {buy.amount * cur_price})"

def _handle_sell(sell: Sell, state: State) -> None:
    try:
        cur_amount = state.holdings[sell.symbol].amount
    except KeyError:
        raise f"Security not found in holdings: {sell.symbol}"
    if cur_amount > sell.amount :
        holdings[sell.symbol].amount -= sell.amount
        # change holding.value?
    else:
        raise f"Not enough money ({State.cash}) to buy {Buy.symbol}"


def _handle_action(a: Action, state: State) -> None:
    """Executes the given action, if possible"""
    if isinstance(a, Buy):
        _handle_buy(a, state)
    elif isinstance (a, Sell):
        _handle_sell(a, state)
for i in range (num_days):

    actions = b.act(state)
    for action in actions:
        _handle_action(action, state)

print(_handle_buy((Buy("AAPL", 5)), State(1000,["AAPL", Holding(20, 20)], datetime(2020, 1, 1))))