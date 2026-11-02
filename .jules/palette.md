## 2026-11-02 - Grouping CLI Inputs
**Learning:** Interleaving user prompts (input()) with long-running data processing causes scripts to block unnecessarily, leading to poor UX for automated/long tasks.
**Action:** Group all input() prompts at the start of CLI scripts and use print() statements to provide status updates.
