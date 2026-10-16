## 2024-10-16 - Pandas Anti-Pattern
**Learning:** Found O(N^2) complexity in `python/automated_report2.py` due to using `.iterrows()` while doing repetitive `.sum()` filtering on internal DataFrames. Vectorized operations provided over 200x speedup for 10k rows.
**Action:** Always check Pandas scripts in `python/` for the `.iterrows()` anti-pattern and replace it with `groupby().sum()` and `.map()` where possible to prevent serious performance bottlenecks.
