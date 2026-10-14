## 2024-10-24 - Pandas iterrows Bottleneck
**Learning:** The `iterrows()` loop combined with boolean indexing (`df[df['col'] == val]`) creates an O(N*M) bottleneck in Python scripts dealing with large CSV reports.
**Action:** Always replace `iterrows()` with vectorized operations like `groupby().sum()` and `map()` for data aggregation to achieve O(N+M) performance.
