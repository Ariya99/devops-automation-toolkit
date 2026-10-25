## 2024-05-18 - Formula/CSV Injection in Excel Exports
**Vulnerability:** String data in pandas DataFrames exported to Excel was not sanitized, allowing for Formula/CSV Injection if a string starts with `=`, `+`, `-`, `@`, `\t`, or `\r`.
**Learning:** Python scripts exporting CSV data to Excel files using `pandas.to_excel()` or `openpyxl` are vulnerable to Formula Injection if they don't explicitly sanitize text values. This is common when handling operation names or strings from CSV input.
**Prevention:** Always prepend a single quote (`'`) to string values starting with execution characters before exporting to Excel, using a sanitization function applied via `df[col].map()`.
