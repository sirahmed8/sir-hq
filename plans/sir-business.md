# PLAN: SIR Business
Status: planned, not started. Wave 2. Replaces: SIR Restaurant, SIR Market, SIR Pharmacy, SIR Library. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 1. Mission and audience
One point-of-sale and operations suite for small Egyptian businesses with four modes: restaurant, supermarket, pharmacy, library/bookstore. Audience: shop owners and their cashiers.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Business` |
| GitHub (private) | `sirahmed8/sir-business` |
| Firebase project / OAuth app name | `sir-business` / "SIR Business" |
| Cloudflare project | `sir-business` (`sir-business.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-business` (Android, iOS, Windows) |
| Platforms | Windows desktop (Electron, offline first) + web portal + Android tablet later; Arabic first |
| Money | Free single-device starter; paid monthly plans in EGP (Restaurant 450/750/1950 today; Market 950/2450/4900 today, to be re-priced from real costs); Launching Soon fallback |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Four copies of one shell with no data layer, seeded mock arrays, hardcoded admin and preset PINs, fake upgrade success and canned AI answers (Pharmacy invents stock; patient-safety risk).
- Restaurant rules let any signed-in user read/write every branch; kill switch with a hardcoded rescue PIN.
- Electron build deps missing in three repos; `node_modules` symlinked between projects.

## 4. What to port from the old project
- Shared: shell, POS, shifts, receipts and ESC/POS, scale driver, FEFO inventory, reports, PIN lock UX, updater, Electron main/preload (sandbox on).
- Restaurant: KDS, waiter, kiosk, floor plan, delivery hub, ZATCA phase 2. Market: procurement, Customer 360, e-commerce, ETA/ZATCA signers. Pharmacy: expiry radar, controlled-drug log. Library: borrowing + deposits, study desks, members, catalog.

## 5. Screens and entities
**Screens:** Onboarding wizard (linear), Lock screen, POS, Orders/KDS, Inventory, Purchasing, Customers, Reports, Staff, Devices, Settings, Billing, Owner dashboard, Help; mode-specific screens per vertical
**Entities:** Tenant, Branch, User/Role, Product, StockLot, Sale, Shift, Supplier, PurchaseOrder, Customer, Table/Order (restaurant), Prescription/Patient (pharmacy), Loan/Member (library)
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Flagship: demand and expiry forecasting with plain-language suggestions from real sales only. Assistant: grounded help. Pharmacy: no clinical advice; interactions only from a cited dataset with a pharmacist-review disclaimer, otherwise the feature is off.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Per-tenant claims in rules; tenant-isolation tests with two tenants.
- PINs hashed (argon2/scrypt); no preset users; license check server-side; kill switch removed or disclosed in the EULA.
- Patient data: consent, encryption at rest, deletion flow.

## 8. Milestones
### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-business`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-business` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Business", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Core with SQLite (encrypted) + sync to Firestore; Restaurant POS sale end to end with receipt print preview.
### M2 Parity with the old project
- [ ] Restaurant mode complete (KDS, floor plan, delivery, ZATCA behind a flag until keys), then Market, Pharmacy, Library modes on the same core.
- [ ] Parity checklist per mode from the four inventories.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Forecast + help assistant; eval sets; no invented numbers.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Signed installer only when a certificate is affordable; until then SmartScreen note in install guide; migration importer from old exports; archive the four old repos.

## 9. Risks and open decisions
- Hardware drivers (printers, scales) need real devices to test.
- ZATCA/ETA certificates are owner/government steps.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
