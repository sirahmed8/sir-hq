# PLAN: SIR Control Room (HQ dashboard and Telegram reports, lives in `D:\Projects\_SIR`)
Audited 2026-11-10. New plan file (none existed). Internal tool for one owner: not sold, not listed. It is not a SIR product folder; its code is in `_SIR/plans/generate_dashboard.py`, `_SIR/plans/dashboard_template.html`, `_SIR/scripts/serve-control-room.py`, `_SIR/scripts/refresh-control-room.py`, `_SIR/scripts/deliver/`, `_SIR/mods/` and `_SIR/ops/`.

## 1. Purpose (plain words)
One page that tells Ahmed the true state of every project (what is built, what is checked, what is blocked, what only he must do) and a Telegram channel that sends him short reports and asks for his approval on a phone tap. It also keeps the memory files that let any AI continue the work.

## 2. Names and parts
| Part | Where | State |
|---|---|---|
| Dashboard generator | `plans/generate_dashboard.py` (reads `plans/dashboard_parts/*.html` through `plans/dashboard_page.py`, feeds `plans/dashboard_feeds.py`, `plans/dashboard_repos.py`, `plans/dashboard_notes.py`) | built, verified 2026-11-12: the artifact, `ops/dashboard.html` and `ops/public/dashboard.html` are byte-identical, `pytest tests -q` = 62 passed |
| Local server on port 8899 with 15 minute refresh, health JSON, restart supervisor | `scripts/serve-control-room.py`, scheduled task `SIR_ControlRoom_Server` | built, unverified; `ops/control-room-health.json` said "healthy" at 2026-11-10 |
| Published page (Claude artifact) | link in `ops/DASHBOARD_URL.txt`; refresh with `scripts/refresh-control-room.py`, which writes `ops/artifact/CHANGED.txt` | built, unverified; `scripts/publish_artifact.py` records a hash in `ops/artifact/PUBLISHED.txt` only when the publish really succeeded (last true hash `20ee1159`); republish is an HQ step |
| Telegram sender | `scripts/deliver/send-telegram.mjs` | **verified today**: `node --test scripts/deliver/send-telegram.test.mjs` = 6 of 6 pass (mock server) |
| Telegram buttons and approvals | `scripts/deliver/send-buttons.mjs`, `approval.py`, `telegram-inbox.mjs` | built, unverified |
| Briefing formatter | `scripts/deliver/format-briefing.mjs` with `test-format-briefing.mjs` | built, unverified |
| Mods | `mods/sir-context` (injects plan and inbox into every chat), `mods/sir-guards` (no PRs, no deleting legacy, AHome privacy fence) | built, unverified; the dashboard is not a mod - MAIN_PLAN step 6 now points to `plans/generate_dashboard.py` + `ops/public/` (doc gap fixed 2026-11-10) |
| CI | `.github/workflows/verify.yml` (compiles Python, generates the dashboard) | built, unverified |

## 3. Current state
Claimed: Control Room cycle 3 done (print stylesheet, PDF export, high contrast, content-visibility), Round 13 detached daemon, autopilot queue running four jobs. PORTFOLIO.md says `_SIR` has 47 commits since 2026-11-02.
Verified today: Telegram sender tests 6 of 6. Everything else unverified. The unit tests in `scripts/test_*.py` could not be imported as modules by `python -m unittest scripts.test_x` (no package files); run them as files instead (task 1 below).
Not started: a written dashboard acceptance test (every number on the page traced to a file), automatic republish of the artifact, weekly Telegram report in the standard-26 format for all products, approval flow with expiry and audit log, a single page for "what only Ahmed can do" that is generated from `OWNER_ACTIONS.md`.

## 4. Rules (each needs a test or command)
1. AHome is shown as counts and status only. Test: generator output grepped for any AHome task text, note or message string from its fixtures finds nothing.
2. Every state word follows the truth rule: "verified" only with a dated evidence file; otherwise "built, unverified" or "not started". Test: the generator refuses to print "verified" without an evidence path.
3. No token or chat id in any output, log or page. Test: `gitleaks` plus a grep of `ops/dashboard.html`.
4. Telegram approvals: a tap can only approve an item that was created by the system, within 24 hours, once. Test: replay of the same callback is ignored.
5. Report text is plain Arabic, no emoji, no em-dash, no private content from any project.
6. The dashboard page served on port 8899 binds to 127.0.0.1; phone access only through the tailnet.

## 5. Shared pieces this tool owns for everyone
- Telegram delivery, buttons and approvals: every other plan points here (and SIR Platform later wraps the same sender). Nobody writes a second bot.
- Status schema: every project writes `.sir/status.json` (already present in Laptop Manager and Study); the dashboard reads it. Define the schema in `docs/status-schema.md` (task 3).
- Quota and model ledger: `ops/ACCOUNT_LEDGER.md`, `ops/MODELS.json`, `scripts/sync_quota_ledger.py`.

## 6. Screens
Overview (projects by wave with true state), Project detail (plan, next task, last commit, CI link, evidence list), Owner actions, Quota and models, Reports and alerts, Settings (language Arabic/English, theme, high contrast). Five states, RTL and LTR, 320 px to 4K, WCAG 2.2 AA. Screenshots in `ops/cycle*-control-*.png` exist for earlier cycles (old; retake).

## 7. AI and support
The manager AI reads `plans/INSTRUCTIONS_FOR_MANAGER.md` and `plans/MANAGER_MEMORY.md`. A page assistant is n/a; the dashboard links to the runbooks. Fallback when Claude ends (about 2026-11-23): `scripts/hq_autopilot.py` plus Gemini/CLI agents from `GEMINI.md`.

## 8. Operations
Weekly Telegram report per product (one block each) plus emergency alerts (outage, leaked key, CI red for 24 hours, disk below threshold, quota near end). Heartbeat file `ops/PM_HEARTBEAT.txt`. Backups: `scripts/backup_offsite_encrypted.py` (has tests). Daily artifact republish check using `CHANGED.txt` vs `PUBLISHED.txt`.

## 9. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Truth | every project row on the page links to a `.sir/CHECKPOINT.md` date; CI green URL recorded |
| M1 | Data checks | dashboard test traces each number to a file; AHome fence test passes |
| M2 | Reports | weekly Telegram report for all 16 products sent once (API says ok) |
| M3 | Approvals | tap-to-approve flow with replay protection tested |
| M4 | Auto republish | `refresh-control-room.py` result published without a manual step, or documented as owner action |
| M5 | Quality | screenshots at 390 and 1440, Arabic and English, light/dark |
| M6 | Handover | a fresh Antigravity chat continues from the files alone (record of the test) |

## 10. Next 10 tasks (each under 2 hours)
1. Run the four `scripts/test_*.py` files as scripts and save results. Files: `.sir/evidence` in `_SIR/ops/reviews/`. Check: exit codes recorded.
2. Add the AHome fence test for the generator. Files: `plans/test_dashboard_privacy.py`. Check: passes; fails if a note string is injected.
3. Write `docs/status-schema.md` and make the generator warn on a missing `.sir/status.json`. Check: warning list printed for projects without it.
4. "Verified needs evidence" rule in the feeds: a round counts as verified only when a verification file shows PASS. Check: `tests/test_r42_dashboard.py` drives `plans/dashboard_feeds.py` with a fake project.
5. Owner page generated from `ops/OWNER_ACTIONS.md` (one tap per item, exact steps). Check: screenshot at 390 px.
6. Weekly report builder using `format-briefing.mjs`; dry run output saved. Check: test-format-briefing passes plus a golden file.
7. Approval replay protection in `approval.py` with tests. Check: second callback returns "already used".
8. Add the CI step that fails on a secret pattern in `ops/dashboard.html`. Check: workflow green on push.
9. Retake the screenshots at 320, 390, 768, 1440 in both languages. Check: files dated today.
10. Handover test: write `ops/reviews/handover-test.md` after starting a fresh chat that continues from `NEXT.md` only. Check: file records what it did and any gap.

## 11. Risks and open questions (defaults)
- The artifact is hosted on claude.ai and may stop updating after the subscription ends: default is the local page on 8899 over the tailnet is the main view, the artifact is a convenience.
- The dashboard is large (117 KB template): default is split into modules before adding features (under 300 lines per file rule).
- Telegram bot token handling: default is user env vars only, rotate on any doubt.
- Page numbers about quota are from ledgers, not from a vendor API: label them "estimate".

## 12. Only the owner can do
Rotate the Telegram bot token in BotFather; sign in to Tailscale on his phone; tap approvals in Telegram.

## 13. Market-grade note
Internal tool. `plans/competitors/sir-control-room.md` compares observability tools; its price claims cite vendor pages but need a date check ("(unsourced, verify)" where no link). No country legal pack; nothing public.
