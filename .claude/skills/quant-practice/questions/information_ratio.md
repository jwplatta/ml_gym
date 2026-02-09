# Compute Information Ratio vs Sharpe Ratio

For each non-benchmark ticker, compute:
1. Information Ratio (IR) from residual returns.
2. Sharpe Ratio (SR) from original returns.

Use annualization with `sqrt(252)` and return a DataFrame with columns `IR` and `SR`.

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
df = pd.DataFrame()
df['IR'] = resid.mean() / resid.std() * np.sqrt(252)
df['SR'] = ret.mean() / ret.std() * np.sqrt(252)
df = df.drop('QQQ')
df
```
