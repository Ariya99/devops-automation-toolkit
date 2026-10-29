## 2024-05-18 - Optimized openpyxl dataframe writing and conditional formatting
**Learning:** `iterrows()` is slow for appending Pandas DataFrames to `openpyxl` worksheets. Creating new `PatternFill` objects repeatedly in a loop is also memory-inefficient and slow.
**Action:** Use `openpyxl.utils.dataframe.dataframe_to_rows()` (with `index=False`, `header=False`) instead of `iterrows()`. Cache style objects like `PatternFill` at the module level or outside the loop rather than recreating them for every cell.
