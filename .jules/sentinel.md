## 2024-05-24 - Prevent Formula/CSV Injection in Excel Exports
**Vulnerability:** Python scripts exporting dataframes to Excel via Pandas/Openpyxl did not sanitize strings, leaving them vulnerable to Formula/CSV Injection if inputs started with characters like `=`, `+`, `-`, or `@`.
**Learning:** Formula injection allows attackers to execute arbitrary code or exfiltrate data when a user opens the resulting Excel file and accepts prompts. This pattern is common in data science/analytics scripts that directly export unvalidated data.
**Prevention:** Always sanitize string data being written to Excel/CSV by prepending a single quote (`'`) to any string that begins with dangerous execution characters (`=`, `+`, `-`, `@`, `\t`, `\r`).
