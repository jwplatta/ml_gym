# Calculate Overall Return

Download daily close prices for `SPY` from Yahoo Finance starting on `2020-01-01`.
Compute daily returns, then calculate the overall return for the full sample period.

```python
import yfinance as yf

px = yf.download(['SPY'], start='2020-01-01')['Close']
```

## Solution

```python
ret = px / px.shift() - 1
overall_return = (1 + ret['SPY'].dropna()).prod() - 1
overall_return
```
