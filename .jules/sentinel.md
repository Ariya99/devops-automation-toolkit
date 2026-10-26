## 2024-10-26 - Path Traversal in CLI Scripts
**Vulnerability:** Path Traversal via User Input in CLI Scripts.
**Learning:** Ensure that user inputs for filenames do not contain traversal characters like `/` or `\` in CLI scripts, as it allows arbitrary file read/write.
**Prevention:** Explicitly validate input strings against traversal characters or use secure path handling. (Note: Direct validation is preferred per memory over `os.path.basename` for CLI tools).
