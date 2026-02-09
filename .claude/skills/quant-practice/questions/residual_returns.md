# Calculate Residual Returns

Using the rolling beta to `QQQ`, compute the daily residual return (alpha) for each ticker:
`resid = ret - beta * ret_QQQ`.

## Setup

```python
import yfinance as yf

px = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOGL', 'QQQ'], start='2016-01-01')['Close']
ret = px / px.shift() - 1

corr = ret.rolling(252).corr(ret['QQQ'])
vol = ret.rolling(252).std()
beta = (corr * vol).div(vol['QQQ'], axis=0)
```

## Solution

```python
resid = ret - beta.multiply(ret['QQQ'], axis=0)
resid
```
