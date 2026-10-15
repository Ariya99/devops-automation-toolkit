## 2024-05-24 - [Formula/CSV Injection in Python Exports]
**Vulnerability:** String columns (like `OPERATION_NAME`) were being directly exported to Excel/CSV without sanitization. If any of the strings started with special characters like `=`, `+`, `-`, or `@`, they could be executed as formulas by Excel upon opening the file, potentially leading to macro injection/remote code execution.
**Learning:** External or user-provided strings should never be implicitly trusted when formatting for spreadsheet software.
**Prevention:** Sanitize text values destined for spreadsheet export by prepending a single quote (`'`) to strings that begin with formula execution characters, effectively forcing the application to interpret them as plain text.
