## 2024-05-15 - Vectorizing Pandas iterrows and Boolean Masking
**Learning:** Found an O(n^2) performance bottleneck in `python/automated_report2.py` where `df.iterrows()` combined with inner loop boolean masking (`df[df['OPERATION_NAME'] == name]`) was used for aggregations.
**Action:** Replace `iterrows()` and boolean masking with vectorized `groupby().sum()` and mapping to convert O(n^2) time complexity to O(n), vastly improving performance on large datasets.
