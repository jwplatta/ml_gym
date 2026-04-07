"""
Portfolio Weighting Schemes Comparison

This script compares three different approaches to constructing portfolio weights:
1. Optimal (mean-variance): Maximizes Sharpe ratio using full covariance matrix
2. Equal volatility: Allocates inversely to volatility (ignores correlations and returns)
3. Sharpe ratio: Allocates proportional to individual Sharpe ratios (ignores correlations)

Key Question: Which weighting scheme produces the best risk-adjusted returns?

Concepts Covered:
- Mean-variance optimization (Markowitz)
- Risk parity / volatility weighting
- Position sizing based on Sharpe ratios
- Leverage and its effect on Sharpe ratio
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def optimal_weights(sigma, mu):
    """
    Calculate mean-variance optimal weights (maximum Sharpe ratio portfolio).

    Args:
        sigma: Covariance matrix of returns (captures variances AND correlations)
        mu: Expected returns vector

    Returns:
        np.array: Optimal weights normalized to sum to 1 in absolute terms

    Mathematical Background:
        This is the tangency portfolio from Modern Portfolio Theory (Markowitz):
        w* = Σ^(-1) × μ

        The formula accounts for:
        - Higher expected returns → larger weights
        - Higher variance → smaller weights (risk penalty)
        - Correlations → diversification benefit

    Financial Intuition:
        - Overweights high-return, low-vol assets
        - Reduces exposure to highly correlated assets (less diversification benefit)
        - Can produce extreme weights if returns/vols differ significantly
        - In practice, often requires constraints (no short sales, max weight, etc.)
    """
    # Core mean-variance optimization formula
    wgt = np.linalg.inv(sigma) @ mu

    # Normalize so absolute weights sum to 1
    # This allows for long/short positions while controlling total exposure
    wgt = wgt / np.abs(wgt).sum()

    return wgt


def eqvol_weights(sigma):
    """
    Calculate equal volatility (risk parity) weights.

    Args:
        sigma: Covariance matrix (only diagonal elements are used)

    Returns:
        np.array: Weights inversely proportional to volatility

    Mathematical Background:
        w_i ∝ 1 / σ_i
        Where σ_i = sqrt(σ²_i) is the volatility (std dev) of asset i

    Financial Intuition:
        - Allocate MORE to low-volatility assets
        - Allocate LESS to high-volatility assets
        - Goal: Each position contributes equal risk to portfolio
        - Ignores expected returns (assumes all assets have same Sharpe ratio)
        - Ignores correlations (treats assets as independent)

    When to use:
        - When you believe all assets have similar risk-adjusted returns
        - When you want diversification without return forecasts
        - For risk management (avoid concentration in volatile assets)
    """
    # Extract volatility from diagonal of covariance matrix
    # np.diag(sigma) gives variances (σ²), so we take sqrt
    wgt = 1 / np.sqrt(np.diag(sigma))

    # Normalize weights
    wgt = wgt / np.abs(wgt).sum()

    return wgt


def sr_weights(sigma, mu):
    """
    Calculate Sharpe ratio weights (allocate proportional to individual Sharpe ratios).

    Args:
        sigma: Covariance matrix (only diagonal elements are used)
        mu: Expected returns vector

    Returns:
        np.array: Weights proportional to Sharpe ratio of each asset

    Mathematical Background:
        w_i ∝ μ_i / sig_i^2 = Sharpe_i / sig_i

        Note: This divides by variance (σ²), not std dev (sig)
        So it's actually proportional to SR/vol, which overweights low-vol assets

    Financial Intuition:
        - Allocate MORE to high Sharpe ratio assets
        - Allocate MORE to low volatility assets (via σ² in denominator)
        - Ignores correlations between assets
        - Simple heuristic: "bet more on better risk-adjusted opportunities"

    Limitations:
        - Doesn't account for diversification benefits (correlations)
        - Can concentrate portfolio in few high-SR assets
        - Less sophisticated than mean-variance optimization

    Comparison to optimal weights:
        - Optimal uses Σ^(-1) (accounts for correlations)
        - SR weights uses 1/σ² (ignores correlations)
    """
    # Sharpe ratio weighting formula: mu / variance
    wgt = mu / np.diag(sigma)

    # Normalize weights
    wgt = wgt / np.abs(wgt).sum()

    return wgt

def gen_strat_returns():
    """
    Generate synthetic return series for three strategies with different characteristics.

    Returns:
        pd.DataFrame: Daily returns for strategies A, B, C (2010-2019)

    Strategy Characteristics:
        A: 10% return, 10% vol, corr 0.3 with B
        B: 12% return,  6% vol, corr 0.3 with A (best Sharpe ratio)
        C:  4% return,  2% vol, uncorrelated (low vol, low return)

    Key Design Features:
        - Strategy B has highest Sharpe ratio (12% / 6% = 2.0)
        - Strategy A has moderate Sharpe ratio (10% / 10% = 1.0)
        - Strategy C has lowest Sharpe ratio (4% / 2% = 2.0) - ties with B!
        - A and B are correlated (diversification benefit is limited)
        - C is uncorrelated (provides pure diversification benefit)

    This setup tests:
        - Whether optimal weights correctly identify B as best opportunity
        - Whether C gets included despite low return (diversification value)
        - How different weighting schemes handle correlation structure
    """
    np.random.seed(5)

    # Correlation matrix: A and B are correlated (0.3), C is independent
    corr = [[1, 0.3, 0],
            [0.3, 1, 0],
            [0,   0, 1]]
    corr = np.array(corr)

    # Annualized volatilities converted to daily
    # A: 10% vol (high), B: 6% vol (medium), C: 2% vol (low)
    vols = np.diag(np.array([0.1, 0.06, 0.02])) / np.sqrt(252)

    # Build covariance matrix: Σ = V × Corr × V
    sigma = vols @ corr @ vols

    # Expected daily returns (annualized / 252)
    # A: 10% annual, B: 12% annual, C: 4% annual
    mu = np.array([0.1, 0.12, 0.04]) / 252

    # Generate business day dates (2010-2019)
    dates = pd.date_range('20100101', '20191231', freq='B')

    # Generate correlated returns from multivariate normal distribution
    rets = np.random.multivariate_normal(mu, sigma, size=len(dates))
    rets = pd.DataFrame(rets, columns=['A', 'B', 'C'], index=dates)

    return rets


# ==============================================================================
# PART 1: Generate and Visualize Data
# ==============================================================================

rets = gen_strat_returns()
print(rets)

# Plot cumulative returns to visualize strategy performance over time
# cumsum() adds up daily returns to show total gain/loss
rets.cumsum().plot()
plt.show()

# ==============================================================================
# PART 2: Analyze Individual Strategy Statistics
# ==============================================================================

# Calculate key statistics for each strategy
stats = {}
stats['ret'] = rets.mean() * 252              # Annualized return
stats['vol'] = rets.std() * np.sqrt(252)      # Annualized volatility
stats['SR'] = rets.mean() / rets.std() * np.sqrt(252)  # Sharpe ratio
stats = pd.DataFrame(stats)
print(stats)

# Expected output interpretation:
# - B should have highest Sharpe ratio (~2.0)
# - C should have good Sharpe ratio despite low return (low vol helps)
# - A should have moderate Sharpe ratio (~1.0)

# Compute covariance matrix from returns
# This captures both variances (diagonal) and correlations (off-diagonal)
sigma = rets.cov()
print(sigma)

# Compute mean returns (expected return estimates)
mu = rets.mean()
print(mu)

# ==============================================================================
# PART 3: Calculate Weights Using Different Schemes
# ==============================================================================

weights = {}

# Optimal weights: mean-variance optimization (accounts for correlations)
weights['opt'] = optimal_weights(sigma, mu)

# Equal vol weights: inverse volatility (ignores returns and correlations)
weights['eqvol'] = eqvol_weights(sigma)

# Sharpe ratio weights: proportional to mu/variance (ignores correlations)
weights['sr'] = sr_weights(sigma, mu)

weights = pd.DataFrame(weights)
weights.round(2)  # Display rounded for readability

# Expected weight patterns:
# - opt: Should favor B (high SR) and C (diversification)
# - eqvol: Should favor C (lowest vol), then B, then A
# - sr: Should favor B and C (both have SR = 2.0)

# ==============================================================================
# PART 4: Compare Portfolio Performance
# ==============================================================================

# Construct portfolio returns for each weighting scheme
combo_rets = {}

# For each scheme, multiply returns by weights and sum across strategies
# (rets * weights['opt']): element-wise multiply each strategy's returns by its weight
# .sum(1): sum across columns (axis=1) to get portfolio return each day
combo_rets['opt'] = (rets * weights['opt']).sum(1)
combo_rets['eqvol'] = (rets * weights['eqvol']).sum(1)
combo_rets['sr'] = (rets * weights['sr']).sum(1)

combo_rets = pd.DataFrame(combo_rets)

# Calculate Sharpe ratio for each portfolio
combo_sr = combo_rets.mean() / combo_rets.std() * np.sqrt(252)
print(combo_sr)

# Expected results:
# - 'opt' should have highest Sharpe ratio (uses correlations optimally)
# - 'sr' should be close to 'opt' (correlations matter less here)
# - 'eqvol' should be lower (ignores returns entirely)

# Key insight: Accounting for correlations (opt) should beat ignoring them (sr, eqvol)

# ==============================================================================
# PART 5: Leverage and Sharpe Ratio
# ==============================================================================

# Important concept: Leverage doesn't change Sharpe ratio!
# If you scale all weights by a constant (leverage up/down), SR stays the same

constant = 5  # 5x leverage

# Apply leverage: multiply weights by 5
# This increases both return AND volatility proportionally
scaled = (rets * (weights['opt'] * constant)).sum(1)

# Calculate Sharpe ratio with leverage
print(scaled.mean() / scaled.std() * np.sqrt(252))

# Result should be IDENTICAL to unleveraged optimal portfolio Sharpe ratio
# Why? SR = return/vol, and leverage scales both by same factor:
#   SR_levered = (c × return) / (c × vol) = return / vol = SR_unlevered
#
# This is why Sharpe ratio is the right metric for comparing strategies:
# it's invariant to leverage (position sizing doesn't affect risk-adjusted returns)
