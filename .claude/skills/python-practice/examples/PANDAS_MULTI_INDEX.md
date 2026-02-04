# Pandas Multi-index Examples

## Easy

Question: Using the sales DataFrame (MultiIndex index: Region, Store), select the row for Region='East' and Store='Store_2' and return it as a Series.
Answer: `sales.loc[('East', 'Store_2')]`

Question: Using `price_long` (a Series with MultiIndex index: `Date`, `Ticker`), get all prices for ticker `AMD` as a Series indexed only by `Date`.
Answer: price_long.xs('AMD', level='Ticker')

Question: `prices_multi_cols` has MultiIndex columns with levels (close, Ticker). Select the close prices for COST and IWM and return a DataFrame with those two columns.
Answer: prices_multi_cols.loc[:, ('close', ['COST', 'IWM'])]

Question: From price_long, select all tickers for the date 2025-10-02. Return a Series indexed by Ticker.
Answer: price_long.xs(pd.Timestamp('2025-10-02'), level='Date')

Question: Using sales, compute total revenue by Region (sum over stores). Return a Series indexed by Region.
Answer: `sales['revenue'].groupby(level='Region').sum()`

## Medium

## Hard
