## 2025-02-14 - Fix Path Traversal in CSV Script
**Vulnerability:** Path traversal vulnerability due to accepting raw user input for filenames passed directly to `pd.read_csv()` and `pd.ExcelWriter()`.
**Learning:** Taking file names directly from `input()` without validation allows attackers to read or write to arbitrary files across the file system using directory traversal payloads like `../` or `/etc/passwd`.
**Prevention:** Sanitize raw filename input using `os.path.basename()` to strip off any directory structures provided by a user before utilizing them in file operations.
