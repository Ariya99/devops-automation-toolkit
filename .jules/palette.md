## 2024-11-07 - CLI Input Blocking Pattern
**Learning:** Python CLI scripts in this repository consistently scatter `input()` prompts throughout the script (e.g., asking for an output filename after data processing). This blocks users mid-execution during potentially long-running data processes.
**Action:** Always group all user `input()` prompts at the very start of the script and add status `print()` statements to provide immediate interaction feedback and prevent mid-execution blocking.
