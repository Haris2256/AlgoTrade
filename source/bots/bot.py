from abc import ABC, abstractmethod

from source.common.action import Action, Sell, Buy
from source.common.state import State
from source.deprecated import variables
from dateutil.relativedelta import relativedelta

watchlist = variables.watchlist_sheet


class Bot(ABC):
    @abstractmethod
    def act(self, state: State):
        """Subclasses must implement this method"""
        pass
