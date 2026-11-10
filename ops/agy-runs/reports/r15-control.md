# r15-control report — Control Room and Telegram menu

Worker: devin-cli (SWE-2 Flash Medium), project `_SIR`, branch `main`.
Brief: `ops/briefs/r15-control.prompt.txt`. Plan: `.sir/plans/r15-control.md`. Checklist: `.sir/r15-control_CHECKLIST.md`.

## Resume state

On resume there was no `.sir/CHECKPOINT.md` and no `.sir/r15-control_CHECKLIST.md`; the active checkpoint was `ops/HQ_CHECKPOINT.md`. A prior worker had already left uncommitted changes implementing most of the brief. I audited them, fixed remaining defects, verified what the sandbox allowed, and prepared the report. New project files created: `.sir/CHECKPOINT.md`, `.sir/plans/r15-control.md`, `.sir/r15-control_CHECKLIST.md`, `ops/locks/_SIR` (lock could not be released — `rm` was rejected by tool permissions).

## What was implemented

### 1. Telegram `/menu` and Control Room telemetry

- `scripts/deliver/telegram-inbox.mjs`
  - `MENU` is `['[الإدارة] اختار:', 'الحالة=status', 'تنضيف المساحة=clean_disk', 'إطفاء الألعاب=game_off']`; `/menu`, `/start`, `/help` invoke `send-buttons.mjs` with those rows.
  - `ops/telegram-actions.json` already wires `status`, `clean_disk` (`sir-laptop-admin.exe care clean --execute`), and `game_off` (PowerShell process stop for game launchers).
- `plans/generate_dashboard.py`
  - `PRIVATE_TASK_RE = re.compile(r"[\w.-]*(?:ahome|habiba)[\w.-]*", re.I)` plus `sanitize_autopilot_text()` mask private names in autopilot log lines.
  - `parse_autopilot()` reads `ops/autopilot_state.json` (listener pid, last tick, runner count), `ops/AUTOPILOT_QUEUE.json` (private items rewritten to `name="private-task"`, `title="Private project task"`, `private=true`), and the last 10 lines of `ops/autopilot.log` (sanitized).
  - `parse_account_ledger()` parses the `ops/ACCOUNT_LEDGER.md` table, strips outer pipes, skips the header and separator rows, and handles 8/7/6/short row shapes with `—` fillers; returns the last 10 rows.
  - Both are injected into the template as `autopilot=` and `account_ledger=`; both `ops/dashboard.html` and `ops/artifact/control-room.html` are written from the same output.
- `plans/dashboard_template.html`
  - New sidebar links and sections `#autopilot` and `#account-ledger`, bilingual EN/AR strings, `renderAutopilot()` and `renderAccountLedger()`, both escaping every dynamic value through `esc()`, registered in `applyLang()` and the IntersectionObserver section list.
  - Verified present in generated output: `ops/dashboard.html` contains `id="autopilot"`, `id="account-ledger"`, the embedded `D.autopilot`/`D.account_ledger` payload, and 0 occurrences of `habiba` (case-insensitive). `ahome` appears only as the intended project label `AHome (private)` and the standing privacy sentence; no private task names leak (private queue rows render as "Private project task" / "مهمة خاصة").

### 2. Owner approvals flow

- `scripts/deliver/ask-approval.mjs` (new): `node ask-approval.mjs <id> "<text>"`. Validates id (`^[\w.-]{1,50}$`, no `ahome`/`habiba`, text ≤ 1000 chars, no private names), upserts a `pending` row into `ops/bus/approvals.json` atomically (tmp + rename), then runs `send-buttons.mjs` with `موافق=approve_ok:<id>` and `رفض=approve_no:<id>`. On send failure it marks the row `send_failed`. It reads Telegram credentials from env or the Windows user scope, same as the other deliver scripts.
- `scripts/deliver/telegram-inbox.mjs`
  - New callback branch `approve_ok:<id>` / `approve_no:<id>` records `{answer: approved|rejected}` into `ops/bus/approvals.json` via `recordApproval()` (atomic write), removes the buttons, answers the callback query, and confirms in chat.
  - `recordApproval()` now always writes the full schema `{id, text, status, answer, created_at, answered_at}`; legacy `ok:<id>`/`no:<id>` answers are still appended to `ops/approvals.jsonl` for `scripts/deliver/approval.py` and are now also mirrored into `ops/bus/approvals.json` so both stores stay consistent.
- Docs: `scripts/deliver/README.md` line 11 documents `ask-approval.mjs`; `ops/bus/README.md` line 7 documents `ops/bus/approvals.json` and its schema.

### 3. Artifact freshness

- `plans/generate_dashboard.py` already writes `ops/dashboard.html` and `ops/artifact/control-room.html` from one template and updates `ops/artifact/CHANGED.txt` with the content hash; `PUBLISHED.txt` keeps the last published hash so `artifact_synced` stays truthful.
- Observed state: `ops/control-room-refresh.log` shows the refresh worker ran the generator successfully at `2026-11-10 10:48:13` → `dashboard.html & control-room.html generated (293760 bytes, hash 3a9daf04, git 48f05fa, synced=False)`. `CHANGED.txt` = `3a9daf04`, `PUBLISHED.txt` = `20ee1159` (last published artifact is older; HQ republish is a separate step and `notify_hq_artifact_outdated()` already leaves a single bus notice).

### 4. CI

- `.github/workflows/verify.yml` runs `python -m compileall plans scripts`, `python plans/generate_dashboard.py`, and Gitleaks.
- Local evidence available in this sandbox: the refresh worker executed `python plans/generate_dashboard.py` green at 10:48 (covers the exact CI step); `git diff --check` is clean; the only changed Python file is `plans/generate_dashboard.py` itself (other `scripts/*.py` untouched); grep found no token-shaped strings in `scripts/deliver` (env var names only). GitHub Actions could not be checked because `git add`/`git commit`/`git push`/`gh`/`python`/`node` were all rejected by tool permissions, so nothing was pushed and no Actions run exists for these changes.

## Commands run and real output (this session)

- `git status --short --branch` → `## main...origin/main` with the modified/untracked list quoted in the checkpoint; no ahead/behind markers.
- `git diff --check` → only LF→CRLF warnings, no whitespace errors, exit 0.
- `cat ops/artifact/CHANGED.txt ops/artifact/PUBLISHED.txt` → `3a9daf04` / `20ee1159`.
- `tail -n 6 ops/control-room-refresh.log` → refresh at 10:45 (hash a9267f1d) and 10:48 (hash 3a9daf04), both `synced=False`, exit 0.
- `git add ...`, `git add --dry-run ...`, `git commit --dry-run ...`, `rm ops/locks/_SIR` → all rejected by tool permissions ("User rejected this tool call"). Earlier in the session `node`, `python`, `py`, `powershell`, `curl`, `gh`, `webfetch`, `schtasks`, `date`, `cmp`, `awk`, `command -v`, `git diff --no-index` were likewise rejected; only read-only shell commands (`cat`, `tail`, `ls`, `git status/diff/log`) and the file tools worked.
- Grep verifications (read-only): `habiba` = 0 matches in `ops/dashboard.html` and `ops/artifact/control-room.html`; `private-task|Private project task|autopilot|account-ledger` = 76 matches in `ops/dashboard.html`; no `bot<digits>:<secret>` or literal token patterns under `scripts/deliver`.

## What is verified vs. not

Verified by observation: generated HTML contains both new sections with real telemetry embedded; private autopilot names are masked; `habiba` absent; artifact files regenerated from the same payload; approvals code paths reviewed line-by-line and schema made consistent; `git diff --check` clean.

Not verified (sandbox denials): live `/menu` button round-trip on Telegram, live `ask-approval` send + `approve_ok`/`approve_no` callback round-trip, `node --check`/`node --test`, `python -m compileall`, GitHub Actions status, browser screenshots at 320/390/768/1024px, and RTL visual pass. No screenshots were taken because no browser/interpreter command was permitted.

## Uncertainties

- `ops/bus/approvals.json` does not exist yet; it is created on first `ask-approval` run or first approval callback. Other chats should treat a missing file as "no approvals".
- The content hash includes volatile fields (`last_tick`, log tail), so `CHANGED.txt` will keep changing each refresh and `artifact_synced` will stay false until HQ republishes; this is truthful but means the published artifact is always "stale" by hash even when content is current. r16 already plans a stable owner-visible hash.
- `parse_account_ledger()` guesses column alignment for short rows; the current ledger parses correctly for the observed shapes but exotic rows may shift fields into `note`.

## Recommendations (next)

1. Commit and push this working tree (all changes are complete and `git diff --check` clean), then confirm the `verify` workflow run.
2. Run one live `node scripts/deliver/ask-approval.mjs test-1 "تجربة موافقة"` and tap both buttons once to prove the round-trip, then delete the test rows from `ops/bus/approvals.json`.
3. Schedule the r16 hardening: serve only `ops/public/`, Host-header gate, private-path 404s, POST→405, stable content hash, `mark-published.py`.
4. Consider gitignoring or truncating `ops/bus/approvals.json` churn if answer history grows.

## Checklist state

`.sir/r15-control_CHECKLIST.md`: items 1, 2, 3 ticked after the evidence above; item 4 left unticked because GitHub Actions could not be observed (push/CI blocked by tool permissions). Done signal: `blocked` — implementation complete in the working tree, commit/push/CI verification denied by sandbox.
