# First 10 Tasks to Hand to Free Agents: SIR Business (sir-business-tasks.md)

Tasks ready to queue for free CLI agents. Each task includes a title and one-paragraph brief. All tasks are designed to be completed in under 2 hours.

---

## 1. Deep scan of four legacy apps
Scan the four legacy applications (SIR Market, SIR Restaurant, SIR Pharmacy, SIR Library) to produce a shared module list and per-mode differences. Output: `.sir/reports/parity.md` with a table of each module and which legacy apps contain it, plus keep/drop recommendations. Check: table with module name, apps containing it, and keep/drop decision for each.

## 2. Data layer ADR decision
Decide and record the data layer architecture in `docs/adr/001-data-sync.md`. The ADR must name the conflict resolution rule (last write wins per field, or server order) for offline-to-online sync. Check: ADR file exists and names the conflict resolution rule.

## 3. Scaffold monorepo
Scaffold the monorepo structure: `apps/desktop`, `apps/portal`, `packages/core`. Ensure `npm run build` exits 0 in all three directories. Check: all three directories have valid package.json and build exits 0.

## 4. Money module with integer piasters
Implement the money module with integer piasters and tests for rounding, discounts, and tax. Files: `packages/core/src/money/`. Check: 30 unit tests green and run via `npm test -- packages/core/src/money/`.

## 5. SQLite schema and migrations
Implement SQLite schema and migrations for Product, Batch, and Sale. Check: migration test creates the database file, reopens it, and verifies no in-memory fallback exists in the source code (grep test).

## 6. POS screen: add item, pay cash, save sale, five states
Build the POS screen with add-item flow, cash payment, save sale, and the five states (idle, loading skeleton, empty with one action, error with retry, populated). Check: screenshot captured at 1366x768 and an e2e test passes.

## 7. Receipt builder (ESC/POS bytes) with golden-file tests
Implement the ESC/POS thermal receipt binary generator with golden-file tests. Check: golden bytes equal the reference file; test passes across light/dark.

## 8. PIN lock with hashed storage and lockout
Implement PIN lock with hashed storage (argon2 or scrypt) and lockout after 5 wrong tries, with no hard-coded PIN anywhere. Check: test of 5 wrong tries locks the account; grep finds no PIN literal in the codebase.

## 9. Tenant rules for cloud sync with emulator tests
Implement tenant rules for cloud sync with emulator tests. Check: cross-shop read fails (user from shop A cannot read shop B or another branch without a claim).

## 10. Shop owner interview script
Write the interview script for 5 shop owners (price, pain points) in `docs/research/interview.md`. To be run by the owner or a volunteer. Results later go to `plans/competitors/sir-business.md` with dates. Check: file exists with interview questions.