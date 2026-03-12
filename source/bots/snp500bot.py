from datetime import date, datetime

from dateutil.relativedelta import relativedelta

from source.bots.bot import Bot
from source.common.action import Action, Sell, Buy
from source.common.history.ahistory import AHistory
from source.common.history.history import HistoryError
from source.common.portfolio import Symbol
from source.common.state import State
from source.deprecated import variables

SNP500_STOCK = "VOO"

class SNP500(Bot):
    def __init__(self):
        super().__init__()

    def act(self, state: State) -> list[Action]:
        actions: list[Action] = []

        for symbol, quantity in state.holdings.items():
            if symbol != SNP500_STOCK:
                actions.append(Sell(symbol, quantity))

        quantity = state.cash / state.history.market_price(SNP500_STOCK, state.cur_time)
        actions.append(Buy(SNP500_STOCK, quantity))
        return actions


