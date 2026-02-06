# Compute Drawdowns and Durations

Download daily close prices for `TSLA` and `SPY` from Yahoo Finance starting on `2021-01-01`.
Compute each asset's drawdown series, where drawdown is defined as:

`drawdown_t = price_t / running_max_t - 1`

Then compute:
1. The full drawdown time series for both tickers.
2. The worst (most negative) drawdown for each ticker.
3. The drawdown duration series (number of consecutive days since last peak), and the maximum duration for each ticker.

```python
import yfinance as yf
px = yf.download(['TSLA', 'SPY'], start='2021-01-01')['Close']
```

## Solution

```python
import pandas as pd


def drawdown(px: pd.DataFrame) -> pd.DataFrame:
    running_max = px.expanding(min_periods=1).max()
    return px / running_max - 1


def duration(px: pd.DataFrame) -> pd.DataFrame:
    peak = px.expanding(min_periods=1).max()
    res = pd.DataFrame(index=px.index, columns=px.columns, dtype=float)

    for col in px.columns:
        for i, dt in enumerate(px.index):
            if px.loc[dt, col] >= peak.loc[dt, col]:
                res.loc[dt, col] = 0
            else:
                res.loc[dt, col] = 1 if i == 0 else res.iloc[i - 1][col] + 1

    return res


dd = drawdown(px)
worst_dd = dd.min()

ddd = duration(px)
max_duration = ddd.max()

dd, worst_dd, ddd, max_duration
```
