## 2024-11-06 - Prevent CSV/Formula Injection in Excel Exports
**Vulnerability:** Python scripts exporting unvalidated string data from CSVs into Excel files (e.g. using `to_excel` or `ws.append()`) are susceptible to Formula/CSV Injection if strings start with `=`, `+`, `-`, or `@`.
**Learning:** This repo contains multiple Python scripts converting CSV status reports into `.xlsx` using pandas/openpyxl without sanitizing cell values.
**Prevention:** Always prepend a single quote (`'`) to string fields starting with special formula characters before writing to Excel files. Use the shared utility in `python/excel_utils.py`.
