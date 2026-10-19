## 2026-10-19 - [Vectorized Pandas Operations]
**Learning:** The `iterrows()` pattern is an anti-pattern in Pandas and can cause severe bottlenecks when iterating and computing across multiple DataFrames (O(N*M) time complexity).
**Action:** Use vectorized operations like `groupby().sum()`, `map()`, and `np.where()` to perform lookups and calculations in O(N) time. Also, to prevent `RuntimeWarning` during vectorized division, safely handle division by zero using `.replace(0, np.nan)` on the denominator before dividing.
