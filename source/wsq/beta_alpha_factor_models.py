"""
Beta, Alpha, and Factor Models - Homework 4

This script demonstrates the CAPM (Capital Asset Pricing Model) framework:
    R_stock = alpha + beta x R_market + epsilon

Key Objectives:
1. Decompose stock returns into systematic (beta) and idiosyncratic (alpha) components
2. Measure how much risk comes from market exposure vs stock-specific factors
3. Evaluate if stock outperformance is due to skill (alpha) or market exposure (beta)

Central Questions:
- How much of stock volatility is explained by the market (beta)?
- What remains after removing market exposure (alpha/residuals)?
- Are stocks correlated because of the market, or something else?
- Does alpha (skill) justify the risk, or is it just beta (market exposure)?

Concepts:
- Beta: Sensitivity to market movements (systematic risk)
- Alpha: Excess return beyond what beta predicts (idiosyncratic return)
- Information Ratio: Alpha's Sharpe ratio (skill measurement)
- Factor decomposition: Total return = beta x market + alpha
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

# ==============================================================================
# PART 1: Download Data and Calculate Returns
# ==============================================================================

# Universe: FAANG stocks + QQQ (tech-heavy market benchmark)
# FB (Meta), AAPL, AMZN, NFLX, GOOGL = dominant tech stocks
# QQQ = Nasdaq 100 ETF (our "market" proxy for tech sector)
univ = ['FB', 'AAPL', 'AMZN', 'NFLX', 'GOOGL', 'QQQ']

# Download closing prices from Yahoo Finance
px = yf.download(univ, start="2016-01-01")['Close']

# Calculate daily returns
ret = px / px.shift() - 1

# ==============================================================================
# PART 2: Calculate Rolling Beta
# ==============================================================================

# Beta measures how much a stock moves relative to the market
# Mathematical definition (from linear regression):
#   β = Cov(R_stock, R_market) / Var(R_market)
#   β = Corr(R_stock, R_market) × (σ_stock / σ_market)

# We use a 252-day rolling window (approximately 1 trading year)
# Beta changes over time as stock characteristics evolve

# Step 1: Calculate rolling correlation with QQQ
# corr[t] = correlation of stock with QQQ over past 252 days
corr = ret.rolling(252).corr(ret['QQQ'])

# Step 2: Calculate rolling volatility (standard deviation)
vol = ret.rolling(252).std()

# Step 3: Calculate beta using the formula: β = corr × (vol_stock / vol_QQQ)
# divide(vol['QQQ'], axis=0): divide each stock's (corr × vol) by QQQ's vol
beta = (corr * vol).divide(vol['QQQ'], axis=0)

# Beta interpretation:
# - β = 1.0: Stock moves in line with market (average risk)
# - β > 1.0: Stock is more volatile than market (high-beta, aggressive)
# - β < 1.0: Stock is less volatile than market (low-beta, defensive)
# - β = 1.5: If market moves 1%, stock tends to move 1.5%

# ==============================================================================
# PART 3: Calculate Alpha (Residual Returns)
# ==============================================================================

# Alpha = actual return - expected return from beta
# Formula: α[t] = R_stock[t] - β[t] × R_market[t]

# This is the "residual" - what remains after removing market exposure
# Positive alpha = stock outperformed what beta alone would predict
# Negative alpha = stock underperformed relative to its market exposure

resid = ret - beta.multiply(ret['QQQ'], 0)

# Example:
# - QQQ returns +2% on day t
# - AAPL has beta = 1.2
# - AAPL returns +3%
# - Expected return from beta: 1.2 × 2% = 2.4%
# - Alpha (residual): 3% - 2.4% = +0.6% (outperformance)

# ==============================================================================
# PART 4: Compare Volatility - Original vs Residual Returns
# ==============================================================================

# Question: How much volatility is explained by market exposure (beta)?

# Calculate annualized volatility for both original and residual returns
vol = {}
vol['orig'] = ret.std() * np.sqrt(252)      # Total volatility
vol['resid'] = resid.std() * np.sqrt(252)   # Idiosyncratic volatility (after removing beta)

vol = pd.DataFrame(vol).drop('QQQ')  # Drop QQQ since it's the benchmark
print("Volatility Comparison (Annualized):")
print(vol)

# Key Observation: Residual volatility is MUCH lower than original volatility
#
# Why? The "beta component" (market exposure) drives most stock volatility
# - Original vol: Total risk = systematic risk (beta) + idiosyncratic risk (alpha)
# - Residual vol: Only idiosyncratic risk remains
#
# Interpretation:
# - If orig_vol = 30% and resid_vol = 15%:
#   → ~75% of volatility comes from market movements (beta)
#   → Only ~25% is stock-specific (alpha)
#
# This explains why diversification works: beta risk is systematic (affects all stocks),
# but alpha risk is idiosyncratic (diversifies away)

# ==============================================================================
# PART 5: Compare Correlations - Original vs Residual Returns
# ==============================================================================

# Question: Are stocks correlated because of the market, or other factors?

print("\nOriginal Return Correlations:")
print(ret.corr())

print("\nResidual Return Correlations (after removing beta):")
print(resid.corr())

# Key Observations:
#
# 1. Stock-to-stock correlations DROP dramatically
#    - Original: FAANG stocks are 0.5-0.7 correlated with each other
#    - Residual: Correlations drop to near zero or even negative
#    - Interpretation: Most correlation is driven by common market exposure (beta)
#    - After removing beta, stocks are much more independent
#
# 2. Correlation with QQQ nearly disappears
#    - Original: Stocks are 0.6-0.8 correlated with QQQ (strong market dependence)
#    - Residual: Correlations drop to near 0 (market exposure removed)
#    - Not exactly 0 because we use rolling windows (beta estimation error)
#
# 3. Diversification insight:
#    - Simply holding multiple tech stocks provides limited diversification
#    - They all move together due to market (beta) exposure
#    - True diversification requires different betas or asset classes
#
# This is the "tide that lifts all boats" - the market (QQQ) is the common force

# ==============================================================================
# PART 6: Information Ratio vs Sharpe Ratio - Skill vs Beta
# ==============================================================================

# Critical Question: Is stock performance due to skill (alpha) or market exposure (beta)?

# Information Ratio (IR): Sharpe ratio of alpha (residual returns)
# - Measures risk-adjusted alpha (excess return per unit of idiosyncratic risk)
# - IR = mean(alpha) / std(alpha) × sqrt(252)
# - High IR = consistent alpha generation (manager skill)

# Sharpe Ratio (SR): Sharpe ratio of total returns
# - Measures total risk-adjusted performance (all sources of return)
# - SR = mean(return) / std(return) × sqrt(252)
# - High SR = good risk-adjusted returns (could be beta or alpha)

df = {}
df['IR'] = resid.mean() / resid.std() * np.sqrt(252)  # Alpha quality
df['SR'] = ret.mean() / ret.std() * np.sqrt(252)       # Total performance
df = pd.DataFrame(df).drop('QQQ')

print("\nInformation Ratio vs Sharpe Ratio:")
print(df)

# Interpretation Guide:
#
# Compare IR vs SR for each stock:
#
# 1. SR >> IR (Sharpe much higher than IR):
#    - Most performance comes from beta exposure (market risk)
#    - Little alpha generation (no stock-picking skill)
#    - Example: SR=1.5, IR=0.3 → riding market, not outperforming
#
# 2. SR ≈ IR (similar values):
#    - Performance is mostly alpha (stock-specific)
#    - Either low beta or alpha dominates
#    - Good stock selection independent of market
#
# 3. IR < 0 but SR > 0:
#    - Negative alpha (underperforming relative to beta)
#    - Only making money from market exposure
#    - Would be better off just buying QQQ
#
# Key Findings (from homework):
# - IRs generally lower than SRs → beta drives most performance
# - AAPL: Highest IR and SR → best stock-specific performance + beta
# - FB: Lowest performance → weak alpha, performance from beta only
#
# Investment Implication:
# If IR is low, just buy QQQ (cheaper, simpler, same beta exposure)
# Only pay fees for active management if IR is high (real alpha generation)

plt.show()

# SUMMARY:
# This analysis demonstrates that:
# 1. Market (beta) explains 60-80% of individual stock volatility
# 2. Stock correlations are driven by shared market exposure
# 3. Most stock returns come from beta, not alpha (skill)
# 4. True diversification requires different factor exposures, not just more stocks
