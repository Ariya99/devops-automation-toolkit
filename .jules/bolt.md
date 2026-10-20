## 2023-10-24 - Pandas iterrows Anti-Pattern
**Learning:** Found a major performance bottleneck where `iterrows()` was used with `.loc` lookups and `.sum()` on slices for each row in a DataFrame. This creates O(N^2) complexity and scales terribly with dataset size.
**Action:** When performing data aggregations or mappings in Pandas, avoid `iterrows()` entirely. Use vectorized operations like `groupby().sum()`, `map()`, and `np.where()` (for safe conditional logic like division) instead. This changes complexity from O(N^2) to O(N) and executes at C-level speeds.
