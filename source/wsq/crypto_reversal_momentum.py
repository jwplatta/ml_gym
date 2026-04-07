"""
Reversal / Momentum - Time Horizon Analysis

This script explores how reversal tends to exist at shorter horizons and momentum
at longer horizons using 4-hour cryptocurrency price data.

Objectives:
1. Generate rank-demeaned-normalized cross-sectional reversal strategies at
   4, 8, 12, 16, 20, and 24 hour frequencies (horizons 1-6 in units of 4h bars)
2. For each strategy, use the average return over the lookback period to rank assets
3. Compute Sharpe ratios to identify which horizons exhibit reversal vs. momentum
4. Test a lagged version that skips the first bar to strengthen momentum signals

Key Concepts:
- Reversal: Assets that performed poorly tend to outperform (negative autocorrelation)
- Momentum: Assets that performed well continue to outperform (positive autocorrelation)
- Rank-demean-normalize: Rank assets by returns, subtract mean rank, normalize by sum of absolute weights
"""

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from binance.client import Client as bnb_client

# Initialize Binance client
# Note: Use tld='US' for US-based users to access Binance.US API
#client = bnb_client()
client = bnb_client(tld='US')

def get_binance_px(symbol, freq, start_ts='2020-01-01', end_ts='2022-12-31'):
    """
    Download historical OHLCV (Open, High, Low, Close, Volume) data from Binance.

    Parameters
    ----------
    symbol : str
        Trading pair symbol (e.g., 'BTCUSDT')
    freq : str
        Frequency/timeframe for candles (e.g., '4h' for 4-hour bars)
    start_ts : str
        Start date in 'YYYY-MM-DD' format
    end_ts : str
        End date in 'YYYY-MM-DD' format

    Returns
    -------
    pd.DataFrame
        DataFrame with OHLCV data indexed by open_time
    """
    # Fetch historical klines (candlestick) data from Binance API
    data = client.get_historical_klines(symbol, freq, start_ts, end_ts)

    # Define column names matching Binance API response structure
    columns = [
        'open_time', 'open', 'high',
        'low', 'close', 'volume',
        'close_time', 'quote_volume',
        'num_trades', 'taker_base_volume',
        'taker_quote_volume', 'ignore'
    ]

    data = pd.DataFrame(data, columns=columns)

    # Convert timestamps from POSIX milliseconds to datetime objects
    data['open_time'] = data['open_time'].map(lambda x: datetime.utcfromtimestamp(x/1000))
    data['close_time'] = data['close_time'].map(lambda x: datetime.utcfromtimestamp(x/1000))
    return data

# ============================================================================
# DATA DOWNLOAD AND PREPARATION
# ============================================================================

# Define the cryptocurrency universe (7 major cryptocurrencies vs USDT)
univ = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'BNBUSDT', 'XRPUSDT', 'DOTUSDT', 'MATICUSDT']

# Set frequency to 4-hour bars
freq = '4h'

# Download price data for each symbol
px = {}
for x in univ:
    data = get_binance_px(x, freq)
    # Extract only the closing price and index by open_time
    px[x] = data.set_index('open_time')['close']

# Combine into a single DataFrame with symbols as columns
px = pd.DataFrame(px).astype(float)

# Ensure regular time series (fill any gaps in the time index)
px = px.reindex(pd.date_range(px.index[0], px.index[-1], freq=freq))

# Compute 4-hour returns: ret[t] = (px[t] - px[t-1]) / px[t-1]
ret = px.pct_change().dropna()

# ============================================================================
# STRATEGY 1: STANDARD REVERSAL STRATEGIES (lag=1)
# ============================================================================
# Test reversal strategies at different time horizons:
# - hor=1: 4 hours (1 bar lookback)
# - hor=2: 8 hours (2 bars lookback)
# - hor=3: 12 hours (3 bars lookback)
# - hor=4: 16 hours (4 bars lookback)
# - hor=5: 20 hours (5 bars lookback)
# - hor=6: 24 hours (6 bars lookback)

strats = {}
for hor in [1, 2, 3, 4, 5, 6]:
    # Step 1: Compute average return over the lookback window (hor bars)
    avg_ret = ret.rolling(hor, min_periods=1).mean()

    # Step 2: Rank assets cross-sectionally at each time point
    # rank(1) ranks across columns (assets), with method='average' for ties
    avg_ret = avg_ret.rank(1)

    # Step 3: Demean the ranks (subtract cross-sectional mean)
    # This centers the portfolio weights so longs and shorts balance
    avg_ret = avg_ret.subtract(avg_ret.mean(1), 0)

    # Step 4: Normalize weights by sum of absolute values
    # This ensures the portfolio is dollar-neutral and fully invested
    avg_ret = avg_ret.divide(avg_ret.abs().sum(1), 0)

    # Step 5: Compute strategy returns
    # shift() lags the weights by 1 period (trade on past signal)
    # Multiply weights by next period's returns and sum across assets
    strats[hor] = (avg_ret.shift() * ret).sum(1)

# Convert dictionary of strategies to DataFrame
strats = pd.DataFrame(strats)

# ============================================================================
# PERFORMANCE ANALYSIS: SHARPE RATIOS BY YEAR
# ============================================================================
# Compute annualized Sharpe ratio for each strategy by year
# Formula: Sharpe = (mean / std) * sqrt(number of periods per year)
# For 4h bars: 252 trading days * 24 hours / 4 hours per bar = 1512 periods/year
sr = strats.resample('YE').mean() / strats.resample('YE').std() * np.sqrt(252*24/4)
print(sr)

# Plot Sharpe ratios by year and horizon
# Negative Sharpe = reversal (betting against recent winners works)
# Positive Sharpe = momentum (betting with recent winners works)
ax = sr.plot(kind='bar')
plt.show()

# ============================================================================
# STRATEGY 2: LAGGED REVERSAL STRATEGIES (lag=2, "skip the first bar")
# ============================================================================
# The first bar after a price move often contains the strongest reversal effect
# (mean reversion from microstructure noise, bid-ask bounce, etc.)
# By skipping the first bar (using shift(2) instead of shift(1)), we test whether
# momentum emerges at longer horizons after the initial reversal dissipates.
#
# This is analogous to how UMD (momentum) at monthly frequency skips the most
# recent month to avoid short-term reversal contamination.

strats_lag = {}
for hor in [1, 2, 3, 4, 5, 6]:
    # Same portfolio construction as before
    avg_ret = ret.rolling(hor, min_periods=1).mean().rank(1)
    avg_ret = avg_ret.subtract(avg_ret.mean(1), 0)
    avg_ret = avg_ret.divide(avg_ret.abs().sum(1), 0)

    # Key difference: shift(2) instead of shift(1)
    # This skips one 4-hour bar between signal formation and execution
    # Example: Use avg return from t-3 to t-1 to trade at t (instead of t-1 to trade at t)
    strats_lag[hor] = (avg_ret.shift(2) * ret).sum(1)

# Convert to DataFrame
strats_lag = pd.DataFrame(strats_lag)

# ============================================================================
# FINAL RESULTS: OVERALL SHARPE RATIOS (lag=2 strategies)
# ============================================================================
# Compute full-sample annualized Sharpe ratios for the lagged strategies
# This shows whether skipping the first bar reveals momentum at longer horizons
sr_lag = strats_lag.mean() / strats_lag.std() * np.sqrt(252*24/4)
print(sr_lag)

ax = sr_lag.plot(kind='bar', title='Annualized Sharpe Ratios for Lagged Strategies (lag=2)')
plt.show()
