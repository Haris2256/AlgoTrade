from dataclasses import dataclass
from datetime import datetime

from source.common.history.ahistory import TBILL
from source.common.history.history import History
from source.common.portfolio import Symbol


@dataclass
class State:
    cash: float
    holdings: dict[Symbol, float]
    cur_time: datetime
    history: History

    def net_value(self):
        net: float = self.cash
        for symbol, quantity in self.holdings.items():
            price = self.history.market_price(symbol, self.cur_time)
            net += quantity * price
        return net

    def tbill(self):
        """Returns the price of the T-Bill, i.e. the risk-free rate"""
        return self.history.market_price(TBILL, self.cur_time)