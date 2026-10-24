## 2023-10-24 - Formula Injection in Excel Exports
**Vulnerability:** Unsanitized Pandas DataFrames exported to Excel (Formula/CSV Injection).
**Learning:** String values starting with special characters like `=` can execute malicious formulas when the exported file is opened in Excel.
**Prevention:** Prepend a single quote (`'`) to strings starting with `=`, `+`, `-`, `@`, `\t`, `\r` before writing to Excel or CSV.
