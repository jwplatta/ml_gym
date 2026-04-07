"""
Momentum Trading Strategy - Homework 3

This script implements a classic momentum strategy:
- Signal: Rolling Sharpe ratio over past year (measures risk-adjusted performance trend)
- Rule: Go long assets with Sharpe > 1, equal-weight them
- Rationale: "Winners keep winning" - assets with strong recent risk-adjusted returns
  tend to continue outperforming

Key Concepts:
1. Momentum effect: Empirical phenomenon where past winners outperform
2. Time-series momentum: Uses asset's own past returns (vs cross-sectional)
3. Signal quality: Using Sharpe ratio filters for consistency, not just raw returns
4. Portfolio construction: Equal-weight longs (no shorts, no leverage)

Universe:
- QQQ: Nasdaq 100 (tech stocks)
- TLT: 20+ year Treasury bonds (safe haven)
- GLD: Gold (inflation hedge, alternative currency)
- RWO: Global real estate (real assets)

These are uncorrelated asset classes, providing diversification.
"""

import math

import yfinance as yf

# ==============================================================================
# PART 1: Download Data and Calculate Returns
# ==============================================================================

# Universe: 4 diversified asset class ETFs
univ = ['QQQ', 'TLT', 'GLD', 'RWO']

# Download price data from Yahoo Finance
px = yf.download(univ, start="2016-01-01")

# Extract adjusted close prices (adjusted for splits and dividends)
# Using adjusted prices ensures returns accurately reflect true investor experience
adj_close = px['Adj Close']

# Calculate daily returns
# ret[t] = price[t] / price[t-1] - 1
ret = adj_close / adj_close.shift() - 1

# ==============================================================================
# PART 2: Compute Momentum Signal
# ==============================================================================


def compute_momentum(ret):
    """
    Calculate rolling Sharpe ratio as a momentum signal.

    Args:
        ret: DataFrame of daily returns (index=date, columns=tickers)

    Returns:
        DataFrame of momentum signals (annualized rolling Sharpe ratios)

    Signal Logic:
        - Sharpe > 1: Strong risk-adjusted momentum (good)
        - Sharpe between 0 and 1: Positive but weak momentum (marginal)
        - Sharpe < 0: Negative momentum (avoid)

    Why use Sharpe ratio instead of raw returns?
        - Filters for consistency (not just lucky gains)
        - Penalizes volatility (risky assets need higher returns to qualify)
        - Better predictor of future performance than raw returns alone
    """
    # Rolling 252-day (1 year) Sharpe ratio calculation:
    # SR = (mean return / std dev of returns) × sqrt(252)
    # sqrt(252) annualizes the daily Sharpe ratio
    momentum = ret.rolling(252).mean() / ret.rolling(252).std() * math.sqrt(252)
    return momentum


momentum = compute_momentum(ret)
print(momentum)


# ==============================================================================
# PART 3: Construct Portfolio Weights
# ==============================================================================


def compute_portfolio(momentum):
    """
    Convert momentum signals into portfolio weights.

    Args:
        momentum: DataFrame of momentum signals

    Returns:
        DataFrame of portfolio weights (same shape as momentum)

    Portfolio Rules:
        1. Filter: Only include assets with Sharpe > 1
        2. Equal-weight: Divide capital equally among qualifying assets
        3. Long-only: No short positions, no leverage

    Example:
        - Momentum: [QQQ: 1.5, TLT: 0.8, GLD: 1.2, RWO: -0.3]
        - Qualifying: QQQ and GLD (both > 1)
        - Weights: [QQQ: 0.5, TLT: 0, GLD: 0.5, RWO: 0]
    """
    # Step 1: Create binary indicator (1 if momentum > 1, else 0)
    # (momentum > 1) creates boolean, *1 converts to integer
    portfolio = (momentum > 1) * 1

    # Step 2: Normalize to equal weights
    # portfolio.abs().sum(1): count of qualifying assets on each date
    # div(..., 0): divide across index (axis=0) to get equal weights
    # If 2 assets qualify → each gets 0.5 weight
    # If 0 assets qualify → all weights are 0 (stay in cash)
    portfolio = portfolio.div(portfolio.abs().sum(1), 0)

    return portfolio


portfolio = compute_portfolio(momentum)

# ==============================================================================
# PART 4: Analyze Portfolio Performance
# ==============================================================================

# Calculate strategy returns
# portfolio.shift(): use yesterday's weights to avoid look-ahead bias
# We decide weights at close of day t-1, earn returns on day t
strat_ret = (portfolio.shift() * ret).sum(1)

# Clean data: Start returns when we have first valid momentum signal
# First 252 days are NaN (need 252 days to calculate first Sharpe ratio)
strat_ret = strat_ret.loc[momentum.dropna().index[0]:]

# ---------------------------------------------------------------------------
# Question 1: What is the annualized Sharpe ratio of the strategy?
# ---------------------------------------------------------------------------

overall_sharpe = strat_ret.mean() / strat_ret.std() * math.sqrt(252)
print(f"Overall Sharpe Ratio: {overall_sharpe:.2f}")

# Interpretation:
# - SR > 1: Excellent (strategy generates strong risk-adjusted returns)
# - SR 0.5-1: Good (decent risk-adjusted returns)
# - SR < 0.5: Marginal (weak risk-adjusted performance)

# ---------------------------------------------------------------------------
# Question 2: What is the Sharpe ratio within each year?
# ---------------------------------------------------------------------------

# Define Sharpe calculation as a lambda for reuse
sharpe = lambda x: x.mean() / x.std() * math.sqrt(252)

# Group returns by year and calculate Sharpe for each year
# This shows consistency: does the strategy work every year or just lucky?
yearly_sharpe = strat_ret.groupby([x.year for x in strat_ret.index]).apply(sharpe)
print("\nYearly Sharpe Ratios:")
print(yearly_sharpe)

# Look for:
# - Consistency: positive Sharpe most years (robust strategy)
# - Outliers: one great year driving all returns (fragile strategy)
# - Drawdowns: negative Sharpe years (when did it fail and why?)

# ---------------------------------------------------------------------------
# Question 3: How correlated is the strategy with underlying assets?
# ---------------------------------------------------------------------------

correlations = ret.corrwith(strat_ret)
print("\nCorrelations with individual assets:")
print(correlations)

# Interpretation:
# - Low correlation: Strategy timing adds value (not just buying and holding)
# - High correlation with one asset: Strategy is basically that asset
# - Negative correlation: Strategy zigs when asset zags (good diversifier)

# Desired outcome: Low correlations indicate true diversification benefit
# The strategy is making active timing decisions, not passive holding

# ---------------------------------------------------------------------------
# Question 4: Plot cumulative returns over time
# ---------------------------------------------------------------------------

# cumsum() shows total return trajectory
# Helps visualize: drawdowns, consistency, regime changes
strat_ret.cumsum().plot(title='Momentum Strategy Cumulative Returns')

# STRATEGY INSIGHTS:
# This momentum approach captures trends across asset classes:
# - Stays invested in trending assets (QQQ in bull markets)
# - Rotates to safe havens during risk-off (TLT in downturns)
# - Opportunistically holds gold during inflation scares
# - Can go to cash when no assets have strong momentum (defensive)
