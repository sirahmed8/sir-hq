Fix every item that failed verification of r47-skills-encyclopedia.

Verification file: D:\Projects\_SIR\ops\verifications\r47-skills-encyclopedia.md
Project: D:/Projects/SIR Portfolio

Failed items:
- Item 1: For EVERY skill (read its SKILL.md and its scripts/references headers in full, not just the title): write one digest file ops/encyclopedia/<tool>/<skill-name>.md with what it does, when to use it, inputs/outputs, tools/MCPs needed, risks, 3 key rules -> Digest files exist for all sources (1007 files, 385 unique names; `find ops/encyclopedia -name "*.md" | wc -l` = 1124 incl. deep/), but PROGRESS.md itself states "It does NOT yet deep-read every script's full header or every reference file end-to-end" and HQ bus note 15:57 says "1007 mechanical digests ... not a deep read: queue a real LLM pass". Sample digest `ops/encyclopedia/claude/skill-creator.md` has no inputs/outputs or tools sections filled ("none declared", "none flagged by keyword scan"). Coverage done, required full-read depth not done.

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
