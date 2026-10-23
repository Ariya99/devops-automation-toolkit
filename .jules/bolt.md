## 2024-01-01 - [Replaced Pandas iterrows with vectorized aggregations]
**Learning:** Discovered O(N^2) nested dataframe filtering inside an iterrows loop which causes significant bottlenecks for large data sizes.
**Action:** Replaced iterrows with groupby().sum() and map(), and safely handled division by zero using np.where() and replace(0, np.nan).