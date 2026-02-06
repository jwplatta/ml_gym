# Compute Portfolio Returns

Portfolio returns. Using the "portfolio" returned in part(3) and the returns generated in part(1), compute the returns to the simple momentum strategy.
- What is the annualized sharpe ratio of the strategy?
- How about the annualized sharpe ratio within each year?
- How correlated is the strategy with the underlying tickers?
- Plot the cumulative sum of the returns through time

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
```

## Solution

```python
strat_rets = (portfolio.shift() * ret).sum(1)
strat_rets = strat_rets.loc[momentum.dropna().index[0]:]

# NOTE: overall sharpe ratio
strat_rets.mean() / strat_rets.std() * np.sqrt(252)

# NOTE: sharpe by year
sharpe = lambda x: x.mean() / x.std() * np.sqrt(252)
strat_rets.groupby([x.year for x in strat_rets.index]).apply(sharpe)

# NOTE: correlation of strategy with underlying tickers
axs = ret.corrwith(strat_rets).plot(kind='bar')

# NOTE: plot of cumulative returns
axs = strat_rets.cumsum().plot()
```