import traceback
from datetime import date, timedelta, datetime
from enum import Enum
from typing import Generator

import pandas as pd
from pandas import DataFrame
import yfinance as yf

from source.common import pd_utils
from source.common.history.history import History, HistoryError
from source.common.portfolio import Symbol


class Interval(Enum):
    """Security data time interval"""
    ONE_MINUTE = "1m"
    TWO_MINUTES = "2m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    SIXTY_MINUTES = "60m"
    NINETY_MINUTES = "90m"
    ONE_HOUR = "1h"
    ONE_DAY = "1d"
    FIVE_DAYS = "5d"
    ONE_WEEK = "1wk"
    ONE_MONTH = "1mo"
    THREE_MONTHS = "3mo"

TBILL: str = "^IRX"
class AHistory(History):
    """Data on a specific set of symbols, during a specific time-frame"""

    def __init__(self, symbols: list[Symbol], start_date: date, end_date: date, interval: Interval = Interval.ONE_DAY):
        symbols.append(TBILL)
        self.history_data: DataFrame = yf.download(set(symbols), start=start_date, end=end_date, interval=interval.value)
        pd_utils.normalize_dt_index(self.history_data)


    def prev_market_day(self, day: date) -> date:
        prev_day: date = day - timedelta(days=1)
        try:
            return self.history_data.index.asof(datetime.combine(prev_day, datetime.min.time())).date()
        except KeyError:
            raise HistoryError(f"No valid market days before {day}.")

    def pct_change(self, symbol: Symbol, start: datetime, end: datetime) -> float:
        try:
            first_price = self.history_data.loc[pd.Timestamp(start), "Close"].loc[symbol]
            second_price = self.history_data.loc[pd.Timestamp(end), "Close"].loc[symbol]
        except KeyError:
            raise HistoryError(f"Failed to fetch data, {symbol} at times {start}, {end}")
        return (second_price / first_price - 1) * 100

    def market_price(self, symbol: Symbol, timestamp: datetime) -> float:
        try:
            market_price = self.history_data.loc[timestamp, "Close"].loc[symbol]
            return market_price
        except KeyError:
            raise HistoryError(f"Failed to fetch data, {symbol} at time {timestamp}")

    def get_timestamps(self) -> Generator[datetime, None, None]:
        for timestamp, _ in self.history_data.iterrows():
            yield timestamp.to_pydatetime()

    def first_timestamp(self) -> datetime:
        return self.history_data.index[0].to_pydatetime()


def _main():
    ah = AHistory(["AAPL"], date(2025,1,1), date(2025,12,31))
    print('\n'.join(str(v) for v in list(ah.get_timestamps())))

if __name__ == "__main__":
    _main()