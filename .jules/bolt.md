
## 2024-05-24 - Pandas iterrows() Anti-Pattern Optimization
**Learning:** Found a severe performance bottleneck using `iterrows()` inside `python/automated_report2.py` where repeated boolean masking (`df[df['Col'] == val]`) within an `O(N^2)` loop structure was used to lookup values from other DataFrames. This is highly inefficient in Pandas and negates the benefits of its underlying C-optimized structures.
**Action:** Always replace `.iterrows()` data merges/lookups with vectorized `.merge()` and `.groupby()` operations. When doing vectorized division, safely handle zero-division using `np.where()` with `.replace(0, np.nan)`.
