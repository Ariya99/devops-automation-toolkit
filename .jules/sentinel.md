## 2024-10-18 - Prevent CSV/Formula Injection in Data Exports
**Vulnerability:** Untrusted string data exported to CSV or Excel without sanitization can be interpreted as formulas, leading to arbitrary code execution if a user opens the file in Excel or other spreadsheet software (CSV/Formula Injection).
**Learning:** DevOps scripts that aggregate and export execution logs or reports often overlook this risk. Even operational names or log entries can contain malicious payloads beginning with special characters like `=`, `+`, `-`, `@`.
**Prevention:** Always sanitize string outputs before exporting to spreadsheet formats by prepending a single quote (`'`) to any value starting with `=`, `+`, `-`, `@`, `\t`, or `\r`.
