"""
Unconstrained Backtest Example: Time-Series Momentum in Cryptocurrencies

This script tests whether major cryptocurrencies (BTC, ETH, ADA, BNB) exhibit
time-series (TS) momentum - the tendency for assets that have performed well
recently to continue performing well.

Key Concepts:
- Time-Series Momentum: Each asset is traded based on its own past performance
  (unlike cross-sectional momentum which compares assets to each other)
- Z-Score Signal: Measures how much recent returns deviate from long-term average
- Tanh Normalization: Constrains extreme signal values to reasonable portfolio weights
- Unconstrained: Each asset is traded independently without portfolio constraints

Strategy Logic:
1. Compute short-term (10-day) and long-term (365-day) average returns
2. Create z-score: (short_avg - long_avg) / long_term_volatility
3. Scale by sqrt(10) to adjust for averaging 10 days of returns
4. Apply tanh to limit extreme positions
5. Trade based on lagged signals to avoid look-ahead bias

Expected Results:
- Positive Sharpe ratios indicate momentum exists
- Low correlation with buy-and-hold suggests timing adds value
"""

import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

# ============================================================================
# STEP 1: DATA DOWNLOAD AND RETURN CALCULATION
# ============================================================================

# Download daily OHLCV data for 4 major cryptocurrencies from Yahoo Finance
# Tickers use '-USD' suffix for crypto vs US Dollar pairs
# Data starts from January 1, 2016 to present
data = yf.download(['ADA-USD', 'BNB-USD', 'BTC-USD', 'ETH-USD'], '2016-1-1')

# Compute daily returns: ret[t] = (price[t] / price[t-1]) - 1
# This is equivalent to pct_change() but shows the formula explicitly
ret = data['Close'] / data['Close'].shift() - 1

# ============================================================================
# STEP 2: SIGNAL CONSTRUCTION (Z-Score of Short-Term vs Long-Term Returns)
# ============================================================================

# Compute the difference between short-term and long-term average returns
# - Short-term: 10-day rolling average (recent performance)
# - Long-term: 365-day rolling average (baseline performance)
# Intuition: If short_avg > long_avg, the asset is doing better than usual
port = np.sqrt(10) * (ret.rolling(10, min_periods=1).mean() - ret.rolling(365, min_periods=10).mean())

# Divide by long-term volatility to create a z-score
# This normalizes the signal so assets with different volatilities are comparable
# ret.rolling(365).std() measures the typical daily volatility over the past year
port = port / ret.rolling(365, min_periods=10).std()

# Technical note on sqrt(10):
# The standard deviation is calculated on DAILY returns, but we're averaging
# 10 days of returns. The standard error of a 10-day average is:
# std(daily) / sqrt(10), so we multiply by sqrt(10) to get the z-score
# of the 10-day average relative to the daily volatility.

# Apply hyperbolic tangent (tanh) to constrain extreme values
# tanh maps (-inf, inf) to (-1, 1), preventing extreme portfolio positions
# This is the "unconstrained" part - we allow continuous weights rather than
# just -1, 0, or +1, but we still limit the magnitude
port = np.tanh(port)

# ============================================================================
# STEP 3: COMPUTE STRATEGY RETURNS
# ============================================================================

# Multiply lagged portfolio weights by current returns to get strategy returns
# shift() is critical: we use yesterday's signal to trade today (no look-ahead bias)
# For each asset: strat_ret[t] = port[t-1] * ret[t]
# Positive port[t-1] = long position, negative = short position
strat_ret = port.shift() * ret

# ============================================================================
# STEP 4: PERFORMANCE EVALUATION - SHARPE RATIOS
# ============================================================================

# Compute annualized Sharpe ratio for each cryptocurrency's timing strategy
# Formula: Sharpe = (mean_daily_return / std_daily_return) * sqrt(trading_days_per_year)
# We use 365 for crypto markets which trade 24/7 (unlike 252 for equities)
#
# Interpretation:
# - Sharpe > 0: Momentum exists (strategy is profitable)
# - Sharpe > 1: Strong momentum signal
# - Sharpe < 0: Reversal dominates (contrarian strategy would work better)
sr = strat_ret.mean() / strat_ret.std() * np.sqrt(365)
print("Annualized Sharpe Ratios by Asset:")
print(sr)
print()

# ============================================================================
# STEP 5: VISUALIZE CUMULATIVE RETURNS
# ============================================================================

# Plot cumulative returns over time to see strategy performance visually
# cumsum() on returns gives cumulative log returns (approximately)
# Each line represents the timing strategy for one cryptocurrency
ax = strat_ret.cumsum().plot(grid=True)
plt.title('Cumulative Returns of Time-Series Momentum Strategies')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend(title='Asset')
plt.show()

# ============================================================================
# STEP 6: CORRELATION ANALYSIS WITH BUY-AND-HOLD
# ============================================================================

# Compute correlation between timing strategy returns and buy-and-hold returns
# This tells us how much value the timing strategy adds vs. just holding
#
# Interpretation:
# - corr ≈ 1: Timing strategy is similar to buy-and-hold (little value added)
# - corr ≈ 0: Timing strategy is orthogonal (captures different risk)
# - corr < 0: Timing strategy is contrarian to buy-and-hold
#
# Typically we want low correlation, showing the timing adds independent value
corr = strat_ret.corrwith(ret)
print("Correlation between Timing Strategy and Buy-and-Hold:")
print(corr)
