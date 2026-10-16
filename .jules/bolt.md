## 2024-05-18 - Pandas iterrows() Anti-Pattern for Aggregations
**Learning:** Found O(N^2) time complexity bottleneck caused by iterating over a Pandas DataFrame using `iterrows()` and performing filtering/summation inside the loop. In `automated_report2.py`, this approach was taking over 5 seconds for just a few thousand rows.
**Action:** Replace `iterrows()` loops with O(N) vectorized operations using `groupby()` followed by `map()` and `numpy.where()`. This yielded an over 400x speedup and significantly simplified the codebase.
