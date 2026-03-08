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
    if state.cash <= buy.amount * state.cur_time
    try:
        holdings[buy.symbol] += buy.amount
    except KeyError:
        holdings[buy.symbol] = buy.amount

def _handle_sell(sell: Sell) -> None:
    try:
        holdings[sell.symbol] -= sell.amount
    except KeyError:


def _handle_action(a: Action) -> None:
    """Executes the given action, if possible"""
    if isinstance(a, Buy):

    elif isinstance (a, Sell):

for i in range (num_days):

    actions = b.act(state)
    for action in actions:
        _handle_action(action)