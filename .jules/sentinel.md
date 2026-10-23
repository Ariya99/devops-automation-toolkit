
## 2024-10-23 - Prevent Formula/CSV Injection in Excel Exports
**Vulnerability:** Excel export scripts (`python/automated_report2.py`, `python/syncprocess-fails-rating2.py`, `python/syncprocess-fails-rating8.py`) wrote unsanitized dataframe string contents directly into Excel files via `pandas.to_excel()` and `openpyxl`'s `ws.append()`. If imported data contained strings starting with executable characters (`=`, `+`, `-`, `@`, `\t`, `\r`), opening the resulting `.xlsx` files in Excel could lead to arbitrary code execution (Formula/CSV Injection).
**Learning:** Pandas dataframes and `openpyxl` do not natively sanitize strings against Formula/CSV injection when generating Excel artifacts.
**Prevention:** Always explicitly sanitize string columns/data when exporting to Excel by prepending a single quote (`'`) to any string that begins with special executable characters, ensuring they are interpreted as text rather than formulas.
