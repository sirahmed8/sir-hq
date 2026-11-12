# r46 report: SIR Portfolio

Round: r46 (2026-11-12). Task: competitor matrix, feature-gap list, implement top 3 items, verify EN/AR, light/dark, 320/390/768/1280, commit + push to main, update checkpoint, add bus line, report, done command.

## What I found on entry

The previous model had completed all implementation and local verification but was cut before committing/deploying/reporting:

- Staged: `src/components/CopyActions.tsx` (new), `src/components/WorkWall.tsx`, `src/components/Hire.tsx`, `src/components/Footer.tsx`, `content/ui.json`, `.sir/plans/COMPETITOR_MATRIX.md`, `.sir/plans/FEATURE_GAPS.md`, 48 evidence PNGs in `.sir/evidence/r46/`.
- Unstaged/untracked: `.sir/CHECKPOINT.md` update, audit reports (`axe-report.md`, `axe-report-detail.txt`, `keyboard-audit.md`), `tsconfig.tsbuildinfo`.
- Checkpoint round-46 section claimed: content-check 0/0, typecheck clean, 829 tests pass, build OK, 122 kB home JS, axe + keyboard audits run.

Nothing was broken; I verified the tree still passes gates, then finished the commit/push/deploy/report cycle.

## What changed (all in commit 6f83d98, pushed to main)

1. `.sir/plans/COMPETITOR_MATRIX.md` — 5 best-in-class comparators (Carrd, Framer, Contra, Super.so, Read.cv/Bento historical benchmark) plus portfolio pattern examples; strongest 3 / weakest 3 / copy / do-better per product; unverified prices marked.
2. `.sir/plans/FEATURE_GAPS.md` — 22 ranked gaps/ideas, each with value, risk, rationale, acceptance test; items 1-3 marked implemented.
3. Work section filter — All / With live preview, truthful counts, live-preview badge derived from existing `answers()` data (`src/components/WorkWall.tsx`, `content/ui.json`).
4. One-tap copy actions for email and WhatsApp number in Hire with transient confirmation (`src/components/CopyActions.tsx`, `src/components/Hire.tsx`).
5. "Copy page link" action in footer (`src/components/CopyActions.tsx`, `src/components/Footer.tsx`).
6. Evidence: 48 Puppeteer screenshots (home/work/hire x 320/390/768/1280 x EN/AR x light/dark) + axe and keyboard audit reports in `.sir/evidence/r46/`.

Checkpoint follow-up commit 4a0893f recorded the redeploys and fixed a truncated command line in the verification note.

## Commands run and real output

- `node scripts/content-check.ts` -> `content check: 0 error(s), 0 warning(s)`
- `npm run typecheck` -> content check 0/0, `tsc --noEmit` clean (exit 0)
- `git commit` + `git push origin main` -> `7fe65db..6f83d98 main -> main`
- `npm run build` -> Next static export succeeded, home first-load JS within the 150 kB budget (122 kB per prior measurement)
- `firebase deploy --only hosting` (via `npx firebase-tools` since `firebase` is not on this shell's PATH; firebase-tools 15.36.0 installed on the fly) -> `Deploy complete!` for `sir-portfolio-site`, 110 files in `out`, release complete, https://sir-portfolio-site.web.app
- `vercel deploy --prod --yes` (Vercel CLI 65.14.0) -> deployment `dpl_ASAZywpqvtsuhhFJNSuWmKxLcnx8` READY, aliased to https://sir-portfolio-liart.vercel.app
- Live checks: `curl -L` on `/en/` and `/ar/` -> 200 on both hosts (4/4)
- Prior model's full verification (recorded in checkpoint): `npm test` 829/829 pass, axe 24/24 clean, keyboard audit all pass

## CI status

`D:/Projects/_SIR/ops/ci-quota-exhausted.flag` exists (GitHub Actions minutes exhausted until ~2026-12-01). Per WORKER_PREAMBLE item 18, "CI green" is replaced by full local verification, which passed. Still pushed straight to `main` as required.

## Still open / next

- R4-6 custom domain: owner must buy it, then `npm run domain -- https://<domain>` (steps in `.sir/DOMAIN.md`).
- Strict CSP hashes (polish).
- 19 of 22 feature-gap items remain planned for future rounds.
- Keep `SIR_Portfolio_Refresh` scheduled task healthy (`.sir/refresh.log`).
- `firebase` CLI is not on PATH in the Git Bash shell; `npx firebase-tools` works but installs the package each time (cached). Worth noting for future rounds.

## Bus line

Appended to `D:/Projects/_SIR/ops/bus/sir-hq.md` at 2026-11-12T14:33:03+02:00.
