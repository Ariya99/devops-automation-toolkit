## 2023-11-01 - Optimizing Data Processing in Python Script
**Learning:** Found an $O(N^2)$ algorithm in `automated_report2.py` where `df.iterrows()` iteratively recalculates sums across full Pandas DataFrames (`df_executed`, `df_all_status`, `df_failed`) per row. This is severely unoptimized and inefficient for large datasets.
**Action:** Replace `iterrows()` iterations with Pandas vectorized mapping (e.g. `groupby().sum()`) and explicit column assignments. This improves performance exponentially.
