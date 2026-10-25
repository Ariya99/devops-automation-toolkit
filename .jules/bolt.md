## 2024-10-25 - Avoid iterrows for Internal DataFrame Operations
**Learning:** Iterating over rows with `iterrows()` is extremely slow for data transformations in this codebase due to the overhead of creating Pandas Series objects for every row, particularly resulting in an O(N*M) time complexity bottleneck.
**Action:** Always prefer vectorized operations like `groupby().sum()`, `map()`, `merge()`, or `np.where()` over `iterrows()` to achieve O(N) performance and massive speedups.
