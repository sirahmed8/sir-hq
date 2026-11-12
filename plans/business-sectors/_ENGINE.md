# The SIR Business engine, and how a sector plugs into it

> Round r56 (2026-11-12). This is the shared spine behind every sector file in `plans/business-sectors/`.
> It follows `plans/sir-business.md` (the merged plan), `plans/PRODUCT_DIRECTION_2026-11-12.md` section 3 and section 8, `standard/23-premium-code-bar.md` and `standard/OWNER_DEFAULTS.md`.
> Nothing here is built. Every price is a proposal, every legal claim is marked "(unsourced, verify)" until the source is read.

## 0. The rule this file exists for

The owner wrote (section 8): "SIR Business is the biggest project: 25 sectors or more, and EACH sector gets its own specialised software and site: its own data model, screens, workflows, reports, onboarding, templates, terminology, sector-specific integrations and its own landing page, all on the shared Business engine (accounts, teams, roles, billing, inventory, finance, analytics). Not one generic app with a different label."

So the engine is not the product. The engine is what a sector does not have to write twice. A sector pack is the specialised software: its own screens, its own data model extension, its own workflow, its own words, its own site page.

Two failure modes this file rules out:

1. **The renamed app**: one generic screen set with the sector name swapped in. If the cashier flow of a bakery and the cashier flow of a pharmacy are the same screen, the sector file is a lie. We write them apart on purpose.
2. **The forked product**: every sector becoming its own repository, its own login, its own database, its own billing. That is what the four legacy apps did and what killed them (`ops/inventory/SIR-Restaurant.md`, `ops/inventory/SIR-Business-Library-Market-Pharmacy.md`: fake auth, no data layer, client-side keys, false compliance claims).

The test for a sector pack: a shopkeeper of that sector can run their week without seeing a screen, a field or a word that belongs to another sector, while the owner of five different businesses signs in once.

## 1. Tenancy: one account, several businesses, several branches

```
organizations/{orgId}        one owner (a person or a company group)
  businesses/{businessId}    one shop, one sector template, one currency, one tax identity
    branches/{branchId}      one location (optional; one by default)
      memberships             who works where, with which role
```

- Every document carries `orgId` and `businessId`; branch-scoped documents carry `branchId`. Firestore security rules deny by default: no membership, no read. The rules file is the boundary, not the client (`plans/sir-business.md` section 5.1, emulator test suite is a milestone gate).
- One owner can own up to 5 businesses on one bill (extra business +50% of the base price). Each business has its own team, catalog, stock, receipts, reports, notification channel and subscription state.
- Sectors never cross-read. A pharmacy branch cannot see a market branch even when the same human owns both. Isolation tests run in CI.
- Branch support is not a new plan feature: a business may have several branches on the same plan, the plan counts branches and seats.

## 2. Accounts and identity

| Entry | How | Notes |
|---|---|---|
| Owner sign-up | email + password, Google, or phone OTP (ar-EG, +20 default) | No card, no card wall. Language and currency auto-detected from locale/IP with a manual override (OWNER_DEFAULTS 16) |
| Staff sign-in | phone link, one-time invite link with expiry, or the branch PIN on the tablet | No shared passwords. Deactivation is instant: the membership status changes and the token claim drops on next refresh |
| Owner of the company | server-verified custom claim `company_owner` | Owns the `/owner` analytics page only; every view is audit-logged; break-glass drill-down expires after 30 minutes |

No hard-coded owner email, no preset PIN, no client-side "is admin" check. The legacy apps failed exactly here (`ops/inventory/SIR-Business-Library-Market-Pharmacy.md`: "Google login sets a hardcoded admin", "hardcoded PIN in AppShell", "owner email in bundle"). Those patterns are banned.

## 3. Teams, roles and permissions

- **Role templates** shipped by the engine: owner, manager, cashier, staff. Every sector pack adds its own (pharmacist, waiter, librarian, stylist, trainer, driver, technician, agent).
- **Permissions** are a flat list of verbs the engine checks: `pos.sell`, `pos.void`, `pos.discount`, `inventory.read`, `inventory.write`, `reports.finance`, `reports.customers`, `team.manage`, `settings.billing`, `settings.sector`, `devices.manage`, `audit.read`, plus sector-specific verbs a pack may add (for example `pharmacy.controlled`, `clinic.records`, `library.lend`).
- **Delegation**: a manager gets everything except billing and export. A cashier can sell and refund inside a set limit; anything above it asks for the manager override, which is an audited action with the reason and the user.
- **Invites** expire, can be revoked, and cannot be forwarded (single use). Staff see only their own branch unless the role says otherwise.
- **Attendance** is engine-level: clock in and out on the tablet with a PIN or a QR badge, breaks, late and absent rules, weekly summary, payroll CSV export. The engine never pays anyone (not a money-mover at v1).

## 4. Shifts, money and finance

- **Money** is integer piasters (or integer cents for USD). No floats anywhere in pricing, tax or totals. Rounding is banker's rounding on half, tested.
- **Shifts**: open with a counted float, close with counted cash, the engine shows expected against actual, flags the difference, prints the Z-report, hands the drawer to the next shift.
- **Finance**: cash and bank ledger, petty cash, expenses with a receipt photo and a category, supplier payments, simple operating profit and loss for the shop, a VAT summary for the accountant, clean CSV exports for the books. We are not a bookkeeping system and we do not pretend to be: exports hand off to Zoho, Daftra or the owner's accountant.
- **Tax**: the ETA e-receipt and e-invoice pipeline is a single server-side signer with a spec that is read before it is written (`plans/sir-business.md` section 15). Until the official spec is read, the receipt prints our own sequential number and says so honestly.

## 5. Inventory and purchasing

- Items with variants, units (piece, kilogram, gram, litre, box, pack, hour, service), a barcode, a category, a tax rate, a cost, a price, a reorder point, and an optional FEFO flag.
- **Batches** with expiry exist wherever the sector has them (pharmacy, food, bakery, cosmetics, veterinary drugs, pet food). The engine owns the batch model and the expiry radar (30, 60, 90 days); the sector pack decides which of its items must be batched and what the shelf life is.
- Purchasing: suppliers with price lists and terms, purchase orders in draft, sent, received, partial states, goods receipt with discrepancies, transfers between branches with an in-transit state, cycle counts, waste log, and a reorder suggestion from 30-day velocity (opt-in, never auto-ordered).
- **Never negative silently**: an oversell is allowed offline but it is flagged with an audit entry and reconciled, never hidden.

## 6. Sales, orders and the point of sale

- The POS cart is keyboard-first: barcode scanner as a keyboard (HID wedge), quick keys, quantity multipliers, favourites grid, held and parked orders, split bills, mixed payment (cash, card through Paymob, mobile wallets, InstaPay QR, credit for B2B customers).
- Discounts and refunds are limited by role, need a reason, and are written to an append-only audit log.
- Receipts: a receipt layout per sector pack (header, columns, VAT line, loyalty line, QR, footer) rendered to ESC/POS bytes for thermal printers and to the browser for A4 prints. A reprint from a stored sale works offline.
- **Kitchen display** is a module, not a separate product: `kds.fire` opens it for the sectors that need it (restaurant, cafe, bakery, fast food).

## 7. Customers, loyalty and the credit book

- Customer profiles: name, phone, WhatsApp opt-in flag, and for B2B sectors a credit limit, a payment term and a balance.
- Loyalty: points and tiers by visits or by spend, coupons, memberships with sessions for service sectors (a gym member buys 20 sessions and uses 7).
- The **credit book** (دفتر العملاء) is an engine module enabled by the sectors that sell on credit (grocery, wholesale, hardware, garage): a per-customer ledger of what is owed, with a due date, a limit, and a statement.
- Privacy: export and delete on request, never sold, never used for advertising, opt-in for marketing only.

## 8. Notifications, digests and the one bot

- One bot for the whole product (`@SIRBusinessBot`): the owner links his own account with a one-time code, then the bot sends per-business digests (today against yesterday, cash variance, low stock, expiring batches) and alerts (a licence about to expire, a failed sync). The bot never holds business data that the account cannot see itself (`plans/BOT_ARCHITECTURE.md`).
- In-app notification centre, email for receipts and invoices, WhatsApp deep links for customer messages using the owner's own account (read-only API, never scraped).

## 9. Offline mode and sync

- The POS keeps selling with no connection: catalog and cart cached in IndexedDB, mutations queued, receipts printable from the queue.
- Conflict rule (documented in `docs/adr/001-offline-sync.md`): server order wins per field for quantities; money rows are never merged; a sale is an atomic local-then-server commit with an idempotency key so a retry never charges twice.
- A sync chip is always visible: synced, syncing, offline with the pending count.

## 10. Hardware

Every device sits behind an interface with a simulated driver for CI and a golden-file test suite: ESC/POS thermal printers (58 mm and 80 mm), barcode scanners, cash drawers, weighing scales, kitchen displays, customer displays, kiosks, card terminals, and a local bridge on Windows. A sector pack declares which devices it needs; the engine implements them once. No vendor lock-in, no hardware bundle forced on the customer.

## 11. Analytics

- **Business level** (the customer): sales by hour, day, week, month; by item, category, employee, payment method; inventory valuation; low stock and expiry; loyalty cohorts; cash reconciliation; a today against yesterday card; a weekly Telegram digest; CSV and PDF export.
- **Company level** (the owner of SIR Business, never the customer): businesses by sector and trial cohort, activation, trial to paid conversion, MRR in EGP and USD, churn, usage, error rate, sync failures, support volume, and a per-business health score. Aggregates only, no customer content, no employee names in analytics.

## 12. Privacy of businesses and employees

This is the part a sector pack may not weaken.

- **The business owns its data.** We hold it for the service, we never sell it, we never train a model on it, and we never show one business to another.
- **Employee data** (attendance, payroll export, performance): collected only with the business's own lawful basis, visible to that business, exportable and deletable, and never part of our analytics.
- **Special-category data** (patient records, prescriptions, drug interactions, member health notes) is encrypted per tenant (AES-GCM with a wrapped key), never enters analytics, never enters an AI prompt, and is deleted on request with a documented grace period.
- **Audit log**: append-only, who did what, when, on which entity, with a reason where a reason exists.
- **Export and delete**: self-serve from settings, JSON and CSV per business. Deletion is soft for 30 days, then purge; backups age out in 90 days.
- **Egypt PDPL and consumer law**: the legal pack is drafted with a lawyer (owner step). No compliance claim is published before it is signed off; the legacy apps claimed SOC 2 and ISO 27001 with no evidence and that is banned.
- **We hold the data about businesses, employees and usage with strict privacy** (the owner's words). That is a promise about our own conduct, and it is testable: the owner analytics page has no drill-down into customer content without an audit-logged break-glass.

## 13. How a sector pack plugs in

A sector pack is a typed manifest plus its own modules. It never forks the engine.

```ts
// packages/core/src/sectors/registry.ts (the contract every pack implements)
export interface SectorPack {
  id: string;                 // "restaurant"
  nameAr: string;             // "مطعم"
  nameEn: string;             // "Restaurant"
  group: SectorGroup;         // "food-and-drink"
  baseTemplate: BaseTemplate; // "restaurant" | "market" | "pharmacy" | "clinic" | "service" | "retail" | "b2b" | "hospitality" | "education" | "production"
  modules: ModuleId[];        // modules this pack enables from the registry
  featureFlags: FeatureFlag[];// what is on for this pack and in which plan
  roleTemplates: RoleTemplate[];   // sector roles and their permissions
  terminology: TermMap;       // Arabic and English words the UI must use
  catalogSeed: SeedBundle;    // categories, units, shelf lives, default roles, receipt layout, first-week checklist
  reportPack: ReportKey[];    // which reports are on the dashboard by default
  integrations: IntegrationId[];    // devices and services this pack needs
  landing: LandingContent;    // Arabic and English copy for the sector page
  riskNote: string;           // regulation and data risk, with "(unsourced, verify)" markers
}
```

**The module registry** (`packages/core/src/modules/index.ts`) is the menu of everything that can be switched on: `pos`, `tables`, `kds`, `inventory.fefo`, `purchasing`, `credits`, `appointments`, `memberships`, `prescriptions`, `records`, `jobcards`, `rooms`, `leads`, `deliveries`, `deliveries.zones`, `attendance`, `shift`, `students`, `grades`... Each module is code written once, tested once, and listed by name honestly (a name in the registry with no implementation behind it is a bug, not a placeholder).

**Feature flags** decide what a pack turns on and what a plan unlocks: `pos.sell`, `inventory.fefo`, `appointments.reminders`, `students.records`, `pharmacy.controlled`. A flag is set by three things and nothing else: the sector pack, the plan, and the branch. No flag is set by a URL parameter or a client-side toggle that hides a feature the plan does not include; the server decides.

**Sector packs are additive**: a pack may add entities (tables, appointments, prescriptions, job cards, rooms, students), screens, reports and roles. It may not change the meaning of a sale, a payment, a shift or a customer in another pack.

### What a sector pack may never do

- No second login, no second database, no second billing path, no second customer model.
- No fake data in a production path. Seeds are marked "review before going live" and are empty states until the shop enters real data.
- No clinical or legal advice (a pharmacy pack may show a drug interaction flagged from a licensed data source; it may never invent one).
- No false compliance claim on any screen ("ETA compliant" only after the spec is read and the signer is live).
- No emoji in the UI, no em-dash in copy, Arabic first then English mirrored.

## 14. The shape of a sector file

Every file in `plans/business-sectors/` has the same eleven parts so that two sectors can be compared line by line:

1. Who runs it and the daily pain
2. The data model (entities and fields, units, batches, expiry, tables, appointments, prescriptions)
3. Screens and workflows that belong to this sector only
4. Roles and permissions
5. Reports and KPIs
6. Integrations that matter
7. The onboarding wizard and the ready template data
8. The landing page outline (Arabic and English)
9. Pricing tier notes
10. Competitors (3 to 5, with what they charge and where they are weak)
11. The first 10 tasks, written as briefs in `ops/briefs/business-<sector>-tasks.md`

Plus the honest part: risks, unknowns and what we refuse to fake.

## 15. Build order and the shared gates

A sector is built when the engine is ready for it, not before. The order is in `_INDEX.md` (market size first, then effort). Three gates apply to every sector and are not repeated per sector:

1. **Engine gate**: tenancy, money, POS, inventory, shifts, roles, offline queue and the module registry are working and tested.
2. **Sector gate**: the pack compiles, the template seed loads, the sector screens pass the five-state and layout rules (320, 390, 768, 1280, 1920 px in Arabic and English, light and dark), and the receipt golden test matches.
3. **Truth gate**: no fake numbers on any screen, the compliance copy matches reality, the seed is labelled as a seed, and the sector page names nothing we have not read a source for.

A sector that cannot pass the truth gate ships as "on the way" with a waitlist entry, never as a half-template.

## 16. Adding a sector later

The cost of one more sector is one pack: the manifest, the extra entities and screens, the terminology map, the seed, the receipt layout, the report pack, the landing copy and the ten task briefs. The engine does not change. If a new sector needs an engine change, the change goes into the engine once and every existing pack keeps working (that is the regression test: the sector suite runs the whole catalogue after any engine change).

Estimated effort per sector pack after the engine is stable: 6 to 12 days for a sector with new modules (appointments, prescriptions, tables), 2 to 4 days for a sector that only configures existing modules (a variant of retail). The estimate is a plan, not a promise.
