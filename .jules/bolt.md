## 2023-10-28 - Replace Pandas iterrows with vectorized grouping for aggregations
**Learning:** Using `iterrows()` combined with boolean DataFrame indexing inside loops (e.g., `df[df['col'] == val]`) is a common performance anti-pattern for aggregation tasks that causes O(N^2) complexity and severe bottlenecks on large data sets.
**Action:** When aggregating multiple DataFrames by a shared column, avoid looping. Instead, use vectorized operations such as `groupby('col')['target'].sum()`, map the grouped series back using `.map()`, and resolve calculations safely with `np.where()`.
