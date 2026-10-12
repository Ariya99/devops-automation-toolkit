## 2024-05-18 - Pandas iterrows O(N^2) Anti-Pattern
**Learning:** Using `df.iterrows()` inside Python combined with boolean dataframe indexing (e.g., `df[df['OPERATION_NAME'] == operation_name]`) scales extremely poorly, causing O(N^2) complexity. This causes severe bottlenecks on scripts that need to summarize over multiple files or large datasets.
**Action:** Always prefer vectorized operations like `.groupby().sum()` and `.map()` to perform aggregations in Pandas.
