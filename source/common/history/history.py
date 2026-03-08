from abc import ABC, abstractmethod
from datetime import date, datetime
from typing import Any

import yfinance as yf
from pandas import DataFrame

from source.common.portfolio import Symbol

class HistoryError(Exception):
    """Error encountered when retrieving history data"""
    pass

class History(ABC):
    """History of security data"""
    @abstractmethod
    def get_closing_price(self, symbol: Symbol, day: date) -> float:
        """Retrieves the closing price of a given symbol on a given day"""
        pass

    @abstractmethod
    def prev_market_day(self, day: date) -> date:
        """Retrieves the most recent valid market day strictly before the given day, assuming there is one."""
        pass

    @abstractmethod
    def pct_change(self, symbol: Symbol, first_day: date, second_day: date) -> float:
        """Retrieves the change in price of a given symbol between two dates"""
        pass