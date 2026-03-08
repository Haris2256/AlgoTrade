from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from pandas import DataFrame

STOCKS_SHEET = Path("../../data/stocks.xlsx")

type Symbol = str

@dataclass
class Holding:
    value: float
    amount: float


def _stock_df() -> DataFrame:
    """Retrieve dataframe containing stock sheet data"""
    return pd.read_excel(STOCKS_SHEET)

def get_holding(symbol: Symbol) -> Holding:
    """Retrieves holding for given stock symbol"""
    df = _stock_df()
    amount, value = df.loc[df['name'] == symbol, ['amount', 'book value']].values[0]
    return Holding(
        value,
        amount
    )




