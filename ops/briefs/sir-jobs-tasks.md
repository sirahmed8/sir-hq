# First 10 Tasks to Hand to Free Agents: SIR Jobs (sir-jobs-tasks.md)

Tasks ready to queue for the free CLI agents (Kilo, OpenCode, Devin CLI, ZCode). Each has a title and a one-paragraph brief. All are scoped to under 2 hours. Work in `D:\Projects\SIR Jobs` (app code) and write reports/evidence only inside that project or `D:\Projects\_SIR\ops\`. Never open `D:\Projects\AHome`. Never put secrets in git. Every task ends with the project's gates run and pasted into the checkpoint: `npm test`, `npm run lint`, `npm run typecheck`. PERSONAL product: do not add public hosting, Firebase, Vercel, billing or auth; do not charge anyone. Version stays 1.0.0. No placeholders, no invented data, every screen keeps five states, Arabic RTL and English, 44 px targets, bidi-isolated mixed text.

## 1. Proof report command
Add `npm run proof-report` printing rows with and without proof, counts by stage, and the list of "Applied" rows missing a proof file. Files: `scripts/proof-report.mjs`. Check: output matches `data/` reality; zero "Applied" without proof after the run; exits non-zero if any unproven "Applied" exists.

## 2. Redaction test for outside AI providers
Write a unit test that feeds a CV containing name, phone, address and email into the drafter prompt builder and asserts none of those strings appear in the prompt sent to any non-local provider. Files: `src/drafter.mjs` (if not already redacting), `test/test-redaction.mjs`. Check: test fails on an unredacted builder and passes on the redacted one; paste both outputs.

## 3. Source terms review
For every source in `scripts/digest/`, write `docs/SOURCES.md` with: source name, feed/API URL, terms URL, allowed/manual-only decision, and date checked. Switch off (config flag, not deletion) any source whose terms forbid automation. Check: every configured source has a row; disallowed ones show `enabled: false`; `npm test` green.

## 4. Arabic source: Wuzzuf official feed or manual import
Add Wuzzuf as an official-feed or manual-import-only source (no scraping if terms forbid). Files: `scripts/digest/sources/wuzzuf.mjs` (or manual importer), fixture under `test/fixtures/`. Check: offline fixture test passes; source appears disabled if terms are not confirmed; terms link recorded in `docs/SOURCES.md`.

## 5. Arabic freelance source: Mostaql manual import
Add a manual-import path for Mostaql project listings (title, budget, URL, client rating) into the openings view, since Mostaql exposes no public job API for automation. Files: `scripts/digest/sources/mostaql-import.mjs`, importer docs in `docs/OWNER_STEPS.md`. Check: importing the sample fixture creates staged applications visible in the pipeline; `npm test` green.

## 6. Outcome tracker on job detail
Add outcome (Interviewed, Offered, Rejected, Ghosted), outcome date and offer amount (USD + EGP via cached FX with rate date) to the job detail dialog, persisted through the existing pipeline notes path. Files: `src/public/js/views/detail.js` (or current detail view), `src/routes/pipeline.mjs`. Check: choosing Offered with an amount shows live EGP conversion; outcome persists after reload; empty states honest (gap 4 in `.sir/plans/FEATURE_GAPS.md`).

## 7. Weekly outcomes digest dry run
Implement `scripts/apply/weekly-report.mjs`: ISO-week breakdown from `data/apply-metrics.json` and pipeline stages (applications sent, answers, interviews, offers by source and role family), emitting the Arabic Telegram message without sending on `--dry-run`. Check: dry run prints the message with real counters (0 when empty, never estimates); second identical send the same day is blocked by the ledger (test).

## 8. Salary negotiation card on OFFERED stage
Offered stage cards show a negotiation card: offered amount, counter-offer, notes, final accepted amount, EGP conversion at cached FX with the rate date visible. Files: pipeline view + `src/routes/pipeline.mjs`. Check: entering a counter-offer updates the final amount; reload persists; totals appear in the pipeline subtitle; five states intact.

## 9. CSV/LinkedIn import rebuild
Implement `scripts/import_csv.mjs`: reads a CSV with company, role, date, status; creates applications with new ids only; skips duplicates (reports them); `--dry-run` prints what would change. Check: importing a sample CSV twice yields no duplicates on the second run; skipped duplicates are listed; `npm test` green.

## 10. No-applications nudge
If no application was staged or submitted in 7 days, show a gentle, dismissible "search again" nudge on the pipeline view with the action running the digest. Files: pipeline view + one small helper. Check: with last activity older than 7 days the nudge shows; after staging anything it disappears; 320 px safe; Arabic and English; light and dark.

All tasks: after finishing, run the gates (`npm test`, `npm run lint`, `npm run typecheck`), update the project checkpoint, commit to `main` with a clear message. Do not push to `D:\Projects\_SIR` for project-code changes; push the SIR Jobs repo. Reports go to `D:\Projects\_SIR\ops\agy-runs\reports\<task>.md`.
