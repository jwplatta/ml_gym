"""
S&P 500 Mean-Reversion Strategies

This script implements two variations of mean-reversion trading on the S&P 500:

Strategy 1: Unconstrained Rank-Based (uses all 500 stocks)
- Rank stocks by yesterday's return
- Long recent losers (negative ranks), short recent winners (positive ranks)
- Fully market-neutral (sum of weights = 0)

Strategy 2: Long-Short Decile (uses top/bottom 10% only)
- Long bottom 10% (biggest losers)
- Short top 10% (biggest winners)
- 50% long + 50% short = dollar-neutral

Key Concept: Mean Reversion
- Assumption: Extreme daily moves tend to reverse (winners fade, losers bounce)
- Contrarian approach: Bet against recent price movements
- Works best in range-bound markets, fails in strong trends

Risk Considerations:
- Market-neutral (hedged against market direction)
- High turnover (rebalances daily → transaction costs matter)
- Assumes liquidity to trade 500 stocks daily
- Vulnerable to momentum regimes (when trends persist)
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

# ==============================================================================
# Data Download: S&P 500 Universe
# ==============================================================================

# Scrape current S&P 500 constituents from Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
tickers = pd.read_html(url, storage_options={"User-Agent": "Mozilla/5.0"})[0].Symbol.to_list()

# Replace periods with hyphens (Yahoo Finance convention)
# Example: BRK.B → BRK-B
tickers = [x.replace('.', '-') for x in tickers]

# Download daily price data for 2023
data = yf.download(tickers, '2023-1-1', '2023-12-12')

# Calculate daily returns
ret = data['Close'] / data['Close'].shift() - 1
ret = ret.iloc[1:]  # Drop first row (NaN from shift)


def get_stats(strat_ret):
    """
    Calculate annualized performance statistics.

    Args:
        strat_ret: Series of daily strategy returns

    Returns:
        Series with Sharpe ratio, annual return, and annual volatility
    """
    stats = {}
    stats['SR'] = strat_ret.mean() / strat_ret.std() * np.sqrt(252)
    stats['ret'] = strat_ret.mean() * 252
    stats['vol'] = strat_ret.std() * np.sqrt(252)
    stats = pd.Series(stats)
    return stats

# ==============================================================================
# STRATEGY 1: Unconstrained Rank-Based Mean Reversion
# ==============================================================================

# Step 1: Negate returns (so winners become losers, losers become winners)
# We want to BUY losers and SELL winners (mean reversion logic)
negate = ret * -1.

# Step 2: Rank stocks cross-sectionally each day
# rank(1) ranks across columns (axis=1)
# After negation: rank 1 = biggest winner (we'll short), rank 500 = biggest loser (we'll long)
ranked = negate.rank(1)

# Step 3: Demean ranks to create market-neutral portfolio
# Subtract cross-sectional mean so weights sum to zero
# High rank → positive weight (long), low rank → negative weight (short)
demeaned = ranked.subtract(ranked.mean(1), 0)

# Step 4: Normalize so absolute weights sum to 1
# Controls leverage: |weights| = 1 means fully invested
port = demeaned.divide(demeaned.abs().sum(1), 0)

# Portfolio characteristics:
# - All 500 stocks have positions (long or short)
# - Market-neutral (sum = 0)
# - Fully invested (|sum| = 1)

# Visualize portfolio weights on example day
port.loc['20230330'].sort_values().plot(title='Strategy 1: Portfolio Weights (2023-03-30)')
plt.ylabel('Weight')
plt.xlabel('Stock (sorted by weight)')
plt.show()

# Verify fully invested (should always = 1)
port.abs().sum(1).round(2).plot(title='Total Absolute Exposure')
plt.ylabel('Sum of |weights|')
plt.show()

# Verify dollar neutrality (should always = 0)
port.sum(1).round(2).plot(title='Net Market Exposure')
plt.ylabel('Sum of weights')
plt.show()

# Calculate strategy returns
# port.shift(): use yesterday's weights (avoid look-ahead bias)
# "Market orders" assumption: we execute at today's close
strat_ret = (port.shift() * ret).sum(1)

print("Strategy 1 - Unconstrained Rank-Based:")
print(get_stats(strat_ret))

# Plot cumulative returns
strat_ret.cumsum().plot(title='Strategy 1: Cumulative Returns')
plt.ylabel('Cumulative Return')
plt.show()

# ==============================================================================
# STRATEGY 2: Long-Short Decile (Top/Bottom 10%)
# ==============================================================================

# This strategy only trades the extremes: biggest losers and biggest winners
# More concentrated bets, less diversified than Strategy 1

# Step 1: Negate returns and convert ranks to percentiles
# pct=True: rank as percentiles (0 to 1) instead of integers
negate = ret * -0.1
pct = negate.rank(axis=1, pct=True)

# Step 2: Create LONG positions (bottom 10% = biggest losers)
# pct > 0.9 means top 90th percentile after negation = biggest losers
long = (pct > 0.9) * 1
# Equal-weight within the long basket, scale to 50% of capital
long = long.divide(long.abs().sum(1), 0) * 0.5

# Step 3: Create SHORT positions (top 10% = biggest winners)
# pct < 0.1 means bottom 10th percentile after negation = biggest winners
short = (pct < 0.1) * -1.0
# Equal-weight within the short basket, scale to 50% of capital
short = short.divide(short.abs().sum(1), 0) * 0.5

# Step 4: Combine long and short portfolios
port = short.add(long, fill_value=0)

# Portfolio characteristics:
# - ~50 stocks long (10% of 500)
# - ~50 stocks short (10% of 500)
# - 50% long + 50% short = dollar-neutral
# - More concentrated than Strategy 1 (only 100 positions vs 500)

# Visualize portfolio weights on example day
# Note: Date '20210330' may not exist in 2023 data, using available date
available_dates = port.index[port.sum(1) != 0]
if len(available_dates) > 60:
    example_date = available_dates[60]
    port.loc[example_date].sort_values().plot(title=f'Strategy 2: Portfolio Weights ({example_date})')
    plt.ylabel('Weight')
    plt.xlabel('Stock (sorted by weight)')
    plt.show()

# Verify fully invested (should = 1: 0.5 long + 0.5 short)
(port.abs()).sum(1).plot(title='Total Absolute Exposure')
plt.ylabel('Sum of |weights|')
plt.show()

# Verify dollar neutrality (should = 0: longs offset shorts)
port.sum(1).plot(title='Net Market Exposure')
plt.ylabel('Sum of weights')
plt.show()

# Calculate strategy returns
strat_ret = (port.shift() * ret).sum(1)

print("\nStrategy 2 - Long-Short Decile:")
print(get_stats(strat_ret))

# Plot cumulative returns
strat_ret.cumsum().plot(title='Strategy 2: Cumulative Returns')
plt.ylabel('Cumulative Return')
plt.show()

# COMPARISON:
# Strategy 1 (All stocks): Lower concentration, smoother returns, more diversified
# Strategy 2 (Deciles): Higher concentration, potentially higher alpha, more volatile
#
# Which performs better depends on:
# - Strength of mean reversion in extremes vs middle
# - Transaction costs (Strategy 2 trades fewer stocks)
# - Market microstructure (liquidity, spreads)
