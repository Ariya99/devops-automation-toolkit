## 2024-05-01 - CSV/Formula Injection in Excel Exports
**Vulnerability:** User-controlled string data written directly to Excel files via pandas or openpyxl could lead to CSV/Formula injection.
**Learning:** If user-supplied data starts with special formula execution characters (`=`, `+`, `-`, `@`, `\t`, `\r`), Excel may attempt to execute it as a formula, which could lead to arbitrary command execution on the system opening the file.
**Prevention:** Always sanitize string data in pandas dataframes or any other output format intended for Excel by prepending a single quote (`'`) to values starting with these special characters before exporting.
