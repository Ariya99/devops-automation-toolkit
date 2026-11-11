## 2024-03-24 - Formula/CSV Injection in Pandas Excel Export
**Vulnerability:** User-provided or external CSV data exported to Excel via `pandas.DataFrame.to_excel` without sanitizing strings that begin with formula execution characters (`=`, `+`, `-`, `@`, etc). This allowed Formula Injection (DDE Injection).
**Learning:** Pandas `to_excel` does not automatically sanitize string content, meaning CSVs with malicious payloads get exported into runnable Excel formulas.
**Prevention:** Always map a sanitization function over DataFrames (e.g., `df.map(func)`) to prepend a single quote `'` to strings starting with special characters before exporting them to Excel formats.
