# Portfolio Returns: Correlation With Tickers

Portfolio returns. Using the `portfolio` returned in part (3) and the returns generated in part (1), compute the returns to the simple momentum strategy.

Question: How correlated is the strategy return series with the underlying tickers?

## Setup

```python
import yfinance as yf
import numpy as np

data = yf.download(['QQQ', 'TLT', 'GLD', 'RWO'], start='2020-01-01')

adj_close = data['Close']
ret = adj_close / adj_close.shift() - 1

momentum = ret.rolling(252).mean() / ret.rolling(252).std() * np.sqrt(252)

port = (momentum > 1) * 1
portfolio = port.div(port.abs().sum(1), 0)

strat_rets = (portfolio.shift() * ret).sum(1)
strat_rets = strat_rets.loc[momentum.dropna().index[0]:]
```

## Solution

```python
ret.corrwith(strat_rets)
```
