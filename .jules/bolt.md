## 2023-10-20 - Vectorized Pandas Operations over iterrows
**Learning:** Found that using `.iterrows()` in Pandas for calculating per-row metrics on large datasets in `automated_report2.py` acts as a massive performance bottleneck, scaling poorly (O(n*m)) as dataset size increases.
**Action:** Always replace `.iterrows()` iteration with vectorized Pandas operations, such as `.groupby().sum()` combined with `.map()`. When performing vectorized division, handle potential `ZeroDivisionError`s safely by replacing zeros with `np.nan` prior to division within `np.where()`.
