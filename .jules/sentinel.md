## 2024-10-26 - Fix Path Traversal and Formula Injection
**Vulnerability:** Path Traversal and Formula Injection
**Learning:** Python scripts directly taking user input for file operations or exporting unsanitized data to CSV/Excel are vulnerable to path traversal and CSV injection.
**Prevention:** Always strip directory traversal characters from user-provided file names. Always sanitize string data being exported to Excel formats by prepending a single quote to values starting with special execution characters (=, +, -, @, \t, \r).
