from abc import ABC, abstractmethod
from datetime import date, datetime
from typing import Any, Generator

import yfinance as yf
from pandas import DataFrame

from source.common.portfolio import Symbol

class HistoryError(Exception):
    """Error encountered when retrieving history data"""
    pass

class History(ABC):
    """History of security data"""

    @abstractmethod
    def prev_market_day(self, day: date) -> date:
        """Retrieves the most recent valid market day strictly before the given day, assuming there is one."""
        pass

    @abstractmethod
    def pct_change(self, symbol: Symbol, start: datetime, end: datetime) -> float:
        """Retrieves the change in price of a given symbol between two timestamps"""
        pass

    @abstractmethod
    def market_price(self, symbol: Symbol, timestamp: datetime) -> float:
        """Retrieves the symbol's market price at the given time"""
        pass

    @abstractmethod
    def get_timestamps(self) -> Generator[datetime, None, None]:
        """A generator that iterates over all contained timestamps"""
        pass

    @abstractmethod
    def first_timestamp(self) -> datetime:
        """Retrieves the earliest timestamp"""