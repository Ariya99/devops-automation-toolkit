## 2024-10-24 - Pandas iterrows() bottleneck
**Learning:** Found an O(N²) performance anti-pattern in `python/automated_report2.py` where `df.iterrows()` and boolean indexing are used together for aggregations.
**Action:** Replace `iterrows()` with vectorized pandas operations like `.groupby().sum()` and `.map()` for ~250x speedups. Always use vectorized mapping/merging when aggregating data from multiple dataframes based on a key.
