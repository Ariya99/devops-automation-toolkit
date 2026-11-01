## 2026-11-01 - Prevent Input Blocking in CLI Scripts
**Learning:** Grouping user inputs at the start of long-running Python CLI scripts prevents blocking later during execution.
**Action:** Always group input() calls at the script's start and provide a clear status update (e.g., print('Processing data...')) prior to long-running tasks.
