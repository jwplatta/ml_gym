# Perform Regression on SPY

Download daily close price data for SPY and META from Yahoo Finance since 2016-01-01.

```python
import yfinance as yf
px = yf.download(['SPY', 'META'], start='2016-01-01')['Close']
```

## Easy Difficulty
Compute daily returns and run a linear regression of META returns on SPY returns using scikit-learn. Include an intercept. Report the intercept (alpha), SPY coefficient (beta).

## Medium Difficulty
Also compute compute residuals.

## Hard Difficulty
Also compute the mean of residuals, the information ratio (mean / std * sqrt(252)), and the correlation of residuals with SPY returns.

## Solution
```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

ret = px / px.shift() - 1

data = ret[['SPY', 'META']].dropna()
X = data[['SPY']]
Y = data['META']

model = LinearRegression(fit_intercept=True)
model.fit(X, Y)

alpha = float(model.intercept_)
beta = float(model.coef_[0])

# residuals
pred = pd.Series(model.predict(X), index=X.index)
resid = Y - pred

# mean residuals
resid_mean = float(resid.mean())
resid_ir = float(resid.mean() / resid.std() * np.sqrt(252))
resid_corr = float(resid.corr(X['SPY']))

# all solutions
alpha, beta, resid_mean, resid_ir, resid_corr
```
