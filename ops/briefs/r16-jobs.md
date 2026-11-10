# Brief r16-jobs: SIR Jobs, repair the front end, close the security and Telegram gaps, then improve it

You work only in `D:/Projects/SIR Jobs` (Node ESM, no framework, server on 127.0.0.1:3456). An independent reviewer found real faults behind "UI broken, brand yellow missing" and behind the repeated Telegram files. Evidence: `D:/Projects/_SIR/ops/reviews/2026-11-10/review-jobs.md` (read it first).

## Rules
- Never ask the owner anything; decide, write it in `.sir/CHECKPOINT.md`, continue.
- After EVERY numbered task: run `npm test` (must print 0 failures) and `npm run doctor`, then `git add -A`, `git commit`, `git push origin main` (straight to main, no pull request), then add one line with the commit hash to `.sir/CHECKPOINT.md` "Done".
- Version stays 1.0.0. No emoji, no em dashes, no placeholder text, no invented numbers or data in anything the owner sees. Never read anything under `D:/Projects/AHome`.
- Do not send real Telegram messages while testing: always run with `SIR_TELEGRAM_API_BASE=http://127.0.0.1:9` or the ledger `dryRun` option, and use a temp `ledgerPath`.
- Do not stop the running server except through Task Scheduler (`schtasks /End /TN SIR_Jobs_Server` then `/Run`) after all tests pass; then check `curl http://127.0.0.1:3456/api/health`.
- Files you create stay under 300 lines. The old path `D:\AI_Models_Hub` must never appear; the correct one is `D:\Projects\AI_Models_Hub`.
- Paste real command output in `.sir/evidence/r16-jobs.md` for every acceptance check. Do not call anything done until the check prints what is asked.

## Read first
1. `D:/Projects/_SIR/ops/reviews/2026-11-10/review-jobs.md`
2. `.sir/CHECKPOINT.md`, `.sir/DESIGN.md` (seed colour `#A16207`)
3. `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md` (rule 7 on yellow) and `D:/Projects/_SIR/standard/23-premium-code-bar.md`
4. `src/public/app.css`, `src/public/index.html` (lines 40-70), `src/telegram-ledger.mjs`

## Part A: fixes (in this order)

**1. Repair the corrupted CSS.**
File `src/public/app.css`. Lines 4, 213, 215, 233, 290, 291, 292, 337 and one more contain `: :` (for example `*,*: : before,*: : after` and `.app-dialog: : backdrop`). Replace every `: :` with `::`. Add `test/test-css-valid.mjs` that fails when `app.css` contains `: :` and also checks balanced braces; add it to the `test` script in `package.json`.
Acceptance: `grep -c ": :" src/public/app.css` prints `0`; in the browser `getComputedStyle(document.body).margin` is `0px`; `npm test` passes.

**2. Remove the horizontal scroll on phones.**
Files `src/public/index.html` (line 53 `<div class="header-telemetry sr-only" aria-hidden="true">`, line 56 `#telemetry-host-badge`), `src/public/app.css` (`.sr-only` line 229, `.header-telemetry` line 294). Delete the `sr-only` wrapper (it is `aria-hidden`, nothing reads it) or make it `display:none`; make `.sr-only` rules use `!important` for width and height; add `overflow-x: clip` on `body`; make the host badge truncate (`max-width:100%; overflow:hidden; text-overflow:ellipsis`).
Acceptance: with chrome devtools emulate 320, 390, 768, 1280 and 1920 px wide, on each of the six views, `document.documentElement.scrollWidth === window.innerWidth`. Save one screenshot per width of the pipeline view in `docs/screenshots/r16/widths/`.

**3. Restore the brand colour (yellow/gold).**
Files `src/public/app.css` (`:root`, `[data-theme="dark"]`, `[data-theme="contrast"]`), `src/public/logo.svg`, `favicon.svg`, `manifest.json` (`theme_color`), `.sir/DESIGN.md`. The project seed is `#A16207`. Define `--brand`, `--brand-hover`, `--brand-soft`, `--on-brand` in each theme: light `#A16207` with white text only if contrast is at least 4.5:1 (else use dark text), dark theme a lighter gold such as `#EAB308` with dark text. Use the brand for the primary button, active tab, focus ring, logo shield and the top bar accent. Keep green for success, red for danger, neutral for secondary. Replace blue `#2563EB`, `#3B82F6`, `#60A5FA`, `#38BDF8` everywhere in CSS and SVG. Write the contrast ratios of text-on-brand for all three themes in `.sir/evidence/r16-jobs.md`.
Acceptance: `grep -nE "#2563EB|#3B82F6|#1D4ED8|#60A5FA" src/public/*.css src/public/*.svg src/public/manifest.json` prints nothing; screenshots of pipeline view at 390 px and 1280 px in light and dark in `docs/screenshots/r16/brand/` show the gold primary button.

**4. Close the cross-site POST hole.**
File `src/server.mjs` (all `req.method === 'POST'` blocks, helper `readJsonBody`). Add a function `guardPost(req, res)` called before every POST: reject (403) when `Origin` is present and is not one of `http://127.0.0.1:3456`, `http://localhost:3456`, `https://ahmed.tail9e9aa7.ts.net:3456`; reject (415) unless `Content-Type` starts with `application/json`; require header `X-SIR-Token` equal to a per-process token served by `GET /api/session` (only to allowed Host and Origin). Update `src/public/app.js` so every `fetch` POST sends the token and JSON content type (one helper `apiPost(path, body)`).
Acceptance: `curl -s -o /dev/null -w "%{http_code}" -X POST http://127.0.0.1:3456/api/pipeline/move-stage -H "Origin: http://evil.example.com" -H "Content-Type: text/plain" --data '{"id":"X","stage":"APPROVED"}'` prints `403`; the same without Origin and without token prints `401` or `403`; the UI approve button still works (screenshot or test). New test `test/test-post-guard.mjs`.

**5. Make the Telegram ledger crash-safe and race-safe.**
File `src/telegram-ledger.mjs` (`saveLedger`, `recordTelegramDispatch`, `safeSendTelegram`, `loadLedger`), `src/money-engine.mjs` (`formatArabicTelegramBrief`).
(a) Write the ledger atomically: write to `telegram-sent.json.tmp`, then `renameSync`; keep a `.bak` copy of the last good file; when the main file fails to parse, load the `.bak` instead of starting empty and log it.
(b) Reserve before sending: acquire a lock file `data/telegram-sent.lock` (create with `wx` flag, stale after 2 minutes), append a `pending` entry with the hash, send, then mark it `sent`. A `pending` entry younger than 10 minutes blocks a second send of the same hash or category/day; if the send call throws or times out, keep the entry as `unknown` and do not resend for 10 minutes.
(c) Hash a normalised text for the daily money brief: strip digits that come from FX conversion (or hash the list of job ids plus date instead of the text), so a changed exchange rate does not defeat the hash.
(d) Print in the Telegram text and in the UI that the inbox digest is a separate daily message.
Tests in `test/test-r16-ledger-race.mjs` (temp ledger path, `dryRun`): two `safeSendTelegram` calls started at the same time send once; a simulated crash between send and record does not resend within 10 minutes; a truncated ledger file is recovered from `.bak`; the brief with FX 54.04 and 54.09 hashes the same.
Acceptance: `node test/test-r16-ledger-race.mjs` all pass; `npm test` passes.

**6. Make the daemon really restart after a crash.**
Files `scripts/install-autostart.ps1`, `scripts/supervisor.ps1`, new `scripts/supervisor-hidden.vbs`, `scripts/service-status.ps1`. Register a second task `SIR_Jobs_Watchdog` (AtLogOn plus repeat every 5 minutes, hidden through `wscript //B`) that runs `supervisor.ps1 -Once`: if `http://127.0.0.1:3456/api/health` does not answer within 3 seconds, run `schtasks /Run /TN SIR_Jobs_Server` and write a line to `.sir/health.txt`. Do not start a second server when the port is bound. `service-status.ps1` must print the real restart settings read from Task Scheduler.
Acceptance: `Get-ScheduledTask SIR_Jobs_Watchdog | Select State` prints Ready; run `scripts/supervisor.ps1 -Once` while the server is up and see "healthy, nothing to do"; no console window appears (run it from a hidden wscript and confirm the task result code is 0). Do not kill the live server to test; test the "down" branch by pointing `-Port 3999` at an unused port and using `-WhatIf`.

**7. Stop the inbox job from freezing the server.**
Files `src/inbox.mjs` (lines about 319-323 and 486), `src/server.mjs` (`startInboxJob`). Replace `execFileSync` by async `execFile` (promisified) with `windowsHide: true`; make `runInboxPipeline` async and have `startInboxJob` await it.
Acceptance: start an inbox job in test mode with a runner that sleeps 5 s; during that time `curl http://127.0.0.1:3456/api/health` answers in under 200 ms (add this as `test/test-r16-inbox-nonblocking.mjs`).

**8. Remove invented numbers from the money brief.**
File `src/money-engine.mjs` (lines 35, 65, 95, 125, 155 `winProbability`, and the line in `formatArabicTelegramBrief` that prints "نسبة القبول التقريبي"). Delete `winProbability` and the printed percentage; rank by pay and payment speed only; every EGP figure is shown with its USD source and the FX rate and date used. Update `test/test-r10-ui-money.mjs`.
Acceptance: `grep -rn "winProbability\|نسبة القبول" src` prints nothing; `npm test` passes.

**9. Lint and type check.**
Files `package.json`, new `eslint.config.mjs`, `tsconfig.json`, `.github/workflows/verify.yml`. Add dev dependencies `eslint` and `typescript` (exact versions), scripts `lint` (`eslint src scripts test`) and `typecheck` (`tsc --noEmit --allowJs --checkJs --skipLibCheck src/*.mjs`). Fix what they report (do not silence rules wholesale). In CI add a `windows-latest` job running `npm ci`, `npm run lint`, `npm run typecheck`, `npm test`.
Acceptance: `npm run lint` and `npm run typecheck` exit 0; after push `gh run list --limit 1` shows `completed success` for every job.

**10. Small hygiene.** Remove the fake `Set-Cookie: sir_jobs_session=active` from `src/server.mjs`; add `.sir/.memory/` and generated reports (`.sir/reports/daily-money-brief.txt`, `.sir/jobs/TRACKER.md` if generated) to `.gitignore` or move them under `data/`; move owner email and tailnet host to `data/config.json` read at start with the current values as defaults.
Acceptance: `curl -sI http://127.0.0.1:3456/ | grep -i set-cookie` prints nothing; `git status --short` is clean after a normal run.

## Part B: at least 10 visible improvements (each with a screenshot or command as proof)

**B1. Gold brand identity.** New logo (gold shield with a check, drawn as SVG, 3 sizes) used in header, favicon, manifest icons 192 and 512, and desktop launcher icon. Proof: screenshots of header at 390 and 1280 px; `assets/brand/icon.ico` regenerated.

**B2. Split `src/public/app.js` (2,510 lines).** ES modules under `src/public/js/`: `api.js`, `state.js`, `views/pipeline.js`, `views/openings.js`, `views/proposals.js`, `views/cash.js`, `views/profile.js`, `views/security.js`, `i18n.js`, `dialogs.js`; each under 300 lines; `index.html` loads `js/main.js` as a module. Proof: `wc -l src/public/js/*.js src/public/js/views/*.js` all under 300; all existing UI tests still pass.

**B3. Split `src/server.mjs` (1,218 lines)** into `src/routes/{pipeline,money,profile,fx,health,inbox,static}.mjs` plus `src/http-utils.mjs` with one `sendJson(res, status, body)` helper that removes the repeated `res.writeHead` blocks. Proof: `wc -l src/server.mjs` under 300 and `npm test` passes.

**B4. Five states on every view.** Each of the six views has: skeleton matching the final layout while loading, an empty state with one clear action, an error state with a Retry button that re-runs the failed request, and the populated state; plus offline state from the service worker. Proof: `scripts/states_check.mjs` forces each state by intercepting fetch and saves 4 screenshots per view at 390 px in `docs/screenshots/r16/states/`.

**B5. Application card actions that cannot be hit by mistake.** Approve is the only primary (gold) action; Reject sits apart with a 2-second hold-to-confirm ring; an "Undo" toast for 8 seconds after approve, reject and move-stage using the existing `undo.mjs`. Proof: screenshot of the hold ring in progress and of the undo toast at 390 px; `test/test-undo.mjs` extended with the HTTP flow.

**B6. Deadline strip.** A strip on top of the pipeline: next 3 deadlines from the data with days left, colour only by urgency (neutral, gold within 7 days, red within 2 days), tapping a chip scrolls to the card. Show "No deadlines in the data" when empty. Proof: screenshot with data at 390 px; unit test for days-left maths including the Cairo time zone.

**B7. Pipeline filters.** Chips for stage, source and "needs proof"; filter state saved in the URL hash (`#stage=SCREENING&q=python`) so a refresh and a shared link keep it; result count announced in the live region. Proof: screenshot at 1280 px and a test that loads the page with a hash and checks the filtered count.

**B8. Command palette (Ctrl+K and a search button on mobile).** Opens from the trigger with a 160 ms spring scale, lists views, filters, actions (open specs, copy proposal, export CV), arrow keys and Enter work, focus returns to the trigger on close, `prefers-reduced-motion` respected. Proof: screenshot at 390 and 1280 px; a11y test asserts `aria-modal` and labelled input.

**B9. Real Arabic.** Move all visible strings to `src/public/i18n/en.json` and `ar.json` with `data-i18n` attributes; language switch swaps text and flips `dir`; numbers and currency keep left-to-right isolation; a test fails if a key exists in only one file. Proof: screenshots of pipeline and cash views in Arabic at 390 px with at most a handful of English labels (names, URLs, currency codes).

**B10. Cash view honesty.** Show each opportunity with source name, link, date seen and what the owner must do next; a "last refreshed" time from the data file; an empty state "No opportunities in the data file, run the digest" instead of sample rows. Proof: screenshot with real data and with an empty data file (temp copy).

**B11. Inbox panel states.** Show last run time, how many items, whether the local model was used, and a Run button that is disabled while a job runs with a progress text; errors show the real message and a Retry. Proof: screenshots in idle, running (use the slow runner), and error states at 390 px.

**B12. Keyboard and touch.** Every button, chip and link at least 44 by 44 px under 768 px; visible gold focus ring (3:1 contrast); skip link; Esc closes any dialog and returns focus. Proof: a script measures all `button, a, [role=tab]` at 390 px and prints `0 under 44`; axe-style checks in `test/test-a11y-ui.mjs` extended.

**B13. Motion polish.** Card enter stagger 40 ms, tab indicator spring `stiffness 400 damping 30`, dialog scale-from-trigger 220 ms, all disabled under `prefers-reduced-motion: reduce` (the rule currently dropped by the CSS bug at line 337). Proof: a test that reads the computed `animation-duration` under emulated reduced motion and finds `0.01ms`; a 3-second screen recording or 4 stills in `docs/screenshots/r16/motion/`.

**B14. Printable and shareable CV link in Profile.** Buttons "Download CV (PDF)" and "Copy proposal text" with clear success toasts; the CV PDF is regenerated when profile data changes (compare hash). Proof: `curl -sI http://127.0.0.1:3456/api/profile/cv.pdf` returns `application/pdf` and a size above 10 KB; screenshot of the profile view.

## Last step
Update `.sir/CHECKPOINT.md` with real numbers (tests passed, lint and typecheck results, latest CI run id and result, which tasks are done and which were skipped and why), commit and push, then run:

`python D:/Projects/_SIR/scripts/agy-done.py r16-jobs ok "<one line: tasks done, tests passed, CI run id and result>"`

If CI is red or any acceptance check failed, use `fail` instead of `ok` and say which.
