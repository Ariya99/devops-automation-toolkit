## 2024-11-07 - Formula Injection in Pandas to_excel
**Vulnerability:** When exporting a Pandas DataFrame to Excel via `to_excel()`, string data starting with `=`,`+`,`-`,`@`,`\t`, or `\r` can cause Formula/CSV Injection if opened in Excel.
**Learning:** Pandas `to_excel` does not automatically sanitize string fields from user-provided data.
**Prevention:** Apply a sanitization function mapping over the dataframe's cells and renaming its columns that prepends a single quote `'` to strings starting with those characters before writing to Excel.