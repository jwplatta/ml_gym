# Compute Daily Returns

Download daily price data for QQQ, TLT, GLD, RWO from yahoo finance since 2016-01-01. Using the adjusted close price data, compute daily returns. This should be a DataFrame with index=date, columns=ticker and values=daily returns.

```python
import yfinance as yf
data = yf.download(['QQQ', 'TLT', 'GLD', 'RWO'], start='2020-01-01')
```

## Solution

```python
adj_close = data['Close']
ret = adj_close / adj_close.shift() - 1
```