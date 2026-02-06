# Performance Stats
- "rets" variable below is a DataFrame containing randomly generated, hypothetical daily returns. Rows represent days and columns represent symbols.
- Please complete the function "compute_stats".
- compute_stats takes as input rets and returns a new DataFrame (stats) containing performance stats as specified below. rows of the result should be symbols and columns the performance stat label.
    1. "avg": average return (annualized)
    2. "vol": volatility (annualized)
    3. "sharpe": sharpe ratio (annualzied)
    4. "hit_rate": percent of returns which are positive
- Plot the sharpe ratios in "stats" in ascending order.

```python
import numpy as np
import pandas as pd

np.random.seed(5)
rets = np.random.normal(0.05/252,0.1/np.sqrt(252), (1000,5))
columns = ['A','B','C','D','E']
rets = pd.DataFrame(rets,columns = columns)
```

## Solution
```python
def compute_stats(rets):
    # fill out the body here
    # return a DataFrame "stats"
    # columns should be performance stat label
    # rows should be symbols
    stats = pd.DataFrame()
    stats['avg'] = rets.mean() * 252
    stats['vol'] = rets.std() * np.sqrt(252)
    stats['sharpe'] = stats['avg'] / stats['vol']
    stats['hit_rate'] = (rets > 0).sum() / rets.count()
    return stats

stats = compute_stats(rets)
stats['sharpe'].sort_values().plot(kind='bar')
```