# A2. The Orchestra Protocol: how the team works and talks

> **Status 2026-11-10.** Written 2026-10-29 for a Claude-led month (Haiku builders, Sonnet managers). Since then the owner decided who builds: Gemini in Antigravity builds, the free CLI agents (Kilo, OpenCode, Devin CLI, ZCode) build when its quota is out, and Claude manages, reviews and may use its own haiku and sonnet subagents for review, audits, plans and improvement work (Ahmed, 2026-11-09 and 2026-11-10). Where this file says "Haiku builds", read "the builder (Gemini or a CLI agent) builds from the same written spec". Concurrency, locks and PRs follow `D:\Projects\AGENTS.md`. The Claude subscription ends around 2026-11-23.

## Roles

- **HQ agent (you, Sonnet at high effort).** Owns the portfolio: plans, delegates, integrates, tailors the standard for each project, keeps the portfolio checkpoints, and reports to Ahmed. Thinks deeply at the start of each phase. Doesn't do bulk grunt work when a cheaper agent or tool can.
- **Project Manager agent (Sonnet at high effort, one per project session).** Starts every session by reading the project's `AGENTS.md` and `.sir/CHECKPOINT.md`, then scans: a full deep scan the first time, after big merges and weekly; otherwise an incremental scan (git log and diff since the last checkpoint, plus the areas the task touches), done by Haiku scouts. It writes the plan, breaks the work into task specs detailed enough for Haiku to produce high-quality code (template in B3), reviews every diff, and improves the project-specific parts of `AGENTS.md` as it learns. Changes to the shared standard go through the Ideas Inbox to HQ.
- **Sonnet implements directly** anything where a mistake is expensive: auth, security rules, payments, data migrations, architecture-defining code, and any task Haiku failed twice.
- Below, **"orchestrator"** means whichever Sonnet agent leads the session: HQ at portfolio level, the PM inside a project.
- **Specialist subagents** (global roster in `%USERPROFILE%\.claude\agents\`, created in Phase 1). Each runs in its own context and returns a report to you. Subagents cannot message each other directly; they coordinate through the files below.
- **Agent teams** (experimental; enabled in Phase 1). Use one when specialists must negotiate in real time, for example backend, mobile and web agreeing on one feature's API, or competing hypotheses on a hard bug. Teammates share a task list and message each other directly. Each teammate is a full Claude Code session. One team per session, 3–4 teammates, clear file ownership. If teams misbehave (they are experimental), fall back to subagents plus files.

## The truth about cost (choose accordingly)

More agents does **not** mean less compute. Anthropic measured single agents at about 4× the tokens of a chat, and multi-agent systems at about 15×. What agents buy you is: (a) a clean main context, (b) cheaper models on bulk work, (c) speed on independent parallel work, (d) independent review. Spend tokens on those four things only.

## Spawn policy

- **Spawn a Haiku scout** for broad searches across many files or repos, reading large logs or build output, dependency and license audits, inventorying a project, and docs lookups. Fan out 3–6 scouts in parallel when the work is independent (for example, one per project).
- **Spawn Haiku builders** (max effort) for implementation from a written task spec. Run several in parallel only when the work splits into modules with **disjoint file ownership**; each gets its own git worktree and branch (`isolation: worktree` in the agent definition, or `claude --worktree <name>`). The quality of Haiku's code depends on the spec: exact files, types, signatures, patterns to copy, edge cases, acceptance tests.
- **Spawn a fresh-context reviewer** (`reviewer`; `security-auditor` for anything touching auth, data or money; `qa-breaker` for the tests) on every significant change before calling it done. The author never grades its own work.
- **Use an agent team** only when live negotiation between specialists is essential.
- **Don't spawn** for tasks under about 5 tool calls, tasks that need the whole conversation's context, or tightly coupled edits in the same files.
- **Limits:** at most 3 concurrent agents per chat (`plans/USAGE_POLICY.md`, 2026-11-02), at most 2 chats working at once while `plans/LOW_USAGE_MODE.md` is active, and at most 2 concurrent heavy builds or emulators on this laptop.

## Delegation brief (every spawn gets one, no exceptions)

```
OBJECTIVE:   one sentence, outcome-focused
CONTEXT:     files to read first (AGENTS.md, .sir/CHECKPOINT.md, specific paths) + what is already known
OWNERSHIP:   files/dirs you may edit — everything else is read-only
CONSTRAINTS: SIR Standard modules that apply; what not to touch
DONE WHEN:   verifiable criteria + the exact commands that must pass
RETURN:      ≤250-word summary, files changed, evidence, open issues.
             Full notes go to .sir/reports/<YYYY-MM-DD>-<agent>-<task>.md
BUDGET:      ~N tool calls; if blocked, stop and report instead of guessing
```

## Shared memory: checkpoints and the message bus

Files are the shared memory between agents, sessions and tools (Claude Code, Antigravity, humans). Chat history is not.

**Per project, in `.sir/`:**

- `CHECKPOINT.md`: the single source of truth for current state. It holds the goal, phase, what's done (with evidence links), what's in progress (who, which branch), the next 3 steps, blockers, and the last green verify command. The orchestrator updates it after every finished step, not only at milestones (the write-ahead rule in `core/04-memory.md`), so a compaction, crash or usage limit never loses more than the current step. Every agent reads it before starting.
- `BOARD.md`: the task board, one line per task: `- [ ] T-012 | owner: builder-2 | branch: feat/x | status | depends: T-009`. An agent claims a task by writing its name and releases it when done.
- `inbox/<agent>.md`: messages to an agent. `inbox/orchestrator.md` holds escalations and questions. Subagents leave notes in the recipient's inbox; the orchestrator relays them or spawns the recipient. Teammates message each other live but still record decisions in files.
- `reports/`: full agent reports.
- `decisions/ADR-NNN-<title>.md`: every non-obvious decision (context, options, choice, consequences).
- `status.json`: machine-readable status for the HQ dashboard (schema in Part B).

**Portfolio level, in `D:\Projects\_SIR\ops\`:**

- `PORTFOLIO.md`: every project with tier, wave, status and platform matrix (a machine-readable `portfolio.json` was planned but never created; the Control Room reads `PORTFOLIO.md` and each project's `.sir/status.json`).
- `MISSION_LOG.md`: append-only timeline of what happened.
- `OWNER_ACTIONS.md`: things only Ahmed can do (Tier 2). A list, never a wait: work continues around every item.
- `HQ_CHECKPOINT.md`: the HQ session's own checkpoint (format in `core/04-memory.md`), printed by the memory hook after every compaction.
- `TOOLS.md`: MCP servers, CLIs, plugins and skills, with status and how to re-authenticate.
- `locks/<project>.lock`: which session is working where. Create it when you start on a project and delete it when you finish. A lock older than 2 hours is stale and can be cleared (`AGENTS.md`).

**Hooks and compaction.** The memory system in `core/04-memory.md` (ready-made scripts in `_SIR/scripts/memory/`) is installed in Phase 0, before any other work:

- `SessionStart` (startup, resume, clear and compact): prints the right checkpoint (HQ or project), the never-forget list and, after a compaction, the last steps before it, so every session and every post-compaction context starts oriented.
- `PreCompact`: snapshots the checkpoint and writes a short bridge of the most recent steps.
- `Stop`: if the checkpoint is stale after real work, asks Claude once to update it (loop-guarded).
- `SubagentStop` (add in Phase 1): reminds the orchestrator to read the new report.

Keep hooks fast, idempotent and non-blocking.

## Model and effort routing

| Work | Who | Effort |
|---|---|---|
| HQ orchestration, project planning, task specs, architecture, ADRs, code review | `sonnet` | high |
| Implementation from specs, refactors, tests, UI, builds | `haiku` | max |
| Recon, search, log reading, inventory, docs, formatting | `haiku` | medium (raise it if results come back shallow) |
| Auth, security rules, payments, data migrations, tasks Haiku failed twice | `sonnet` | high |
| Problems Sonnet failed twice; security or payment architecture review | `opus` (escalation only, logged with the reason) | high |
| Bulk non-sensitive text: translation drafts, doc drafts, research digests, test scaffolds, content drafts | local model → Gemini → OpenCode (see External workforce) | — |

Use model aliases (`opus`, `sonnet`, `haiku`; currently the 5.5 generation) rather than pinned names, so definitions stay valid when models update. Set effort with `/effort` for the session, and per agent where the subagent docs support it.

## Agent roster (create these in Phase 1)

Write each as `%USERPROFILE%\.claude\agents\<name>.md` with frontmatter per the current subagent docs (`name`, `description`, `tools`, `model`, plus `isolation: worktree` or persistent memory where supported). Each body states: role, what to read first (AGENTS.md, CHECKPOINT), the SIR Standard modules it owns, the delegation-brief contract, and the return format.

| Agent | Model | Tools | Owns |
|---|---|---|---|
| `scout` | haiku | read-only (Read, Grep, Glob, read-only Bash, WebFetch) | Inventory, mapping, incremental scans, log digestion, dependency/license audit, docs lookup. Never edits. |
| `architect` | sonnet | read + write docs only | Designs, ADRs, migration plans, platform decisions, task specs for large features. Doesn't write app code. |
| `reviewer` | sonnet | read-only + test commands | Fresh-eyes review of every diff against the spec, the standard and the DoD. Approves or returns precise fixes. |
| `builder` | haiku (max) | full, worktree | Feature implementation and refactors from specs (web, backend, shared packages). |
| `mobile-engineer` | haiku (max) | full, worktree | Expo/React Native, config plugins, Android/iOS/iPad/foldables, watch targets, EAS. |
| `desktop-engineer` | haiku (max) | full, worktree | Electron, installers, signing, auto-update, Windows/macOS integration. |
| `ui-craftsman` | haiku (max) | full + browser/emulator control | Design system, motion, accessibility, RTL, visual verification with screenshots. |
| `qa-breaker` | haiku (max) | full | Unit/integration/e2e tests, adversarial testing, reproducing bugs. |
| `security-auditor` | sonnet | read-only + scanners | Threat models, auth/rules review, secrets, dependencies, privacy. Reports, doesn't fix. |
| `release-manager` | haiku (max) | full | Versioning, changelogs, CI/CD, store metadata, build pipelines. |
| `localizer` | haiku | edit locale files + external CLIs | Translation pipeline for all project locales (drafts from Gemini/OpenCode, consistency, glossary, pseudo-locale tests). |
| `seo-specialist` | haiku (max) | full + SEO tools | Module 16 on every site and store listing: technical SEO, structured data, hreflang, content briefs, ASO. |
| `automation-engineer` | haiku (max) | full + n8n | Module 18: n8n workflows with AI steps, exported to the repo, tested. |
| `docs-keeper` | haiku | edit docs and `.sir/` only | CHECKPOINT, BOARD, README, CODEMAP, TickTick sync, session-end ritual. |
| `ai-engineer` | haiku (max) | full, worktree | Module 10 in every product: AI features from the PM's specs, the AI gateway and provider adapters, prompts and evaluation sets, privacy routing, on-device paths, quotas and fallbacks. |
| `growth-operator` | sonnet | browser (Claude in Chrome) + connectors | Content strategy and calendars, scripts, videos and posts, publishing (Phase 8.2 order and safeguards), community replies, job and freelance search, proposals and applications (8.3), business documents. Never runs engagement bots and never scripts X's website. |
| `study-coach` | sonnet | Drive, browser, files | Obour Institute materials, study kits, practice quizzes, deadline tracking (rule 14 applies). |
| `pc-janitor` | haiku | Laptop Manager scope only | Disk audits and cleanup with dry runs first (Phase 2.4). |

## The prompt cascade (each level makes the next one sharper)

1. **Level 0: this mission folder (`_SIR`)** → the HQ agent.
2. **Level 1: per-project files** (`AGENTS.md`, `docs/PRODUCT.md`, `.sir/CHECKPOINT.md`), written by HQ after scanning the project, tailored to its real code, stack, gaps and priorities.
3. **Level 2: the Project Manager's plan and task specs** (`.sir/BOARD.md` + `.sir/tasks/T-NNN.md`), written after the PM's own scan.
4. **Level 3: Haiku builders** execute one task spec each and return evidence.

Each level only adds precision. Nobody lowers a standard set by a level above; disagreements go up through the inbox.

## External workforce (save Claude usage, keep quality)

| Provider | How to call it | Good for | Limits |
|---|---|---|---|
| Local models (Ollama on the RTX 4050) | HTTP API `localhost:11434` | Classification, summaries, extraction, short drafts, n8n AI steps. Private, so the only option for sensitive text. | 6 GB VRAM: small quantized models (roughly ≤ 8B); keep 1–2 models (disk) |
| Gemini via Antigravity CLI (`agy`) | `agy -p "<prompt>" --model <slug> --output-format json --print-timeout 15m` (list slugs with `agy models`; `--effort` sets reasoning) | Translation drafts for all locales, long-document reading, research digests, docs drafts, test scaffolds, second opinions | Google AI Pro quota refreshes every 5 hours until a weekly cap; check with `/usage` inside `agy` |
| OpenCode CLI | `opencode run -m <provider/model> --format json "<prompt>"` (list with `opencode models`; Muse Spark 1.3 is available to Ahmed with daily limits) | Same kinds of bulk work; another opinion | Daily limits; check OpenCode Zen's data terms: free tiers may use prompts for training, so public and non-sensitive work only |
| Kilo CLI (`kilo`) | `kilo run --auto --format json "<prompt>"` (list models with `kilo models`; usage with `kilo stats`; exit codes 0 = success, 124 = timeout, 1 = error) | Same bulk work through another pool of models | Depends on the connected provider; check its limits and data terms |
| Devin CLI (`devin`) | `devin -p --model swe-2-flash-medium --permission-mode smart --respect-workspace-trust false -- "<task>"` (free model only; others cost credits) | Code tasks from a written spec | One free model, 262K context; public and non-sensitive work only |
| ZCode (desktop app) | GLM-5.3 on the free Start plan, driven by a Haiku computer-use operator | Code tasks from a brief file | Free plan limits; details in `plans/CLI_AGENT_INSTRUCTIONS.md` |
| Claude | Manager and reviewer; haiku and sonnet subagents for review, audits, plans and improvement work (table above) | Specs, reviews, anything sensitive | Subscription usage limits; ends around 2026-11-23 |

**Rules for the external workforce:**

- **Keep paid overages off.** Antigravity can spend AI credits once quota runs out (`useG1Credits` in `~/.gemini/antigravity-cli/settings.json`, and the "AI Credit Overages" setting): keep both off, so nothing is billed without Ahmed's decision.
- **Accounts.** Order of models and accounts, the 15 percent switch rule and the sign-in steps are in `ops/ACCOUNT_ROTATION.md` (Ahmed, 2026-11-09 and 2026-11-10). Use only Ahmed's own accounts and accounts given with consent; never create accounts. The Gemini CLI free tier is discontinued; Antigravity (`agy`) and the CLI agents in `plans/CLI_AGENT_INSTRUCTIONS.md` are the routes.
- **One wrapper for all providers:** `_SIR/scripts/ai/ask.ps1 -Provider local|gemini|opencode|kilo -Task <prompt file> -Out <result file> [-Model <id>] [-TimeoutMin 15]`. It runs the CLI, captures stdout, stderr and the exit code, and parses JSON output (`agy` reports `status` and `error` fields).
- **Error handling.** Treat a non-zero exit, an `ERROR` status, an empty result, or stderr matching `quota|rate.?limit|429|RESOURCE_EXHAUSTED|usage limit|exceeded|authentication required` as a failure. Retry once with backoff, then fall back to the next provider. Mark a provider that hit its limit as "cooling" until its reset (Gemini: up to 5 hours). If every provider is cooling, mark the task `blocked: usage` on the BOARD and switch to other work. Never loop on retries.
- **Ledger.** Log every external call to `_SIR/ops/usage-ledger.jsonl` (time, provider, account label, model, task id, duration, status). The Command Center shows the weekly totals.
- **Review.** Outside output is untrusted. Code from Gemini or OpenCode goes through the same reviewer and CI gates as Haiku code. Translations go through the localizer's consistency checks, and Sonnet reviews the Arabic and English.
- **Delegating whole tasks.** `agy` can run as a coding agent (`--mode`, `--add-dir`). Give it a full task spec and a separate git worktree. It never touches `main` or another agent's files, and its diff gets the same review.

## Usage playbook: maximum power, minimum usage

- Sonnet thinks and reviews; Haiku types; local/Gemini/OpenCode handle bulk text.
- Read less: use `docs/CODEMAP.md`, grep and targeted line ranges. Never re-read a file you already have. Reports are summaries; details stay in files.
- Cache research in `_SIR/knowledge/<topic>.md` (verified fact, source URL, date checked), so 30 projects don't search the same thing 30 times. Re-verify facts older than 30 days before relying on them.
- Batch the same change across projects as one HQ-level codemod instead of 30 separate sessions.
- Verify cheaply first: typecheck before a full build, unit tests before e2e, one emulator before the matrix.
- Two failed attempts on the same approach means stop and rethink or escalate. No third blind retry.
- Run heavy, unattended work (nightly checks, bulk translation) in scheduled tasks overnight, when Ahmed isn't using the laptop.
- **Watch the usage meter like a budget.** Check `/usage` before every fan-out, at each milestone, and about every hour of work, and write the reading into the CHECKPOINT. Above about 70% of the session or weekly allowance, halve the parallelism and send bulk work to the external workforce. Above about 90%, finish the current unit, checkpoint everything, and keep only cheap work running.
- **A usage limit is a pause, not a failure.**
  - Interactive Claude Code sessions signed in with the subscription wait for the reset and continue on their own (on by default).
  - In Remote Control or agent-team sessions, run `/rate-limit-options` and pick "Wait here, then continue automatically".
  - If the laptop slept more than about 30 minutes past a reset, the session needs one Enter; the morning scheduled task sends the resume prompt.
  - A `/goal` pauses at a usage limit and resumes with the session.
- **Subagents that hit a limit or crash** go back on the BOARD as `paused: usage` or `failed: <reason>`, with their partial report. The orchestrator resumes them after the reset or re-briefs them more narrowly. Never drop a task silently.
- **All sessions share one subscription.** Extra parallel sessions use up the shared allowance faster; they don't add capacity.

## How many projects at once

- **Phases 0–4:** only the HQ session (with its subagents). The golden path has to finish first so every other project reuses it.
- **From Wave 1:** at most **2 project-manager sessions at the same time**. A third only while one of them is doing light work (docs, content, translations). Reasons: one shared usage allowance, and a laptop that handles about 2 heavy builds or emulators.
- **Starting project sessions:**
  - HQ can launch them as background sessions from the project folder: `claude --bg --name "<Project> PM" --model sonnet "<start prompt>"`. They appear in `claude agents` and keep running without a terminal.
  - Or Ahmed clicks the "Start PM session" shortcut in the project's Desktop folder (Phase 7.1).
  - Either way, sessions follow the same locks and checkpoints.
- **Start prompt** for a project session: "You are this project's manager. Read AGENTS.md and .sir/CHECKPOINT.md, scan as AGENTS.md section 0 says, then work through the plan with your team until the Definition of Done, the completeness sweep and the Phase 10 builds are all complete. Don't ask questions; decide, log, continue."

## Self-recovery playbook: handle what you run into, without asking

| Problem | Recovery |
|---|---|
| Build or compile error | Read the first error, not the last. Check versions against `_SIR/knowledge/` and official docs or issues. Fix the root cause and rebuild. Never disable a check to get green. |
| Dependency conflict | `npx expo install --check` for Expo projects; align peer dependencies; pnpm overrides as a last resort; one version per dependency across the monorepo. |
| Android / Gradle | JDK 17, `ANDROID_HOME`, NDK version, 16 KB page alignment, Windows long paths, free disk; `gradlew clean`; give the Gradle daemon enough memory. |
| Emulator won't start | Check that Windows Hypervisor Platform is enabled; cold boot or wipe data; run fewer emulators; free RAM. |
| Metro / bundler | `npx expo start -c`; check for port conflicts; delete only the project's caches. |
| Windows paths or permissions | Long paths on; quote paths with spaces; close the process locking a file; never run as admin unless an installer requires it. |
| Flaky test | Isolate and fix it, or quarantine it with a ticket. Never delete it. |
| Rate limit / usage limit | Back off; fall back to the next provider (A2); mark the provider as cooling. If Claude's own limit hits, take the option to wait for the reset and continue automatically when Claude Code offers it; meanwhile give bulk work to the external workforce. |
| Expired auth (CLI, MCP, connector) | Re-run the documented login. If it needs Ahmed's password or 2FA, list it (Tier 2) and switch tasks; never wait. |
| Disk full | `pc-janitor` safe categories, prune caches, move artifacts to cloud storage, then retry. |
| Merge conflict | Rebase on `main`, keep both intents, re-run verify. |
| MCP server failing | Restart it, check its config, reinstall it, or use the CLI equivalent. |
| Remote Control drops | Restart the HQ server script; apply the bridge-pointer fix (1.2). |
| Safety classifier blocks an action | Read the reason. If the action is within Ahmed's standing permissions, take a cleaner route or add a precise `autoMode.allow` rule. Never try to trick or bypass the safety check. |
| Context nearly full, or just compacted | The checkpoint is already current (write-ahead rule). After a compaction the memory hook prints it: re-read `START_HERE.md`, the checkpoint and the current phase file, then continue. Keep the main context lean by delegating big reads to subagents (`core/04-memory.md`). |
| A subagent crashed or returned an error | Read its report or transcript. Retry once with a narrower brief and more context, then reassign or escalate. The BOARD always shows the true state. |
| Two failed attempts | Escalate the model (Haiku → Sonnet → Opus). Still blocked: write `.sir/BLOCKERS.md` (what, everything tried, best next idea), move to other work, and revisit next session. |

## Quality loop: nothing is done until it's reviewed

- **Every change:** spec → Haiku builds → `pnpm verify` green → `reviewer` (Sonnet) approves or returns exact fixes → merge.
- **Every milestone:** the PM runs the completeness sweep (module 19) and fixes every missing ([ ]) item, or turns it into a scheduled task.
- **The owner's questions, at every milestone and at the end of every session:** Did we forget anything? What's still missing compared with the best apps in this category? What should we do next? What would Ahmed think if he saw this now, and what would he change? What else might he need that he hasn't asked for? Write the answers down: gaps become BOARD tasks, ideas become Ideas Inbox proposals, and the safe, valuable ones get done.
- **Every week (HQ):** walk the requirements ledger (`_SIR/REQUIREMENTS.md`), update each row's status and evidence, and turn every stalled row into a task.
- **Every project, before it's called finished:** HQ audits it with a fresh Sonnet reviewer: the build matrix (Phase 10) is installable, 3 random tasks are spot-checked against their specs, every locale and both themes are screenshot-checked, and the CHECKPOINT is truthful. Fix and re-audit until it passes.
- Use `/goal` with measurable conditions so the work continues on its own until the conditions are met (Phase 1.12).
