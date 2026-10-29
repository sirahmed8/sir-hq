# 14 — Continuity and handoff (any agent, any tool)

- **State lives in the repo, not in chat:** CHECKPOINT, BOARD, ADRs, CHANGELOG, `docs/`. A new agent with zero history must be able to continue from the files alone.
- **Session-end ritual:** ask the owner's questions (AGENTS.md section 9); update CHECKPOINT, BOARD, CHANGELOG (Unreleased) and `status.json`; commit; release the lock; report.
- **Memory within and between sessions:** the checkpoint is updated after every finished step (write-ahead), so a compaction, crash or usage limit never loses more than the current step. On Ahmed's workstation, the memory hooks (`D:\Projects\_SIR\core\04-memory.md`) reprint it after every compaction.
- **Rules for every successor agent, including Gemini in Antigravity:**
  - Read before writing. Match existing patterns.
  - No architecture rewrites, library swaps or folder restructures without an ADR approved by a separate reviewer agent.
  - Never delete or skip tests, lower thresholds, bypass hooks or commit secrets.
  - Nothing is "done" without `pnpm verify` output.
  - If unsure, write to `.sir/inbox/orchestrator.md` and flag it in your report; never guess silently.
- **Enforcement beats instructions.** Rules files guide agents; CI enforces. Required checks, branch protection, CODEOWNERS and pre-commit hooks keep `main` healthy even if an agent ignores the rules.
- **Same rules in every tool.** `AGENTS.md` is read natively by Antigravity, Codex, OpenCode, Kilo, Cursor and Copilot, and by Claude Code through `CLAUDE.md`. Shared skills live in `.agents/skills/` (read by Antigravity and Codex) and are mirrored to `.claude/skills/`. Machine-level configs for every tool are generated from `D:\Projects\Laptop Manager\agent-config\` (step 1.13 in `D:\Projects\_SIR\phases\01-workstation.md`).
- **Recurring maintenance:**
  - Monthly: dependency updates through Renovate/Dependabot PRs; cost review; security advisories.
  - Each Expo SDK release: upgrade within one SDK cycle.
  - Yearly: the Google Play target-API bump (each August); the Apple minimum Xcode/SDK change (each spring); certificate, domain and developer-account renewals; a legal-document review.
  - Quarterly: a backup restore test; an access-rules review.
