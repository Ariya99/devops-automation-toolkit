
## 2024-05-24 - Pandas Aggregation with iterrows
**Learning:** Found a common anti-pattern where script iterations were repeatedly filtering large Pandas DataFrames inside an `iterrows()` loop (resulting in O(N^2) complexity) instead of utilizing pre-aggregation (like `groupby().sum()`) and mapping.
**Action:** Use `groupby` to pre-calculate sums or other aggregations on the full dataframe first, then use `map` to apply the results to the target dataframe, which can turn an O(N^2) operation into O(N) and run 50x+ faster.
