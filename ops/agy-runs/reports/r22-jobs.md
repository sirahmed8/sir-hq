# r22-jobs — SIR Jobs mobile/dashboard UX remediation (round 22)

Date: 2026-11-11. Repo: `D:\Projects\SIR Jobs`, branch `main`.
Brief: fix the 8 owner-reported iPhone (390px dark) defects at the root,
self-audit at 320/390/768/1280px in EN+AR light+dark, log defects in
`.sir/DEFECTS_R22.md`, add browser tests, commit+push to main, CI green.

## What changed (by defect)

1. **Header jumble** — `src/public/index.html`, `src/public/app.css`,
   `src/public/js/shell.js`, `src/public/js/profile.js`.
   Rebuilt as a compact toolbar: menu button + logo + title on the left,
   icon-only search and settings buttons on the right. Metrics moved to a
   second `.header-chips` row: USD/EGP rate chip (live value only after
   `/api/fx` resolves), Milestone-1 target chip (button opening the target
   dialog), and a dot + label status chip. `shell.js` maps loopback hosts
   to `Local service`, Tailnet hosts to `Tailnet Connected`; the bare
   `54.07` and black-oval `13,518 EGP` blob are gone — every number is
   labelled. Light/dark/high-contrast contrast preserved via tokens.

2. **Clipped yellow strip** — root cause: `.banner-policy` rendered under
   the sticky header and the page lacked `viewport-fit=cover`, so iOS
   safe-area insets clipped it. Added `viewport-fit=cover` to the viewport
   meta, `padding-top: env(safe-area-inset-top)` on `.app-header`, and the
   banner now sits below the toolbar inside the content wrapper. It is
   dismissible (persisted in `localStorage.sir_jobs_banner_dismissed`).
   Browser test asserts `banner.top >= header.bottom`.

3. **5-line policy block** — shortened to one line
   ("Nothing is submitted automatically.") plus a `Details` expander
   (`aria-expanded`) and a dismiss button. EN/AR strings added to
   `src/public/i18n/{en,ar}.json` with key parity.

4. **Filter chips** — `.filter-chip-row` is now a single
   `overflow-x:auto` row; chips are `flex:0 0 auto` with equal
   `min-height: var(--touch-target-min)` and shared radius/spacing tokens
   matching `.input-search`. Counts moved out of labels into `.chip-count`
   badges fed from real `jobsData.items` counts
   (`updateJobFilterCounts()` in `src/public/js/views/openings.js`).

5. **Opportunity cards** — rebuilt in `openings.js`:
   `.job-card-head` (title + company), `.job-meta-row` (location · Source ·
   age chip with separators), `.job-pay-line` (USD pay + `≈ EGP` only when
   the pay string explicitly states `/hr`, `/mo` or `/yr` AND a live FX
   rate is known, annotated with rate + source + date — no invented
   conversions), `<details class="job-fit">` collapsible analysis, and a
   stable `.job-actions-row` so `Specs & Fit` is never clipped. All scraped
   fields pass through the new `escHtml()` in `dialogs.js` (XSS hardening);
   detail dialog fields escaped too; invented fallback fit text replaced
   with honest "no data" copy; a filtered-index bug in `showJobDetail`
   fixed. Brittle `top-pay` substring filter replaced by `isTopPayJob()`
   requiring an explicit hourly unit and rate >= $35.

6. **Bottom nav** — five items with one-line labels
   (Pipeline/Openings/Cash/Proposals/More + AR equivalents), centred
   icon+label, `.active` gets a `--brand-soft` pill + top indicator bar,
   `min-height` 48px inside a 56px+safe-area bar (>=44px targets).
   Content wrapper gets bottom padding so nothing hides under the bar.

7. **Drawer** — on <=1023px the four primary `.nav-tab`s (pipeline,
   openings, proposals, cash) are `display:none`; the drawer keeps
   Profile, Security/Diagnostics and Inbox. Badge seeds zeroed; every
   badge is fed from real API counts (staged/openings/proposals/cash/
   inbox) in one badge style; `badge-proposals` id wired (was missing);
   cash badge added in `cash.js`. Footer dev text
   `127.0.0.1:3456 DAEMON: OK` replaced by dot + calm
   `Local service`/`Connected`/`Offline (cached)`; daemon badge shows
   `Healthy/Degraded/Offline` (`security.js`).

8. **Self-audit loop** — `scripts/r22-audit.mjs` spins up a real server +
   headless Chrome via CDP and captures the full matrix; 66 PNGs in
   `docs/screenshots/r22/`. `test/test-r22-mobile-ux.mjs` asserts:
   no horizontal overflow on 7 views x 4 widths, banner below header,
   equal filter-chip heights AND a single shared top (no wrapping),
   equal header-chip heights, all touch targets >=44px, no header value
   without a label, bottom-nav content clearance, 5 short labels, card
   anatomy, drawer dedupe + integer badges + no dev-text leak, and an
   Arabic RTL smoke pass. Defect log: `.sir/DEFECTS_R22.md` — 3 cycles,
   cycle 3 clean.

Also fixed along the way: malformed `.app-nav:: -webkit-scrollbar`
selectors; dead CSS removed to keep `app.css` under the strict <60KB
budget (final 61,357 B); `test-a11y-ui.mjs` touch-target assertion
updated for `.filter-chip`; `test-auth-ui-flow.mjs` accepts the calm
`Local service` label; `test-cycle23-etag-offline-retry.mjs` status-text
assertions updated to the new calm labels; `windowsHide: true` added to
all `r22-audit.mjs` child processes (R11-5 contract); SW cache bumped to
`sir-jobs-v7`; asset `?v=` bumped.

## Commits pushed to main

- `f6aebcb` fix(r22): rebuild mobile dashboard chrome per owner iPhone audit
- `499619d` test(r22): deepen mobile audit assertions and capture evidence matrix
- `f1f598f` docs(r22): defect log and audit-cycle evidence
- `ebb52ed` fix(r22): restore semantic button tokens, final CSS budget trim
- `c9fefb3` fix(r22): restore reduced-motion selector contract, update checkpoint
- `70d58e1` fix(r22): keep CSS under 60KB budget after reduced-motion fix
- `f30d46f` fix(r22): windowsHide on audit script child processes
- `8b26abe` test(r22): align cycle23 status assertions with calm drawer labels
- `9d2a5a4` test(r22): inject fixture job card so anatomy check is data-independent

## Verification — real output

Local (Windows, Node):

- `npm test` — full 32-suite chain. Every suite passes; the chain was run
  to completion in segments after fixes (digest 11/11, dashboard 12/12,
  pipeline 10/10, security 9/9, undo 3/3, evals 4/4, a11y-ui 9/9,
  scheduled-run, motion-physics 8/8, decision-velocity, offline-resilience,
  ux-friction 9/9, theme-interaction 1/1, auth-ui-flow 1/1,
  cycle12 6/6, fx 4/4, round8 5/5, cycle17 5/5, cycle18 5/5, r10 7/7,
  r11 5/5, r12 5/5, cycle22 4/4, cycle23 4/4, r15-inbox 11/11,
  css-valid 3/3, post-guard 4/4, r16-ledger-race 6/6,
  r16-inbox-nonblocking 1/1, r16-features 15/15,
  r19-no-horizontal-scroll 1/1, r22-mobile-ux 1/1).
- `node test/test-r22-mobile-ux.mjs` —
  `✔ R22 mobile UX audit: overflow, banner, chips, targets, labels at
  320/390/768/1280 en+ar (17004ms)`, 1 pass 0 fail.
- `node test/test-a11y-ui.mjs` — 9/9 pass (CSS 61,357B < 61,440B).
- `node test/test-motion-physics.mjs` — 8/8 pass.
- `npm run lint` / `npm run typecheck` — run inside CI windows job
  (passed on the watched run); locally clean.
- `npm run doctor` — 6/6 gates green (run earlier this round).

CI (GitHub Actions, `verify` workflow on `main`):

- Runs 42927876888, 42928161672, 42928492629, 42928588317,
  42928656235 failed during the round; root causes found and fixed:
  missing `.btn-success`/`.btn-danger` tokens (ebb52ed), reduced-motion
  selector contract + 60KB CSS budget (c9fefb3, 70d58e1),
  `windowsHide` on audit script (f30d46f), stale cycle23 status
  assertions (8b26abe), data-dependent card anatomy check on clean CI
  checkouts (9d2a5a4).
- Final watched run on `9d2a5a4`: **GREEN** — `gh run watch 42929042639`
  completed with all jobs passing:
  `windows in 2m3s` (checkout, setup-node, Chrome install, npm install,
  lint, typecheck, npm test all checkmarks),
  `tests in 1m16s` (npm test pass), `secrets in 8s` (gitleaks pass).
  `gh run list` confirms `verify main push 42929042639` completed
  successfully on commit `9d2a5a4`.
- The final docs-only checkpoint commit `e541f2b` also passed:
  `gh run watch 42929370054` — windows 2m4s, tests 1m7s, secrets 9s,
  all jobs green. HEAD of `main` is verified green.

## Screenshots / evidence

- `docs/screenshots/r22/` — 66 PNGs: every view x {320,390,768,1280} x
  {en,ar} x {light,dark} as applicable.
- `.sir/DEFECTS_R22.md` — per-cycle defect table with root causes.
- `.sir/CHECKPOINT.md` — Now/Next step/Open promises updated.

## Still open / honest notes

- Banner dismissal persists in localStorage with no restore UI; the
  submission rule remains visible in the Security view. Logged in
  checkpoint open promises.
- Owner should re-check the dashboard on a real iPhone (390px dark)
  against the original defect list.
- CI status: GREEN — runs 42929042639 (`9d2a5a4`) and 42929370054
  (`e541f2b`, current HEAD) both fully passed per `gh run watch`.
  Earlier red runs are all explained and fixed.
