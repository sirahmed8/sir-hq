# First 10 Tasks to Hand to Free Agents: SIR Controller (sir-controller-tasks.md)

Tasks ready to queue for the free CLI agents (Kilo, OpenCode, Devin CLI, ZCode). Each has a title and a one-paragraph brief. All are scoped to under 2 hours. Work in `D:\Projects\SIR Controller` (app code) and write reports/evidence only inside that project or `D:\Projects\_SIR\ops\`. Never open `D:\Projects\AHome`. Never put secrets in git. Version stays 1.0.0. No placeholders, no invented data, every screen keeps five states, Arabic RTL and English, 44 px targets, bidi-isolated mixed text.

## 1. Inventory vendored components and binaries with licence column
Files: `docs/THIRD_PARTY.csv`, legacy engine folder inventory. Check: every vendored folder has a row with licence column; exit non-zero if any component missing licence. Done when: the file lists each component with licence; `npm test` green.

## 2. Write LICENSE_DECISION.md: what may be sold, what stays free
Files: `docs/LICENSE_DECISION.md`. Check: file cites each licence file path; exit non-zero if any licenced component unclear. Done when: every vendored folder has a row; `npm test` green.

## 3. Remove binaries from new repo layout, add size check script
Files: new repo layout, `scripts/check-size.mjs`. Check: fails on a 6 MB test file; CI passes. Done when: size check script fails on 6 MB test file; CI passes.

## 4. UI spike ADR (WinUI 3 vs Tauri), 2 hours, measured size and start time
Files: `docs/adr/001-ui.md`. Check: ADR has numbers present for both options; measured size and start time recorded. Done when: ADR file exists with numbers; `npm test` green.

## 5. Optimizer read-only scan v0 (startup items, disk free, power plan) as JSON
Files: `apps/optimizer/engine/scan.ps1` or `.cs`. Check: output validated by a JSON schema test; exit non-zero if schema mismatch. Done when: JSON output passes schema validation; `npm test` green.

## 6. Plain-words explanation for mapper findings (rules, no AI)
Files: unit tests for 10 findings in Arabic and English, explanation logic. Check: unit tests pass for 10 findings both languages; explanation never changes anything itself. Done when: all 10 unit tests pass Arabic and English; `npm test` green.

## 7. Portal scaffold with server-side owner check
Files: Next.js portal with landing, downloads, pricing, and `/owner` route. Check: client flag flip test returns 403; owner route shows metrics only with verified owner token. Done when: `--dry-run` prints the message with real counters (0 when empty, never estimates); second identical send the same day is blocked by the ledger (test).

## 8. Signed webhook package with 10 negative tests
Files: signed-webhook implementation, test wrapper. Check: 10 negative tests (tampered, replayed, unsigned, wrong timestamp, etc.) all pass. Done when: all 10 tests pass; `npm test` green.

## 9. Honest-claims lint for site and README
Files: lint rule that fails on "boost", "100%" without a linked benchmark. Check: fails on "boost" or "100%" without a linked benchmark; passes on claims with linked benchmark. Done when: lint rule is active and enforced in CI; `npm test` green.

## 10. No-claims nudge for README: gentle dismissible notice if unsupported claim detected
Files: README markdown update, one small helper component. Check: with unsupported claim the nudge shows; after fixing claim it disappears; 320 px safe; Arabic and English; light and dark. Done when: nudge appears/ disappears as expected; `npm test` green.

All tasks: after finishing, run the gates (`npm test`, `npm run lint`, `npm run typecheck`), update the project checkpoint, commit to `main` with a clear message. Do not push to `D:\Projects\_SIR` for project-code changes; push the SIR Controller repo. Reports go to `D:\Projects\_SIR\ops\agy-runs\reports\<task>.md`.