## 2023-11-20 - Grouping CLI inputs for better UX
**Learning:** When developing CLI tools, scattering `input()` prompts throughout a long-running script blocks progress and requires constant user attention. Grouping all inputs at the beginning improves UX by letting users enter all required data upfront and then leaving the process to complete.
**Action:** Always group user inputs at the start of Python CLI scripts and provide immediate feedback (like `print("\nProcessing data...")`) before starting long-running data operations.
