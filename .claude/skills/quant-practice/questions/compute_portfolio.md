# Compute Portfolio

Create a portfolio. Complete the function compute_portfolio. This function takes as input the DataFrame "momentum" from above. It returns a new DataFrame "portfolio" which has the same index/columns and has as values portfolio weights. The weights are computed as follows. On each date, equal-weight long the tickers with a momentum signal above 1.

## Setup

```python
import yfinance as yf
import math

data = yf.download(['QQQ', 'TLT', 'GLD', 'RWO'], start='2020-01-01')

adj_close = data['Close']
ret = adj_close / adj_close.shift() - 1

momentum = ret.rolling(252).mean() / ret.rolling(252).std() * math.sqrt(252)
```

## Solution

```python
def compute_portfolio(momentum):
    # fill out the body here
    # return a DataFrame "portfolio" containing portfolio weights
    port = (momentum > 1) * 1
    portfolio = port.div(port.abs().sum(1), 0)

    return portfolio

portfolio = compute_portfolio(momentum)
```
