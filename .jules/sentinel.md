
## 2024-05-18 - Formula/CSV Injection in Excel Exports
**Vulnerability:** Python scripts exporting Pandas DataFrames directly to Excel (.xlsx) files using `to_excel` or `openpyxl` `append` failed to sanitize string fields, allowing malicious cell payloads (e.g. `=cmd|' /C calc'!A0`) to execute arbitrary code when a victim opens the exported Excel file.
**Learning:** Pandas and openpyxl do not sanitize data by default. User-controlled strings must be neutralized before being written to an Excel file format.
**Prevention:** A central sanitization utility module (`excel_utils.py`) should be used to prepend a single quote (`'`) to string values starting with execution characters (`=`, `+`, `-`, `@`, `\t`, `\r`) before appending the data to the document.
