from datetime import datetime

import pandas as pd


def normalize_dt_index(df: pd.DataFrame) -> None:
    """Normalizes indices of a dataframe such that it can be indexed with pd.Timestamp. Assumes the current index is convertible to pd.Timestamp"""
    if not isinstance(df.index[0], pd.Timestamp):
        df.index = pd.to_datetime(df.index)


