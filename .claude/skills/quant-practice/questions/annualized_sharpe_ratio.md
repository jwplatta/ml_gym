# Compute Annualized Sharpe Ratio

Compute the signal. Complete the compute_momentum function which computes a simple momentum signal. The function takes in a DataFrame with index = date, columns=ticker and values containing daily returns. It returns a new DataFrame with index = date, columns=ticker and values containing the momentum signal for the ticker on that day. The momentum signal for each ticker is defined as the **annualized sharpe ratio** of the past 252 days.

## Setup
```python
import yfinance as yf
data = yf.download(['QQQ', 'TLT', 'GLD', 'RWO'], start='2020-01-01')

adj_close = data['Close']
ret = adj_close / adj_close.shift() - 1

def compute_momentum(ret):
    momentum = None
    return momentum
```

## Solution

```python
def compute_momentum(ret):
    momentum = ret.rolling(252).mean() / ret.rolling(252).std() * math.sqrt(252)
    return momentum

momentum = compute_momentum(ret)
```