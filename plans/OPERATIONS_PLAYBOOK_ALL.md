# SIR OPERATIONS PLAYBOOK (rewritten 2026-11-10 by the plans audit)
Standard: 26 (autonomous operations). Scope: all products, scaled to what exists. Today no product is live to outside users, so most loops below are written but not scheduled. Each loop item says what exists now.
Principle: AI managers run from written runbooks; Ahmed is the chairman. He is contacted only for emergencies and for acts only a person can do (sign-in, passkey, 2FA, CAPTCHA, payment, identity, legal signature, buying a domain or plan). Everything else is decided, logged and done by the manager or the project AI.

## 0. What exists today (built, unverified unless stated)
| Piece | Where | State |
|---|---|---|
| Telegram sender | `scripts/deliver/send-telegram.mjs` | verified 2026-11-10: 6 of 6 tests pass (mock server) |
| Briefing formatter, buttons, approvals | `scripts/deliver/` | built, unverified |
| Dashboard generator and daemon | `plans/generate_dashboard.py`, `scripts/serve-control-room.py`, `scripts/refresh-control-room.py` | built, unverified |
| Autopilot queue | `scripts/hq_autopilot.py`, `ops/AUTOPILOT_QUEUE.json` | built, unverified |
| Quota ledger sync | `scripts/sync_quota_ledger.py` | built, has a test file |
| Offsite encrypted backup | `scripts/backup_offsite_encrypted.py` | built, has a test file |
| Stale lock purge | `scripts/purge_locks.py` | built, has a test file |
| Per-project health lines | Laptop Manager, Jobs, Study `.sir/health.txt` or health endpoints | built, unverified |
Note: the earlier text said `python D:/Projects/_SIR/scripts/generate_dashboard.py`; the real path is `plans/generate_dashboard.py`.

## 1. Daily loop (08:00 Cairo time; scheduled by the autopilot once verified)
1. Health: read each project's health line or endpoint; for a public product also `/status`. On a 5xx run the product's restart or rollback runbook, then re-check.
2. Quota and cost: read `ops/ACCOUNT_LEDGER.md`; rotate the account at 15 percent left per `ops/ACCOUNT_ROTATION.md`; check each cloud console budget alert (the owner sets the cap; no product is allowed to pass it).
3. Support triage (public products only, after launch): inbox and assistant escalations sorted into answered, bug, feature request. A bug becomes a failing test in the repo first, then a brief to the project's builder chat.
4. Refresh the dashboard (`python D:/Projects/_SIR/plans/generate_dashboard.py` or the refresh script) and republish the artifact if its hash changed.
5. Send the chairman one short Arabic message (4 lines): what changed, what failed, what the AI already did, the one tap needed if any.

## 2. Weekly loop (Monday)
1. Security and dependencies: `npm audit` / `pip-audit` / `cargo audit` per repo; update patch and minor versions on a branch of work, run the project's verify command, push to `main` only when green (no pull requests rule). Major upgrades are separate tasks.
2. Backups: run each product's backup and one restore test into a temporary folder; compare hashes; log the result. AHome and private products back up locally only.
3. Visibility check (public products only): run `scripts/check_ai_visibility.py` (to be built; see `VISIBILITY_PLAN_ALL.md`) with a fixed question list in Arabic and English; record whether the product is mentioned and how it is described in `ops/visibility-weekly.json`.
4. Insight: aggregate consented, privacy-first usage counts; list the top 3 improvements for next week's backlog. Private products produce local-only insight.
5. Weekly Telegram report per product in simple Arabic.

## 3. Monthly loop (1st of the month)
1. Competitor refresh: re-check each `plans/competitors/<slug>.md` for price and feature changes; every changed number needs a link and a date.
2. Models: review `ops/MODELS.json`; run the product eval sets on new candidate models; change a default only if the eval score is not lower.
3. Legal refresh: check store policy changes and data-protection rule changes for the markets in use; update templates; keep the "AI-drafted, to be reviewed by a qualified lawyer" marker.
4. Money reconciliation (after payments exist): compare gateway records with the database; fix orphan transactions; list failed renewals.
5. Restore drill for one product chosen at random; record the result.

## 4. In-product support assistant (every public product)
- Grounded only in the product's docs, FAQ, changelog and the signed-in user's own state. If something is not in those sources it says it does not know and opens a ticket.
- Language follows the user (Egyptian Arabic, Modern Standard Arabic, English).
- Bug flow: with the user's consent it attaches the last client errors with personal data removed and files a ticket.
- Limits: free users get 5 questions per rolling 24 hours (config value; the badge shows "3 / 5 free questions remaining today"); paying users get a higher fair-use cap set by cost, not unlimited; owners are unmetered. The earlier "30 per day / unmetered for subscribers" is removed because it cannot be afforded on free provider tiers.
- Provider chain with failover through the Platform `ai-proxy`; daily cost cap; kill switch; eval set per product (refusal, grounding, language).

## 5. Incident runbook
| Severity | Example | AI action | Tell the chairman |
|---|---|---|---|
| P3 | UI glitch, one client error | log, add to next cycle | no |
| P2 | one API route returns 500 | read logs, reproduce in a test, fix, verify, deploy | no |
| P1 | payment webhook signature mismatch or booking mismatch | pause checkout (switch to "launching soon"), isolate the handler, fix, reconcile | one line after the fact |
| P0 | database unreachable, data loss risk, leaked key, legal notice | restart, roll back to the last verified deployment, read-only mode, rotate keys | immediately if down more than 15 minutes, or at once for a key leak, legal notice, platform ban or money at risk |

## 6. Guard rails (limits the AI may not pass)
1. AI cost cap per product per day: set in `config/limits.json` of each product by the owner. No default amount is assumed here (the old "5 USD per day" and "15 USD per month" figures were not tied to any budget). Reaching the cap switches the product to the rule-based fallback.
2. Ad spend: zero until the owner sets a number.
3. Deletions: no automated permanent delete of user data or buckets without a verified snapshot, and never of `legacy/` before M6.
4. Brand voice: public channels post under the brand name; agents never pose as Ahmed in conversations.
5. Tier 3 stays: no leaking secrets, no CAPTCHA or 2FA bypass, no fake reviews or engagement, no engagement bots, no scripting X's website, no payments by the AI, no graded work, AHome data never leaves its private systems.

## 7. Management ladder and handover
Owner > manager AI (reads `plans/INSTRUCTIONS_FOR_MANAGER.md` and `plans/MANAGER_MEMORY.md`) > project AIs (builder and operator per product) > review AIs (a different model or lens). The Claude subscription ends around 2026-11-23; the manager role then passes to Gemini in Antigravity or a free CLI agent, which continues from `NEXT.md`, `ops/HQ_CHECKPOINT.md` and each `.sir/CHECKPOINT.md`. Handover test: a fresh chat must continue from files alone; record the result in `ops/reviews/`.
