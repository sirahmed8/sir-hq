# Report: r67-build-sir-portfolio (Devin, 2026-11-12)

## What I found on arrival
- Uncommitted work from a previous model: `content/timeline.json` edits (new SIR AI + product-family milestones), a **broken** `scripts/weekly-refresh.mjs` (imports and whole body deleted, leaving undefined `path`/`root`/`execSync` references), a new `scripts/check-cv-print.mjs`, `cvdiag.tmp.mjs` temp file, `.sir/PLAN_REFRESH.md`, `.gitignore` additions, a regenerated `assets/brand/icon.png` (19 bytes differ, same 256x256 PNG).
- Stale lock `ops/locks/sir-portfolio.lock` owned by opencode for already-finished r50; replaced with my own, released at the end.
- CI quota flag `ops/ci-quota-exhausted.flag` present → local verification substituted per WORKER_PREAMBLE rule 18.

## Repairs (commit 437b2f1)
- `scripts/weekly-refresh.mjs` restored from HEAD (`node --check` clean); deleted `cvdiag.tmp.mjs`.
- `content/timeline.json`: added dated "SIR AI goes live" (2026-11-11) and "product family is named" entries. Verified claims first: `sir-ai-official.web.app` and `sir-ai-pi.vercel.app` both curl 200; SIR AI `.sir/CHECKPOINT.md` confirms a real `/api/ask` answer on both hosts and Telegram bot `getMe` ok (@SirAiAssistantBot). Softened "bot works" to "bot is live" to match evidence.
- `scripts/check-cv-print.mjs` rewritten: the file:// approach silently failed because the Next export uses absolute `/_next/` asset paths — under file:// the stylesheet 404s, the print CSS never applies, header/footer render, and PDFs come out 2 pages. Now serves `out/` over a tiny node:http server and uses `preferCSSPageSize` so `@page` rules apply. Result: **en and ar CVs each print exactly 1 A4 page** (`.sir/evidence/cv-print-*.pdf`).

## Feature gaps shipped (all from `.sir/plans/FEATURE_GAPS.md`)
- **#6 Work search** — client-side filter over product name + both summary languages, live "N shown" count, empty state with clear action, `aria-live`. Verified: "negm" → 1 card, "zzzznope" → empty state + 2 clear buttons, clear restores 13.
- **#7 Hero open-to line** — truthful line from `profile.openTo` under the CTA row (rendered as text, not chips; the entries are sentences — noted in the gaps file).
- **#10 BackToTop** — new `src/components/BackToTop.tsx`: appears past 640px scroll, 44px target, `end-5` logical inset (verified x=326 en / x=20 ar at 390px), reduced-motion aware smooth scroll, `no-print`.
- **#15 Social read date** — "All numbers read on {social.readAt}" under the Social grid, both languages.
- **#18 JSON-LD ItemList** — home page emits ItemList of all 13 products (position/name/summary/#work-<id> url) beside the Person schema; verified `ItemList:13` in served HTML.
- **#22 Product deep links** — WorkWall cards have `id="work-<id>"`; opening a row `replaceState`s the hash, `/<lang>/#work-<id>` auto-opens on load and hashchange. Verified `#work-jobs` opens panel, click → `#work-study`.
- **#8 Notes reading time** — `readingTime()` in `src/content/index.ts` (200 wpm en / 160 ar, min 1) on index + detail.
- **#9 Related notes** — `relatedNotes()`: shared title/summary word overlap with en+ar stopword lists, deterministic tie-breaks, hidden when empty. Verified live ("the-agent-team" → what-done-means, why-truthful-profiles).
- **#13 Save contact** — `SaveContactButton` downloads a .vcf built only from public fields; blob content verified in headless Chrome (FN/N/TITLE/EMAIL/TEL/URL all correct).
- **#14 CV print** — closed via the new check-cv-print.mjs (1 A4 page both languages).
- **#20 Forced-colors audit** — puppeteer `forced-colors: active`: focus outline solid 2px everywhere, system colors apply, card borders preserved; no control loses its boundary.

## Honest triage of the rest
FEATURE_GAPS.md now statuses all 22: 12 implemented, #4 obsolete after r50 (all previews removed), deferred with reasons: #5 (needs real per-product content fields), #11 (no finished product yet), #12 (needs sourced quotes), #16 (no shortcuts exist yet), #17 (needs 192/512px PNG icons; only 256px brand icon), #19 (needs owner decision + privacy disclosure), #21 (CI quota exhausted).

## CSP decision (was an open promise)
`script-src 'unsafe-inline'` stays: Next static export emits ~30 inline `self.__next_f` RSC payload scripts per page with no nonce/hash hook; per-path sha256 headers across ~50 pages would be huge and brittle. Documented in CHECKPOINT.

## Verification (all local, CI quota flag present)
- `npm run content:check -- --strict` → 0 errors, 0 warnings
- `npm run typecheck` → clean (content-check + tsc --noEmit)
- `npm test` → 843/843 pass
- `npm run build` → success, home `/[lang]` 124 kB First Load JS (budget 150)
- `node scripts/axe.mjs` → 24/24 route-theme-lang combos, 0 serious/critical
- `node scripts/keyboard-audit.mjs` → all pass en+ar (fixed one unnamed search input with aria-label)
- `node scripts/check-cv-print.mjs` → 1 page en + ar
- Puppeteer functional checks for search/empty/clear/back-to-top/deep-link/vCard blob

## Deploys (every batch, both hosts)
- Firebase Hosting `sir-portfolio-site` release complete (110 files) after each batch.
- Vercel production READY → https://sir-portfolio-liart.vercel.app after each batch.
- curl 200 verified: `/en/`, `/ar/`, `/en/notes/`, `/ar/notes/`, `/en/cv/` on both hosts; new strings confirmed live ("Save contact", "ItemList", "min read", "Related notes", "Search products", "ابحث في المنتجات", "قُرئت كل الأرقام").

## Commits on main
`437b2f1` repairs+CV test+timeline · `c03f8c6` gaps 6/7/10/15 · `860f1b1` gaps 18/22 · `d83d9b6` gaps 8/9 · `0805d29` gaps 13/14 · `d79f05f` triage+checkpoint · `02facbd` tasks ledger.

## Still open
- R4-6/T-041 custom domain — owner must buy it, then `npm run domain -- https://<domain>`.
- Deferred feature gaps listed above with their blockers.
- `SIR_Portfolio_Refresh` weekly task unchanged and healthy (`scripts/weekly-refresh.mjs` restored).

## Notes for the next tool
- `.sir/CHECKPOINT.md` "Next step (exact)" is current; lock released; team.md + sir-hq.md bus lines written.
- Local static server used for audits: `node scripts/serve.mjs 4173` (killed after use).
