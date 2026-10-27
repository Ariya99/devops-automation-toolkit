## 2024-10-27 - Caching OpenPyXL Style Objects
**Learning:** Recreating `PatternFill` style objects inside a loop in OpenPyXL is extremely slow and memory inefficient.
**Action:** Cache style objects like `PatternFill` at the module or function level and reuse them rather than recreating them for every cell.

## 2024-10-27 - Iterrows vs Dataframe_to_rows
**Learning:** Using `pandas.DataFrame.iterrows()` to append rows to an OpenPyXL worksheet is significantly slower than using `openpyxl.utils.dataframe.dataframe_to_rows()`.
**Action:** Always use `dataframe_to_rows(df, index=False, header=False)` when appending DataFrames to openpyxl worksheets.
