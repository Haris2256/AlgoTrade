from dataclasses import dataclass
from datetime import datetime

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
        net += sum(self.history.market_price(symbol, self.cur_time) for symbol in self.holdings)
        return net