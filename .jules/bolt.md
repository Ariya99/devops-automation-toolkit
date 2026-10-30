## 2023-11-20 - Excel Styling and DataFrame Export Optimization
**Learning:** In openpyxl, recreating `PatternFill` style objects for every cell in a loop is extremely inefficient. Additionally, iterating over a Pandas DataFrame using `iterrows()` to append to a worksheet is slow.
**Action:** Cache `PatternFill` style objects at the module or function level and reuse them. Use `openpyxl.utils.dataframe.dataframe_to_rows(df, index=False, header=False)` instead of `iterrows()` for significantly faster DataFrame exporting to Excel.
