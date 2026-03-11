from datetime import date, datetime

from dateutil.relativedelta import relativedelta

from source.bots.bot import Bot
from source.common.action import Action, Sell, Buy
from source.common.history.ahistory import AHistory
from source.common.history.history import HistoryError
from source.common.portfolio import Symbol
from source.common.state import State
from source.deprecated import variables

APPLE_STOCK: Symbol = "AAPL"

class Dumbass(Bot):
    def __init__(self):
        super().__init__()

    def act(self, state: State) -> list[Action]:
        try:
            owned: float = state.holdings[APPLE_STOCK]
        except KeyError:
            owned: float = 0

        actions: list[Action] = []

        cur_date = state.cur_time.date()
        try:
            prev_date = state.history.prev_market_day(cur_date)
            pct_change = state.history.pct_change(APPLE_STOCK, prev_date, cur_date)
        except HistoryError:
            pct_change = 0

        print(pct_change)
        if pct_change >= 2:
            actions.append(Sell(APPLE_STOCK, owned))
        elif pct_change <= 0.1:
            actions.append(Buy(APPLE_STOCK, 1))

        return actions


# state = State(
#     1000,
#     {},
#     datetime(2025, 1, 16),
#     AHistory(["AAPL"], date(2025,1,1), date(2025,1,31))
# )
# dumbass = Dumbass()
# print(dumbass.act(state))
