## 2024-05-24 - Pandas iterrows() anti-pattern in reporting scripts
**Learning:** Found O(N*M) performance bottleneck in Pandas CLI scripts due to `iterrows()` combined with DataFrame filtering/summing per row.
**Action:** Always replace `iterrows()` with vectorized `.groupby().sum()`, `.map()`, and `np.where()` for faster execution when doing large data aggregation, taking care to safely handle division by zero using `.replace(0, np.nan)`.
