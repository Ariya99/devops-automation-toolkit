## 2024-11-04 - Formula/CSV Injection in Excel Exports
**Vulnerability:** Pandas DataFrame exports to Excel were vulnerable to CSV/Formula Injection if the raw data contained unescaped execution characters (e.g., `=`, `+`, `-`, `@`, `\t`, `\r`).
**Learning:** Using `pandas.to_excel` or appending `openpyxl` rows from untrusted data can lead to arbitrary command execution when users open the resulting Excel file.
**Prevention:** Create a global utility function `sanitize_for_excel` that conditionally prepends a single quote (`'`) to strings starting with execution characters, and apply it via `df.map()` to cells and `df.rename(columns=lambda x: ...)` to headers before exporting.
