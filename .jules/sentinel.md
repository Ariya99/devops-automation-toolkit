## 2024-10-21 - Formula/CSV Injection in Excel Exports
**Vulnerability:** Python scripts exporting DataFrames to Excel (`.xlsx`) via pandas/openpyxl without sanitizing string columns can lead to Formula/CSV injection. If a malicious input in a CSV begins with special execution characters (`=`, `+`, `-`, `@`, `\t`, `\r`), it might execute arbitrary commands when opened in Excel.
**Learning:** Pandas `to_excel` alone does not escape strings that look like formulas. The codebase frequently aggregates CSV data and exports to Excel, opening this vector.
**Prevention:** Apply a sanitization function to all string-type columns (e.g. using `df.select_dtypes(include=['object', 'str'])`) that prepends a single quote (`'`) to values starting with risky characters before writing to Excel or CSV.
