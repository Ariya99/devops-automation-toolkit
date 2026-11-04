## 2023-10-18 - Pandas Iterrows Bottleneck

**Learning:** Iterating through rows with `df.iterrows()` and filtering a different dataframe on each iteration is an extreme performance bottleneck (O(N*M)) that causes scripts to run in O(seconds) rather than O(milliseconds).

**Action:** Always replace `iterrows()` + internal filters with vectorized group-by aggregations and `.map()` or `.merge()` for mapping aggregated data to target dataframes.
