## 2026-10-25 - Group User Inputs in CLI Scripts
**Learning:** Users can get blocked if additional inputs are required *after* a long-running data processing task has already begun. In CLI scripts, all user inputs should be collected upfront.
**Action:** Group all `input()` calls together at the start of Python CLI scripts and provide immediate status feedback (e.g., `print('Processing...')`) before commencing long-running data operations.
