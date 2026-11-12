# MANAGER SUCCESSION (how the work continues when any manager or agent hits a limit)
Version: 1.0.0 (living document, updated when the handover process changes).
This document ensures zero context loss when the current manager (Claude HQ) or any agent hits a quota limit, fails, or is replaced. The next manager/agent reads only files and continues.

---

## 1. Order of Use (Model & Tool Rotation)
When the current model/tool hits a limit, the runner switches to the next in this exact order. Never skip. Never use a model not on this list without a written reason in the checkpoint.

| Priority | Model / Tool | Account / Access | When Used | Notes |
|---|---|---|---|---|
| 1 | **Claude (Sonnet 5.5 / Opus)** | Ahmed's Pro subscription | Manager (HQ), reviews, briefs, planning, hard debugging, design decisions | Does NOT build product code. Uses Haiku subagents for screen ops. |
| 2 | **Gemini in Antigravity** | Ahmed's Pro account (primary) | Autonomous building (primary builder) | Quota cuts trigger switch to #3. |
| 3 | **Free CLI Agents (rotation)** | Free tiers, no paid overages | Building when Antigravity quota out | Order per `ops/ACCOUNT_ROTATION.md`: Kilo (kilo/kilo-auto/free), OpenCode (opencode/big-pickle, glm-5.3-flash-free, deepseek-v4.1-flash-free, OpenRouter free), Devin CLI (swe-2-flash-medium), ZCode (GLM-5.3 Start plan). |
| 4 | **Haiku Agents (Claude subagents)** | Ahmed's Pro subscription | Screen ops (computer use), repetitive tasks, TickTick refresh, account rotation, simple fixes | Low effort, fast, drives browser/CLI. Never Sonnet for these. |
| 5 | **Local Models (qwen3:8b, qwen2.5-coder)** | `D:\Projects\AI_Models_Hub` via `_SIR/scripts/ai/ask.ps1` | Summaries, translation drafts, digests, first-pass reviews, classification (private text stays local) | Free, no quota. Claude reviews the result; does not produce it. |

**Hard rules:**
- Never buy credits or enable overages (AGENTS.md: "No budget").
- Never use Sonnet for screen ops or repetitive tasks (Haiku only).
- Never use Opus unless stuck twice on the same task with written reason.
- The runner (`scripts/cli-run2.sh`) rotates tools automatically; each round reads the checkpoint.

---

## 2. Verifier & Scout Agents (Continuous Quality)
These agents run independently of the builder. They are the "second pair of eyes" that never stop.

### Verifier Agent
- **Runs**: After every milestone exit check, before any "done" claim.
- **Checks**: Every task against `ops/LESSONS.md` (all 50+ lessons), `standard/23-premium-code-bar.md`, `plans/GEMINI_QUALITY_CHARTER.md`, product's `.sir/QUALITY.md`, `plans/WEAK_MODEL_PLAYBOOK.md` (definition of done).
- **Output**: PASS/FAIL per lesson, list of defects with file:line, before/after evidence in `.sir/evidence/`.
- **Gate**: No milestone marked done until Verifier PASS on all relevant lessons.
- **Runs as**: Haiku agent (low effort) or local model via `ask.ps1`.

### Scout Agents (one per product)
- **Runs**: Daily (scheduled at :00 or :30 per `OWNER_DEFAULTS.md` item 12).
- **Reads**: Product's plan, `ops/LESSONS.md`, `OWNER_DEFAULTS.md`, `.sir/CHECKPOINT.md`, recent commits.
- **Tests**: Product against every lesson in `LESSONS.md` (automated where possible, browser tests at 4 widths × 2 languages × 2 themes).
- **Reports**: "Found without being told" section in daily note to `ops/bus/<slug>.md`.
- **Escalation**: If 3 consecutive cycles find nothing worth fixing AND a fresh reviewer agrees → project done.
- **Runs as**: Haiku agent or Kilo/OpenCode background.

---

## 3. Suggestions Approval Flow (`ops/SUGGESTIONS.md`)
Ideas and improvements from any agent (builder, verifier, scout, HQ) flow through this file.

| Stage | Who | Action | File |
|---|---|---|---|
| **Capture** | Any agent | Append to `ops/SUGGESTIONS.md` with: timestamp, agent, product, idea, source (lesson, complaint, observation), effort estimate (S/M/L). | `ops/SUGGESTIONS.md` |
| **Triage** | HQ Manager (Claude) | Daily review: tag `ACCEPTED`/`DEFERRED`/`REJECTED` with reason. Accepted items get a task ID and go to the product's `.sir/TASKS.md`. | `ops/SUGGESTIONS.md` |
| **Implement** | Builder agent | Picks up from `.sir/TASKS.md`, builds, tests, commits, pushes. | Product repo |
| **Verify** | Verifier agent | Checks against lessons, quality bar. | `.sir/evidence/` |
| **Close** | HQ Manager | Marks `DONE` in `SUGGESTIONS.md` with commit hash. | `ops/SUGGESTIONS.md` |

**No idea is lost**: even rejected items stay in the file with reason. Deferred items have a revisit date.

---

## 4. New Manager Takes Over From Files Only
When the current manager (Claude HQ) is replaced or a new chat takes over, the new manager reads ONLY these files and continues. No oral handover, no memory.

### Required Reading (in order)
1. `D:/Projects/AGENTS.md` (workspace laws)
2. `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md` (worker manual)
3. `D:/Projects/_SIR/standard/OWNER_DEFAULTS.md` (standing rules)
4. `D:/Projects/_SIR/ops/LESSONS.md` (cross-project lessons)
5. `D:/Projects/_SIR/plans/MAIN_PLAN.md` (master plan)
6. `D:/Projects/_SIR/plans/WAVE_STUDY.md` (build order)
7. `D:/Projects/_SIR/ops/OWNER_REQUEST_LEDGER.md` (owner requests)
8. `D:/Projects/_SIR/ops/HQ_CHECKPOINT.md` (HQ state: Now, Next step, Open promises, Re-read list)
9. `D:/Projects/_SIR/ops/MISSION_LOG.md` (one-line history)
10. `D:/Projects/_SIR/ops/bus/sir-hq.md` (latest 20 lines)
11. For each active product: `<project>/.sir/CHECKPOINT.md`, `.sir/TASKS.md`, `.sir/PLAN.md`

### First Actions
1. Run `git status`, `git log -5`, `git diff --stat` in `D:/Projects` and each active project.
2. Read uncommitted edits: finish or fix them, never revert.
3. Check CI: `gh run list --limit 3` → `gh run watch <id>` for any red runs; fix first.
4. Update `HQ_CHECKPOINT.md` with new "Now" and exact "Next step".
5. Post one line to `ops/bus/sir-hq.md`: "Manager handover at <timestamp>. Continuing from <next step>."

### Continuity Guarantees
- **Checkpoint format** (in `HQ_CHECKPOINT.md` and every `.sir/CHECKPOINT.md`):
  ```
  Now: <what was just finished, with evidence>
  Next step: <exact command or task, e.g., "Run task 3 in sir-education-hub/.sir/TASKS.md">
  Open promises: <list of things promised but not done, with owner/action>
  Re-read list: <files to re-read before next step>
  ```
- **Mission log**: one line per finished step in `ops/MISSION_LOG.md` (timestamp | project | what).
- **Bus messages**: durable, in `ops/bus/<slug>.md`; new manager reads last 20 lines.

---

## 5. Daily Plain-Words Report to Owner
Every day, the manager (or the autopilot script) sends ONE Telegram message to the owner with this exact format:

**Title**: SIR Daily Report — <date> (e.g., "SIR Daily Report — 2026-11-12")

**Body** (max 5 lines, each one fact):
1. What shipped today: <product> <milestone/task> — <what it means for him>
2. What's blocked: <product> <reason> — <what he needs to do (one tap or nothing)>
3. Money: <product> <real number> — <source> (never invented)
4. Agents: <which models/tools ran, which hit limits>
5. Next: <one concrete thing happening tomorrow>

**End**: "المطلوب منك: لا شيء" or the single tap needed (e.g., "المطلوب منك: اضغط موافقة على Paymob").

**Rules**:
- No file paths, commit hashes, or technical jargon.
- No mix of Arabic and English in one sentence (except product names).
- Numbers with their meaning (e.g., "5 applications sent, 2 first replies received").
- Read last 15 lines of `ops/bus/telegram-outbox.md` before sending; do not repeat what another agent said in the last 2 hours.
- After sending, append one line to `telegram-outbox.md`: `<timestamp> | <agent name> | <one-line summary>`.

---

## 6. Quota Limit Protocol (When a Model Hits "Usage Limit")
1. **Immediately**: Write what is done and the exact next step into the checkpoint (`.sir/CHECKPOINT.md` or `HQ_CHECKPOINT.md`).
2. **Commit and push** to `main`.
3. **Stop**. The runner (`cli-run2.sh`) detects the quota message and switches to the next model/tool in the Order of Use.
4. **Next model reads** the checkpoint and continues from "Next step".
5. **No context loss**: all state is in files.

---

## 7. Emergency Handover (If Manager Fails Mid-Task)
If the manager chat crashes, times out, or is killed:
1. The autopilot (`hq_autopilot.py`) detects no heartbeat for 10 minutes.
2. It reads `HQ_CHECKPOINT.md` "Next step" and launches the next available model/tool with that prompt.
3. The new manager reads the required files (section 4) and continues.
4. A note is posted to `ops/bus/sir-hq.md`: "Emergency handover at <timestamp>. Previous manager unresponsive. Continuing from <next step>."

---

## 8. Owner Action Items (When Only He Can Act)
When a task truly cannot be done by any agent (Tier 3: sign-in, 2FA, payment, CAPTCHA, identity check, creating new accounts, speaking as him to people):
1. Write **one tiny exact step** in `D:/Projects/_SIR/ops/OWNER_ACTIONS.md`.
2. Format: `- [ ] <date> | <product> | <exact action> | <where> | <expected result>`
3. Continue all other work. Do not stop.
4. Owner sees it in the daily report (line 2) and acts.
5. Agent detects completion (file change, env var, API response) and continues.

---

## 9. Version History
- 1.0.0 (2026-11-12): Initial version from r44 portfolio plans upgrade.