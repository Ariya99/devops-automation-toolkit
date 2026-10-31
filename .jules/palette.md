## 2024-03-20 - Grouping Interactive Inputs in CLI Scripts
**Learning:** When developing interactive CLI data processing scripts, users can be left hanging if the script prompts for input, processes data for a long time, and then pauses unexpectedly for more input later in the script.
**Action:** Always group user inputs (`input()`) at the start of the script to prevent blocking later, and include clear `print` statements for status updates (e.g., progress indicators) and success notifications to provide immediate interaction feedback during long-running tasks.
