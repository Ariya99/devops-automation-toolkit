## 2024-10-24 - CLI Progress Indicators

**Learning:** When developing CLI scripts for data processing, the absence of a visual user interface means that users can be left waiting without feedback. Providing explicit status updates during long-running tasks acts as a functional loading state, significantly reducing user frustration.
**Action:** Always include clear `print` statements (e.g., "Loading CSV files...", "Processing data...") and success notifications for intermediate operations in scripts to serve as progress indicators.
