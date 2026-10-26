## 2024-10-26 - Path Traversal Mitigation
**Vulnerability:** Constructing file paths from unsanitized user input allows path traversal.
**Learning:** Always sanitize user-provided file names using `os.path.basename()` when writing files to a specific directory to prevent them from breaking out of intended directories.
**Prevention:** Strip directory paths from file names using `os.path.basename()` before utilizing them in file operations.
