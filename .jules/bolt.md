## YYYY-MM-DD - Pandas iterrows() performance bottleneck
**Learning:** Found O(N*M) performance bottlenecks by using `iterrows()` to loop over pandas DataFrames while performing conditional sums inside the loop. This is a common anti-pattern that defeats pandas' vectorized C optimizations.
**Action:** Replace `iterrows()` loops with vectorized operations like `groupby().sum()` and `map()` or `merge()` to leverage pandas' C backend and drastically reduce time complexity from O(N*M) to O(N log N).
