## 2024-10-21 - Prevent Formula Injection in Excel Exports
**Vulnerability:** Untrusted CSV data (like OPERATION_NAME) was being directly exported to Excel formats using Pandas and openpyxl without sanitization, leading to a Formula/CSV Injection vulnerability.
**Learning:** When generating Excel files dynamically from user-provided or external CSV files, formulas starting with special characters can execute malicious code on the user's machine when opened.
**Prevention:** Always sanitize string data being exported to Excel by prepending a single quote (`'`) to values starting with `=, +, -, @, \t, \r`.
