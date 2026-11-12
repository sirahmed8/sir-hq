# SIR Business task queue (r61, 2026-11-12)

Planning-only until SIR Business is the active build project. Read `plans/sir-business.md`, `plans/business-sectors/_INDEX.md`, `plans/business-sectors/_ENGINE.md`, `ops/competitors/sir-business.md` and the matching `plans/business-sectors/<slug>.md` + `ops/briefs/business-<slug>-tasks.md` before starting any task. Commit and push each finished task straight to `main` on `sirahmed8/sir-business` for product files, or to `D:/Projects/_SIR` for HQ files, as the task says. Do not touch `legacy/` (read-only). Version stays 1.0.0. No fake data, no fake AI, no compliance claims without the accountant/pharmacist gates in the plan.

Wave A tasks 1-10 are ready to queue now. Tasks 11-48 are smaller follow-on briefs gated by the milestone named in the brief; queue them only when their dependency is merged.

## Wave A: ready now

### 1. M0 - Recreate the Desktop folder kit from scratch
**Brief:** In `D:\Projects\SIR Business` and `C:\Users\a7med\Desktop\SIR Projects\SIR Business`, recreate the OWNER_DEFAULTS kit for the new build: confirm `folder.ico` exists and is the project's real icon (run `D:/Projects/_SIR/scripts/make-icons-and-desktop.ps1` if missing), create Desktop shortcuts for Web (`https://sir-business.web.app`), Vercel (`https://sir-business.vercel.app`), Open project folder, and `Start dev`/`Stop dev` only if the product dev scripts exist (skip what does not exist, honestly), and write `Versions.txt` with `1.0.0` plus one plain status line ("SIR Business r61: planning refreshed; M0 not started"). Delete no old kit files.
**Files:** `D:\Projects\SIR Business\folder.ico`, `C:\Users\a7med\Desktop\SIR Projects\SIR Business\*`, `D:\Projects\SIR Business\.sir\CHECKPOINT.md`
**Done when:** the Desktop folder exists with every present shortcut working or deliberately skipped, `Versions.txt` exists, and a one-line note is appended to the product `.sir/CHECKPOINT.md`.
**Check:** `ls "C:\Users\a7med\Desktop\SIR Projects\SIR Business"` prints the kit contents; no Firebase project, repo or store is created.
**Skills:** agent-supercharged-os, bootstrap, laptop-admin

### 2. M0 - Verify dual hosting skeleton and record it
**Brief:** In `D:\Projects\SIR Business`: confirm `firebase projects:list` shows `sir-business`; if it does not, stop and write one exact action to `D:/Projects/_SIR/ops/OWNER_ACTIONS.md` asking the owner to run `firebase projects:create sir-business`, then continue with what is possible. Verify `vercel.json`/`.vercel` linking or run `npx vercel link --yes --project sir-business` and `npx vercel import` if needed. Set only the env keys present in `.env.example` on both hosts via the documented Firebase/Vercel env commands; never print secrets. Leave git clean and push `main` if changed.
**Files:** `D:\Projects\SIR Business\firebase.json`, `D:\Projects\SIR Business\.firebaserc`, `D:\Projects\SIR Business\vercel.json`, `D:\Projects\SIR Business\.env.example`, `D:\Projects\SIR Business\.sir\CHECKPOINT.md`
**Done when:** `https://sir-business.web.app` and `https://sir-business.vercel.app` both return 200 via curl (retry once on timeout), and both URLs plus the Firestore region are written into `.sir/CHECKPOINT.md`.
**Check:** two curls print `200`; `gh repo view sirahmed8/sir-business` prints the private repo; no secret appears in output.
**Skills:** firebase_basics, firebase_app_hosting_basics, firebase_hosting_basics, env-vars, deployments-cicd, verification

### 3. M1 - Scaffold the Next.js + Firebase monorepo
**Brief:** In `D:\Projects\SIR Business`, create npm workspaces: `apps/web` (Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4, ESLint, absolute imports), `packages/core` (typed module stubs for tenancy, money, inventory, sales, sync, sectors), `packages/ui` (design tokens and five-state primitives), and root `package.json` scripts `verify`, `build`, `test`, `test:rules`, `test:sectors`. No Tailwind/Next drift from `standard/23-premium-code-bar.md`. Do not wire real data yet.
**Files:** `D:\Projects\SIR Business\package.json`, `D:\Projects\SIR Business\apps\web\*`, `D:\Projects\SIR Business\packages\core\src\*`, `D:\Projects\SIR Business\packages\ui\src\*`, `D:\Projects\SIR Business\turbo.json` if used
**Done when:** `npm install` exits 0; `npm run verify` exits 0; `npm run build` exits 0 in `apps/web`.
**Check:** paste the exit codes or output tails into `.sir/CHECKPOINT.md` under the task line.
**Skills:** next-forge, bootstrap, agent-supercharged-os, verification

### 4. M1 - Money module with integer piasters
**Brief:** Implement `packages/core/src/money/money.ts` with no framework dependencies: `Money { amountPiasters: number }`, add/sub/mul, `format('egp'|'usd')` with plain digits, banker's rounding on half, discount engine (percent + cap), VAT add/extract, and guards against NaN/Infinity/float. Export only through `index.ts`. Vitest with exactly 30 cases including rounding ties, overflow, and ar/en formatting.
**Files:** `D:\Projects\SIR Business\packages\core\src\money\money.ts`, `D:\Projects\SIR Business\packages\core\src\money\money.test.ts`, `D:\Projects\SIR Business\packages\core\src\money\index.ts`
**Done when:** `npm test -- money` prints 30 passed.
**Check:** exit code 0; `grep -R "toFixed" packages/core/src/money` returns nothing because piasters stay integers until formatting.
**Skills:** database-reliability-transactions, financial-analysis, karpathy-skills, agent-supercharged-os

### 5. M1 - Firestore rules v0 + emulator cross-tenant denial suite
**Brief:** Write `firestore.rules` v0 (deny by default; allow org-owner, business-member and branch-staff roles; no reads without membership; writes validated by role), `firebase.json` emulator config, `packages/core/src/tenancy/tenancy.ts` with `Organization`, `Business`, `Branch`, `Membership` types and pure `can(role, permission)`, and `test/rules.test.mjs` run by `firebase emulators:exec --only firestore`. Assertions: shop A cannot read shop B `sales`; cashier cannot update a closed sale; non-member cannot open a business doc. Do not deploy rules yet.
**Files:** `D:\Projects\SIR Business\firestore.rules`, `D:\Projects\SIR Business\firebase.json`, `D:\Projects\SIR Business\packages\core\src\tenancy\tenancy.ts`, `D:\Projects\SIR Business\test\rules.test.mjs`
**Done when:** `firebase emulators:exec --only firestore "npm test -- rules"` prints all assertions passed; `firebase deploy --only firestore:rules` is not run.
**Check:** emulator summary line is copied into `.sir/CHECKPOINT.md`.
**Skills:** firestore_rules_creation, firebase_security_rules_auditor, firebase_firestore, database-reliability-transactions

### 6. M1 - Sector catalogue data file with the 41 sector packs
**Brief:** Implement `packages/core/src/sectors/sectors.ts` and `sectors.data.ts` as the runtime mirror of `plans/business-sectors/_INDEX.md`: exactly the 41 slugs, Arabic/English names, group, pack key, modules, role templates, onboarding checklist, landing status and risk note. Every legal/compliance string keeps "(unsourced, verify)" until the accountant/pharmacist gates pass. Export `getSector(slug)` and `SECTOR_COUNT`. Unit test asserts 41 unique slugs and every slug matches a file in `plans/business-sectors/_INDEX.md`.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\sectors.ts`, `D:\Projects\SIR Business\packages\core\src\sectors\sectors.data.ts`, `D:\Projects\SIR Business\packages\core\src\sectors\sectors.test.ts`, `D:\Projects\_SIR\plans\business-sectors\_INDEX.md`
**Done when:** `npm test -- sectors` passes; `SECTOR_COUNT === 41`; slug list equals the `_INDEX.md` table.
**Check:** no sector missing a `riskNote`; no em-dashes; no pack marked "ready" before its smoke suite exists.
**Skills:** firebase_firestore, database-reliability-transactions, api-documentation, karpathy-skills

### 7. M1 - Auth + custom-claims scaffold with five-state login
**Brief:** Wire Firebase Auth in `apps/web`: Google sign-in, phone OTP (ar-EG default, +20) and email/password. Login screen follows five states and L8/L21 bidi rules. Add `apps/web/src/app/api/claims/set/route.ts` that sets `company_owner`/`business_role` claims only after validating `ADMIN_CLAIMS_TOKEN` from env. Staff PIN uses argon2 hash util in core with 5-try lockout helper and tests. No hard-coded admin emails anywhere.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\login\*`, `D:\Projects\SIR Business\apps\web\src\app\api\claims\set\route.ts`, `D:\Projects\SIR Business\packages\core\src\auth\*`, `D:\Projects\SIR Business\packages\ui\src\states\*`
**Done when:** `npm run build` exits 0; login renders signed-in state via Firebase Auth emulator; `grep -ri "admin@" apps packages` returns nothing; emulator auth test passes.
**Check:** `firebase emulators:exec --only auth,firestore "npm test"` output tail is recorded.
**Skills:** firebase_auth_basics, auth, firestore_rules_creation, modern-ui-ux-design-system, anti-vibecoded-design-system, a11y-debugging

### 8. M1 - Tenancy schema + emulator seed
**Brief:** Define `packages/core/src/tenancy/schema.ts` with Zod validation at boundaries, Firestore path helpers (`orgPath`, `businessPath`, `memberPath`) and `scripts/seed-emulator.mjs` that creates demo org "Studio Demo" with two businesses (restaurant + pharmacy), one branch each, owner plus two staff each, deterministic data, emulator-only label `EMULATOR_ONLY`. Guard the script so it refuses to run unless `PROJECT_ID` ends with `-demo-sir-business`.
**Files:** `D:\Projects\SIR Business\packages\core\src\tenancy\schema.ts`, `D:\Projects\SIR Business\scripts\seed-emulator.mjs`, `D:\Projects\SIR Business\test\tenancy.test.ts`
**Done when:** seed script prints created doc counts; schema typechecks; tenancy test asserts org-business cross-links resolve.
**Check:** no seed runs against `sir-business` prod; script asserts the emulator project id.
**Skills:** firebase_firestore, database-reliability-transactions, agent-supercharged-os, karpathy-skills

### 9. M1 - Offline-sync ADR refresh against POS reality
**Brief:** Refresh `docs/adr/001-offline-sync.md` to the r61 architecture: IndexedDB catalog cache plus cart queue, Firestore pending-write semantics, server-order timestamp conflict rule for quantity fields, no-merge for money rows, idempotency keys (`sale:{uuid}`), receipt reprint from queued sale, visible sync chip states (synced/syncing/offline N pending), and the exact conflict table for two devices selling the last unit offline. Reference task 3 scaffold and task 5 rules. ADR plus test plan only; no implementation.
**Files:** `D:\Projects\SIR Business\docs\adr\001-offline-sync.md`, `D:\Projects\SIR Business\docs\adr\001-offline-sync.test-plan.md`
**Done when:** ADR names conflict rule, idempotency scheme and negative-stock policy; reviewer can implement without guessing.
**Check:** file has Context, Decision, Conflict table, Failure modes, Test plan; no silent oversell.
**Skills:** database-reliability-transactions, firebase_firestore, api-documentation, karpathy-skills

### 10. M2 gate - Legacy parity report with per-file verification
**Brief:** Regenerate `.sir/reports/parity.md` in the product repo covering `legacy/SIR Restaurant`, `legacy/SIR Market`, `legacy/SIR Library` and `legacy/SIR Pharmacy`: columns `Legacy path | Feature | Core/template destination | Verdict (port/rebuild/drop/defer) | Evidence`. Verify every module cited in `plans/sir-business.md` sections 6.1-6.4 exists at the cited path with git grep; correct stale rows; keep under ~500 lines; cite `D:/Projects/_SIR/ops/inventory/SIR-*.md` as sources.
**Files:** `D:\Projects\SIR Business\.sir\reports\parity.md`, `D:\Projects\_SIR\plans\sir-business.md`, `D:\Projects\_SIR\ops\inventory\SIR-*.md`
**Done when:** report exists; every "port" row has a verified path; every mismatch is listed under Corrections.
**Check:** `grep -c "legacy/" .sir/reports/parity.md` is at least 80; zero rows claim a path that does not exist.
**Skills:** agent-supercharged-os, api-documentation, verification, binary-reverse-engineer

## Wave B: engine API and platform depth (gated by M1/M2)

### 11. `/api/v1` route skeleton with auth guard and audit event
**Brief:** Create `apps/web/src/app/api/v1/` route helpers: `requireAuth()` reads Firebase ID token, `requireMembership(businessId, permission)` checks server-side role, `audit(event)` writes to `auditLogs`, and `apiError()` returns consistent JSON. Add one smoke route `/api/v1/health` that returns `{ ok: true, service: 'sir-business' }` without tenant data.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\_lib\*`, `D:\Projects\SIR Business\apps\web\src\app\api\v1\health\route.ts`, `D:\Projects\SIR Business\apps\web\src\app\api\v1\health\route.test.ts`
**Done when:** `npm test -- api-health` passes; unauthenticated `/api/v1/health` still returns ok but `/api/v1/businesses` without token returns 401.
**Check:** route test asserts 401 for missing token and 200 for health; no tenant data in health response.
**Skills:** api-engineer, api-testing, firebase_auth_basics, firestore_rules_creation

### 12. Sale commit endpoint with idempotency and piasters
**Brief:** Implement `POST /api/v1/businesses/:id/pos/sales`: validate membership and `pos.sell`, require `Idempotency-Key`, recompute totals server-side in integer piasters, write sale + lines + payment in one Firestore transaction, return canonical sale doc. Reject closed-shift sales, negative totals and unknown payment methods.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\businesses\[id]\pos\sales\route.ts`, `D:\Projects\SIR Business\packages\core\src\sales\commitSale.ts`, `D:\Projects\SIR Business\packages\core\src\sales\commitSale.test.ts`
**Done when:** replaying the same idempotency key returns the same sale and does not double-write; totals match money module tests.
**Check:** integration test asserts duplicate key -> same saleId; cross-tenant token -> 403; cashier role -> allowed; closed shift -> 409.
**Skills:** database-reliability-transactions, api-engineer, api-testing, financial-analysis, firebase_firestore

### 13. Receipt payload endpoint with honest ETA/ZATCA status
**Brief:** Implement `GET/POST /api/v1/businesses/:id/pos/receipts/:saleId`: return receipt payload (lines, totals, taxes, business tax fields) and queue ETA e-receipt or ZATCA invoice only when `taxEnrollment.status === 'enrolled'` and signer onboarding is complete. Otherwise return `status: 'not_enrolled'` with copy that never says compliant.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\businesses\[id]\pos\receipts\[saleId]\route.ts`, `D:\Projects\SIR Business\packages\core\src\receipts\receiptPayload.ts`, `D:\Projects\SIR Business\packages\core\src\receipts\receiptPayload.test.ts`
**Done when:** receipt payload matches sale totals; un-enrolled business returns honest status; no ETA claim in copy.
**Check:** test asserts `not_enrolled` path and golden receipt bytes for one cash sale.
**Skills:** api-engineer, api-documentation, api-testing, firebase_firestore

### 14. Inventory batches and FEFO endpoint
**Brief:** Implement `/api/v1/businesses/:id/inventory/:productId/batches` GET/POST/PATCH for batch qty, expiry, supplier and branch. FEFO pick is computed server-side for sale lines that require batch; pharmacy/food packs require reason codes for adjustments. Controlled-drug batches are append-only.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\businesses\[id]\inventory\[productId]\batches\route.ts`, `D:\Projects\SIR Business\packages\core\src\inventory\fefo.ts`, `D:\Projects\SIR Business\packages\core\src\inventory\fefo.test.ts`
**Done when:** FEFO chooses earliest expiry with stock; expired batch cannot be sold; adjustment without reason fails for pharmacy pack.
**Check:** unit tests cover FEFO order, expiry block and reason-code enforcement.
**Skills:** firebase_firestore, database-reliability-transactions, api-engineer, api-testing

### 15. Purchasing orders endpoint
**Brief:** Implement `/api/v1/businesses/:id/purchasing/orders` GET/POST/PATCH for PO lifecycle draft -> sent -> partial -> received -> closed, goods receipt discrepancies and supplier invoice link placeholder. Server validates `inventory.manage` or `purchasing.manage` by role.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\businesses\[id]\purchasing\orders\route.ts`, `D:\Projects\SIR Business\packages\core\src\purchasing\purchaseOrder.ts`, `D:\Projects\SIR Business\packages\core\src\purchasing\purchaseOrder.test.ts`
**Done when:** receiving more than ordered creates discrepancy record, not silent stock increase; status transitions are enforced.
**Check:** tests cover draft->sent->received and over-receipt discrepancy.
**Skills:** api-engineer, database-reliability-transactions, financial-analysis, api-testing

### 16. Customers, consent flags and credit ledger endpoints
**Brief:** Implement `/api/v1/businesses/:id/customers` GET/POST/PATCH with consent flags (marketing, WhatsApp), credit/receivables ledger for B2B packs, and privacy hooks that mark customer docs exportable/deletable. No customer PII in analytics or AI prompts.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\businesses\[id]\customers\route.ts`, `D:\Projects\SIR Business\packages\core\src\customers\customer.ts`, `D:\Projects\SIR Business\packages\core\src\customers\customer.test.ts`
**Done when:** customer create/update validates phone format and consent; credit ledger balances in piasters; delete request marks soft-delete.
**Check:** tests assert consent flags persist, ledger sums correctly and PII fields are excluded from analytics payloads.
**Skills:** api-engineer, firebase_security_rules_auditor, database-reliability-transactions, api-testing

### 17. Reports snapshot endpoints with role gating
**Brief:** Implement `/api/v1/businesses/:id/reports/:slug` for sales-by-hour/day/item/method/cashier, inventory valuation, low stock, expiry, loyalty cohort, cash reconciliation and owner today-vs-yesterday. Cashier role gets only shift-safe reports; finance reports require owner/manager.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\businesses\[id]\reports\[slug]\route.ts`, `D:\Projects\SIR Business\packages\core\src\reports\registry.ts`, `D:\Projects\SIR Business\packages\core\src\reports\registry.test.ts`
**Done when:** each report slug returns deterministic aggregates from seeded emulator data; unauthorized role returns 403.
**Check:** test matrix covers owner, manager, cashier, staff and cross-tenant denial.
**Skills:** api-engineer, api-testing, financial-analysis, firestore_rules_creation, firebase_security_rules_auditor

### 18. Billing checkout, webhook and portal endpoints
**Brief:** Implement `/api/v1/billing/checkout`, `/api/v1/billing/webhook/:provider` and `/api/v1/billing/portal` for Paymob and Fawry test mode. Checkout creates a hosted payment URL or tokenized intent; webhook verifies HMAC, rejects replays and applies idempotent plan transitions; portal returns provider cancel/update link. If keys are absent, endpoints return `billing_not_configured` and UI shows "Subscriptions launching soon" style disabled state.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\billing\checkout\route.ts`, `D:\Projects\SIR Business\apps\web\src\app\api\v1\billing\webhook\[provider]\route.ts`, `D:\Projects\SIR Business\apps\web\src\app\api\v1\billing\portal\route.ts`, `D:\Projects\SIR Business\packages\core\src\billing\*`
**Done when:** signed webhook upgrades/downgrades plan exactly once; bad signature returns 401; missing keys return honest disabled state.
**Check:** tests cover valid webhook, replay, bad signature, downgrade and missing-config path.
**Skills:** api-engineer, api-testing, env-vars, deployments-cicd, financial-analysis, database-reliability-transactions

### 19. AI "Ask your business" with whitelisted queries and eval gate
**Brief:** Implement `POST /api/v1/ai/ask`: map natural language to a whitelisted read-only query set (sales by item/hour/method/cashier, expiry next 7 days, low stock, best-selling week), never expose patient/secret rows, meter per plan, and phrase answers through the LLM only after numbers are computed. Add `eval/ai-ask.jsonl` with 50 pinned questions and a script that fails if any numeric answer mismatches.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\ai\ask\route.ts`, `D:\Projects\SIR Business\packages\core\src\ai\queryMap.ts`, `D:\Projects\SIR Business\packages\core\src\ai\ask.test.ts`, `D:\Projects\SIR Business\eval\ai-ask.jsonl`, `D:\Projects\SIR Business\scripts\eval-ai-ask.mjs`
**Done when:** eval script prints 50/50; pharmacy zero-stock question returns "0"; no AI key in client bundle.
**Check:** `grep -R "GEMINI\|OPENAI\|API_KEY" apps/web/src packages/ui/src` returns no client-side key usage.
**Skills:** ai-sdk, ai-gateway, gemini-api-dev, firebase_ai_logic_basics, api-testing, omniroute-resilience-gateway

### 20. Grounded support assistant
**Brief:** Implement `POST /api/v1/ai/support` that answers only from `docs/help/*.md` and changelog files, cites the source page, refuses to invent policy, and enforces free-tier daily cap. Arabic Egyptian dialect first, English mirrored. Add citation check so every answer includes at least one docs path.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\ai\support\route.ts`, `D:\Projects\SIR Business\packages\core\src\ai\support.ts`, `D:\Projects\SIR Business\packages\core\src\ai\support.test.ts`, `D:\Projects\SIR Business\docs\help\*.md`
**Done when:** support test asserts citation present; quota test blocks after cap; unsupported question returns docs link not invention.
**Check:** tests cover Arabic query, English query, quota exhaustion and citation requirement.
**Skills:** ai-sdk, ai-gateway, api-documentation, chat-sdk, api-testing

### 21. Telegram bot webhook, link flow and digest
**Brief:** Implement `POST /api/v1/telegram/webhook` with secret verification, `/start <code>` one-time account link, per-business opt-in digest command, and alert commands for low stock/expiry/Z-report. Map chat to membership server-side; never store bot token in client.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\telegram\webhook\route.ts`, `D:\Projects\SIR Business\packages\core\src\telegram\bot.ts`, `D:\Projects\SIR Business\packages\core\src\telegram\bot.test.ts`
**Done when:** emulator test links a chat to a membership, sends digest payload shape, and rejects bad secret.
**Check:** test asserts unknown chat gets link instructions; digest excludes PII beyond business name and totals.
**Skills:** chat-sdk, api-engineer, api-testing, firebase_firestore

### 22. Owner analytics endpoint claim-gated and audited
**Brief:** Implement `GET /api/v1/owner/metrics` requiring `company_owner` custom claim verified server-side. Return aggregate fleet, funnel, money, health, churn and product metrics only; no tenant PII. Every view writes an audit event and supports a break-glass counter visible to the owner.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\owner\metrics\route.ts`, `D:\Projects\SIR Business\packages\core\src\owner\metrics.ts`, `D:\Projects\SIR Business\packages\core\src\owner\metrics.test.ts`
**Done when:** non-owner gets 403; owner gets aggregate JSON; audit log records view.
**Check:** tests assert claim gate, aggregate-only fields and audit write.
**Skills:** api-engineer, firebase_security_rules_auditor, api-testing, financial-analysis, firestore_rules_creation

### 23. Devices register, token rotate and revoke
**Brief:** Implement `/api/v1/devices` GET/POST/PATCH for POS/kiosk/device registration, hashed token storage, last-seen update and revoke. Kiosk lock state is server-authoritative; device cannot self-escalate role.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\devices\route.ts`, `D:\Projects\SIR Business\packages\core\src\devices\devices.ts`, `D:\Projects\SIR Business\packages\core\src\devices\devices.test.ts`
**Done when:** device token is stored hashed; revoke blocks next auth; kiosk lock cannot be changed by device role.
**Check:** tests cover register, rotate, revoke and role-escalation denial.
**Skills:** api-engineer, firebase_security_rules_auditor, api-testing, database-reliability-transactions

### 24. Privacy export and deletion jobs
**Brief:** Implement `/api/v1/privacy/export` POST/GET and `/api/v1/privacy/delete` POST. Export creates a zip job (JSON + CSV per entity) written to Storage with expiring signed URL, available in grace period. Delete schedules soft-delete -> 30-day restore -> purge with documented retention; health data follows license-configurable retention.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\api\v1\privacy\export\route.ts`, `D:\Projects\SIR Business\apps\web\src\app\api\v1\privacy\delete\route.ts`, `D:\Projects\SIR Business\packages\core\src\privacy\export.ts`, `D:\Projects\SIR Business\packages\core\src\privacy\delete.ts`
**Done when:** export job produces downloadable zip for emulator tenant; delete marks soft-delete and schedules purge; no purge before restore window.
**Check:** tests cover export contents, signed URL expiry, soft-delete and purge schedule.
**Skills:** api-engineer, firebase_security_rules_auditor, accidental-data-loss-prevention, database-reliability-transactions, api-testing

## Wave C: wave-1 sector packs (gated by sector registry from task 6)

### 25. Sector pack registry and feature flags
**Brief:** Implement `packages/core/src/sectors/registry.ts` that loads the 41 pack manifests, validates required sections (data model, screens, workflows, reports, onboarding, landing, pricing notes, competitors, tasks, risks), and exposes `registerPack`, `getPack`, `isEnabled(business)`. Feature flags live in `businesses/{id}/featureFlags` and are server-checked.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\registry.ts`, `D:\Projects\SIR Business\packages\core\src\sectors\registry.test.ts`, `D:\Projects\SIR Business\packages\core\src\sectors\packs\*.ts`
**Done when:** registry validates all 41 manifests; unknown pack returns honest `not_available`; flag off hides pack screens.
**Check:** test asserts 41 manifests, required keys and flag gating.
**Skills:** firebase_firestore, database-reliability-transactions, api-documentation, karpathy-skills

### 26. Supermarket pack
**Brief:** Build `supermarket` pack on market base: FEFO inventory, barcode POS, weigh-and-label, loyalty at scale, procurement reorder points, reports for shrink/expiry/fast movers. Files include pack manifest, seed catalog, POS screen variant, inventory screens, reports, onboarding answers, landing page `/sectors/supermarket` and `/ar/sectors/supermarket`.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\supermarket.ts`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\supermarket\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\supermarket\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\supermarket\page.tsx`
**Done when:** pack registers; seed applies; smoke test sells one weighed item offline and Z-report shows it; landing page renders bilingual honest status.
**Check:** `pnpm test:sectors -- supermarket` green; screenshot at 390px ar+en light+dark shows five states.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, anti-vibecoded-design-system, a11y-debugging, firebase_firestore

### 27. Grocery shop pack
**Brief:** Build `grocery-shop` pack: neighbourhood credit book, small basket POS, short credit cycle, supplier price lists, basic reports. Same file pattern as supermarket but different terminology, seed and workflows.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\grocery-shop.ts`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\grocery-shop\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\grocery-shop\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\grocery-shop\page.tsx`
**Done when:** credit sale records customer balance; pack smoke test passes; landing page states credit-book workflow honestly.
**Check:** `pnpm test:sectors -- grocery-shop` green; no supermarket-only features leak into copy.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, a11y-debugging, firebase_firestore

### 28. Restaurant pack
**Brief:** Build `restaurant` pack: table service floor plan, KDS fire, waiter ordering, kiosk, QR menu, delivery zones, recipe cost engine, portions/FEFO, Z-report. Reuse core POS and inventory; add restaurant-specific screens and seeds.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\restaurant.ts`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\restaurant\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\restaurant\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\restaurant\page.tsx`
**Done when:** table -> order -> KDS -> pay flow works on emulator; recipe cost report computes; landing page lists real workflows only.
**Check:** `pnpm test:sectors -- restaurant` green; KDS fire event test passes.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, anti-vibecoded-design-system, a11y-debugging, database-reliability-transactions

### 29. Cafe pack
**Brief:** Build `cafe` pack on restaurant base minus full-service floor plan: quick-service POS, modifiers, tabs, day parts, loyalty. Different seed, terminology and landing page.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\cafe.ts`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\cafe\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\cafe\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\cafe\page.tsx`
**Done when:** modifier-heavy sale computes correctly; tab open/close works; landing page does not claim table-service features.
**Check:** `pnpm test:sectors -- cafe` green; modifier pricing tests pass.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, a11y-debugging, database-reliability-transactions

### 30. Pharmacy pack
**Brief:** Build `pharmacy` pack: FEFO expiry radar, patient profiles encrypted, controlled-drug append-only log, DDI warnings labeled "(unsourced, verify)" until licensed data, prescription print, supplier price lists. Patient fields are excluded from analytics and AI.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\pharmacy.ts`, `D:\Projects\SIR Business\packages\core\src\pharmacy\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\pharmacy\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\pharmacy\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\pharmacy\page.tsx`
**Done when:** controlled log rejects edit; patient decrypt round-trip test passes; DDI alert shows disclaimer; zero-stock AI answer returns "0".
**Check:** `pnpm test:sectors -- pharmacy` green; security rules test denies cashier patient-history access.
**Skills:** firebase_security_rules_auditor, firestore_rules_creation, database-reliability-transactions, modern-web-guidance, taste-design-engine, ai-sdk

### 31. Bakery pack
**Brief:** Build `bakery` pack: weight-priced POS (kg), production batches, day-old discount rules, allergen labeling notes, hot/cold catalog. Uses restaurant + retail machinery.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\bakery.ts`, `D:\Projects\SIR Business\packages\core\src\bakery\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\bakery\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\bakery\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\bakery\page.tsx`
**Done when:** kg price computes per weight; production batch decrements stock; landing page mentions food-safety honestly.
**Check:** `pnpm test:sectors -- bakery` green; weight pricing tests pass.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, database-reliability-transactions, firebase_firestore

### 32. Butcher and fresh grocery pack
**Brief:** Build `butcher-fresh-grocery` pack: weight POS, FEFO batches with expiry, fridge/cold-chain list, cutting rules, supplier price lists. Same-day freshness copy must be honest.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\butcher-fresh-grocery.ts`, `D:\Projects\SIR Business\packages\core\src\fresh\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\butcher-fresh-grocery\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\butcher-fresh-grocery\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\butcher-fresh-grocery\page.tsx`
**Done when:** FEFO expiry radar flags meat/dairy batches; weight sale works; landing page does not claim food-safety certification.
**Check:** `pnpm test:sectors -- butcher-fresh-grocery` green; expiry tests pass.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, database-reliability-transactions, firebase_firestore

### 33. Pharmacy chain foundation
**Brief:** Build `pharmacy-chain` pack only after `pharmacy` is stable: multi-branch stock view, central buying PO, branch transfer workflow, consolidated expiry report. Reuses pharmacy patient/controlled rules per branch.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\pharmacy-chain.ts`, `D:\Projects\SIR Business\packages\core\src\pharmacy-chain\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\pharmacy-chain\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\pharmacy-chain\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\pharmacy-chain\page.tsx`
**Done when:** branch transfer creates in-transit state; consolidated expiry report aggregates branches; patient rules stay branch-scoped.
**Check:** `pnpm test:sectors -- pharmacy-chain` green; cross-branch patient access denied.
**Skills:** firebase_firestore, database-reliability-transactions, modern-web-guidance, taste-design-engine, firebase_security_rules_auditor

## Wave D: service, retail, production and remaining packs (gated by wave C stability)

### 34. Service booking core for salon, barber, spa, gym, clinic, dental, vet, optical, photography, laundry, repair, car-wash
**Brief:** Implement shared service-appointment machinery used by wave-2/4 packs: calendar, staff assignment, deposits/no-show fees, packages with expiry, reminders. Each pack still gets its own manifest, seed, screens and landing page; this task builds only the reusable core plus one reference pack (`salon`).
**Files:** `D:\Projects\SIR Business\packages\core\src\services\appointments.ts`, `D:\Projects\SIR Business\packages\core\src\services\packages.ts`, `D:\Projects\SIR Business\packages\core\src\sectors\packs\salon.ts`, `D:\Projects\SIR Business\apps\web\src\app\(app)\services\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\salon\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\salon\page.tsx`
**Done when:** salon booking flow books stylist, collects deposit flag and sends reminder payload; package expiry decrements sessions.
**Check:** `pnpm test:services -- appointments packages` green; salon smoke test passes.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, database-reliability-transactions, firebase_firestore

### 35. Clinic and dental appointment packs
**Brief:** Build `clinic` and `dental-clinic` packs on service core: appointments, intake forms, visit notes, prescriptions print (not eRx), lab/imaging order tracking, reminders; dental adds treatment plans, tooth chart and staged payments. Patient data encrypted and excluded from AI/analytics.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\clinic.ts`, `D:\Projects\SIR Business\packages\core\src\sectors\packs\dental-clinic.ts`, `D:\Projects\SIR Business\packages\core\src\clinic\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\clinic\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\dental-clinic\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\clinic\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\clinic\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\sectors\dental-clinic\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\dental-clinic\page.tsx`
**Done when:** appointment booking and visit note persist; dental staged payment schedule computes; no medical advice text appears.
**Check:** `pnpm test:sectors -- clinic dental-clinic` green; encryption test passes for patient fields.
**Skills:** firebase_security_rules_auditor, firestore_rules_creation, database-reliability-transactions, modern-web-guidance, taste-design-engine

### 36. Retail matrix packs: clothing, electronics-phone, hardware-materials, wholesale-distribution, stationery-gifts, bookstore, school-shop
**Brief:** Build seven retail/B2B packs on retail core: size/color matrix, IMEI serial tracking, bulk price lists and contractor credit, tiered pricing and receivables, gift wrap/engraving, ISBN catalog, student wallets and term plans. Each gets manifest, seed, screens, reports, onboarding and bilingual landing page.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\{clothing-retail,electronics-phone,hardware-materials,wholesale-distribution,stationery-gifts,bookstore,school-shop}.ts`, `D:\Projects\SIR Business\packages\core\src\retail\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\*\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\*\page.tsx`
**Done when:** each pack smoke test passes; B2B credit ledger balances; electronics IMEI uniqueness enforced; school-shop child data minimal and parent-linked.
**Check:** `pnpm test:sectors -- clothing-retail electronics-phone hardware-materials wholesale-distribution stationery-gifts bookstore school-shop` green.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, database-reliability-transactions, firebase_firestore, firebase_security_rules_auditor

### 37. Service ticket packs: laundry, repair-shop, car-wash, spa-wellness, veterinary-clinic, optical-shop, florist, print-shop, photography-studio
**Brief:** Build nine service/job-ticket packs: item intake tags, quote-before-work approval, per-kg pricing, subscription car wash, packages, pet records/vaccines, lens catalog/prescriptions, event orders/same-day windows, job tickets/proofs/unit pricing, sessions/expiring galleries. Each gets manifest, seed, screens, reports, onboarding and bilingual landing page.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\{laundry,repair-shop,car-wash,spa-wellness,veterinary-clinic,optical-shop,florist,print-shop,photography-studio}.ts`, `D:\Projects\SIR Business\packages\core\src\tickets\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\*\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\*\page.tsx`
**Done when:** each pack smoke test passes; repair quote requires customer approval before work; photography gallery links expire; pet/vet records stay minimal.
**Check:** `pnpm test:sectors -- laundry repair-shop car-wash spa-wellness veterinary-clinic optical-shop florist print-shop photography-studio` green.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, database-reliability-transactions, firebase_firestore

### 38. Production packs: factory-workshop and furniture-carpentry
**Brief:** Build `factory-workshop` and `furniture-carpentry` packs: bill of materials, work orders, output, scrap, custom sizes, deposits and delivery slots. No heavy ERP claims; job-order scope only.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\factory-workshop.ts`, `D:\Projects\SIR Business\packages\core\src\sectors\packs\furniture-carpentry.ts`, `D:\Projects\SIR Business\packages\core\src\production\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\factory-workshop\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\furniture-carpentry\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\factory-workshop\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\factory-workshop\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\sectors\furniture-carpentry\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\furniture-carpentry\page.tsx`
**Done when:** BOM explodes to materials; work order output updates stock; furniture custom spec and deposit schedule persist.
**Check:** `pnpm test:sectors -- factory-workshop furniture-carpentry` green; scrap log requires reason.
**Skills:** modern-web-guidance, taste-design-engine, database-reliability-transactions, firebase_firestore, api-engineer

### 39. Hospitality, real estate and education packs: hotel-guest-house, real-estate-office, private-school-nursery, training-center, library, bookstore already covered
**Brief:** Build `hotel-guest-house`, `real-estate-office`, `private-school-nursery` and `training-center` packs: room calendar/housekeeping/deposits, listings/leads/commission/doc vault, child-minimal attendance/fees/parent billing, cohorts/attendance/teacher share. `library` and `bookstore` were covered in task 36; do not duplicate.
**Files:** `D:\Projects\SIR Business\packages\core\src\sectors\packs\{hotel-guest-house,real-estate-office,private-school-nursery,training-center}.ts`, `D:\Projects\SIR Business\packages\core\src\hospitality\*`, `D:\Projects\SIR Business\packages\core\src\realestate\*`, `D:\Projects\SIR Business\packages\core\src\education\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\sectors\*`, `D:\Projects\SIR Business\apps\web\src\app\sectors\*\page.tsx`, `D:\Projects\SIR Business\apps\web\src\app\ar\sectors\*\page.tsx`
**Done when:** hotel room calendar blocks dates; real-estate lead pipeline stages; school/nursery child fields are minimal and parent-linked; training cohort attendance computes teacher share.
**Check:** `pnpm test:sectors -- hotel-guest-house real-estate-office private-school-nursery training-center` green; child-data test asserts no marketing fields.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, firebase_security_rules_auditor, database-reliability-transactions, firebase_firestore

### 40. POS hardware layer: ESC/POS print bridge, barcode wedge, cash drawer, customer display, kiosk lock
**Brief:** Implement M5 hardware layer: ESC/POS byte builder with golden tests, browser print fallback, USB/Bluetooth barcode wedge input, cash drawer kick command, customer display live cart, and kiosk locked profile. Web-first; fiscal ETA hardware remains out of scope.
**Files:** `D:\Projects\SIR Business\packages\core\src\hardware\escpos.ts`, `D:\Projects\SIR Business\packages\core\src\hardware\escpos.test.ts`, `D:\Projects\SIR Business\apps\web\src\app\(app)\pos\hardware\*`, `D:\Projects\SIR Business\apps\web\src\app\(app)\kiosk\*`
**Done when:** golden receipt bytes match fixture; drawer kick sends command in emulator/hardware test mode; kiosk cannot navigate outside allowed routes.
**Check:** `pnpm test:print` golden equal; kiosk route guard test passes.
**Skills:** modern-web-guidance, modern-app-engineering, verification, api-testing, database-reliability-transactions

### 41. Owner analytics page `/owner`
**Brief:** Build company owner page at `/owner` protected by `company_owner` claim: fleet overview, funnel, MRR/ARR/ARPU, health, churn, product adoption, AI eval drift and TV-monthly export. All metrics aggregate; tenant drill-down requires audited break-glass.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\owner\*`, `D:\Projects\SIR Business\apps\web\src\app\api\v1\owner\metrics\route.ts`, `D:\Projects\SIR Business\packages\core\src\owner\metrics.ts`, `D:\Projects\SIR Business\packages\core\src\owner\metrics.test.ts`
**Done when:** page renders only aggregate metrics; non-owner redirected/403; every view audit-logged.
**Check:** Playwright or route test asserts 403 for member token and 200 for owner claim token.
**Skills:** modern-web-guidance, taste-design-engine, modern-ui-ux-design-system, api-engineer, firebase_security_rules_auditor, financial-analysis

### 42. Legal pack, privacy pages and DPA
**Brief:** Write bilingual `/privacy`, `/terms`, `/refunds`, `/cookies`, DPA download and sub-processor list. No SOC 2/ISO claims; liability cap and arbitration clauses per OWNER_DEFAULTS; cookie banner blocks trackers until consent and has equal Reject; data export/delete links visible.
**Files:** `D:\Projects\SIR Business\apps\web\src\app\privacy\*`, `D:\Projects\SIR Business\apps\web\src\app\terms\*`, `D:\Projects\SIR Business\apps\web\src\app\refunds\*`, `D:\Projects\SIR Business\apps\web\src\app\cookies\*`, `D:\Projects\SIR Business\apps\web\src\app\legal\dpa\*`, `D:\Projects\SIR Business\docs\legal\*`
**Done when:** pages render ar+en; cookie banner blocks GA/Meta until consent; DPA PDF downloads; no false compliance claims.
**Check:** grep for SOC 2/ISO returns only "not claimed" context; cookie test asserts tracker blocked pre-consent.
**Skills:** api-documentation, modern-web-guidance, taste-design-engine, a11y-debugging, verification

### 43. Launch readiness instrumentation and pilot checklist
**Brief:** Add product analytics events for activation funnel (signup -> sector -> first product -> first sale -> day-2 active), consent-gated only; add support assistant feedback events; write `docs/launch-checklist.md` covering dual-host curl, rules suite, eval gate, legal pages, sector smoke suite, pilot consent letters and rollback rehearsal.
**Files:** `D:\Projects\SIR Business\packages\core\src\analytics\events.ts`, `D:\Projects\SIR Business\packages\core\src\analytics\events.test.ts`, `D:\Projects\SIR Business\docs\launch-checklist.md`, `D:\Projects\SIR Business\apps\web\src\app\api\v1\analytics\*`
**Done when:** events fire in emulator and exclude PII; checklist has measurable acceptance for every M0-M6 gate.
**Check:** analytics test asserts no customer names/phones in payloads; checklist references real commands.
**Skills:** website-traffic-analytics, api-engineer, api-testing, verification, agent-supercharged-os

### 44. Arabic/English copy deck and localization QA
**Brief:** Create `packages/ui/src/i18n` dictionary structure, Egyptian-dialect UI strings for core flows, English mirror, bidi tests for mixed Arabic/English/numbers, and a copy lint that bans em-dashes, emoji headers, banned AI words and "(RTL)" labels.
**Files:** `D:\Projects\SIR Business\packages\ui\src\i18n\*`, `D:\Projects\SIR Business\packages\ui\src\i18n\copy.test.ts`, `D:\Projects\SIR Business\scripts\lint-copy.mjs`
**Done when:** copy lint passes on core screens; bidi test covers product names, prices and phone numbers; no banned words.
**Check:** `node scripts/lint-copy.mjs` exits 0; test asserts logical CSS properties only.
**Skills:** modern-web-guidance, taste-design-engine, anti-vibecoded-design-system, a11y-debugging, verification

### 45. Performance, PWA and five-state audit
**Brief:** Run Lighthouse/PWA audit, 120 Hz transform audit, reduced-motion pass, five-state completeness on 30 core screens, 320-1920 px layout audit both directions and themes. Fix only verified blockers; document skips honestly.
**Files:** `D:\Projects\SIR Business\docs\qa\five-state-audit.md`, `D:\Projects\SIR Business\docs\qa\responsive-audit.md`, `D:\Projects\SIR Business\apps\web\src\app\**\*.tsx`, `D:\Projects\SIR Business\packages\ui\src\*`
**Done when:** audit docs list every screen with states and breakpoints; zero P0/P1 layout or accessibility blockers remain.
**Check:** Lighthouse PWA >= 90 on preview; audit docs have no "TODO" placeholders.
**Skills:** verification, chrome-devtools, a11y-debugging, modern-web-guidance, taste-design-engine, emil-motion-impeccable

### 46. Security hardening pass before pilot
**Brief:** Run `firebase_security_rules_auditor` style review on all rules and API routes: deny-by-default, server-side membership checks, rate limits on auth/AI/billing, HMAC webhooks, no secrets in client, PIN lockout, audit on sensitive reads, health-data exclusion from analytics/AI.
**Files:** `D:\Projects\SIR Business\firestore.rules`, `D:\Projects\SIR Business\apps\web\src\app\api\**\route.ts`, `D:\Projects\SIR Business\docs\security\review-2026-11.md`
**Done when:** review doc lists every route/rule with verdict; all P0/P1 fixed or gated; emulator suite green.
**Check:** `firebase emulators:exec --only firestore "npm test -- rules"` green; grep for client-side secrets returns nothing.
**Skills:** firebase_security_rules_auditor, firestore_rules_creation, api-testing, auth, karpathy-skills

### 47. Pilot instrumentation and support runbook
**Brief:** Prepare 3-business pilot kit: consent letter template, onboarding script per sector, daily check-in sheet, bug triage severity definitions, rollback rehearsal steps and support runbook for ETA/ZATCA/payment/print failures.
**Files:** `D:\Projects\SIR Business\docs\pilot\consent-letter.md`, `D:\Projects\SIR Business\docs\pilot\onboarding-script.md`, `D:\Projects\SIR Business\docs\pilot\check-in-sheet.md`, `D:\Projects\SIR Business\docs\support-runbook.md`
**Done when:** docs are bilingual-ready, reference real commands and contain no fake testimonials or unsupported claims.
**Check:** consent letter has data-use and deletion clauses; runbook maps every P0 to an owner action.
**Skills:** api-documentation, agent-supercharged-os, verification, direct-action-shield

### 48. Final r61 planning handoff note
**Brief:** After tasks 1-47 are merged or explicitly deferred, update `D:/Projects/_SIR/ops/bus/sir-business.md` with one line: current milestone, last green verify, open owner actions and next task id. Do not mark a task done without evidence.
**Files:** `D:\Projects\_SIR\ops\bus\sir-business.md`, `D:\Projects\SIR Business\.sir\CHECKPOINT.md`
**Done when:** bus line exists and checkpoint matches reality; no invented progress.
**Check:** bus line contains date, milestone and next task; checkpoint has no stale "done" claims.
**Skills:** agent-supercharged-os, direct-action-shield, verification
