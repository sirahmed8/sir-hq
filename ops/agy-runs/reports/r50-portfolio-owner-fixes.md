# Report: r50-portfolio-owner-fixes (2026-11-12)

Brief: owner corrections after he read the live site. Work done in `D:\Projects\SIR Portfolio`, commit and push straight to `main`, both hosts redeployed.

## Commits pushed
- `1ab9a5b` r50: owner fixes (28 files, +416/-227)
- `2414f52` checkpoint update (2 files)

## What changed (by brief task)
1. **SIR Portfolio removed from its own project list** everywhere: `content/products.json` rewritten (13 items: sir-ai, education-hub, hagoozat, business, content-studio, controller, laptop-manager, modpack, gta-mods, life [global]; jobs, study [personal]; negm-furniture [client]). SIR Platform dropped (cancelled 2026-11-12). SIR Obour Hub renamed SIR Education Hub. `"rebuilt from zero"` framing removed from `public/llms.txt`, `scripts/gen-static.mjs`, `scripts/make-og.mjs`. Site is the portfolio, not a project.
2. **No live preview for any project except SIR AI, and none exists today.** Every item's `earlierVersion` set to null (old addresses were legacy apps, exactly what the owner ordered removed). WorkWall no longer renders preview buttons, embeds, live badges, counts of live previews, or the guaranteed-empty "With live preview" filter (dead UI removed). Featured shows the SIR AI button only when `liveLink()` finds a real address (none does). Hero ledger: 13 total / 13 in development / 0 finished / 0 answering, all computed.
3. **Product count never hard-coded** (computed with `useMemo` in WorkWall): "13 products · 10 for everyone, 2 personal tools, 1 client work" in en and ar (split spans in served HTML). AHome never mentioned. Card chips and layout chip localized via `ui.work.forEveryone/personalTools/clientWork`. `loaders.ts` bug fixed: item `class` was silently dropped, now passed through via `readClass()`. Product classes narrowed to global/personal/client (`types.ts`, `schemas.ts`).
4. **Timeline** rewritten with 4 truthful dated milestones (2023-08-25 GitHub opened; 2026-11-09 one shared standard; 2026-11-11 site live on Firebase + Vercel with notes and RSS; 2026-11-12 first products in development). **Scroll animations**: pages that popped in now reveal (privacy, facts, notes index, note [id], CV), all with IntersectionObserver, 40 ms stagger, fade-and-rise/spring easing, `prefers-reduced-motion` respected, content visible without JS, print forces all visible. `.rise` keyframes re-added to `globals.css` (they had been missing since 09ab807, so the Hero entrance and template transition were dead).
5. **CV prints on ONE A4 page** (en and ar). Tightened print-only CSS (`@page` 9mm/11mm margins, 8.2pt/1.24 body, 17pt h1, 10pt h2, tighter cards/sections/grids/spacing, orphans/widows). Verified with puppeteer print-to-PDF serving `out/` over local HTTP: both PDFs contain exactly 1 page (1 `/Type /Page`, `/Count 1`, one MediaBox). Print scrollHeight: 764px en, 731px ar (A4 printable ~1054px at 96dpi). First measurement run read the pages via `file://` and got stale/unstyled results (identical byte counts); fixed the harness, re-verified with CSS loading.
6. **Hire `<dl>` fix** (a11y): CopyButton moved inside `<dd>` so each dl-wrapped `<div>` contains only dt+dd. **Axe: 0 serious/critical (in fact 0 violations) on all 24 route-theme-language combos** (before the fix: 1 serious `definition-list` on home in en/ar, light/dark). **Keyboard audit: all pass in en and ar.**
7. Checkpoint, TASKS.md updated; one line appended to `ops/bus/sir-hq.md`.

## Verification (CI quota flag present at `D:/Projects/_SIR/ops/ci-quota-exhausted.flag`; full local verification substituted, per preamble rule 18)
- `npm run content:check` / `npm run typecheck`: `content check: 0 error(s), 0 warning(s)`, tsc --noEmit clean.
- `npm test`: **pass 843, fail 0** (fixture-independent earlierVersion tests added).
- `npm run build`: success; 21 static HTML pages; First Load JS shared ~103 kB (home ~122 kB, under 150 kB budget).
- `node scripts/axe.mjs`: 0 violations on all 24 combos (routes /, /cv/, /facts/, /privacy/, /notes/, /notes/the-agent-team/ x en/ar x light/dark).
- `node scripts/keyboard-audit.mjs`: all pass (en and ar).
- Live curl after deploy: 200 on `/en/`, `/ar/`, `/en/cv/`, `/ar/cv/` on both hosts; new `llms.txt` framing ("Every product is in active development and none is listed as finished.") live on both hosts; **zero occurrences of "SIR Portfolio"** in the served English home HTML on both hosts.
- Firebase Hosting: release complete (`https://sir-portfolio-site.web.app`). Vercel: production READY (`https://sir-portfolio-liart.vercel.app`), confirmed by `vercel ls` and curl.

## What is still open
- `public/og/*.png` OG images predate the r50 status line; regenerate with `npm run og` when convenient.
- `firebase` CLI bin is missing from the npm global PATH on this machine (`vercel` works); Firebase deploy ran via `node .../firebase-tools/lib/bin/firebase.js deploy --only hosting`.
- Custom domain still owner action (`.sir/DOMAIN.md`); CSP `unsafe-inline` polish unchanged.
- A parallel worker produced new untracked files during this round (`.sir/evidence/cv-print-en.pdf`, `cv-print-ar.pdf`, `cvdiag.tmp.mjs`, `scripts/check-cv-print.mjs`, and re-modified `content/timeline.json` after my push). Left untouched.
- Housekeeping note: an intermediate local commit `2006435` accidentally swept in files from another session's unstaged work (`.gitignore`, `assets/brand/icon.png`, `scripts/dev-*.ps1`, tsbuildinfo deletion). The push failed on a network error before it left the machine, so it was reset and re-created as `2414f52` (CHECKPOINT/TASKS only). Remote main contains only `1ab9a5b` and `2414f52`; the other session's files remain uncommitted for their owner.
- CI remains unverifiable until the GitHub Actions quota resets (~2026-12-01); local verification above stands in for it.
