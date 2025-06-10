import pandas as pd


def moving_average_crossover_signals(df: pd.DataFrame) -> pd.Series:
    """Generate trading signals based on moving average crossover."""
    signals = pd.Series(index=df.index, dtype="object")
    above = df["MA_20"] > df["MA_50"]
    signals[above & (~above.shift(1, fill_value=False))] = "buy"
    signals[(~above) & above.shift(1, fill_value=False)] = "sell"
    return signals
