## 2024-05-18 - Improved CLI UX

**Learning:** When users run interactive CLI scripts that take a while to run, the lack of immediate feedback makes them think the process has hung. Also, having inputs scattered throughout the process (like asking for date input *after* processing data) breaks the user's focus and requires them to stick around instead of just starting the script and letting it run. Grouping inputs at the start and adding status messages greatly improves the UX of CLI tools.

**Action:** Group all user inputs at the beginning of CLI scripts. Add print statements to provide immediate feedback during long-running operations. Provide clear completion messages.
