## 2024-10-14 - Fix Formula Injection in Excel Exports
**Vulnerability:** Python scripts processing CSV data and exporting to Excel (`automated_report2.py`, etc.) failed to sanitize cell values. This allowed Formula/CSV Injection where malicious data (e.g. starting with `=`) could be executed as a macro/formula when the exported file is opened in Excel.
**Learning:** Exporting untrusted data directly to Excel formats via libraries like pandas or openpyxl inherently carries Formula Injection risks.
**Prevention:** Sanitize string data before Excel export by prepending a single quote (`'`) to any string starting with special execution characters (`=`, `+`, `-`, `@`, `\t`, `\r`).
