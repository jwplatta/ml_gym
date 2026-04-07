"""
Fundamental Stock Data Loading

This script demonstrates how to load fundamental financial statement data from two sources:
1. SimFin: Bulk historical data for many companies (requires free API key)
2. Yahoo Finance: Individual company data with most recent updates

Fundamental Data vs Price Data:
- Price data: Market's perception (what investors think)
- Fundamental data: Company's reality (actual business performance)

The Three Core Financial Statements:
1. Income Statement: Revenue, expenses, profit (earnings power)
2. Balance Sheet: Assets, liabilities, equity (financial health)
3. Cash Flow Statement: Cash in/out (liquidity, sustainability)

Common Use Cases:
- Calculate valuation ratios (P/E, P/B, EV/EBITDA)
- Screen for value/growth stocks
- Build factor models (profitability, quality)
- Predict future returns using fundamentals
"""

import os

import dotenv
import simfin as sf
import yfinance as yf

# Load environment variables (API keys, data directories)
dotenv.load_dotenv()

# ==============================================================================
# SimFin: Bulk Fundamental Data
# ==============================================================================

# Configure SimFin API (get free key from simfin.com)
api_key = os.getenv('SIMFIN_API_KEY')
sf.set_data_dir(os.getenv('SIMFIN_DATA_DIR', '~/simfin_data/'))
sf.config.set_api_key(api_key=api_key)

# Load quarterly fundamental data for all US stocks
# This downloads data locally for fast subsequent access
income = sf.load_income(variant='quarterly', market='us')
balance_sheet = sf.load_balance(variant='quarterly', market='us')
cash_flow = sf.load_cashflow(variant='quarterly', market='us')

# Inspect available fields
print(income.columns)
print(balance_sheet.columns)
print(cash_flow.columns)

# Common fields you'd typically use:
# Income: Revenue, Gross Profit, Operating Income, Net Income, EPS
# Balance: Total Assets, Total Debt, Stockholders Equity, Cash & Equivalents
# Cash Flow: Operating Cash Flow, Free Cash Flow, Capex


def describe_data(data, data_name):
    """Print summary statistics about the fundamental dataset."""
    size = len(set(data.index.get_level_values(0)))  # Number of unique tickers
    start_dt = data.index.get_level_values(1).min().strftime('%Y%m%d')
    end_dt = data.index.get_level_values(1).max().strftime('%Y%m%d')
    print(f'{data_name}: {size} tickers. Date range: {start_dt} to {end_dt}')


describe_data(income, 'Income Data')
describe_data(balance_sheet, 'Balance Sheet Data')
describe_data(cash_flow, 'Cash Flow Data')

# ==============================================================================
# Yahoo Finance: Recent Individual Stock Data
# ==============================================================================

# SimFin data lags ~1 month; Yahoo Finance is more current
# Use yfinance for latest quarter or individual stock deep-dives

yf_ticker = yf.Ticker('AAPL')

# Load quarterly fundamental statements for AAPL
income_yf = yf_ticker.quarterly_financials
cash_flow_yf = yf_ticker.quarterly_cashflow
balance_sheet_yf = yf_ticker.quarterly_balance_sheet

# Common Fundamental Ratios to Calculate:
# ----------------------------------------
# Profitability:
#   - ROE = Net Income / Stockholders Equity
#   - ROA = Net Income / Total Assets
#   - Gross Margin = Gross Profit / Revenue
#
# Valuation (combine with price data):
#   - P/E = Market Cap / Net Income
#   - P/B = Market Cap / Book Value (equity)
#   - EV/EBITDA = Enterprise Value / EBITDA
#
# Growth:
#   - Revenue growth = (Revenue[t] - Revenue[t-1]) / Revenue[t-1]
#   - Earnings growth = Year-over-year EPS change
#
# Financial Health:
#   - Debt/Equity = Total Debt / Stockholders Equity
#   - Current Ratio = Current Assets / Current Liabilities
#   - Free Cash Flow = Operating Cash Flow - Capex
#
# Quality Factors (predict future returns):
#   - High ROE + Low Debt = Quality companies
#   - Consistent earnings growth = Stable businesses
#   - Positive free cash flow = Sustainable operations
