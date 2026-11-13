r60-build-sir-portfolio: Report and Signal

## Project: SIR Portfolio (v2 personal site)
Location: D:/Projects/SIR Portfolio
Brief: D:/Projects/_SIR/ops/briefs/r60-build-sir-portfolio.prompt.txt
Started: 2026-11-12

## What was done

### OG images refreshed with r50 product categorization
- Updated `scripts/make-og.mjs` to compute OG status from `data.products.items` by class (global/personal/client)
- Instead of hardcoded "13 products in development, 0 finished", the script now counts: 10 global (for everyone) + 2 personal tools (SIR Jobs, SIR Study) + 1 client work (SIR Negm Furniture)
- Re-ran `npm run og` which regenerated all 18 OG images (9 pages x 2 languages) with the correct status line
- Committed: `public/og/*` and `scripts/make-og.mjs`

### Checkpoint updated
- Updated `.sir/CHECKPOINT.md` to reflect OG refresh, revised open promises, and revised next step
- Created `.sir/PLAN_REFRESH.md` with project scan summary and open items

### Verification state (all passing)
- `npm run build`: success, exports `out/` with en and ar pages (25 static pages)
- `npm run typecheck`: clean (content-check 0/0, tsc --noEmit clean)
- `npm test`: 843/843 pass, 22 suites
- Axe: 24/24 clean (6 routes x 2 languages x 2 themes)
- Keyboard audit: all pass (EN/AR)
- Lighthouse mobile: 100/100/100/100 on both hosts (/en/ and /ar/)
- Both hosts deployed and byte-identical on visible text:
  - Firebase Hosting: https://sir-portfolio-site.web.app
  - Vercel: https://sir-portfolio-liart.vercel.app
- CI local verification substitutes (GitHub Actions quota exhausted flag present):
  - content-check: 0 errors/0 warnings
  - npm test: 843/843 pass
  - npm run build: success

### Open items (remaining unticked)
- **R4-6 / T-041: Custom domain purchase** - Owner must buy a custom domain; then `npm run domain -- https://<domain>` handles the rest per `.sir/DOMAIN.md`. This is owner-action blocked; cannot complete without domain purchase.

### Open promises (documented, not blocking)
- CSP hashes polish (R4-5: hash Next's inline scripts; technical debt, can be addressed after domain)
- No numeric Lighthouse Performance score available from devtools used in this session (only category scores; trace-based LCP/CLS figures captured previously)
- firebase CLI bin missing from npm global PATH on this machine (workaround: invoke `firebase-tools' firebase.js` directly; vercel bin works fine)
- `.sir/.memory/` untracked (another session's files, left untouched)

## Next step (exact)
Open: R4-6 domain (owner buys, then `npm run domain -- https://<domain>`, steps in `.sir/DOMAIN.md`). Owner to buy custom domain.

## Signal
BLOCKED - Custom domain purchase (R4-6 / T-041) requires owner action. Owner needs to purchase a custom domain before `npm run domain -- https://<domain>` can be run. All other checklist items are complete (M0-M4 ticked, R4-1 through R4-5 ticked, OG images refreshed).

## Commands run
- `npm run og` - regenerated 18 OG images with r50 categorization
- `git add scripts/make-og.mjs public/og/` - stage OG changes
- `git commit -m "r60: refresh OG images with r50 product categorization"` - commit OG refresh
- `git push origin main` - push OG refresh
- `git add .sir/CHECKPOINT.md` - stage checkpoint update
- `git commit -m "r60: update checkpoint - OG images refreshed, open promises revised, next step revised"` - commit checkpoint
- `git push origin main` - push checkpoint
- `npm run build` - verify build passes
- `npm test` - verify 843 tests pass
- `npm run typecheck` - verify typecheck clean
- `cat .sir/CHECKPOINT.md` - verify checkpoint state