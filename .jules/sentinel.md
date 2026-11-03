## 2024-05-18 - Fix Formula Injection in Excel Exports
**Vulnerability:** Untrusted user data from CSV files was exported directly to Excel formats without sanitization, allowing Formula/CSV Injection where malicious characters like `=`, `+`, `-`, `@` could execute arbitrary commands in a user's spreadsheet application.
**Learning:** Pandas dataframes exported to Excel (`.to_excel` or via `openpyxl`) do not automatically sanitize string fields, requiring an explicit sanitization pass.
**Prevention:** Apply a shared `sanitize_for_excel` function (e.g., prepending `'`) to dataframes via `df.map()` before exporting to Excel formats.
