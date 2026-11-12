# First 10 Tasks to Queue: SIR Business (r53, 2026-11-12)

Ready-to-queue briefs for free CLI agents (Kilo, OpenCode, Devin, ZCode) and Gemini. Each task is under 2 hours. Every task names exact files and a done-when check. Read `plans/sir-business.md` (r53) first; nothing here invents scope beyond it. Commit and push each finished task straight to `main` on `sirahmed8/sir-business` (private repo) or to `D:/Projects/_SIR` for HQ-side files, as the task says. Do not touch `legacy/` (read-only). Version stays 1.0.0.

## 1. M0 — Recreate the Desktop folder kit from scratch
**Brief:** In `D:\Projects\SIR Business` and `C:\Users\a7med\Desktop\SIR Projects\SIR Business`, recreate the §19 OWNER_DEFAULTS kit for the new build: confirm `folder.ico` exists and is the project's real icon (run `D:/Projects/_SIR/scripts/make-icons-and-desktop.ps1` if missing), create Desktop shortcuts Web (`https://sir-business.web.app`), Vercel (`https://sir-business.vercel.app`), Open project folder, and `Start dev`/`Stop dev` pointing at `D:/Projects/_SIR/scripts/` dev scripts if they exist for this product (skip what does not exist, honestly), and write `Versions.txt` with `1.0.0` + one-line plain status ("SIR Business r53: merged plan written; M0 not started"). Delete no old kit files.
**Done when:** the Desktop folder exists with every present shortcut working or deliberately skipped, `Versions.txt` exists, and a one-line note is appended to `.sir/CHECKPOINT.md` (`D:\Projects\SIR Business`).
**Check:** `ls "C:\Users\a7med\Desktop\SIR Projects\SIR Business"` prints the kit contents. Note: do not create Firebase projects, repos or stores in this task.
**Repo:** product folder + Desktop, not `_SIR` git.

## 2. M0 — Verify dual hosting skeleton and record it
**Brief:** In `D:\Projects\SIR Business`: 1) run `firebase projects:list` and confirm `sir-business` exists; if it does not, stop and write one line in `D:/Projects/_SIR/ops/OWNER_ACTIONS.md` asking the owner to run `firebase projects:create sir-business` (agents may not create paid things without the one-time owner tap), then continue with what you can. 2) In the product repo, check `vercel.json`/`.vercel` linking; if the repo is not imported, run `npx vercel link --yes --project sir-business` and import the GitHub repo with `npx vercel import`. 3) Set all `.env` keys present in `.env.example` on both hosts (`firebase apphosting:yaml:update` or Firebase console env JSON, and `npx vercel env pull`/`npx vercel env add`); never print secrets. 4) `git -C "D:\Projects\SIR Business" status` clean; push main if changed.
**Done when:** both URLs return 200 via `curl -s -o /dev/null -w "%{http_code}"` (retry once on timeout), and the two URLs are written into `.sir/CHECKPOINT.md` "Done" with the date.
**Check:** two curls print `200`; `gh repo view sirahmed8/sir-business` prints the private repo.

## 3. M1 — Scaffold the Next.js + Firebase monorepo
**Brief:** In `D:\Projects\SIR Business`, create npm workspaces: `apps/web` (Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4, ESLint, absolute imports), `packages/core` (empty typed modules: `tenancy`, `money`, `inventory`, `sales`, `sync`, `sectors`), `packages/ui` (design tokens + five-state primitives), root `package.json` with `verify` script (tsc + lint + tests). No Tailwind/Next version drift from `standard/23-premium-code-bar.md`. Do not wire real data yet.
**Done when:** `npm install` exits 0; `npm run verify` exits 0; `npm run build` exits 0 in `apps/web`.
**Check:** paste the three commands' exit codes (or real output tails) into `.sir/CHECKPOINT.md` under the task line.

## 4. M1 — Money module with integer piasters (30 tests)
**Brief:** Implement `packages/core/src/money/money.ts` (no framework): `Money { amountPiasters: number }`, add/sub/mul, `format(egp|usd)` with Arabic locale digits off (plain 1,234.56), division rounding banker's on half, discount engine (percent + cap), VAT add/extract, and guards against NaN/Infinity/float. Export types only via `index.ts`. Vitest, exactly 30 cases incl. rounding ties, overflow, currency formatting ar/en.
**Done when:** `npm test -- money` prints 30 passed.
**Check:** exit code 0; `grep -R "toFixed" packages/core/src/money` returns nothing (piasters integers only).

## 5. M1 — Firestore rules v0 + emulator cross-tenant denial suite
**Brief:** In the product repo, write `firestore.rules` v0 (deny by default; allow org-owner, business-member, branch-staff roles; no reads without membership; writes validated by role), `firebase.json` emulator config, and `packages/core/src/tenancy/tenancy.ts` defining `Organization`, `Business`, `Branch`, `Membership` types + pure `can(role, permission)` map. Write `test/rules.test.mjs` run by `firebase emulators:exec --only firestore`: asserts shop A cannot read shop B's `sales`, cashier cannot update a closed sale, non-member cannot open a business doc. Delete nothing legacy.
**Done when:** `firebase emulators:exec --only firestore "npm test -- rules"` prints all assertions passed; `firebase deploy --only firestore:rules` is NOT run (rules deploy is M3 after review).
**Check:** capture the emulator summary line into `.sir/CHECKPOINT.md`.

## 6. M1 — Sector catalogue data file with the 30 launch sectors
**Brief:** Implement `packages/core/src/sectors/sectors.ts`: typed array, exactly the 30 sectors in `plans/sir-business.md` section 4 (id, nameAr, nameEn, group, template key handoff: restaurant/market/library/pharmacy/clinic/service/retail/b2b/hospitality/education, modules[], defaultRoleTemplates[], onboardingChecklist[], riskNote with "(unsourced, verify)" markers for legal claims). Export `getSector(id)` and `SECTOR_COUNT`. Unit test asserts 30 entries, unique ids, every module name resolves against `packages/core/src/modules/index.ts` registry stub (registry lists module ids as strings with empty placeholders removed honestly — no fake implemented modules, the registry is the menu of names, not code). Keep file ≤ 300 lines by splitting data into `sectors.data.ts`.
**Done when:** `npm test -- sectors` prints passed; `SECTOR_COUNT === 30` asserted.
**Check:** no sector missing a `riskNote`; no em-dashes in the copy.

## 7. M1 — Auth + custom-claims scaffold with five-state login screen
**Brief:** Wire Firebase Auth in `apps/web`: Google sign-in + phone OTP (ar-EG defaults, +20) + email/password; login screen in `packages/ui` follows five states (idle, loading skeleton, empty, error+retry, populated-signed-in) and L8/L21 (per-character bidi, no "(RTL)" labels). Server route `apps/web/src/app/api/claims/set/route.ts` sets `company_owner`/`business_role` claims from a validated server secret (env `ADMIN_CLAIMS_TOKEN`, never in git). Staff PIN: argon2 hash util in core, 5-try lockout helper + tests. No hard-coded emails anywhere (grep test).
**Done when:** `npm run build` exits 0; login renders signed-in state via Firebase Auth emulator; `grep -ri "admin@" apps packages` returns nothing; emulator auth test passes.
**Check:** `firebase emulators:exec --only auth,firestore "npm test"` output tail in checkpoint.

## 8. M1 — Tenancy schema + seed script (org → business → branch → membership)
**Brief:** Define `packages/core/src/tenancy/schema.ts` for org/business/branch/membership with Zod validation at boundaries (no `any`), Firestore path helpers (`orgPath`, `businessPath`, `memberPath`), and `scripts/seed-emulator.mjs`: creates demo org "Studio Demo" with 2 businesses (restaurant + pharmacy), 1 branch each, owner + 2 staff each, deterministic data, for emulator only (label `EMULATOR_ONLY`). Run against emulator, export verification prints counts. Nothing seeded to prod ever (guard: `PROJECT_ID` must end with `-demo-sir-business`).
**Done when:** seed script prints the created doc counts; schema tsc clean.
**Check:** tenancy test asserts the cross-link between org and businesses resolves; no seed runs against `sir-business` prod (assert in script).

## 9. M1 — Offline-sync ADR refresh against POS code reality
**Brief:** Rewrite/refresh `docs/adr/001-offline-sync.md` in the product repo to the r53 architecture: IndexedDB catalog cache + cart queue, Firestore pending-write semantics, server-order timestamp conflict rule for quantity fields, no-merge for money rows, idempotency keys (`sale:{uuid}`) for safe retries, receipt reprint from queued sale, visible sync chip states (synced/syncing/offline N pending), and the exact conflict case table (two devices sell last unit of stock offline: server arbitrated by write timestamp + stock reconciled to negative with an audit flag, never silent oversell). Reference the POS flows from task 3 and the rules from task 5. Do not implement; ADR + test plan only.
**Done when:** ADR names the conflict rule, the idempotency scheme, and the negative-stock policy; reviewer can implement without guessing.
**Check:** file exists; sections: Context, Decision, Conflict table, Failure modes, Test plan.

## 10. M2 — Legacy parity report with per-file verification
**Brief:** Regenerate `.sir/reports/parity.md` (product repo) covering all four legacy apps (`legacy/SIR Restaurant|Market|Library|Pharmacy`): table columns `Legacy path | Feature | Core/template destination | Verdict (port/rebuild/drop/defer) | Evidence (grep line)`. Verify every module listed in the r53 maps of `plans/sir-business.md` sections 6.1-6.4 exists at the cited path (git grep); correct anything stale; keep under ~500 lines; cite the inventory docs (`D:/Projects/_SIR/ops/inventory/SIR-*.md`) as sources. This is the sanity check that the r53 maps match the real tree before any porting starts.
**Done when:** report exists; every "port" row has a verified path; every mismatch is listed under "Corrections".
**Check:** `grep -c "legacy/" .sir/reports/parity.md` ≥ 80 rows; zero rows claim a path that does not exist.
