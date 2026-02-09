# Compute Rolling Correlation, Volatility, and Beta

Using daily returns for `META`, `AAPL`, `AMZN`, `NFLX`, `GOOGL`, and `QQQ`, compute:
1. The 252-day rolling correlation of each ticker to `QQQ`.
2. The 252-day rolling beta of each ticker to `QQQ` using: `beta = corr * vol_ticker / vol_QQQ`.

## Setup

```python
import yfinance as yf

px = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOGL', 'QQQ'], start='2016-01-01')['Close']
ret = px / px.shift() - 1
```

## Solution

```python
corr = ret.rolling(252).corr(ret['QQQ'])
vol = ret.rolling(252).std()
beta = (corr * vol).div(vol['QQQ'], axis=0)

corr, beta
```
