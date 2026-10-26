
## 2024-10-24 - Pandas to Excel Iteration Optimization

**Learning:** Using `iterrows()` to append pandas DataFrame rows to an openpyxl Worksheet iteratively is extremely slow, especially for large datasets. Our benchmark showed a ~5.4x difference.
**Action:** Replaced `merged_df.iterrows()` with `dataframe_to_rows(merged_df, index=False, header=False)` from `openpyxl.utils.dataframe` in `python/syncprocess-fails-rating8.py`, which yielded an execution time reduction from 0.7711s to 0.1422s on 10,000 rows.
