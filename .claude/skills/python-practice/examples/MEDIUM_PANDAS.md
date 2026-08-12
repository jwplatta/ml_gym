# Medium Pandas Questions

## Filtering with Rolling Statistics

Question: Filter `prices` to dates where `MARA` closed below `10` and `VLO` closed above its 20-day rolling mean. Return only `['MARA', 'VLO']`, sorted by `MARA` ascending.
Difficulty: MEDIUM
Quality: GOOD
Answer: `mask = (prices['MARA'] < 10) & (prices['VLO'] > prices['VLO'].rolling(20).mean()); prices.loc[mask, ['MARA', 'VLO']].sort_values('MARA')`

## Ranking and Sorting Transformations

Question: Create a DataFrame named `latest_rank` from the latest row of `prices` with columns `ticker`, `last_close`, and `pct_from_median`, where `pct_from_median = last_close / median(last_close) - 1`. Sort descending by `pct_from_median`.
Difficulty: MEDIUM
Quality: GOOD
Answer: `last_row = prices.iloc[-1]; latest_rank = pd.DataFrame({'ticker': last_row.index, 'last_close': last_row.values}); latest_rank['pct_from_median'] = latest_rank['last_close'] / latest_rank['last_close'].median() - 1; latest_rank.sort_values('pct_from_median', ascending=False)`

## Return Filters and Custom Sort Keys

Question: Using `returns`, find dates where absolute `GLD` return is greater than `1.5%` and `BLK` return is negative. Return `['BLK', 'GLD']`, sorted by absolute `GLD` move (largest first).
Difficulty: MEDIUM
Quality: GOOD
Answer: `mask = (returns['GLD'].abs() > 0.015) & (returns['BLK'] < 0); returns.loc[mask, ['BLK', 'GLD']].sort_values('GLD', key=lambda s: s.abs(), ascending=False)`

## Multi-Condition Date and Category Filters

Question: From `price_long`, filter rows where `Ticker` is in `['BLK', 'MCD', 'VLO']`, `Date` is in January 2026, and `close` is between `300` and `1200`. Return `['Date', 'Ticker', 'close']` sorted by `Date` ascending then `close` descending.
Difficulty: MEDIUM
Quality: GOOD
Answer: `mask = price_long['Ticker'].isin(['BLK', 'MCD', 'VLO']) & price_long['Date'].between('2026-01-01', '2026-01-31') & price_long['close'].between(300, 1200); price_long.loc[mask, ['Date', 'Ticker', 'close']].sort_values(['Date', 'close'], ascending=[True, False])`

## MultiIndex Selection and Filtering

Question: Using `panel` (MultiIndex by `Date`, `Ticker`), select rows for tickers `GLD` and `MARA` from `2025-12-01` to `2026-01-15` with columns `['close', 'ret_5d']`. Keep only rows where `ret_5d > 0.05` or `ret_5d < -0.05`, then sort by `ret_5d` descending.
Difficulty: MEDIUM
Quality: GOOD
Answer: `idx = pd.IndexSlice; subset = panel.loc[idx['2025-12-01':'2026-01-15', ['GLD', 'MARA']], ['close', 'ret_5d']]; subset.loc[(subset['ret_5d'] > 0.05) | (subset['ret_5d'] < -0.05)].sort_values('ret_5d', ascending=False)`
