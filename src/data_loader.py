import pandas as pd
from pathlib import Path


def load_us100_csv(path: str | Path) -> pd.DataFrame:
    """Load US100 trading data from a CSV file.

    The CSV is expected to contain at least a `Date` column and OHLCV columns
    such as `Open`, `High`, `Low`, `Close`, and `Volume`.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path, parse_dates=["Date"])
    df.sort_values("Date", inplace=True)
    return df
