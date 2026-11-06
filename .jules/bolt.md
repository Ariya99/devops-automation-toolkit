## 2024-05-24 - Pandas and openpyxl Performance Anti-patterns
**Learning:** In pandas, iterating over rows using `iterrows()` to manually calculate aggregations or apply changes row-by-row is O(n²) and extremely slow. Similarly, appending data to an openpyxl `Workbook` row-by-row with `iterrows()` is slow. In openpyxl, re-creating `PatternFill` objects repeatedly within a large loop significantly slows down applying styles.
**Action:**
1. Use vectorized pandas operations (e.g. `groupby().sum().map()`, `np.where()`) instead of iterating to calculate aggregations.
2. Use `openpyxl.utils.dataframe.dataframe_to_rows()` (with `index=False, header=False`) instead of `iterrows()` for exporting to Excel.
3. Cache openpyxl style objects (like `PatternFill`) outside of loops to prevent recreating them on every iteration.
