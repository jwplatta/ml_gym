# Compare Returns and Residual Returns

Compare original returns vs residual returns for non-benchmark tickers:
1. Compute annualized volatility for each (`orig`, `resid`).
2. Compute correlation matrices for original returns and residual returns.

## Setup

```python
import numpy as np
import pandas as pd
import yfinance as yf

px = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOGL', 'QQQ'], start='2016-01-01')['Close']
ret = px / px.shift() - 1

corr = ret.rolling(252).corr(ret['QQQ'])
vol = ret.rolling(252).std()
beta = (corr * vol).div(vol['QQQ'], axis=0)
resid = ret - beta.multiply(ret['QQQ'], axis=0)
```

## Solution

```python
vol_compare = pd.DataFrame({
    'orig': ret.std() * np.sqrt(252),
    'resid': resid.std() * np.sqrt(252),
}).drop('QQQ')

orig_corr = ret.drop(columns='QQQ').corr()
resid_corr = resid.drop(columns='QQQ').corr()

vol_compare, orig_corr, resid_corr
```
