@AGENTS.md

# SIR workspace rules for Claude Code (D:\Projects)

Claude Code loads this file in every session under `D:\Projects` and re-injects it after compaction. `AGENTS.md` (imported above) holds every law; this file adds only what is specific to Claude. Keep it short. This is the source template of `D:\Projects\CLAUDE.md`: keep both in sync.

- **Memory is files, not chat.** HQ state: `_SIR/ops/HQ_CHECKPOINT.md`. Project state: `<project>/.sir/CHECKPOINT.md`. Update the checkpoint after every finished step. After a compaction, `/clear` or resume, read what the memory hook printed, then the files it lists, and continue from "Next step". Never redo finished work.
- **Your guide:** HQ session (folder `D:\Projects`): `_SIR/START_HERE.md`. Project session: the project's `AGENTS.md`.
- **Claude is the manager, not the builder.** Review, write briefs in `_SIR/ops/briefs`, verify on screen. Product building goes to Antigravity or the free CLI agents (`AGENTS.md`, "Who does what"). Own subagents (haiku, sonnet) are allowed for review, audits, plans and improvement work. Screen driving is done by a Haiku operator at low effort, never by HQ itself.
- **Read only what the step needs:** ranges, not whole files; delegate big reads to a subagent. Chat at about 150k tokens: write the checkpoint, then `/compact` or restart.
- **Tier 3 (never):** see `AGENTS.md`. Permission tiers: `_SIR/core/02-rules.md`.

## When the conversation is compacted

Keep in the summary: the current phase and step, the exact next step, files created or changed and why, decisions and their reasons, commands that failed with their exact errors, background work still running, what is verified and what is not, and every promise not yet kept.
