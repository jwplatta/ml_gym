# Compare Strategy Sharpes

Using the same momentum signal style from Homework 3, build two simple long-only strategies and compare their annualized Sharpe ratios:
1. `Strategy_A`: equal-weight long tickers with `momentum > 1.0`
2. `Strategy_B`: equal-weight long tickers with `momentum > 0.0`

Then identify which strategy has the better risk-adjusted return.

## Setup

```python
import numpy as np
import yfinance as yf

data = yf.download(['QQQ', 'TLT', 'GLD', 'RWO'], start='2020-01-01')
adj_close = data['Close']
ret = adj_close / adj_close.shift() - 1

momentum = ret.rolling(252).mean() / ret.rolling(252).std() * np.sqrt(252)
```

## Solution

```python
port_a = (momentum > 1.0) * 1
port_a = port_a.div(port_a.abs().sum(1), 0)

port_b = (momentum > 0.0) * 1
port_b = port_b.div(port_b.abs().sum(1), 0)

strat_a = (port_a.shift() * ret).sum(1)
strat_b = (port_b.shift() * ret).sum(1)

start_dt = momentum.dropna().index[0]
strat_a = strat_a.loc[start_dt:]
strat_b = strat_b.loc[start_dt:]

sharpe_a = strat_a.mean() / strat_a.std() * np.sqrt(252)
sharpe_b = strat_b.mean() / strat_b.std() * np.sqrt(252)

sharpes = {
    'Strategy_A': float(sharpe_a),
    'Strategy_B': float(sharpe_b),
}
best_strategy = max(sharpes, key=sharpes.get)

sharpes, best_strategy
```
