import traceback
from datetime import date, timedelta, datetime

from pandas import DataFrame
import yfinance as yf

from source.common.history.history import History, HistoryError
from source.common.portfolio import Symbol


class AHistory(History):
    """Data on a specific set of symbols, during a specific time-frame"""

    def __init__(self, symbols: list[Symbol], start_date: date, end_date: date):
        self.history_data: DataFrame = yf.download(symbols, start=start_date, end=end_date, interval="1h")

    def get_closing_price(self, symbol: Symbol, day: date) -> float:
        """Retrieve the closing price of the given symbol on the given market day"""
        try:
            return self.history_data.loc[self.history_data.asof(datetime.combine(day, datetime.max.time())), "Close"].loc[symbol]
        except KeyError:
            traceback.print_exc()
            raise HistoryError("Error retrieving data, traceback above")

    def prev_market_day(self, day: date) -> date:
        """Gets the most recent valid market day strictly before the given day"""
        prev_day: date = day - timedelta(days=1)
        try:
            return self.history_data.index.asof(datetime.combine(prev_day, datetime.min.time())).date()
        except KeyError:
            raise HistoryError(f"No valid market days before {day}.")

    def pct_change(self, symbol: Symbol, start: datetime, end: datetime) -> float:
        try:
            first_price = self.history_data.loc[start, "Close"].loc[symbol]
            second_price = self.history_data.loc[end.strftime("%Y-%m-%d"), "Close"].loc[symbol]
        except KeyError:
            traceback.print_exc()
            raise HistoryError("Error retrieving data, traceback above")
        return second_price / first_price - 1

    def market_price(self, symbol: Symbol, time: datetime) -> float:
        """Gets the market price of the given symbol on the specified day, at the closest time"""
        try:
            market_price = self.history_data.loc[time, "Close"].loc[symbol]
            return market_price
        except KeyError:
            traceback.print_exc()
            raise HistoryError(f"No market price at {time}")