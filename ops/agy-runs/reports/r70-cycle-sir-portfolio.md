# r70-cycle-sir-portfolio — round report

Date: 2026-11-13. Worker: Devin. Lens: **offline and error recovery** (new lens; earlier cycles covered a11y/keyboard, RTL/bidi, copy, feature gaps, CSP, motion).

## Done

1. Took the lock (`ops/locks/sir-portfolio.lock`), logged START in `ops/bus/team.md`, read WORKER_PREAMBLE, CHECKPOINT, TASKS, FEATURE_GAPS, IMPROVEMENT_DOCTRINE, PERPETUAL_LOOP, plan and ledger. `ops/briefs/sir-portfolio-tasks.md` does not exist; used `.sir/TASKS.md` + `.sir/plans/FEATURE_GAPS.md` (noted in checkpoint).
2. Wrote cycle plan `.sir/cycles/2026-11-13-1.md` and audit `.sir/reports/2026-11-13-cycle.md` with a "Found without being told" section (10 findings).
3. Shipped 10 concrete improvements, one commit each, all pushed to `main`:
   - `b0e5306` bilingual 404 actually ships (postbuild.mjs) + polish
   - `9ea8c33` shared clipboard helper + localized copy-failure states (hire, footer, context menu, contact form) + vCard revoke fix
   - `0728885` Enter submits the contact form when valid
   - `90cf224` `[lang]/error.tsx` + `global-error.tsx` bilingual error boundaries
   - `c4383fc` service worker + `offline.html` + registration + `offline-check.mjs` + no-cache headers
   - `bcd8487` `manifest.webmanifest` + PNG icons 192/512/maskable/apple via `make-icons.mjs`
   - `ecd14ee` choose-lang preserves query; chooser page theme/favicon/manifest
   - `b156609` back-to-top leaves tab order/a11y tree while hidden
   - `be22f0f` WorkWall `replaceState` try/catch
   - `2ae9e78` checkpoint/tasks/feature-gaps bookkeeping
4. Verification (local; CI quota flag present, rule 18): content:check 0/0, tsc clean, 843/843 tests, build ok (home 124 kB first-load JS vs 150 kB budget), offline-check 5/5 with server killed, axe 24/24 clean, keyboard audit all pass en+ar.
5. Deployed both hosts and curl-verified: Firebase Hosting (119 files, rebuilt after the last commits — first deploy was stale, caught and fixed) and Vercel production READY. Verified on both: /en/ /ar/ /en/cv/ 200, /sw.js 200 `Cache-Control: no-cache`, /manifest.webmanifest 200 `application/manifest+json`, /offline.html 200, unknown URL → bilingual 404, choose-lang.js carries `location.search`.
6. FEATURE_GAPS #17 marked Implemented; CHECKPOINT.md, TASKS.md updated.

## Evidence highlights

- Before: `out/404.html` = Next default (`next-error-h1`, English only). After: contains `هذه الصفحة غير موجودة`, verified live on both hosts.
- Before: no SW/manifest/icons; offline = browser error page. After: `scripts/offline-check.mjs` 5/5 PASS — SW active, pages cached, cached page renders with the server process killed, uncached URL shows the bilingual offline page.
- Copy failures: previously silent (form) or unhandled rejection (context menu); now every surface shows "Couldn't copy, try again" / «تعذّر النسخ، حاول مجدداً».

## Left / open

- Owner-blocked: custom domain (R4-6/T-041); everything else is one command away.
- Deferred FEATURE_GAPS: #5, #11, #12, #16, #19 (owner decision), #21 (CI quota).
- `ui.notFound` strings are unused content (real 404s come from `public/404.html`); cleanup candidate.
- Lighthouse numeric Performance score still not measurable with local tooling.
- `ops/briefs/sir-portfolio-tasks.md` missing — HQ may want to fix the brief template or create the file.

## Ideas for new tasks

- Purge or use `ui.notFound` (dead strings) — tiny cleanup task.
- Lighthouse CI budget check once Actions quota resets (#21).
- Consider `Cache-Control: immutable` for `/icons/*.png` and `/og/*.png` (content-stable assets currently get no explicit rule).
- A "what's new" note mechanism when content/*.json changes materially.
