## 2024-10-26 - Grouping CLI Inputs and Status Messaging
**Learning:** Scattered `input()` prompts in CLI tools can block long-running data processing tasks, leading to poor user experience.
**Action:** Group all user `input()` prompts at the beginning of the script and provide clear `print()` statements for status updates (e.g., "Reading CSV files...", "Processing...") during long-running tasks.
