## 2024-05-24 - [Vectorized Operations vs iterrows()]
**Learning:** Pandas `.iterrows()` loops containing inner mask-searches over full dataframes result in immense O(n*m) complexity bottlenecks. When iterating large data sets and repeatedly searching them inside the loop, the performance degrades massively.
**Action:** Always replace `.iterrows()` with native vectorized grouping, masking, mapping, and merging like `.groupby().sum()`, `pd.merge()`, `.map()`, and `np.where()`.
