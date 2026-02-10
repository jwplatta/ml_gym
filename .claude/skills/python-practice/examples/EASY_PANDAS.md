# Easy Pandas Questions

## Very Easy

Question: Sort `sales_df` by `revenue` in descending order and return the top 5 rows.
Difficulty: VERY-EASY
Quality: AVERAGE
Answer: `sales_df.sort_values('revenue', ascending=False).head(5)`

Question: Compute total `revenue` by `region`.
Difficulty: VERY-EASY
Quality: AVERAGE
Answer: `sales_df.groupby('region')['revenue'].sum()`

Question: For each `region`, find the maximum single-row `revenue`.
Difficulty: VERY-EASY
Quality: AVERAGE
Answer: `sales_df.groupby('region')['revenue'].max()`

Question: Count how many rows each `sales_rep` has, sorted from most to fewest.
Difficulty: VERY-EASY
Quality: AVERAGE
Answer: `sales_df.groupby('sales_rep').size().sort_values(ascending=False)`

## Easy

Question: Filter `sales_df` to rows where `region` is `'North'` and `units` is greater than 80.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df[(sales_df['region'] == 'North') & (sales_df['units'] > 80)]`

Question: Sort `sales_df` first by `region` ascending, then by `revenue` descending.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df.sort_values(['region', 'revenue'], ascending=[True, False])`

Question: Compute mean `units` by `product`, sorted from highest to lowest.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df.groupby('product')['units'].mean().sort_values(ascending=False)`

Question: Compute both total `revenue` and average `units` by `region`.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df.groupby('region').agg({'revenue': 'sum', 'units': 'mean'})`

Question: Filter rows where `revenue` is above the dataset median revenue.
Difficulty: EASY
Quality: GOOD
Answer: `sales_df[sales_df['revenue'] > sales_df['revenue'].median()]`

Question: Filter `sales_df` to only products in `['Widget', 'Gadget']` and keep columns `date`, `product`, `revenue`.
Difficulty: EASY
Quality: AVERAGE
Answer: `sales_df[sales_df['product'].isin(['Widget', 'Gadget'])][['date', 'product', 'revenue']]`