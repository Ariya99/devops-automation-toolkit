## 2026-10-13 - [Path Traversal in Output Excel Filenames]
**Vulnerability:** In `python/automated_report2.py` and `python/syncprocess-fails-rating8.py`, user input is used directly (or with minimal formatting) to construct the output file path. For instance, `output_filename = 'SyncHealth_Report_' + output_filename + '.xlsx'`.
**Learning:** This enables a malicious user to supply an output filename containing path traversal sequences (e.g., `../../../etc/cron.d/malicious`) to write the resulting Excel file to an arbitrary location on the file system, potentially overwriting important files.
**Prevention:** Use `os.path.basename()` to extract only the filename component from user input to prevent path traversal when constructing file paths for writing.
