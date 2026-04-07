"""
Fama-French 3-Factor Risk Analysis on ARKK

This script performs multi-factor risk attribution using the famous Fama-French model:

Model: R_ARKK = α + β_mkt × (Mkt-RF) + β_size × SMB + β_value × HML + ε

The Three Factors:
1. Mkt-RF: Market risk premium (market return minus risk-free rate)
   - Captures general market exposure (like CAPM beta)
2. SMB: Small Minus Big (size factor)
   - Difference between small-cap and large-cap stock returns
   - Positive loading = tilted toward small caps
3. HML: High Minus Low (value factor)
   - Difference between value stocks and growth stocks
   - Positive loading = value tilt, negative = growth tilt

Analysis Performed:
- Factor loadings (betas): How sensitive is ARKK to each factor?
- R-squared: What % of variance is explained by these factors?
- Risk contribution: How much volatility comes from each factor?
- Stress testing: Impact of extreme factor moves (5-sigma events)
- Factor neutralization: What's ARKK's alpha independent of factors?
- Rolling exposures: How do factor loadings change over time?

Use Case: Understanding if ARKK's returns come from:
- Factor exposure (systematic bets on market, size, value)
- True alpha (manager skill independent of factors)
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import yfinance as yf


def load_ff3():
    """
    Load daily Fama-French 3-factor data.

    Data source: Kenneth French's data library
    Download from: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

    Returns:
        DataFrame with Mkt-RF, SMB, HML as decimal returns (not percentages)

    Factors explained:
        - Mkt-RF: Market excess return (broad market - risk-free rate)
        - SMB: Small cap premium (small stocks - large stocks)
        - HML: Value premium (value stocks - growth stocks)
    """
    ff3 = pd.read_csv('F-F_Research_Data_Factors_daily.CSV')
    ff3['Unnamed: 0'] = pd.DatetimeIndex(ff3['Unnamed: 0'].map(str))
    ff3 = ff3.set_index('Unnamed: 0')

    # Convert from percentage to decimal (divide by 100)
    return ff3[['Mkt-RF', 'SMB', 'HML']] / 100


# ==============================================================================
# PART 1: Load Data
# ==============================================================================

# Load Fama-French factor returns
ret = load_ff3()

# Download ARKK (ARK Innovation ETF) price data
# ARKK is a growth-focused ETF with heavy tech/innovation exposure
arkk = yf.download('ARKK', start='2020-01-01')['Close']

# Calculate ARKK returns and merge with factor data
ret['ARKK'] = arkk.pct_change()
ret = ret.dropna()
print(ret)



# ==============================================================================
# PART 2: Basic Performance Analysis
# ==============================================================================

# Plot cumulative returns (total wealth from $1 investment)
ax = (ret['ARKK'] + 1).cumprod().plot(title='ARKK Cumulative Returns')
plt.ylabel('Cumulative Return ($1 initial)')
plt.show()

# Calculate Sharpe ratio (risk-adjusted performance)
sr = ret['ARKK'].mean() / ret['ARKK'].std() * np.sqrt(252)
print('Sharpe Ratio: ', sr)

# ==============================================================================
# PART 3: Fama-French 3-Factor Regression
# ==============================================================================

# Prepare independent variables (the three factors)
X = ret[['Mkt-RF', 'SMB', 'HML']]
X = sm.add_constant(X)  # Add intercept (alpha)

# Run OLS regression: ARKK ~ alpha + beta_mkt*Mkt + beta_size*SMB + beta_value*HML
mod = sm.OLS(ret['ARKK'], X)
res = mod.fit()
print(res.summary())

# ==============================================================================
# PART 4: Factor Loadings (Betas)
# ==============================================================================

print("\nFactor Loadings:")
print(res.params)

# Market beta is the most important - measures overall market sensitivity
print('Market Beta: ', res.params['Mkt-RF'])

# Interpretation:
# - const (alpha): Excess return not explained by factors (manager skill)
# - Mkt-RF: Market beta (expect ~1.0 for equity ETF, >1.0 for high-beta tech)
# - SMB: Size tilt (expect negative for large-cap tech stocks)
# - HML: Value/Growth tilt (expect very negative for growth-focused ARKK)

# ==============================================================================
# PART 5: R-squared - Variance Explained
# ==============================================================================

# R-squared: What fraction of ARKK's variance is explained by the 3 factors?
r_sq = res.predict(X).var() / ret['ARKK'].var()
print('\nR-squared: ', r_sq)

# Interpretation:
# - R² = 0.80: 80% of variance explained by factors, 20% is idiosyncratic
# - High R²: Returns mostly driven by factor exposure (not stock picking)
# - Low R²: Returns have large idiosyncratic component (active management)

# ==============================================================================
# PART 6: Risk Contribution Analysis
# ==============================================================================

# How much does each factor contribute to ARKK's total volatility?
# Risk contribution = std(factor × loading) / std(total return)
risk_contr = X.multiply(res.params).std()[['Mkt-RF', 'SMB', 'HML']] / ret['ARKK'].std()
print('\nRisk Contribution by Factor:')
print(risk_contr)

# Interpretation:
# - Sum of risk contributions ≈ R²
# - Shows which factors dominate risk profile
# - For ARKK: expect market risk to dominate, followed by growth (HML)

# ==============================================================================
# PART 7: Stress Testing - 5-Sigma Shock
# ==============================================================================

# What happens to ARKK if a factor has an extreme move (5 standard deviations)?
x_std_shock = (X[['Mkt-RF', 'SMB', 'HML']].std() * 5) * res.params[['Mkt-RF', 'SMB', 'HML']].abs()
print('\n5-Sigma Shock Impact (extreme one-day moves):')
print(x_std_shock)

# Interpretation:
# - Market 5-sigma shock: Mkt-RF moves 5× typical daily vol
# - Impact on ARKK: beta × shock magnitude
# - Example: If market beta = 1.3 and market 5-sigma = 7%, ARKK impact ≈ 9%
# - Useful for VaR (Value at Risk) calculations and tail risk management

# ==============================================================================
# PART 8: Statistical Significance
# ==============================================================================

print('\nT-statistics (significance tests):')
print(res.tvalues)

# T-stat interpretation:
# - |t| > 2: Factor loading is statistically significant (reject H₀: β=0)
# - Expect high t-stat for Mkt-RF (market beta always significant)
# - Look for significant alpha (const) → evidence of manager skill

# ==============================================================================
# PART 9: Factor Neutralization - Extract Pure Alpha
# ==============================================================================

# Remove factor exposures to isolate ARKK's idiosyncratic returns (alpha)
# Neutralized return = actual return - (factor betas × factor returns)
neut = ret['ARKK'] - X.multiply(res.params)[['Mkt-RF', 'SMB', 'HML']].sum(1)

# Calculate Sharpe ratio of factor-neutral returns
neut_sr = neut.mean() / neut.std() * np.sqrt(252)
print('\nFactor-Neutralized Sharpe Ratio: ', neut_sr)

# Comparison:
# - Original Sharpe: Total performance (factors + alpha)
# - Neutralized Sharpe: Alpha-only performance (manager skill)
# - If neutralized SR << original SR: Returns mostly from factor bets
# - If neutralized SR ≈ original SR: Returns from stock selection (alpha)

# ==============================================================================
# PART 10: Rolling Factor Exposures - Time-Varying Risk
# ==============================================================================

# Factor exposures (betas) change over time as fund strategy evolves
# Rolling window analysis shows how ARKK's factor tilts have shifted


def get_betas(ret):
    """
    Estimate factor loadings from a subset of return data.

    Args:
        ret: DataFrame with ARKK and Fama-French factor returns

    Returns:
        Series of factor loadings (const, Mkt-RF, SMB, HML)
    """
    X = ret[['Mkt-RF', 'SMB', 'HML']]
    X = sm.add_constant(X)
    mod = sm.OLS(ret['ARKK'], X)
    res = mod.fit()
    return res.params


# Calculate rolling 252-day (1-year) factor loadings
betas = {}
for dt in ret.index:
    # Use trailing 252 days of data
    start_dt = dt - pd.tseries.offsets.Day() * 252
    sub_ret = ret.loc[start_dt:dt]

    # Only compute if we have at least 60 days of data
    if len(sub_ret) > 60:
        betas[dt] = get_betas(sub_ret)

betas = pd.DataFrame(betas).T

# Plot rolling factor exposures over time
betas.plot(title='ARKK Rolling Factor Exposures (252-day window)')
plt.ylabel('Factor Loading (Beta)')
plt.xlabel('Date')
plt.legend(['Alpha', 'Market Beta', 'Size (SMB)', 'Value/Growth (HML)'])
plt.show()

# What to look for in the plot:
# - Market beta stability: Does ARKK maintain consistent market exposure?
# - Size tilt changes: Has ARKK shifted toward smaller or larger companies?
# - Value/Growth evolution: Has ARKK become more or less growth-oriented?
# - Alpha trend: Is the fund generating consistent excess returns?
#
# Use cases:
# - Risk monitoring: Detect when fund drifts from stated strategy
# - Dynamic hedging: Adjust hedges based on current factor exposures
# - Performance attribution: Identify periods of high/low alpha generation
#
# Expected for ARKK:
# - High, stable market beta (~1.2-1.5): Aggressive equity exposure
# - Negative SMB (large-cap bias): Invests in established tech companies
# - Very negative HML (growth tilt): Focus on high-growth, innovation stocks
# - Alpha variability: Depends on whether innovation stocks outperform
