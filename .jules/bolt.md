## 2024-11-20 - Vectorized Pandas Aggregation
**Learning:** Iterating over Pandas DataFrames using `iterrows()` while performing boolean masking inside the loop creates an O(n^2) bottleneck. Using vectorized operations like `groupby().sum()` mapping changes the time complexity to O(n).
**Action:** Always prefer `groupby().sum()` and mapping techniques instead of `iterrows()` for aggregation in data processing scripts.
