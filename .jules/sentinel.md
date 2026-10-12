## 2026-10-12 - Stack Trace Leakage
**Vulnerability:** Found unhandled exceptions in python CLI utility scripts (e.g. automated_report2.py) that could leak internal stack traces to the user (e.g. when opening invalid files).
**Learning:** Even internal-facing CLI tools should fail securely without leaking internal file structures or execution paths via stack traces.
**Prevention:** Always wrap external I/O operations (file reading, writing, user inputs) in try/except blocks, log the error securely, and exit with a safe error message to the user.
