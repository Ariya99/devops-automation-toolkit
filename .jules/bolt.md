## 2024-05-24 - Pandas iterrows() anti-pattern
**Learning:** Found an `iterrows()` loop performing aggregations and mappings in `python/automated_report2.py`, which is an anti-pattern causing a severe performance bottleneck for data manipulation.
**Action:** Replaced the loop with vectorized Pandas operations: `.groupby().sum()`, `.map()`, and vectorized conditional division with `np.where()`. Always use vectorized operations instead of iterating over rows in pandas.
