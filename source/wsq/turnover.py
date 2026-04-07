"""
Portfolio Turnover and Transaction Cost Analysis

This script demonstrates a critical real-world constraint in trading:
transaction costs erode returns, especially for high-turnover strategies.

Key Concepts:
1. Mean-reversion strategy: Buy recent losers, sell recent winners
2. Turnover: How much the portfolio changes each period (triggers trading costs)
3. Gross returns: Performance before transaction costs
4. Net returns: Performance after transaction costs (what you actually earn)
5. Transaction costs: Commissions + slippage (market impact)

Central Question: Does the strategy's alpha survive transaction costs?

Real-world Application:
- High-frequency strategies need very low costs (HFT, market making)
- Low-frequency strategies can tolerate higher costs (value investing)
- Crypto markets often have higher costs than equities
"""

from datetime import datetime

import numpy as np
import pandas as pd
from binance.client import Client as bnb_client

# Initialize Binance API client (no authentication needed for historical data)
client = bnb_client()


def get_binance_px(symbol, freq, start_ts='2019-01-01'):
    """
    Download historical cryptocurrency price data from Binance.

    Args:
        symbol: Trading pair symbol (e.g., 'BTCUSDT')
        freq: Frequency/timeframe (e.g., '1h', '4h', '1d')
        start_ts: Start date as string (default: '2019-01-01')

    Returns:
        pd.DataFrame: Historical OHLCV data with timestamps

    Data Columns:
        - open_time/close_time: Candle start/end timestamps
        - open/high/low/close: OHLC prices
        - volume: Base asset volume
        - quote_volume: Quote asset volume (USDT)
        - num_trades: Number of trades in period
        - taker_base/quote_volume: Volume from taker orders
    """
    # Fetch historical klines (candlestick) data from Binance API
    data = client.get_historical_klines(symbol, freq, start_ts)

    # Define column names for the raw data
    columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_volume',
               'num_trades', 'taker_base_volume', 'taker_quote_volume', 'ignore']

    data = pd.DataFrame(data, columns=columns)

    # Convert from POSIX timestamp (milliseconds since Jan 1, 1970) to datetime
    # Divide by 1000 to convert milliseconds to seconds
    data['open_time'] = data['open_time'].map(lambda x: datetime.utcfromtimestamp(x / 1000))
    data['close_time'] = data['close_time'].map(lambda x: datetime.utcfromtimestamp(x / 1000))

    return data


# ==============================================================================
# PART 1: Data Download and Preparation
# ==============================================================================

# Universe of cryptocurrencies to trade
# These are major coins traded against USDT (Tether stablecoin)
univ = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'BNBUSDT', 'XRPUSDT', 'DOTUSDT', 'MATICUSDT']

# Trading frequency: 1-hour bars
# Higher frequency → more data points, potentially more turnover
freq = '1h'

# Download price data for each symbol
px = {}
for x in univ:
    data = get_binance_px(x, freq)
    # Extract close price and set timestamp as index
    px[x] = data.set_index('open_time')['close']

# Convert to DataFrame (each column is a crypto)
px = pd.DataFrame(px).astype(float)

# Reindex to ensure continuous hourly timeline (fills gaps with NaN)
# This is important because crypto trades 24/7 but API might have gaps
px = px.reindex(pd.date_range(px.index[0], px.index[-1], freq=freq))

# Calculate returns: (price[t] - price[t-1]) / price[t-1]
# pct_change() is equivalent to: px / px.shift() - 1
ret = px.pct_change()


# ==============================================================================
# PART 2: Construct Mean-Reversion Strategy
# ==============================================================================

# This strategy bets on mean reversion: recent losers bounce back, recent winners fade
# Process: Signal → Rank → Demean → Normalize

# Step 1: Calculate signal (average return over lookback horizon)
hor = 1  # Lookback horizon in hours

# Compute rolling mean return for each crypto
# Multiply by -1 because we want to BUY losers (negative returns) and SELL winners
# This is contrarian/mean-reversion logic
signal = -1.0 * ret.rolling(hor, min_periods=1).mean()

# Step 2: Rank signal across cryptos (1 = lowest return, 7 = highest return)
# rank(1) ranks across columns (axis=1), so for each time period
# After negation: high rank = recent loser (we want to buy)
port = signal.rank(1)

# Step 3: Demean the ranks (subtract cross-sectional mean)
# This creates dollar-neutral portfolio: long positions offset by short positions
# port.mean(1) computes mean rank across cryptos at each time
# subtract(port.mean(1), 0) subtracts this mean from each crypto (axis=0 is index)
port = port.subtract(port.mean(1), 0)

# After demeaning:
# - Positive weights: long positions (buy recent losers)
# - Negative weights: short positions (sell recent winners)
# - Sum of weights ≈ 0 (market neutral)

# Step 4: Normalize weights so absolute values sum to 1
# This controls total exposure (leverage)
# port.abs().sum(1) gives sum of absolute weights at each time
# divide(..., 0) divides each crypto weight by this sum
port = port.divide(port.abs().sum(1), 0)

# Final portfolio characteristics:
# - Market neutral (sum of weights ≈ 0)
# - Fully invested (sum of |weights| = 1)
# - Mean-reverting (long losers, short winners)
port

# ==============================================================================
# PART 3: Analyze Portfolio Turnover
# ==============================================================================

# Turnover measures how much the portfolio changes each period
# High turnover = more rebalancing = higher transaction costs

# Turnover calculation:
# TO[t] = Σ|weight[t] - weight[t-1]|
#
# Example:
# - Old weights: [0.3, 0.2, 0.5]
# - New weights: [0.4, 0.3, 0.3]
# - Changes: [0.1, 0.1, -0.2]
# - Turnover: |0.1| + |0.1| + |0.2| = 0.4 (40% of portfolio traded)

to = (port.fillna(0) - port.shift().fillna(0)).abs().sum(1)
to

# Visualize turnover over time
# Spikes indicate major portfolio rebalancing
to.plot()

# Average turnover: how much we trade per period on average
# For hourly data, this is average hourly turnover
to.mean()

# Interpretation:
# - Turnover of 0.5 means 50% of portfolio changes each hour
# - Over 24 hours, that's 12x turnover per day (very high!)
# - High turnover strategies need very low transaction costs to be profitable

# ==============================================================================
# PART 4: Calculate Gross Returns (Before Costs)
# ==============================================================================

# Gross return: what you'd earn in a frictionless world (no costs)
# Formula: R[t] = Σ(weight[t-1] × return[t])
#
# Key point: Use LAGGED weights (port.shift())
# - We decide weights at time t-1
# - We earn returns at time t
# - This avoids look-ahead bias

gross_ret = (port.shift() * ret).sum(1)

# Calculate annualized Sharpe ratio
# Multiply by sqrt(24*365) because data is hourly:
# - 24 hours per day
# - 365 days per year
# - Total: 8,760 hours per year
sr = gross_ret.mean() / gross_ret.std() * np.sqrt(24 * 365)
print("Sharpe ratio:", sr)

# ==============================================================================
# PART 5: Calculate Net Returns (After Transaction Costs)
# ==============================================================================

# Transaction costs have two components:
# 1. Commission: Fee charged by exchange (basis points of trade value)
# 2. Slippage: Market impact + bid-ask spread (implicit cost)

# Total transaction cost estimate
tcost_bps = 20  # 20 basis points = 0.20% per trade

# Cost per period = Turnover × Cost per unit traded
# - Turnover: fraction of portfolio traded
# - tcost_bps * 1e-4: convert basis points to decimal (20 bps = 0.0020)
#
# Example:
# - Turnover = 0.5 (50% of portfolio traded)
# - Cost = 0.5 × 0.0020 = 0.001 = 0.1% return drag

# Net return = Gross return - Transaction costs
net_ret = gross_ret.subtract(to * tcost_bps * 1e-4, fill_value=0)

# Calculate net Sharpe ratio (what you actually earn)
net_sr = net_ret.mean() / net_ret.std() * np.sqrt(24 * 365)
print("Net Sharpe ratio:", net_sr)

# INTERPRETATION:
# Compare gross SR vs net SR:
# - If net SR is much lower, transaction costs are killing the strategy
# - If net SR is still positive, strategy survives costs
# - If net SR is negative, strategy is unprofitable in practice
#
# Key lesson: Always test strategies net of realistic transaction costs!
# Many strategies that look good on paper fail in live trading due to costs.
