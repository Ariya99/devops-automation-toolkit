## 2024-10-24 - Pandas Vectorization
**Learning:** Found that Python scripts in this codebase (`python/automated_report2.py`) were processing large datasets using `.iterrows()`, creating severe O(n*m) performance bottlenecks during nested lookups.
**Action:** Always replace `.iterrows()` with vectorized Pandas operations (`groupby().sum()`, `merge()`, `join()`) to utilize C-level optimizations. For divisions, safely handle division-by-zero using `.replace(0, np.nan)` within `np.where()`.
