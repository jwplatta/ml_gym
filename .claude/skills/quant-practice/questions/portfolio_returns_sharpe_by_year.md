# Portfolio Returns: Sharpe By Year

Portfolio returns. Using the `portfolio` returned in part (3) and the returns generated in part (1), compute the returns to the simple momentum strategy.

Question: What is the annualized Sharpe ratio within each calendar year?

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
sharpe = lambda x: x.mean() / x.std() * np.sqrt(252)
sharpe_by_year = strat_rets.groupby([x.year for x in strat_rets.index]).apply(sharpe)
sharpe_by_year
```
