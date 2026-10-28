## 2025-02-21 - Optimize openpyxl Iteration
**Learning:** Using `iterrows()` for inserting Pandas DataFrames into openpyxl is an anti-pattern and very slow. Similarly, instantiating `PatternFill` inside cell iteration loops wastes memory.
**Action:** Always use `openpyxl.utils.dataframe.dataframe_to_rows()` for inserting DataFrames into openpyxl, and cache style objects like `PatternFill` before the loop. Avoid `iterrows()` for manipulating data within Pandas.
