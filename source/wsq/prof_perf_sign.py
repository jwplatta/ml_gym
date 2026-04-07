"""
Profit Calculation and Signal Analysis - Homework 2

This script introduces fundamental quant finance concepts:
1. Position tracking and P&L calculation
2. Performance statistics (average return, hit rate, max drawdown)
3. Signal analysis (testing if a predictive signal has value)

Key Concepts:
- Positions: Dollar amounts invested (positive = long, negative = short)
- Returns: Percentage change in price
- Profit & Loss (P&L): Position x Return
- Hit Rate: Percentage of positive returns
- Signal: Any indicator used to predict future returns
"""

import numpy as np

np.random.seed(2)  # For reproducible random results

# ==============================================================================
# PART 1: Basic P&L Calculation
# ==============================================================================

# Define positions in dollars for each stock
# Positive = long position (profit if stock goes up)
# Negative = short position (profit if stock goes down)
pos = {'AAPL': 1000, 'TSLA': 500, 'BAC': -250, 'GS': 1200}

# Returns for each stock (decimal form: 0.01 = 1%)
ret = {'AAPL': -0.01, 'TSLA': 0.05, 'BAC': 0.01, 'GS': 0.03}


def compute_profit(pos, ret):
    """
    Calculate profit/loss for each position.

    Args:
        pos: Dictionary mapping ticker -> position size in dollars
        ret: Dictionary mapping ticker -> return (as decimal)

    Returns:
        Dictionary mapping ticker -> profit in dollars

    Example:
        Position: $1000 in AAPL, Return: -1% → Profit: $1000 x -0.01 = -$10
        Position: -$250 in BAC, Return: +1% → Profit: -$250 x 0.01 = -$2.50
        (Short positions profit when stocks go down, lose when they go up)
    """
    profit = {}
    for key in pos:
        profit[key] = pos[key] * ret[key]

    return profit


profit = compute_profit(pos, ret)
print(profit)

# ==============================================================================
# PART 2: Performance Statistics
# ==============================================================================


def compute_stats(rets):
    """
    Calculate key performance metrics for a return series.

    Args:
        rets: List or array of returns (typically daily returns)

    Returns:
        Dictionary with statistics:
            - avg: Average (mean) return
            - hit_rate: Fraction of positive returns (win rate)
            - max_ret: Maximum single-period return

    Quant Finance Context:
        - Average return: Expected value, indicates directional bias
        - Hit rate: Consistency metric (high hit rate = frequently profitable)
        - Max return: Best single day (useful for understanding tail events)

        Note: A strategy can have low hit rate but still be profitable if
        winners are much larger than losers (positive skew)
    """
    stats = {}

    avg = 0
    hit_rate = 0
    max_ret = rets[0]  # Initialize with first return

    for ret in rets:
        # Accumulate total return for average calculation
        avg += ret

        # Count winning days
        if ret > 0:
            hit_rate += 1

        # Track maximum return
        if ret > max_ret:
            max_ret = ret

    # Convert sums to averages/rates
    stats['avg'] = avg / len(rets)
    stats['hit_rate'] = hit_rate / len(rets)
    stats['max_ret'] = max_ret

    return stats


# Generate synthetic daily returns
# Normal distribution with:
#   - Mean = 0 (no directional bias)
#   - Std = 10% annualized volatility converted to daily (divide by sqrt(252))
#   - 252 observations (one trading year)
rets = list(np.random.normal(0, 0.1 / np.sqrt(252), 252))
compute_stats(rets)

# ==============================================================================
# PART 3: Signal Analysis
# ==============================================================================

# Generate new synthetic data for signal testing
rets = list(np.random.normal(0, 0.1 / np.sqrt(252), 252))

# Generate a random signal (simulating a trading indicator)
# In practice, this could be technical indicators, ML predictions, etc.
# Normal(0, 1) distribution means ~68% of values are between -1 and +1
signal = list(np.random.normal(0, 1, 252))


def analyze_signal(rets, signal):
    """
    Test whether a signal has predictive power for future returns.

    Args:
        rets: List of actual returns
        signal: List of signal values (same length as rets)

    Returns:
        Dictionary with:
            - pos_ret: Average return when signal > 1 (strong positive)
            - neg_ret: Average return when signal < -1 (strong negative)
            - spread: Difference between pos_ret and neg_ret

    Quant Finance Context:
        This is a basic backtest of a trading signal:
        - Signal > 1: Strong buy signal → go long
        - Signal < -1: Strong sell signal → go long (we still measure realized returns)
        - Spread: Key metric! If positive and large, signal has predictive power

        A good signal should show:
            - High average return when signal is strongly positive
            - Low (ideally negative) return when signal is strongly negative
            - Large positive spread (difference)

        Note: This is a simplified analysis. Real backtests consider:
            - Transaction costs
            - Position sizing
            - Look-ahead bias
            - Out-of-sample testing
    """
    analysis = {}

    pos_ret = 0   # Sum of returns when signal is positive
    pos_ct = 0    # Count of days with positive signal
    neg_ret = 0   # Sum of returns when signal is negative
    neg_ct = 0    # Count of days with negative signal

    for idx in range(len(rets)):
        # When signal is strongly positive (> 1 standard deviation)
        if signal[idx] > 1:
            pos_ct += 1
            pos_ret += rets[idx]

        # When signal is strongly negative (< -1 standard deviation)
        elif signal[idx] < -1:
            neg_ct += 1
            neg_ret += rets[idx]

    # Calculate average returns for each regime
    analysis['neg_ret'] = neg_ret / neg_ct
    analysis['pos_ret'] = pos_ret / pos_ct

    # Spread: The "alpha" or edge from the signal
    # Positive spread = signal has predictive value
    # Zero spread = signal is useless (no better than random)
    # Negative spread = signal is anti-predictive (fade it!)
    analysis['spread'] = round(analysis['pos_ret'] - analysis['neg_ret'], 4)

    return analysis


# Test the signal analysis
# Since both rets and signal are random, we expect spread ≈ 0 (no predictive power)
results = analyze_signal(rets, rets)

print(results)
