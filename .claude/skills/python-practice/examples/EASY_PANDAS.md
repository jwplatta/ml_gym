# Easy Pandas Questions

## Filtering

Question: Filter `sales_df` to rows where `region` is `'North'` and `units` is greater than 80.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df[(sales_df['region'] == 'North') & (sales_df['units'] > 80)]`

Question: Filter rows where `revenue` is above the dataset median revenue.
Difficulty: EASY
Quality: GOOD
Answer: `sales_df[sales_df['revenue'] > sales_df['revenue'].median()]`

Question: Filter `sales_df` to only products in `['Widget', 'Gadget']` and keep columns `date`, `product`, `revenue`.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df[sales_df['product'].isin(['Widget', 'Gadget'])][['date', 'product', 'revenue']]`

## Sorting

Question: Sort `sales_df` first by `region` ascending, then by `revenue` descending.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df.sort_values(['region', 'revenue'], ascending=[True, False])`

## GroupBy Aggregation

Question: Compute mean `units` by `product`, sorted from highest to lowest.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df.groupby('product')['units'].mean().sort_values(ascending=False)`

Question: Compute both total `revenue` and average `units` by `region`.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df.groupby('region').agg({'revenue': 'sum', 'units': 'mean'})`

## Label Selection and Sorting

Question: Using `prices`, select rows from `2025-10-01` through `2025-11-14` and columns `['BLK', 'VLO', 'GLD']`. Return the result sorted by date descending.
Difficulty: EASY
Quality: GOOD
Answer: `prices.loc['2025-10-01':'2025-11-14', ['BLK', 'VLO', 'GLD']].sort_index(ascending=False)`

## Positional Selection and Derived Columns

Question: Take every 7th row from `prices` by position (starting from row 0), keep only `['BLK', 'MARA', 'VLO']`, add a column `spread = VLO - MARA`, and sort by `spread` descending.
Difficulty: EASY
Quality: GOOD
Answer: `result = prices.iloc[::7, :].loc[:, ['BLK', 'MARA', 'VLO']].copy(); result['spread'] = result['VLO'] - result['MARA']; result.sort_values('spread', ascending=False)`

## Quantile Filters

Question: Find dates where `BLK` is in the top 20% of its own historical prices and `MARA` is in the bottom 25% of its own historical prices on the same date. Return `['BLK', 'MARA']` sorted by date.
Difficulty: EASY
Quality: GOOD
Answer: `blk_cut = prices['BLK'].quantile(0.80); mara_cut = prices['MARA'].quantile(0.25); prices.loc[(prices['BLK'] >= blk_cut) & (prices['MARA'] <= mara_cut), ['BLK', 'MARA']].sort_index()`
