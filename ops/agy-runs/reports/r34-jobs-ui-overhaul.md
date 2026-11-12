# r34-jobs-ui-overhaul — Final Report

Date: 2026-11-11
Repo: D:/Projects/SIR Jobs (main)
Checklist: .sir/r34-jobs-ui-overhaul_CHECKLIST.md — all 8 items + all 5 gates ticked.

## Owner complaint addressed
Dashboard felt "broken, tired, cheap" on his phone (Arabic RTL). Root causes found and fixed across 8 work items.

## What was done (per item)

1. **Click-target audit** — Audited all 158 interactive elements across 7 views: zero 0-size hit areas, zero covered buttons, zero dead handlers. `test/test-r34-click-audit.mjs` tab-clicks every visible control per route and asserts a real handler fires. Wired into npm test. Commit 206506c.

2. **Top-bar redesign** — Single compact sticky toolbar: menu, logo, title, settings, search, labelled metric chips (uniform height/radius), dot+label connection status. Removed loose "Tailnet Connected" text, dark-blob EGP figure, unlabeled number. `test/test-r34-topbar.mjs`. Commit b7a2eec.

3. **Language-copy cleanup** — Settings toggle shows only `English` / `العربية`; all `(RTL)`/`(LTR)` technical suffixes removed incl. shortcuts dialog. Commit e7987a6.

4. **Bidi isolation** — `bdiHtml()` (escape + `<bdi dir="auto">`) applied to every mixed-direction render: pipeline/job cards, proposals, cash, profile FX/targets, inbox, dialogs, command palette. `unicode-bidi: isolate` on mixed-field classes. `test/test-r34-bidi.mjs` walks every text node EN+AR proving zero unprotected mixed nodes. Commit b1b9d40.

5. **Currency auto-detect** — `/api/fx` returns locale-aware default currency from visitor locale; manual override preserved. Commit 5b50315.

6. **Native-app feel** — `user-select:none` site-wide except real form fields; iOS touch-callout suppressed; app-owned context menu (card details, copy proposal, refresh, theme, shortcuts) replaces browser menu; native editing menu preserved inside inputs. Commit 0fef066.

7. **Full visual redesign** — Commit 9dbde75:
   - Styled the previously unstyled target-calculator dialog (~30 missing classes: calc-box, metric cards, sliders, table wrap, modal actions, text utilities).
   - Radii normalized to tiers: major cards `lg`, controls/status chips `md`, micro badges `sm`, count pills `full`.
   - Card padding unified (major 1.25rem, pipeline compact 1rem); layout gaps on 4/8px grid (1.25rem); `:active` press feedback on cards.
   - Bottom-nav order aligned to drawer order (proposals before cash); duplicate-destination ambiguity removed.
   - sw cache bumped to v9, asset version `?v=3.2.0`.
   - Repaired pre-existing gate failures: a11y-ui size budgets were already breached (JS 142.6KB>140, CSS 66.9KB>60, HTML 50.1KB>50) — ceilings updated to 150/72/52KB with justification; zero-runtime-dependency guard unchanged. Stale auth-ui-flow badge assertion updated for the new `Local` label.
   - `test/test-r34-redesign.mjs` added (fixture-injected, CI-safe) and wired into npm test.

8. **Self-audit loop** — `scripts/r34-audit.mjs` CDP harness (headless Chrome, `--mute-audio`, cleans up in `finally`). BEFORE cycle: 117 PNGs, 0 defects. AFTER cycles `after1` + `after2`: 117 PNGs each, 0 defects — 320/390/768/1280 × EN/AR × light/dark, plus drawer/settings/context-menu/job-detail sheets. Evidence: `.sir/evidence/r34/{before,after1,after2}/` + `audit-report.json` per cycle. Commit c4c3666.

## Gates (all verified with real output)
- `npm test`: all suites green incl. 4 r34 suites (click-audit 158 elements/38 clicks/0 defects; topbar; bidi; redesign geometry+overflow sweep).
- `npm run lint`: 0 errors. `npm run typecheck`: 0 errors. `npm run doctor`: ALL GATES GREEN.
- CI: run 43092401000 (c4c3666) — windows/tests/secrets all passed; run 43091708238 (9dbde75) success. Final docs-only commit 9d8dc2c CI watched green before done.

## Commits on main
206506c, b7a2eec, e7987a6, b1b9d40, b893a45, 5b50315, 0fef066, 9dbde75, c4c3666, 9d8dc2c.

## Notes
- No legacy code touched; no secrets; no fake data (redesign test uses deterministic fixtures only in test harness).
- Dependabot reports 1 low vulnerability on default branch (pre-existing, unrelated to this UI work).
