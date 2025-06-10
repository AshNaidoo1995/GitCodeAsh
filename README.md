# GitCodeAsh

This project demonstrates a simple US100 trading strategy based on moving
average crossovers. It expects a CSV file containing historical US100 data
and produces buy/sell signals.

## Usage

1. Place a CSV file containing US100 price data on disk. The file should
   include columns: `Date`, `Open`, `High`, `Low`, `Close`, and `Volume`.
2. Run the strategy:

```bash
python -m src.main path/to/us100.csv --output signals.csv
```

The resulting `signals.csv` will contain the original data with additional
moving average columns and a `Signal` column indicating `buy` or `sell`
actions.
