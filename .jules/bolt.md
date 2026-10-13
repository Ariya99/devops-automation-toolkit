## 2024-05-24 - Pandas iterrows() bottleneck
**Learning:** Found an O(N^2) loop using `iterrows()` and boolean indexing in a pandas script (`automated_report2.py`). This is a classic anti-pattern that slows down processing on large datasets.
**Action:** Always replace `iterrows()` with vectorized operations like `groupby().sum()` and `map()` when doing lookup and aggregation. Use masks for conditional updates to prevent division-by-zero.
