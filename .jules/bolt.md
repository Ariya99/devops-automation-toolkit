
## 2025-02-28 - Vectorize pandas aggregation
**Learning:** Replaced iterrows() and boolean indexing with vectorized groupby() and merge() in Pandas scripts to eliminate O(n²) bottleneck.
**Action:** Always favor vectorized pandas operations like `groupby`, `merge`, and `np.where` over iterative operations like `iterrows` for dataset manipulation to improve performance significantly.
