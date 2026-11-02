## 2023-11-02 - Replacing Pandas iterrows() with openpyxl's dataframe_to_rows
**Learning:** Iterating over rows using `iterrows()` to append data to an openpyxl worksheet is extremely slow for large dataframes (can take ~1.8 seconds vs ~0.5 seconds for 10000 rows). Also, recreating `PatternFill` style objects on every cell instead of caching them wastes significant memory and time in Python scripts interacting with openpyxl.
**Action:** Always replace `iterrows()` with `openpyxl.utils.dataframe.dataframe_to_rows` when appending dataframes to openpyxl, and cache style objects outside loops.
