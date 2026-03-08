from dataclasses import dataclass
from datetime import datetime

from source.common.history.history import History
from source.common.portfolio import Holding, Symbol


@dataclass
class State:
    cash: float
    holdings: dict[Symbol, Holding]
    cur_time: datetime
    history: History
    # add stock history