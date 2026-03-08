from datetime import datetime


def yf_datetime_format(dt: datetime) -> str:
    return dt.strftime("%Y-$m-")