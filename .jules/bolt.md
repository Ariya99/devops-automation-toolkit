## 2024-11-06 - Replacing O(n²) iterrows inside DataFrame processing
**Learning:** Using `iterrows()` with boolean masking on DataFrames (e.g. `df[df['col'] == val]`) results in O(n²) performance, becoming a major bottleneck for large datasets.
**Action:** Replace `iterrows` with pre-calculated aggregations using `groupby().sum()` mapping to vectorize the operation and achieve O(n) time complexity.
