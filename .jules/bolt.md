
## 2024-05-13 - Pandas Optimization
**Learning:** This codebase uses data analysis and report generation via Pandas dataframes. A common anti-pattern encountered was row-by-row iteration using `iterrows()` to manually calculate aggregated values, which creates a huge O(N * M) bottleneck when joining or summarizing large data sets.
**Action:** Always prefer vectorization utilizing `groupby()`, `map()`, and direct column arithmetic. Replaced `iterrows()` loop filtering with O(N+M) `df['col'].map(df2.groupby('key')['val'].sum())` for counting instances efficiently.
