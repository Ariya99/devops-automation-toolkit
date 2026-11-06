## 2024-11-20 - Prevent CLI Blocking Mid-Execution
**Learning:** Python CLI scripts that perform long-running data processing must not prompt for user input (like output file names) mid-execution, as this blocks the script and prevents the user from leaving it to run unattended.
**Action:** Always group `input()` calls at the very beginning of the script and add status `print` statements to provide immediate interaction feedback.
