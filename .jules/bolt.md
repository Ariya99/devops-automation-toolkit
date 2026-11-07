## 2024-11-07 - Pandas iteration performance in CLI scripts
**Learning:** Using `iterrows()` with boolean masking (e.g. `df[df['name'] == val]['count'].sum()`) for data aggregation inside loops leads to O(n²) time complexity. In pandas, this can easily take hundreds of milliseconds even on small datasets (1000 rows).
**Action:** Replace `iterrows()` loops for data aggregation with vectorized operations like `groupby().sum()` mapping. This achieves O(n) performance and significantly speeds up processing scripts.
