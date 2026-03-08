import traceback
from datetime import date, timedelta

from pandas import DataFrame
import yfinance as yf

from source.common.history.history import History, HistoryError
from source.common.portfolio import Symbol


class AHistory(History):
    """Data on a specific set of symbols, during a specific time-frame"""

    def __init__(self, symbols: list[Symbol], start_date: date, end_date: date):
        self.history_data: DataFrame = yf.download(symbols, start=start_date, end=end_date)

    def get_closing_price(self, symbol: Symbol, day: date) -> float:
        """Retrieve the closing price of the given symbol on the given market day"""
        try:
            return self.history_data.loc[day.strftime("%Y-%m-%d"), "Close"].loc[symbol]
        except KeyError:
            traceback.print_exc()
            raise HistoryError("Error retrieving data, traceback above")

    def prev_market_day(self, day: date) -> date:
        """Gets the most recent valid market day strictly before the given day"""
        prev_day: date = day - timedelta(days=1)
        try:
            return self.history_data.index.asof(prev_day.strftime("%Y-%m-%d")).date()
        except KeyError:
            raise HistoryError(f"No valid market days before {day}.")

    def pct_change(self, symbol: Symbol, first_day: date, second_day: date) -> float:
        try:
            first_price = self.history_data.loc[first_day.strftime("%Y-%m-%d"), "Close"].loc[symbol]
            second_price = self.history_data.loc[second_day.strftime("%Y-%m-%d"), "Close"].loc[symbol]
        except KeyError:
            traceback.print_exc()
            raise HistoryError("Error retrieving data, traceback above")
        return second_price / first_price - 1

