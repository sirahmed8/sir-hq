# PLAN: SIR Business (Wave 5, GLOBAL product, not started)
Audited 2026-11-10. Replaces `SIR Restaurant`, `SIR Market`, `SIR Pharmacy`, `SIR Library` (all in `legacy/`, kept until M6). Public product, free starter and paid plans in EGP. **GLOBAL**: anyone in the world, accounts, subscriptions, every platform and OS including phone, watch, car, TV. Owner-only analytics page, dual hosting (Firebase + Vercel), subscription grants owner all permissions.

## 1. Purpose (plain words)
A cash-register and shop-management app for small Egyptian businesses. One app with four modes: restaurant, supermarket, pharmacy, library or bookstore. It works without internet, prints receipts, tracks stock and shows the owner what sold today. For global users: any small business anywhere can use the same offline-first POS with cloud sync.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Business` |
| GitHub (private) | `sirahmed8/sir-business` |
| Stack (default) | Electron + Vite + React 19 + TypeScript strict + Tailwind v4 desktop app, SQLite local database (real, not the in-memory fallback), sync to a Cloudflare Worker + Firestore (or D1) cloud when online; web owner portal on Cloudflare Pages |
| Domain | candidates `sirbusiness.app` or an `.eg` name (owner checks `.eg` rules and price: "(unsourced, verify)"). Until then `sir-business.pages.dev` |
| Platforms | **Platform Matrix (GLOBAL):** Windows desktop ✅ (first, offline-first); Web owner portal ✅; Android tablet ✅ Expo/Capacitor decision at M5; macOS Electron build ⏭️ M6+ (only if a user asks); Linux Electron build ⏭️ M6+; iOS ⏭️ skipped; TV ⏭️ skipped; watchOS ⏭️ skipped; Car ⏭️ skipped. Browser extension: skipped. All platforms share the same Firebase project and auth. |
| Money | **Pricing & Free Tier:** Free single-device starter (one shop, one device, offline-first). Paid plans per mode in EGP. Old prices were Restaurant 450/750/1950 and Market 950/2450/4900 per month: treat as test prices to be re-priced from real costs and 5 shop-owner interviews "(unsourced, verify)". EGP first, USD/SAR/AED toggle auto-detected from locale/IP with manual override. "Subscriptions launching soon" + email capture until keys exist. Owner gets all Pro features free. Subscription grants owner all permissions in owner dashboard. |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30); 10 commits, all setup and plan.
Legacy facts (`ops/inventory/SIR-Business-Library-Market-Pharmacy.md`, 2026-10-29, nothing re-run): four copies of one shell; Market has 1,001 tracked files and 53 test files (claimed 1,367 cases, unverified); SQLite falls back to an in-memory engine because `better-sqlite3` was not installed; sessions and cart in localStorage; AI keys in the client (`VITE_`); hard-coded owner emails and preset PINs; seeded mock arrays; canned AI answers, and the Pharmacy AI invents stock (patient-safety risk); Restaurant rules let any signed-in user read and write every branch; Electron build deps missing in three repos.
Nothing from legacy may be called working.

## 4. Security and conduct rules
1. Cloud sync: deny-by-default rules by tenant (shop) and branch; emulator test: user from shop A cannot read shop B or another branch without claim (use `owner-auth` from SHARED_PLATFORM_KIT).
2. No hard-coded PIN, owner email or rescue PIN anywhere (grep test in CI). PINs are hashed (argon2 or scrypt) with lockout; owner claim set server-side.
3. Electron: contextIsolation on, sandbox on, no remote code, typed IPC, signed auto-update (certificate is an owner step).
4. AI keys only on the server proxy (use `ai-proxy` from SHARED_PLATFORM_KIT); AI never invents stock or prices: pharmacy and stock answers come from database queries and the model only phrases them (test: answer for an item with zero stock says zero).
5. Money: totals in integer piasters, rounding tests, receipts reprint from stored data; every void or refund logged with user and reason.
6. Local database encrypted at rest option for pharmacy (SQLCipher or OS-level; decide in ADR); backups to a chosen folder and to cloud with restore test.
7. Webhook and subscription checks server-side only (use `signed-webhook` and `billing-fallback` from SHARED_PLATFORM_KIT); license state cached with grace period so a shop never gets locked out mid-service.
8. Pharmacy and controlled-drug logs append-only; this is a record keeper, not medical advice. Egyptian pharmacy rules: "(unsourced, verify)" with a pharmacist before any pharmacy launch.
9. **Owner-only analytics page**: separate route, server-verified owner token, shows all metrics (active shops, sales volume, errors, churn). No other user sees it.

## 5. Shared pieces (SIR Platform; internal packages first)
`owner-auth`, `signed-webhook`, `billing-fallback`, `ai-proxy`, `legal-pack`, `i18n`, `ui/styles/hooks`, Telegram sender; ESC/POS receipt builder and quarantine-style undo are candidates to move to Platform after the second consumer. Hagoozat's owner dashboard pattern is reused for the web portal. **Reuses SHARED_PLATFORM_KIT entirely; only POS/business-logic features differ.**

## 6. Screens and entities
Onboarding wizard (steps unlock in order), Lock screen, POS, Orders and kitchen display (restaurant), Inventory (FEFO batches), Purchasing, Customers, Reports, Staff, Devices, Settings, Billing, **Owner dashboard**, Help; mode screens: floor plan and delivery (restaurant), weighing scale and procurement (market), expiry radar and controlled-drug log (pharmacy), borrowing, deposits and study desks (library). Entities: Shop, Branch, User, Product, Batch, Sale, Payment, Shift, Customer, Supplier, PurchaseOrder, Device, Subscription, AuditLog.
Five states, Arabic RTL first and English, high-contrast, big touch targets for tablets (44 px minimum), 320 px to 4K, WCAG 2.2 AA, own logo.

## 7. AI and support
Flagship: "ask your shop" (what sold best this week, what is expiring) answered from real queries. Support assistant grounded in `docs/help`. Chain via `ai-proxy` (from SHARED_PLATFORM_KIT), free-tier cap 5 per day, owners unmetered, kill switch, evals with numeric-accuracy checks (answer must equal the SQL result).

## 8. Operations (standard 26 from SHARED_PLATFORM_KIT)
Update channel with staged rollout, crash reports (consent), cloud backup health, license reconciliation job, weekly Telegram report (active shops, sales volume in EGP, errors, churn), status JSON, emergency alerts (sync failure rate, update failure). Support triage by assistant with logs attached when the user agrees.

## 9. Launch package, legal, visibility
Owner buys domain, code-signing certificate, Paymob and Fawry accounts (test mode in code), Play Console later. Legal pack: privacy, terms (EULA style for desktop), refunds and auto-renewal, cookies for the portal, DPA for shops handling customer data, sub-processors; PDPL and consumer rules as tasks. Egyptian e-invoicing (ETA) and Saudi ZATCA phase 2: build only after reading the official technical specs; certificates and onboarding with the tax authority are owner steps; all tax statements here are "(unsourced, verify)". Lawyer and accountant review before paid launch.
**Dual hosting**: Firebase Hosting AND Vercel (import GitHub repo with Vercel CLI), same build, same env vars on both. Both addresses curl-checked (retry once on timeout).
Visibility: Arabic queries by trade ("برنامج كاشير سوبر ماركت", "برنامج صيدلية"), one landing page per mode, comparison pages against named local competitors once the study is sourced, `llms.txt`, facts page, YouTube demo videos of real use, weekly AI-answer check. No fake shop logos or reviews.

## 10. Three-Milestone Roadmap (owner-visible checks)
| Milestone | Goal | Owner-Visible Exit Check |
|---|---|---|
| **M1–M2: Core Slice** | POS sale persists in real SQLite; app restarts and shows the sale; e2e test; parity: inventory, shifts, receipts, reports; then restaurant, library, pharmacy as modes | 1. Run desktop app → make a cash sale → restart app → sale persists. 2. Per-mode checklist ticked against inventory routes. 3. Screenshot at tablet (1366x768) and desktop, LTR/RTL, light/dark. |
| **M3: Security, Legal, Billing, Owner Page** | Rules tests, no-hard-coded-secret grep, billing fallback test, legal pages, owner-only analytics page live | 1. CI grep finds no hard-coded PIN/email. 2. Open `/owner` → server-verified token required → shows active shops, sales volume. 3. Pricing page shows "Subscriptions launching soon" + email capture. 4. Legal pages exist at `/legal/*`. 5. Dual hosting verified: curl both Firebase and Vercel URLs. |
| **M4–M6: AI, Quality, Release** | "ask your shop" numeric eval 100% match with SQL; installer builds; signed installer (owner certificate); 3 real shops piloted with written consent; old folders archived | 1. Run `npm run eval:shop` → answers equal SQL results. 2. Installer builds and passes smoke test on clean VM. 3. Owner signs installer with certificate. 4. 3 real shops piloted with written consent. 5. Legacy folders archived to `old projects\`. |

## 11. Next 10 tasks (each under 2 hours)
1. Deep scan of the four legacy apps: shared module list and per-mode differences. Files: `.sir/reports/parity.md`. Check: table with module, apps containing it, keep/drop.
2. Decide and record the data layer in `docs/adr/001-data-sync.md` (SQLite + sync). Check: ADR names the conflict rule (last write wins per field, or server order).
3. Scaffold monorepo: `apps/desktop`, `apps/portal`, `packages/core`. Check: `npm run build` exits 0 in all three.
4. Money module with integer piasters and tests (rounding, discounts, tax). Files: `packages/core/src/money/`. Check: 30 unit tests green.
5. SQLite schema and migrations for Product, Batch, Sale. Check: migration test creates and reopens the file; no in-memory fallback in code (grep test).
6. POS screen: add item, pay cash, save sale, five states. Check: screenshot at 1366x768 and an e2e test.
7. Receipt builder (ESC/POS bytes) with golden-file tests. Check: golden bytes equal.
8. PIN lock with hashed storage and lockout, no hard-coded PIN. Check: test of 5 wrong tries locks; grep finds no PIN literal.
9. Tenant rules for cloud sync with emulator tests. Check: cross-shop read fails.
10. Interview script for 5 shop owners (price, pain points) in `docs/research/interview.md`, to be run by the owner or a volunteer. Check: file exists; results later go to `plans/competitors/sir-business.md` with dates.

## 12. Risks and open questions (defaults)
- Scope (four businesses): default is Market first, then Restaurant, Library, Pharmacy last (safety).
- Hardware drivers (printers, scales, barcode scanners) need real devices: default is mock device interface with golden tests plus one real printer test by the owner.
- Native module `better-sqlite3` with Electron: default is `electron-rebuild` in CI and a smoke test that opens the DB.
- Tax e-invoicing complexity: default is ship without it, show "e-invoice coming" honestly, then add after reading official specs.
- Competitor and price claims: `plans/competitors/sir-business.md` must carry links or "(unsourced, verify)".

## 13. Only the owner can do
Buy domain and code-signing certificate; create Firebase, Cloudflare, Paymob, Fawry accounts; tax authority onboarding; accountant, lawyer and (for pharmacy) pharmacist review; recruit pilot shops and get written consent; test real printers and scales.

## 14. Competitor Matrix (from plans/competitors/sir-business.md)
| Competitor | Strengths | Flaws | Our Edge | Ideas to Steal |
|---|---|---|---|---|
| (to be sourced) | | | | |

*Every claim in competitor matrix must carry a source link or "(unsourced, verify)".*

## 15. Feature Parity Target (best-in-category)
Match or exceed the best Egyptian POS for: offline-first operation, receipt printing, multi-mode (restaurant/market/pharmacy/library), cloud sync with conflict resolution, owner dashboard with real-time sales, Arabic RTL excellence, Arabic/English bilingual, Egyptian tax compliance ready.