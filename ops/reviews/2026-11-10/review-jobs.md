# Review: SIR Jobs (2026-11-10, independent reviewer)

Repo `D:/Projects/SIR Jobs`, HEAD `a55ea54` (r15 inbox assistant). Checked by running the project's tests in a scratch copy (so no real data or Telegram was touched), calling the live service on 127.0.0.1:3456 (reads, plus one POST with a non-existent id), a browser at 390 px, and reading code. Nothing edited, stopped or committed.

## Verdict
1. The backend is in better shape than the front end: 139 of 139 tests pass, CI is green, the daemon answers, the Telegram ledger really blocks the repeat sends it was built for. Nothing can lint or type-check it, because no linter is configured.
2. The owner's "UI broken, brand yellow missing" is correct and has a clear cause: `src/public/app.css` was corrupted in round 11 (nine selectors contain a space, `: :`), so the global reset and the backdrop and reduced-motion rules are silently dropped. At 390 px the page is 625 px wide (horizontal scroll). The brand colour in `.sir/DESIGN.md` is `#A16207` (warm gold) but round 10 replaced it with blue.
3. Several checkpoint claims are false: "0 viewports overflow", "restart on failure" for the server task, and "no invented numbers" (the money brief shows hard-coded "acceptance" percentages). Mutating POST routes have no Origin or token check.

## Commands run (exact) and results
| Command | Result |
|---|---|
| `npm test` (in a scratch copy, 24 suites) | exit 0, 139 tests, 139 pass, 0 fail, 10 s |
| `gh run list --limit 3` | `verify` workflow success on r15, r13, cycle 23 (CI = `npm test` on ubuntu plus gitleaks only) |
| Lint / type check | none defined (`package.json` has no eslint, tsc or vitest); no JS or CSS validation exists |
| `curl http://127.0.0.1:3456/api/health` | 200, `daemon: SIR_Jobs_Server`, uptime 14,934 s |
| Browser 390x800: `document.documentElement.scrollWidth` | **625** (should be 390) on all six views |
| `grep -c ": :" src/public/app.css` | **9** invalid selectors |
| `Get-ScheduledTask SIR_Jobs_Server` | trigger AtLogOn, **RestartCount 0**, last result 0 |

## Claims table
| # | Claim | Result | Evidence |
|---|---|---|---|
| 1 | Telegram duplicate sends fixed by ledger (r12) | **Verified, with gaps** | `test-r12-telegram-ledger.mjs` passes: 3 runs send once; live ledger has 1 entry; callers all go through `safeSendTelegram`. Gaps D1 to D3 below |
| 2 | Detached daemon `SIR_Jobs_Server` survives IDE exit | **Verified** | task exists, AtLogOn, wscript action, service answers, uptime 4 h |
| 3 | Automatic restart on failure, 3 times | **Not working** | XML has `RestartOnFailure` but the registered task has RestartCount 0; the action is `wscript` which exits at once, so a crashed node is never restarted; `supervisor.ps1` is not registered |
| 4 | "Royal Sapphire" design, zero yellow buttons | **Contradicts the brand** | charter allows yellow when the project brand is yellow; `.sir/DESIGN.md` seed `#A16207`; CSS tokens `--color-primary #2563EB`; the logo is a blue shield |
| 5 | 0 viewports overflow across 8 devices | **Not true** | scrollWidth 625 at 390 px; culprits `.header-telemetry.sr-only` (width forced to 100% by a later media rule) and `#telemetry-host-badge` |
| 6 | Settings window, side menu, RTL mirroring | **Partly** | present and no console errors; CSS pseudo-element rules for the drawer scrollbar and dialog backdrop are dead (`: :` bug); backdrop computed colour is `rgba(0,0,0,0)` |
| 7 | Hidden console for all child processes | **Verified for src** | all `execFileSync` in `src/telegram-ledger.mjs` and `src/inbox.mjs` use `windowsHide: true`; weekly task runs `wscript` + hidden `pwsh` |
| 8 | Weekly digest scheduled task | **Verified registered** | Monday 08:00 trigger, last run 11/09 08:00, result 0 |
| 9 | "No invented numbers" | **Not true** | `src/money-engine.mjs:35,65,95,125,155` hard-code `winProbability` 95/90/88/85/82 shown to the owner as "approximate acceptance %"; EGP amounts move by a few pounds per run with the FX rate |
| 10 | Inbox assistant phase 1 read-only, local model only | **Partly** | uses `ask.ps1 -Provider local -Sensitive` (good); but `runInboxPipeline` uses `execFileSync` up to 200 s inside the server process, so it blocks the whole server while it runs (D5) |
| 11 | Static ETag, HEAD, retry coverage | **Verified** | tests pass; read code |
| 12 | Security: Host allowlist, path traversal, rate limit | **Verified** (Host 403, `..` rejected); but see C1 |

## Defects

### Critical
None.

### High
**H1. `app.css` is corrupted: nine invalid selectors drop whole rules.** `src/public/app.css` lines 4, 213, 215, 233, 290, 291, 292, 337 (and one more): `*,*: : before,*: : after {...}` and `.app-dialog: : backdrop`. One invalid selector in a list invalidates the entire rule, so the reset (`box-sizing`, `margin:0`, `padding:0`) is never applied (measured: body margin 8px, `ul` padding 40px, `h1` margin 9 px), `::backdrop` styles and the reduced-motion override (line 337) are gone. Introduced in `85242ee` (r11) when the CSS was re-flowed.
Reproduce: `grep -n ": :" src/public/app.css`; in a browser `getComputedStyle(document.body).margin` is `8px`.
Fix: replace `: :` with `::` everywhere; add a test that parses the CSS with a real parser (or a regex test for `: :`) and fails on invalid selectors.

**H2. Horizontal scroll on phones (625 px page at 390 px).** `.header-telemetry.sr-only` (`index.html:53`) gets `width:100%` from `.header-telemetry` in a media block (`app.css:294`), which beats `.sr-only` (`app.css:229`), so the "hidden" element is 374 px wide and pushes `scrollWidth`. `#telemetry-host-badge` (`index.html:56`) also extends.
Fix: remove `sr-only` from that wrapper (it is `aria-hidden`, so use `display:none` or delete it), make `.sr-only` use `!important` on width and height, and set `overflow-x: clip` on `body`. Acceptance: `scrollWidth === innerWidth` at 320, 390, 768, 1280, 1920 on every view.

**H3. Brand yellow was removed.** `.sir/DESIGN.md` line 3: seed `#A16207`. `src/public/app.css` `:root` and `[data-theme=dark]` use blue (`#2563EB`, `#3B82F6`); `src/public/logo.svg` and `favicon.svg` are blue/emerald. Charter rule 7 allows yellow when it is the project colour. Fix: define `--brand: #A16207` (light), a lighter gold for dark theme with contrast checked (AA 4.5:1 for text, 3:1 for large), use it for primary button, active tab, focus ring and logo; keep red and green for danger and success.

**H4. Mutating routes accept cross-site requests.** `src/server.mjs` POST handlers (`/api/pipeline/approve|reject|move-stage|record-submission`, `/api/fx`, `/api/money/brief`) check only the Host header (a foreign Host gets 403), not Origin and not a token. A web page open in the owner's browser can send `fetch('http://127.0.0.1:3456/api/pipeline/move-stage',{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain'},body:'{"id":..., "stage":...}'})`, and the body is parsed as JSON regardless of content type. Reproduced: with `Origin: http://evil.example.com` and `Content-Type: text/plain` the server processed the request (returned a validation 400, not 403). `/api/money/brief` can send a Telegram message the same way.
Fix: reject POST when `Origin` is present and not in the allowed set, require `Content-Type: application/json`, and add a per-process token served to the page (like the Laptop Manager does).

**H5. Task restart-on-failure does not exist in reality.** `scripts/sir_jobs_server_task.xml` declares it; the registered task has RestartCount 0 and wscript exits at once, so Task Scheduler sees success. If node crashes, Jobs stays down until the next logon. Fix: register a second AtLogOn/every-5-minutes task that runs the health check and starts the server if port 3456 does not answer (`scripts/supervisor.ps1` exists; wrap it hidden), and make `service-status.ps1` report the real restart settings.

### Medium
**M1. Invented numbers in the money brief.** `src/money-engine.mjs:35-155` hard-coded `winProbability`; `formatArabicTelegramBrief` (line ~397) prints it as "approximate acceptance". `payUsd` values are also constants. The charter and AGENTS.md forbid invented numbers. Fix: drop the percentage from the text, rank by pay and speed only, and label every figure "owner estimate" with its source in `data/`.

**M2. Telegram ledger gaps (the owner complaint).** (D1) `safeSendTelegram` sends first and records after (`src/telegram-ledger.mjs` ~276-310): if `execFileSync` times out at 30 s after Telegram accepted the file, or if `saveLedger` throws, the send is not recorded and the next run sends again. (D2) `saveLedger` is a plain `writeFileSync` (no lock, no temp-file rename); two processes (scheduled digest and the `/api/money/brief` button) can both pass the check and both send; a half-written file is read as corrupt and `loadLedger` then starts a fresh ledger, which forgets every hash. (D3) the money brief text contains FX-derived EGP amounts that change per run (6,484 then 6,489 in the working copy), so the content-hash check never matches; only the one-per-day quota stops repeats. (D4) the inbox digest uses category `inbox_digest`, which is outside the daily quota list, so the owner can now get two Telegram messages a day by design; it should be said in the UI. Fix: reserve before send (write `pending` entry with a lock file), mark `sent` after, keep `pending` entries blocking for 10 minutes, write atomically (temp + rename), keep a `.bak`, and hash a normalised text without volatile numbers.

**M3. Inbox job blocks the server.** `src/server.mjs:575-610` `startInboxJob` wraps `runInboxPipeline` in `setImmediate`, but the pipeline uses `execFileSync` (timeout 200 s, `src/inbox.mjs:319-323`), which freezes the single Node event loop: dashboard and health calls hang while the local model runs. Fix: use async `execFile` or a `child_process.fork` worker.

**M4. No lint, type check or Windows CI.** `package.json` has only `node` test scripts; CI runs on ubuntu and cannot execute the PowerShell/Task Scheduler paths. Fix: add ESLint (flat config, no deps beyond dev), `tsc --noEmit --allowJs --checkJs` over `src`, and a `windows-latest` job running `npm test`.

**M5. Large files.** `src/public/app.js` 2,510 lines, `src/server.mjs` 1,218, `src/inbox.mjs` 679 (rule: 300). Server has 25+ inline route blocks with repeated `res.writeHead` code.

**M6. Fake session cookie.** `Set-Cookie: sir_jobs_session=active` is sent on every response (`src/server.mjs` ~613). It is not a session, adds nothing and teaches the wrong model. Remove it.

### Low
- L1. CSP allows `'unsafe-inline'` for scripts (`src/server.mjs` ~606).
- L2. Hard-coded owner email and tailnet host/IP (`src/server.mjs:58, 68`), also `D:/Projects/_SIR/scripts/...` in `src/inbox.mjs:35`.
- L3. At 390 px the "Filter applications" input and "Real Zeros Benchmark" chip wrap awkwardly; small tap targets (8 buttons or links under 40 px).
- L4. `.sir/.memory/` is untracked; `.sir/jobs/TRACKER.md` and `daily-money-brief.txt` are generated files that change in git on every run (should be ignored or moved to `data/`).
- L5. Seed stage names and baseline applications are code constants (`BASELINE_APPLICATIONS`); if these are real applications, store them in the database import file, not in server code.

## What I could not check
Live Telegram send path (would message the owner), real Outlook or mailbox access of the inbox assistant, Arabic copy quality, 768/1280/1920 screenshots (overflow measured numerically at 390 only; the desktop view loads without console errors), restart behaviour after a node crash (would stop the live service).
