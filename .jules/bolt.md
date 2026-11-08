## 2025-02-18 - Replacing iterrows() with dataframe_to_rows()
**Learning:** Using `iterrows()` in pandas to append data to openpyxl worksheets is highly inefficient (O(n) overhead per row). Using openpyxl's `dataframe_to_rows()` avoids Pandas Series instantiation per row, greatly improving Excel export performance.
**Action:** When exporting Pandas DataFrames to Excel worksheets via openpyxl, replace `for idx, row in df.iterrows(): ws.append(row.tolist())` loops with `for row in dataframe_to_rows(df, index=False, header=False): ws.append(row)`.

## 2025-02-18 - Replacing boolean masking inside iterrows with vectorized groupby mapping
**Learning:** Using boolean masking inside `iterrows` (e.g., `df[df['name'] == val]['count'].sum()`) results in O(n^2) time complexity. Pre-calculating aggregates via `groupby().sum()` and mapping them back reduces this to O(n).
**Action:** When aggregating data in pandas across different dataframes based on a common key, always use `groupby().sum()` combined with `map()` instead of loop-based boolean masking.
