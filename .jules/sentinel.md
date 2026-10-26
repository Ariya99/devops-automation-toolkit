## 2023-10-26 - Path Traversal in File Read

**Vulnerability:** The `python/automated_report2.py` script was directly using `input()` to obtain filenames and passing them to `pd.read_csv()` without sanitizing path separators or traversal characters (e.g., `../`). This allowed for a potential Path Traversal attack, where a user could read arbitrary `.csv` files from the filesystem.

**Learning:** When accepting user input for file operations, even in local CLI scripts, it's crucial to validate the input to ensure it doesn't contain unexpected traversal characters or directory separators if the expectation is to read files from a specific/current directory.

**Prevention:** Ensure user input for filenames is sanitized. Rather than stripping characters, raising a `ValueError` if illegal characters (`..`, `/`, `\`) are detected is a secure approach that fails safely.
