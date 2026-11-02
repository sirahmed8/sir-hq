# MODEL AND EFFORT BY TASK LEVEL (every project chat; Ahmed 2026-10-30: always use subagents, pick model and effort by the task)

The project chat is the Project Manager (Sonnet, medium effort; high only for levels 2-3). It does not do bulk work itself: it writes the task, picks the level below, and spawns a subagent with the `model` and `effort` set explicitly. Several independent tasks go out in one message, at most 3 at once (see USAGE_POLICY.md).

| Level | Task | Model | Effort |
|---|---|---|---|
| 0 | Search, inventory, read logs or large files, link and licence checks, formatting, renames, repeated checks, copying data, simple edits | haiku | low (medium if results come back shallow) |
| 1 | Implement from a written spec, unit tests, UI from a design, translations, docs, config files, browser or app chores with clear steps | haiku | high (max for big modules) |
| 2 | Design, architecture, task specs, ADRs, reviews of every significant diff, hard debugging, refactors across files, plan upgrades | sonnet | high |
| 3 | Auth, security rules, payments and webhooks, data migrations, legal pages, anything touching secrets or user data | sonnet, then a second sonnet reviewer | high (xhigh for threat models) |
| 4 | Stuck after two tries, architecture that is expensive to undo, security or payment design review | opus | high or xhigh, logged with the reason |

Rules
- Write the delegation brief first (objective, files to read, files it may edit, done-when commands, return format, budget). A good brief is what lets haiku do level 1 well.
- The author never grades its own work: a fresh reviewer agent approves each significant change; `qa-breaker` writes the adversarial tests.
- Bulk non-sensitive text (translation drafts, content drafts, research digests) may go to the local model or Gemini through `_SIR/scripts/ai/ask.ps1`. Private text (AHome, Habiba, study material, credentials) stays local.
- Do not spawn for jobs under about five tool calls or for tightly coupled edits in the same files.
- Parallel builders get their own git worktree and disjoint files; merge to `main` yourself, no pull requests.
