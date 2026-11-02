## 2023-11-02 - Formula Injection in Pandas to Excel Exports
**Vulnerability:** User-provided string data processed by Pandas and exported to Excel via openpyxl (`to_excel` or `ws.append`) was not being sanitized. This allowed for Formula/CSV Injection if a string started with `=`, `+`, `-`, `@`, `\t`, or `\r`.
**Learning:** Pandas data manipulation and standard export functions do not automatically sanitize execution characters, leaving downstream applications (like Excel or CSV viewers) vulnerable to formula injection.
**Prevention:** Always apply a sanitization function to all string columns in Pandas DataFrames (e.g., prepending a single quote `'` to strings starting with execution characters) *before* exporting the data to formats commonly opened in Excel.
