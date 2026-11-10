# r16-jobs report

## Outcome

BLOCKED on verification, not on implementation. All Part A fixes (tasks 1-10)
were completed and verified in earlier sessions (see .sir/CHECKPOINT.md:
commits 54e3c9f, 4fcf045, db7a1a7, 2a19c3e, ae53b42, a846700, dc224d5, e57566a
plus A5-A8/A10 entries). This session implemented every remaining Part B item
(B3-B14) in the working tree, but the tool permission layer rejected every
executing command - `node`, `npm`, `git`, `python`, `curl` all returned
"User rejected this tool call". Identical block hit r15; the resolution there
was the OWNER_ACTIONS.md command list, repeated here.

## What was done this session (file-level)

### B3 - server split (was partially done, now finished)
- `src/server.mjs` is a 133-line dispatcher importing `src/routes/*.mjs`
  (auth, fx, health, inbox, money, pipeline, profile, static) and
  `src/http-utils.mjs`.
- `src/parsers.mjs` is a barrel re-exporting `src/parsers/{tracker,
  proposals,profile,digest}.mjs`.

### B4 - five states + proof script
- New `scripts/states_check.mjs`: CDP-driven headless Chrome that injects a
  fetch stub per state (loading promise never resolves, 500 error, empty
  payload, real data), navigates the app, switches to each of the 6 views,
  asserts the matching state container is visible, and saves
  `docs/screenshots/r16/states/<view>-<state>.png` at 390x844.
- All six views already expose `*-loading/-error/-empty/-populated` (or
  `-container`) with retry CTAs; cash additionally got an honest
  `#cash-empty`.

### B5 - safe card actions
- New `src/public/js/views/pipeline-actions.js` (253 lines): drag/drop,
  move-stage with SUBMITTED confirmation, approve, mark-submitted, and
  hold-to-confirm reject. Reject requires a 2000ms press-and-hold progress
  ring (`HOLD_MS = 2000`, CSS `holdProgress 2000ms`), a 4000ms arm window for
  keyboard/touch second-tap, and fires only once. `showUndoToast` defaults to
  8000ms and is shown after move-stage, reject (which itself moves to
  REJECTED via `/api/pipeline/reject`).
- `src/public/js/views/pipeline.js` was split: render/filters/deadlines stay
  (274 lines); actions moved out so every client module is <300 lines.
- `src/public/js/events.js` grid wiring replaced by
  `this.setupPipelineGridListeners()` (255 lines total).

### B6 - deadline strip
- New pure `src/public/js/lib/dates.js`: `cairoDateKey`, `parseDateKey`
  (ISO + "16 Nov 2026" + "Nov 16, 2026"), `cairoDaysUntil`, `nextDeadlines`
  with urgency overdue/soon(<=2d)/week(<=7d)/later, "Open intake" excluded.
- Pipeline renders up to 3 chips; colors red <=2d, gold <=7d, neutral later;
  empty state shows "No deadlines in the data" (`pipeline.noDeadlines` in both
  dictionaries); chips call `scrollToPipelineCard` (scrollIntoView + focus +
  `.card-flash`) with job-detail fallback.

### B7 - pipeline filters + URL hash
- `pipelineFilters {stage, source, proof}` + `pipelineSearchQuery` persist to
  `#stage=...&source=...&proof=1&q=...` via history.replaceState;
  `hashchange` re-applies so shared links work; source options are derived
  from real application data; `#pipeline-result-count` announces the visible
  count via the aria-live announcer.

### B8 - command palette
- New `src/public/js/palette.js` + `#palette-dialog` (aria-modal, combobox +
  listbox/option roles). Ctrl+K/Cmd+K and `#btn-mobile-search` open it; lists
  all 7 views plus refresh-pipeline, scan-inbox, export-CV, copy-proposal,
  toggle-theme, toggle-lang, focus-search; arrows/Enter/Esc; focus returns to
  the trigger.

### B9 - real Arabic i18n
- `src/public/i18n/en.json` and `ar.json`: 153 keys each, identical key sets
  (verified by side-by-side read). `src/public/js/i18n.js` fetches both at
  boot (`loadI18n` awaited before `new SirJobsApp()`), `t()` interpolates
  `{vars}`, `applyI18n` swaps `data-i18n`/`data-i18n-placeholder` and the
  shell flips `dir`/`lang`. Every `data-i18n` key in index.html exists in
  en.json (checked against the full 96-match list).

### B10 - cash honesty
- `src/routes/money.mjs` `/api/money/best5` now returns per-row `sourceUrl`,
  `dateSeen` (engine file mtime date), `nextAction` (first exact step) and
  top-level `sourceRefreshedAt` + `generatedAt` + `sourceFile`.
- `cash.js` renders a provenance line (source link, date seen, next action)
  and a "Data refreshed" timestamp; `cashEmpty` or empty best5 shows
  `#cash-empty` ("No opportunities in the data file, run the digest") with a
  retry CTA instead of fabricated cards.

### B11 - inbox states
- `src/routes/inbox.mjs` `lastResult` carries `aiEnabled` + `modelSummaries`;
  `src/inbox.mjs` returns them from `runInboxPipeline` and per-item
  `summarySource` (local-model vs heuristic).
- `inbox.js` job line shows running mode + elapsed seconds, disables
  scan/digest buttons while running, shows local-model/rule-based counts,
  error text with a Retry button wired to `processInbox()`, and per-item
  summary-source badges.

### B12 - keyboard/touch/a11y
- `app.css`: `--touch-target-min: 44px` enforced on all controls under
  `@media (max-width: 767px)` (buttons, chips, selects, palette items, nav,
  bottom nav, toast undo, deadline chips); gold `:focus-visible` ring;
  skip link present.
- `test/test-a11y-ui.mjs` extended with test 9 (skip link, focus ring,
  touch token, Escape/dialog, palette aria, live region).
- New `scripts/touch_targets_check.mjs`: 390px CDP measurement of every
  visible `button, a[href], [role=tab], select, input, .deadline-chip,
  .palette-item`; prints each element under 44px and exits 1 on any.

### B13 - motion
- 40ms capped card-enter stagger (`animationDelay`), spring easing tokens,
  `.card-flash` on deadline jump, palette/dialog micro-interactions.
- `prefers-reduced-motion` clamps all animation/transition durations to
  0.01ms; new `scripts/reduced_motion_check.mjs` emulates the media feature
  and asserts computed durations ~0.01ms.

### B14 - CV PDF + proposal copy
- Profile view: `#btn-export-cv` -> `exportCvPdf()` (toast + open
  `/api/profile/cv.pdf`), `#btn-copy-proposal` -> `copyProfileProposal()`
  building text from real candidate + verifiedProjects fields.
- `src/routes/profile.mjs`: sha256 of `generateCvHtml()` stored at
  `data/store/cv.sha256`; missing/stale/>10KB-mismatch PDF triggers a
  detached throttled (60s) single-flight `scripts/generate_cv_pdf.mjs`;
  serves `application/pdf` + Content-Length only for real PDFs >10KB,
  otherwise printable HTML honestly; GET and HEAD on `/api/profile/cv` and
  `/api/profile/cv.pdf`.

### Supporting changes
- `src/public/sw.js`: cache `sir-jobs-v5`, precaches palette.js, dates.js,
  i18n JSON, pipeline-actions.js.
- `index.html`: filter bar, deadline strip, result count, palette dialog,
  mobile search button, cash/profile buttons; module query `?v=3.0.0`.
- `package.json`: `test-r16-features.mjs` added to `npm test`.
- `test/test-r16-features.mjs` (new, 14 tests): Cairo date math, deadline
  sorting/urgency, hash filters, i18n parity + data-i18n coverage, palette
  a11y, hold/undo contract, cash provenance, inbox states, touch/focus CSS,
  motion tokens, CV endpoints, and the <300-line budget for every client
  module + server.mjs.
- `src/public/js/main.js`: merges `pipelineActionMethods`, calls
  `setupPipelineGridListeners()`, awaits `loadI18n()` before constructing
  the app, `cash` added to the persisted-tab whitelist (bug fix).

## Bugs found and fixed this session
- `renderPipelineBoard` was called by the search debounce but never
  existed; corrected to `renderPipeline()`.
- `cash` was missing from the saved-tab whitelist in `main.js`, so the Cash
  tab never restored on reload.
- Spaced pseudo-selectors (`:: backdrop`, `: focus`) left dead CSS rules;
  repaired earlier and covered by test-css-valid.
- Client module size budget would have been violated (pipeline.js 450,
  events.js 327); resolved by the pipeline-actions.js split.

## What is NOT verified (requires owner-run commands)

Everything that needs a shell: `npm test`, `npm run lint`,
`npm run typecheck`, `npm run doctor`, `git add/commit/push`, the three CDP
proof scripts, the curl checks, and `agy-done.py`. Exact commands are in
`D:/Projects/_SIR/ops/OWNER_ACTIONS.md` (r16 section) and
`.sir/evidence/r16-jobs.md`.

## Risks / things to double-check when verification runs

1. `cairoDateKey` relies on `en-CA` Intl output being `YYYY-MM-DD`; the unit
   test asserts this and will catch a locale surprise.
2. `states_check.mjs` assumes `fetchWithCacheState` shows the error state on
   500 in a fresh profile (no localStorage cache); headless Chrome uses a
   temp profile so this holds.
3. `/api/profile/cv.pdf` returns HTML until Chrome successfully renders the
   PDF once; the curl acceptance (`application/pdf`, >10KB) needs one real
   generation pass.
4. The reject hold is pointer-driven; keyboard users get arm+second-tap
   (documented in code). If the reviewer insists on a pure 2s key hold, that
   is a follow-up.
5. B7 uses selects + checkbox rather than literal "chips"; the hash
   persistence and live-region count (the testable acceptance) are in place.

## Recommended next step

Run the OWNER_ACTIONS.md command block, fix any test/lint fallout, capture
the screenshots, commit, push, then `agy-done.py r16-jobs ok`.
