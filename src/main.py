from pathlib import Path

import pandas as pd

from .data_loader import load_us100_csv
from .analyzer import add_moving_averages
from .strategy import moving_average_crossover_signals


def run_strategy(data_path: str | Path) -> pd.DataFrame:
    df = load_us100_csv(data_path)
    df = add_moving_averages(df)
    df["Signal"] = moving_average_crossover_signals(df)
    return df


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Run simple US100 trading strategy")
    parser.add_argument("data", help="Path to US100 CSV data file")
    parser.add_argument("--output", help="Path to save results", default="signals.csv")
    args = parser.parse_args()

    result = run_strategy(args.data)
    result.to_csv(args.output, index=False)
    print(f"Signals saved to {args.output}")


if __name__ == "__main__":
    main()
