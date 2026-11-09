## 2024-05-30 - Formula/CSV Injection in Excel Exports
**Vulnerability:** Untrusted input from CSV files was exported to Excel formats without sanitization, allowing Formula/CSV injection.
**Learning:** Pandas dataframes exported to Excel via `openpyxl` or `to_excel` do not automatically escape special characters (`=`, `+`, `-`, `@`, `\t`, `\r`), which execute formulas in Excel.
**Prevention:** Always sanitize both string data cells and column headers by prepending a single quote (`'`) to values starting with execution characters before exporting to Excel.
