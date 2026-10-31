## 2023-10-31 - openpyxl iteration vs dataframe_to_rows

**Learning:** Iterating through a pandas DataFrame with `iterrows()` and manually appending rows to an `openpyxl` worksheet is incredibly slow for large datasets. `openpyxl.utils.dataframe.dataframe_to_rows()` is a much faster, optimized alternative for appending DataFrame rows. Furthermore, recreating style objects like `PatternFill` inside a nested loop for every cell heavily degrades performance compared to caching the style object before the loop and reusing it.
**Action:** Use `dataframe_to_rows(df, index=False, header=False)` instead of `iterrows()` to write DataFrame data to openpyxl worksheets. Cache `openpyxl` style objects (like `PatternFill`, `Font`, `Alignment`) at the module or function level outside of any loops.
