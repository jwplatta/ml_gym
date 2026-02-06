# Simple Reversal Signal

- "rets" variable below is a DataFrame containing randomly generated, hypothetical daily returns. Rows represent days and columns represent symbols
- Please complete the function "reversal_signal"
- reversal_signal takes as input rets and returns a new DataFrame (signal) which has the same rows/columns as rets. The values of signal are 1 if the symbol had the worst return that day, -1 if it had the best return, and 0 otherwise.
- plot the value of signal through time for "A"

Hint: Try to construct a boolean DataFrame first and then convert it to an integer DataFrame

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
def reversal_signal(rets):
    ranked = rets.rank(1, method='first')
    is_max = (ranked == rets.shape[1]) * 1
    is_min = (ranked == 1) * 1
    signal = is_min - is_max
    return signal

signal = reversal_signal(rets)
axs = signal['A'].plot()
```