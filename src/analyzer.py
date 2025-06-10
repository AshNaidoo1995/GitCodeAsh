import pandas as pd


def add_moving_averages(df: pd.DataFrame, windows=(20, 50)) -> pd.DataFrame:
    """Return a new DataFrame with moving average columns."""
    result = df.copy()
    for window in windows:
        result[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
    return result
