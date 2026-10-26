
## 2024-10-26 - Vectorizing DataFrame Construction
**Learning:** In Pandas reporting scripts (`automated_report2.py`), building up rows via `df.iterrows()` and querying individual subsets per row (`df[df['COL'] == value].sum()`) acts as a massive O(N^2) bottleneck for large generated datasets.
**Action:** Replace `iterrows()` row-by-row lookups with vectorized aggregations (`.groupby().sum()`) and mapping (`.map()`), resolving division by zero safely using `np.where()`. This scales instantly rather than lagging severely under moderate data loads.
