## 2024-10-28 - Formula/CSV Injection in Excel Exports
**Vulnerability:** Python scripts exporting Pandas DataFrames to Excel (`.xlsx`) via Openpyxl/Pandas failed to sanitize string fields, allowing execution of arbitrary formulas (CSV Injection) if the input data began with =, +, -, @, \t, or \r.
**Learning:** Always explicitly prepend a single quote (`'`) to string fields beginning with special formula characters prior to saving to Excel formats to force the spreadsheet application to treat the value as plain text.
**Prevention:** Added `sanitize_for_excel` in `excel_utils.py` and mapped it across dataframes before writing them to disk.
