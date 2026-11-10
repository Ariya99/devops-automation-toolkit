## 2024-11-10 - Formula / CSV Injection in Excel Exports
**Vulnerability:** Untrusted data from CSV files was exported directly to Excel spreadsheets without sanitization, allowing potential Formula/CSV Injection if a cell began with `=, +, -, or @`.
**Learning:** The codebase relies on `pandas.to_excel()` and `openpyxl` to export data. These methods write cell values as-is. If an attacker controls the input CSV, they can inject malicious formulas into the generated reports, which execute when a user opens the Excel file.
**Prevention:** Always sanitize DataFrames by prepending a single quote (`'`) to strings starting with special characters before writing them to an Excel file. This neutralizes formulas while preserving the data visually.
