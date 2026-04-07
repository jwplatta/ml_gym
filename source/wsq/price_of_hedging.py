"""
The Price of Hedging - A Portfolio Optimization Study

This script explores the economic cost of hedging by analyzing:
1. Two correlated return series (a main strategy 'X' and a 'HEDGE')
2. Basic statistics: annualized returns, volatilities, Sharpe ratios, and correlations
3. Optimal portfolio weights combining both strategies
4. Sensitivity analysis: how do optimal weights change as hedge returns vary from -10% to +10%?

Key Question: What minimum return does the hedge need to justify including it in the portfolio?
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def gen_strat_returns():
    """
    Generate synthetic daily return series for two strategies with negative correlation.

    Returns:
        pd.DataFrame: Daily returns for 'X' and 'HEDGE' strategies (2010-2019)

    Financial Context:
        - Two strategies with -0.5 correlation (when X goes up, HEDGE tends to go down)
        - Both target 10% annualized volatility
        - Both target 10% annualized return
        - Negative correlation means HEDGE can reduce portfolio volatility
    """
    np.random.seed(5)  # For reproducible results

    # Define correlation matrix: -0.5 means strategies move in opposite directions 50% of the time
    # This negative correlation is valuable for diversification
    corr = [[1, -0.5],
            [-0.5, 1]]
    corr = np.array(corr)

    # Set target annualized volatility of 10% for both strategies
    # Divide by sqrt(252) to convert annual vol to daily vol (252 trading days/year)
    vols = np.diag(np.array([0.1, 0.1])) / np.sqrt(252)

    # Compute covariance matrix: sigma = V * Corr * V (where V is diagonal vol matrix)
    # This combines volatilities and correlations into one matrix
    sigma = vols @ corr @ vols

    # Set expected daily returns: 10% annual return / 252 days = ~0.04% daily
    mu = np.array([0.1, 0.1]) / 252

    # Generate business day dates from 2010 to 2019 (freq='B' excludes weekends)
    dates = pd.date_range('20100101', '20191231', freq='B')

    # Generate random returns from a multivariate normal distribution
    # This creates correlated random returns with our specified mean and covariance
    rets = np.random.multivariate_normal(mu, sigma, size=len(dates))

    # Convert to DataFrame with meaningful column names and date index
    rets = pd.DataFrame(rets, columns=['X', 'HEDGE'], index=dates)

    # Rescale returns to exactly match target volatility (10% annualized)
    # rets.std() computes standard deviation across all rows (axis=0 by default)
    rets = rets / rets.std() * 0.1 / np.sqrt(252)

    # Demean returns (subtract mean to center at zero)
    rets = rets - rets.mean()

    # Add back target expected return to ensure mean matches our target
    rets = rets + mu

    return rets


def opt_weights(sigma, mu):
    """
    Calculate optimal portfolio weights using mean-variance optimization.

    Args:
        sigma: Covariance matrix of returns (measures risk and correlations)
        mu: Expected returns vector (mean return for each asset)

    Returns:
        np.array: Optimal weights that maximize Sharpe ratio

    Mathematical Background:
        - This implements the tangency portfolio from Modern Portfolio Theory
        - Formula: w = Σ^(-1) * μ (inverse of covariance matrix times returns)
        - Weights are normalized so absolute values sum to 1
        - Allows for long/short positions (negative weights)
    """
    # Inverse covariance matrix @ expected returns gives optimal weights
    # This is the closed-form solution for the maximum Sharpe ratio portfolio
    wgts = np.linalg.inv(sigma) @ mu

    # Normalize weights so they sum to 1 in absolute terms
    # abs().sum() allows for both long and short positions
    wgts = wgts / np.abs(wgts).sum()

    return wgts


def calc_sharpe(x):
    """
    Calculate annualized Sharpe ratio for a return series.

    Args:
        x: pd.Series or array-like of daily returns

    Returns:
        float: Annualized Sharpe ratio

    Financial Context:
        Sharpe ratio = (Return - Risk-free rate) / Volatility
        - Measures return per unit of risk
        - Higher is better (more return for the risk taken)
        - We assume risk-free rate = 0 for simplicity
        - Multiply by sqrt(252) to annualize from daily data
    """
    return x.mean() / x.std() * np.sqrt(252)


# ==============================================================================
# PART 1: Generate and Examine Return Data
# ==============================================================================

rets = gen_strat_returns()
print(rets.head())

# Compute key statistics for each strategy
# Create empty DataFrame to store statistics
stats_df = pd.DataFrame()

# Annualized return: daily mean * 252 trading days
# Example: if daily mean = 0.0004, annual = 0.0004 * 252 = 0.1008 (10.08%)
stats_df['ann ret'] = rets.mean() * 252

# Annualized volatility: daily std * sqrt(252)
# We multiply by sqrt(252) not 252 because variance scales linearly, but std scales by square root
stats_df['vol'] = rets.std() * np.sqrt(252)

# Sharpe ratio: return per unit of risk (higher is better)
stats_df['sharpe'] = stats_df['ann ret'] / stats_df['vol']

# ==============================================================================
# PART 2: Calculate Optimal Portfolio Weights
# ==============================================================================

# Compute covariance matrix from returns
# rets.cov() computes pairwise covariances between columns (X and HEDGE)
# Result is a 2x2 symmetric matrix showing variances (diagonal) and covariance (off-diagonal)
sigma = rets.cov()

# Compute mean returns for each strategy
# This is our estimate of expected returns (mu in finance notation)
mu = rets.mean()

# Calculate optimal weights using mean-variance optimization
# This tells us how much to allocate to each strategy to maximize Sharpe ratio
wgts = opt_weights(sigma, mu)

# Construct the combined portfolio
# rets * wgts: element-wise multiplication (broadcasts weights across all dates)
# .sum(1): sum across columns (axis=1) to get single return series
combo = (rets * wgts).sum(1)

# Calculate Sharpe ratio of the combined portfolio
sharpe = combo.mean() / combo.std() * np.sqrt(252)

print('Sharpe: ', sharpe)


# ==============================================================================
# PART 3: Sensitivity Analysis - The Price of Hedging
# ==============================================================================
# Key Question: How much return does the HEDGE need to earn to justify including it?
# We'll vary HEDGE's expected return from -10% to +10% and see how optimal weights change

# Dictionaries to store results for each scenario
wgts = {}      # Will store optimal weights for each hedge return level
sharpes = {}   # Will store portfolio Sharpe ratios for each scenario

# Create a copy to avoid modifying original data
# .copy() creates a new DataFrame so we don't accidentally change 'rets'
rets_copy = rets.copy()

# Loop through different annual return levels for the HEDGE strategy
# np.arange(-0.1, 0.11, 0.01) creates: [-10%, -9%, -8%, ..., 9%, 10%]
for hedge_ret in np.arange(-0.1, 0.11, 0.01):
    # Adjust HEDGE returns to have new expected return while keeping volatility constant
    # Step 1: Remove current mean (demean)
    # Step 2: Add new target mean (hedge_ret / 252 for daily)
    rets_copy['HEDGE'] = rets_copy['HEDGE'] - rets_copy['HEDGE'].mean() + hedge_ret / 252

    # Recalculate expected returns with new HEDGE mean
    mu = rets_copy.mean()

    # Calculate optimal weights for this scenario
    # pd.Series() converts array to Series with strategy names as index
    wgt = pd.Series(opt_weights(sigma, mu), mu.index)

    # Format return as percentage string for readable labels (e.g., "-10%", "0%", "10%")
    hedge_ret_str = '%.0f%%' % (hedge_ret * 100)

    # Store weights and Sharpe ratio for this scenario
    wgts[hedge_ret_str] = wgt
    sharpes[hedge_ret_str] = calc_sharpe((rets_copy * wgt).sum(1))

# Convert dictionaries to DataFrame/Series for easier plotting
# .T transposes so each row is a return scenario, columns are X and HEDGE weights
wgts = pd.DataFrame(wgts).T
sharpes = pd.Series(sharpes)

# ==============================================================================
# PART 4: Visualization
# ==============================================================================

# Plot optimal weights as a stacked bar chart
# Shows how allocation shifts between X and HEDGE as HEDGE's return changes
ax_wgts = wgts.plot(kind='bar', grid=True)

# Plot Sharpe ratios across scenarios
# Shows the portfolio's risk-adjusted return for each HEDGE return level
ax_sr = sharpes.plot(grid=True)

plt.show()

# INTERPRETATION GUIDE:
# - Look for where HEDGE weight crosses zero (breakeven point)
# - If HEDGE has lower return than X, you might still want some for diversification
# - The Sharpe ratio plot shows total portfolio benefit
# - Negative HEDGE weights mean shorting (betting against) the hedge
