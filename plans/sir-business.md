# PLAN: SIR Business (merged, 2026-11-12) - one site, every sector, free trial then subscription

> Status: this file is the single merged plan. It replaces the 2026-11-10 "Previous plan" in full (old version kept in git history). Sources merged: `PRODUCT_DIRECTION_2026-11-12.md` section 3 (the vision, owner, 2026-11-12), `PROJECT_MERGE_RECORD.md` rows 13-24 (SIR Restaurant days 13-14; SIR Market/Library/Pharmacy days 16-23; ideas 12, 19, 20: HR attendance, auto-reorder, B2B ordering), `ops/inventory/SIR-Restaurant.md`, `ops/inventory/SIR-Business-Library-Market-Pharmacy.md` (2026-10-29 scout scans), the old plan on disk (2026-11-10, archived in git), and the HER/checkout/platform laws in `D:/Projects/AGENTS.md`, `standard/23-premium-code-bar.md`, `standard/OWNER_DEFAULTS.md`, `plans/SHARED_PLATFORM_KIT.md`. Competitor evidence lives in `ops/competitors/sir-business.md` (r53, 2026-11-12). Section numbers follow the old plan so cross-references still resolve.

Version: 1.0.0 (never bump while under development). Not built yet. Nothing in this file is called working, live or shipped until a reviewer verifies it end to end.

## 1. The promise (owner vision, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` section 3)

A business owner signs in, chooses the kind of business - restaurant, pharmacy, library, market and every other sector worth supporting - sets up and configures everything for that business, runs it for free, then subscribes. One owner can add several businesses; each business has its own team and workers, roles and permissions, and a complete management system suited to its sector (inventory, orders, staff, schedules, finance, customers, reports), all connected. We (the company) hold the data about businesses, employees and usage with strict privacy. The old modes (Restaurant, Market, Library, Pharmacy) become sector templates of this one product.

One line for the store and the landing page (Arabic first):
"شركة واحدة، كل أنواع النشاط. سجّل، اختر نوع نشاطك، واظبط كل حاجة في دقائق. فضي الأول، والدفع لما تبقى جاهز تكبر."
English: "One site, every kind of business. Sign up, pick your sector, set it up in minutes. Free first, pay when you grow."

## 2. The flow (sign up → sector → setup → trial → subscription)

Premium Apple-level quality, Arabic and English, all platforms. Two hard design laws:

1. **Linear setup wizard, next-only**: the guided setup is a stepper where future steps are not clickable until the current step is validated. No skipping, no dead ends, no surprise forms. Steps: account → business → sector → branch → team → first week plan → done. Each step validates (e.g. branch needs a name, city and currency; first week plan needs at least one opening-questions answer) before the next unlocks with a spring animation. Back is always allowed; lateral jumps only to validated steps.
2. **Every screen has five states**: idle, loading skeleton, empty with one action, error with retry, populated (L34). RTL-first logical CSS, bidi detection on inputs (L8/L21), 44px targets, 320-1920px, light/dark/system/high contrast, spring motion (transform/opacity only).

Flow in detail:

1. **Sign up** (`/signup`): email + password or Google (Firebase Auth) and phone OTP (Egyptian numbers). Language auto-detected from locale (Arabic default for ar-*), currency auto-detected (EGP default, USD override in settings; L22). No card required. Account created → `organizations/{orgId}` with `role: owner` claim set server-side.
2. **Choose your business type** (`/onboarding/sector`): full sector catalogue (section 4) as a searchable, grouped grid of sector cards with real icons (no stock illustrations). Selecting a sector is reversible at this step only. Each sector card shows: what it is, 3 sample "first week" checklist items, the modules it will enable. Choosing does three things at once: creates `businesses/{businessId}`, writes the template key (e.g. `restaurant`), and seeds sector defaults (units, roles, sample floor plan/menu/catalog layout with neutral empty states, never fake data shown as real).
3. **Guided setup & configuration** (`/onboarding/setup/:businessId`): linear stepper, future steps disabled until validated:
   - Step 1 Business basics: name, sector, branch name and address, city, phone, currency, timezone, working hours.
   - Step 2 Identity: logo (optional, upload or initials), receipt header, invoice language (ar/en), tax identifiers (VAT/ETA registration if any, marked optional, stored encrypted).
   - Step 3 Template assembly: pick template modules to enable (suggested set pre-selected; all togglable but never half-configured - disabled modules are hidden, not shown broken).
   - Step 4 Your team: add workers by name + phone or email; assign a role template (owner/manager/cashier/staff + sector-specific, e.g. pharmacist, kitchen, waiter, librarian, stylist). Invites are links; roles are editable later.
   - Step 5 Catalog: import products/services (CSV upload, or scan barcodes, or sector starter catalog: Egyptian grocery EAN seeds, Egyptian drug DB later licensed, library ISBN list - each seed marked "review before going live"), or add manually with five states.
   - Step 6 First week plan: auto-generated checklist from the sector (e.g. restaurant: set tables + KDS test, print a test receipt, add suppliers, set tax rate; pharmacy: FEFO rules, controlled-drug log acknowledgment, pharmacist license number captured, drug interaction data source noted as pending).
   - Step 7 Review & finish: summary of everything set; the business is created in trial mode; redirect to the dashboard with a "You are on trial" banner (days left chip). Back-navigation to edit any step is free; leaving mid-wizard saves a draft (resume banner on next sign-in).
4. **Free trial** (30 days, no card): full Pro capabilities (all sector modules, all seats up to 15, AI metered per fair-use), usage counter, gentle day-20 and day-27 nudges, Telegram notification (opt-in). At day 30 the business moves to the fair free tier if no subscription is added; no data is ever locked hostage: export stays available.
5. **Subscription** (`/settings/billing`): per business plus per seat (section 7). Paymob + Fawry (Egypt) and Stripe/card (international) behind server-side `signed-webhook` + `billing-fallback` (`SHARED_PLATFORM_KIT`): license state cached with a 14-day grace period so a shop never gets locked out mid-service. Annual billing = 2 months free. Any business can be cancelled anytime; invoices in EGP and USD; Paymob test mode in code, production keys are owner steps.
6. **Multi-business**: owner adds more businesses from the same account (`+ New business` in the switcher). Each business: own branch(es), team, catalog, subscription (first business free tier applies only to the oldest business; additional businesses get 50% off base price), own receipts, reports, notifications, Telegram link. One owner bill groups them.

Owner-only analytics page (for the company, not customers): `/owner` on the web portal, server-verified custom claim `company_owner`, IP-session allowlist optional, every view audit-logged. Metrics: businesses by sector and trial cohort, activation (first sale done), trial→paid conversion, MRR (EGP/USD), churn, DAU/WAU per business, error rate, sync failures, support volume, per-business health (setup completed, catalog size, sales in 30d). No customer PII content beyond aggregates; drill-down stops at business level, never at employee name or sale detail, unless the owner invokes a documented break-glass panel that is audit-logged with reason and auto-expires after 30 minutes.

## 3. Names and IDs

| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Business` (Desktop kit: `Desktop/SIR Projects/SIR Business`) |
| GitHub (private) | `sirahmed8/sir-business` (exists, keep) |
| Firebase project | `sir-business` (create at M0 with `firebase projects:create sir-business --non-interactive`, Spark plan; region `me-central1` Doha if available, else `europe-west1`; record in `.sir/CHECKPOINT.md`) |
| Domain | `sirbusiness.app` candidates (or an `.eg` name, owner checks price and `.eg` rules); until then `sir-business.web.app` and Vercel `sir-business.vercel.app` |
| Stack (now, dual hosting) | One TypeScript codebase. `apps/web` Next.js 15+ App Router (marketing + app), deployed to **Firebase App Hosting** (or static export on Firebase Hosting) AND **Vercel** (same build, same env vars on both, curl-checked twice). Server-side ops (AI proxy, billing webhooks, ETA/ZATCA signing, owner analytics API) as Next.js Route Handlers on Vercel and as Firebase Cloud Functions later (Blaze). Firestore data plane on Spark; Cloud Storage for receipts/logos. PWA-first; Capacitor for Android/iOS; Electron for Windows later. |
| Stack (shared core) | `packages/core`: tenancy, RBAC, products/inventory (FEFO), sales/orders/POS, money (integer piasters), sync queue, sector templates, notifications. `packages/ui`: design system (tokens, springs, five-state primitives). |
| Version | 1.0.0 always; no bumps while under development |
| Money | Currency auto-detect from locale/IP with manual override; EGP and USD tables in section 7; `SHARED_PLATFORM_KIT` `billing-fallback` for license caching with grace |
| Telegram | One bot `@SIRBusinessBot` (BOT_ARCHITECTURE): owner links their account (`/start` with a one-time code), receives per-business digests and alerts; never a bot per user |

## 4. Sector catalogue (41 sector packs; depth pass 2026-11-12)

Every sector ships as a specialised pack on the shared engine: its own data model, screens, workflows, reports, onboarding, templates, terminology, sector integrations and landing page. The final list, the reasons for every add/split/rename, the out-of-scope decisions and the build order are authoritative in `plans/business-sectors/_INDEX.md`; the engine contract is `plans/business-sectors/_ENGINE.md`; one plan per sector lives in `plans/business-sectors/<slug>.md`; one tasks file per sector lives in `ops/briefs/business-<slug>-tasks.md`; the machine-readable source is `plans/business-sectors/_data/<slug>.json` rendered by `scripts/build_business_sectors.py`.

The tables below are the grouped launch view from the r53 pass. Where a row was renamed, split or replaced by the 41-pack catalogue, `_INDEX.md` wins. Examples: the r53 "market / supermarket" row is now `supermarket` plus `grocery-shop`; "library and bookstore" is now `bookstore` plus `library`; `stationery-gifts`, `school-shop`, `private-school-nursery`, `training-center`, `pharmacy-chain`, `optical-shop`, `pet-shop`, `furniture-carpentry`, `florist`, `print-shop`, `factory-workshop` and `car-wash` are explicit packs, not generic retail/service labels.

Launch means: pack selectable in onboarding, catalog seed applied, POS usable, reports live. Nothing is faked: unsupported features inside a pack honestly show "on the way" instead of a half-template.

Groups and regulation risks (Egypt unless noted):

### 4.1 Food and beverage

| # | Sector (ar) | Base template | Modules it needs (in addition to the common engine) | Regulation and data risks |
|---|---|---|---|---|
| 1 | Restaurant (مطعم) | restaurant | POS table service + floor plan, KDS, waiter ordering, kiosk, QR menu, delivery aggregator sync, recipe cost engine, portions/FEFO, Z-report | Food safety license (Ministry of Health / local authority), staff health certificates, ETA e-receipt for B2C, ETA e-invoice for B2B catering; no patient-type data; alcohol license if any (flagged, default off) |
| 2 | Café (كافيه) | restaurant | Same engine minus full-service flow; focus on quick service, tabs, happy hour pricing | Same as restaurant; hookah/shisha venue license where applicable |
| 3 | Bakery (مخبز / حلواني) | restaurant + retail mix | Weight-priced POS (kg), production batches, day-old discount rules, hot/cold catalog | Food safety; scale certification (consumer protection); ETA e-receipt |
| 4 | Dessert and ice cream (حلويات وأيس كريم) | restaurant + retail | Flavor matrix (variants), marble-slab style assembly notes, delivery promo bundles | Food safety; allergens labeling for nuts/dairy (consumer protection) |
| 5 | Juice and beverage quick service (عصائر ومشروبات) | restaurant | Modifier-heavy POS (sizes, extras), daily fresh prep checklist | Food safety; minimal license beyond food code |
| 6 | Butchery and fresh grocery (ملحمة وخضار) | market + fefo | Weight POS, FEFO batches with expiry (meat/dairy), fridge list, supplier price lists | Food safety (cold chain); expiry logging; ETA e-receipt |

### 4.2 Health and beauty

| # | Sector (ar) | Base template | Modules it needs | Regulation and data risks |
|---|---|---|---|---|
| 7 | Pharmacy (صيدلية) | pharmacy | FEFO expiry radar, DDI drug-interaction alerts, controlled-drug log (append-only), patient profiles with chronic conditions (encrypted), insurance claims later, suppliers | Egyptian Ministry of Health licensing of the pharmacy and its pharmacist of record; controlled substances (Schedule drugs) need append-only log and strict access; patient health data is special-category: encrypt, no analytics, no AI prompts with patient rows, PDPL + medical license obligations; drug data must come from a licensed source or be labeled "(unsourced, verify)"; fake clinical answers are a patient-safety risk and are banned |
| 8 | General clinic (عيادة) | clinic | Appointments, patient records (visit notes), intake forms, prescriptions print (not eRx), lab/imaging order tracking, reminders | MoH clinic license; patient data special-category (encrypt, export/delete on request, no ad targeting); not a medical device: no diagnosis claims, DDI/interactions only pharmacy side |
| 9 | Dental clinic (عيادة أسنان) | clinic + dental | All clinic modules + treatment plans, tooth chart, staged payments (deposit + installments), follow-up reminders | MoH dental license; patient records (images, charting) encrypted and isolated; same no-diagnosis rule; consent for photos (portraits) required |
| 10 | Gym and fitness (جيم) | service | Memberships, check-in attendance, freeze/resume, class schedule, trainer commissions, body metrics (optional, sensitive) | Labor law; injury waivers; member photos/metrics are personal data (consent + deletion); no medical claims |
| 11 | Salon (صالون حريمي) | service | Booking calendar, stylist commissions, multi-chair assignment, service bundles, no-show fees, retail add-on shelf | Licensing per governorate (health/cosmetic); client photos (before/after) need consent; staff tool hygiene not software scope |
| 12 | Barber / barbershop (حلاقة رجالي) | service | Same as salon minus some retail; walk-in queue, token/ticket display | Same licensing; low data risk |
| 13 | Spa and wellness (سبا وعناية) | service | All service modules + package sales (10-session bundles), expiry of packages, private room scheduling | Licensing; client preferences (sensitivities) are personal data |
| 14 | Veterinary clinic (عيادة بيطرية) | clinic + shop | Appointments, pet records (vaccinations), pet food/drug sales with FEFO, reminders | Veterinary syndicate license; pet records low sensitivity but owner PII normal; controlled vet drugs (some) tracked like pharmacy log optional |

### 4.3 Retail and commerce

| # | Sector (ar) | Base template | Modules it needs | Regulation and data risks |
|---|---|---|---|---|
| 15 | Market / supermarket (سوبر ماركت) | market | FEFO inventory, barcode POS, scale integration, procurement with reorder points, perishables, loyalty, customer 360, weighing-label printing | Food safety; ETA e-receipt B2C and e-invoice B2B (wholesale to restaurants); shrink-wrap pricing accuracy (consumer protection); cash handling controls |
| 16 | Retail clothing and fashion (ملابس) | retail | Size/color matrix, variants, seasonal collections, markdowns, exchange rules, layaway later | Standard retail; ETA e-receipt; textile labeling (consumer protection) |
| 17 | Electronics and mobile shop (إلكترونيات وموبايلات) | retail | IMEI-tracked units (each phone its own serial, warranty dates), service/repair intake, trade-in pricing, carrier bundles | Serial-number tracking recommended; warranty law; VAT on electronics; IMEI is equipment data not personal data, but receipts carry buyer phone if captured |
| 18 | Hardware and building materials (عدد ومواد بناء) | market + b2b | Bulk price lists, contractor accounts with credit/postpay, delivery scheduling, BOM-ish quotes, credit ledger (older Ear) | B2B credit risk (not legal); VAT; ETA e-invoice for B2B |
| 19 | Wholesale and cash-and-carry (جملة) | market + b2b | Tiered pricing, large-quantity discounts, receivables/credit book, route planning later, B2B invoicing (ETA) | ETA e-invoice mandatory B2B; credit exposure tracked in-app, legal terms owner side |
| 20 | School and nursery shop (مقصف وحضانات) | market + service | Campus catalog (uniforms, books, supplies), student wallet top-ups, parent billing, term subscriptions | If linked to a school: student data (name, class) is child data - keep minimal, parent consent, never marketing to children; nursery MoH/MoE licensing |
| 21 | Gift and stationery (هدايا ومكتبة) | retail | Gift wrap flows, greeting-card add-ons, engraving/personalization orders, event management later | Standard retail; low risk |

### 4.4 Services

| # | Sector (ar) | Base template | Modules it needs | Regulation and data risks |
|---|---|---|---|---|
| 22 | Car service and garage (صيانة سيارات / قطع غيار) | garage | Vehicle-in/job-card, parts inventory with SKU, labor estimates + actual, technician assignments, checklists (oil/brakes), insurance claims later | Vehicle data not sensitive; mechanic license; ETA e-receipt/e-invoice; parts provenance (genuine vs counterfeit) honesty rule in UI copy |
| 23 | Laundry and dry cleaning (مغسلة) | service | Item intake with tag/barcode photo, per-item and per-kg pricing, express tiers, unclaimed reminder, partner pickups | Low; dry-cleaning chemicals are environmental/waste regulation, not software; data minimal |
| 24 | Repair shop - electronics/appliances/phone (صيانة) | service + ticket | Ticket-based intake (device, complaint, quote before work, customer approval via SMS/link), spare parts stock, turnaround tracking | Device data may include personal data on devices (photos etc.) - policy: never browse device content, only repair the fault; consent form recommended |
| 25 | Photography studio (استوديو تصوير) | service + project | Session booking, shot lists, album/print orders, watermarked galleries (expiring links), retouching orders | Portrait/privacy consent; client photos special: encrypt storage, expiring links, deletion honors; no biometric categorization ever |
| 26 | Delivery and courier (ديليفري / شركات شحن) | delivery | Order intake, driver assignment + live map (later), proof of delivery (photo/signature),COD reconciliation, zone pricing | Transport permits (governorate); driver ID and vehicle data normal employment data; COD is cash-control problem (two-person rule logs) |

### 4.5 Hospitality and real estate

| # | Sector (ar) | Base template | Modules it needs | Regulation and data risks |
|---|---|---|---|---|
| 27 | Hotel and guest house (فندق / غرفة مفروشة) | hospitality | Room calendar + housekeeping board, reservation window, deposits and refund rules, invoice per stay, city tax handling (tourism) | Tourism ministry (MT) licensing; fire safety certs; guest ID copies (passport) are sensitive - encrypt or store only last-4 + country; PDPL |
| 28 | Real estate office (مكتب عقاري) | realestate | Property listings (photos, price, status), lead pipeline, appointment calendar, contracts + commission calc, document vault per deal | Marketing law (ads truthfulness); deposit/commission disputes contractual; agent licenses (REGA/HECPSYNC not in Egypt - Egypt: real estate brokerage license law); no data-selling |

### 4.6 Education and community

| # | Sector (ar) | Base template | Modules it needs | Regulation and data risks |
|---|---|---|---|---|
| 29 | Library and bookstore (مكتبة) | library | Catalog (ISBN) + OPAC public page, memberships, borrowing + deposits, study-desk booking, holds queue, citation generator | Lending deposits; child members (under 18) - parent consent, minimal data; unlicensed photocopy disclaimer for translations/rights |
| 30 | Tutoring center (سنتر دروس) | education | Groups/cohorts, attendance, fee collection (term), teacher payout share, progress reports to parents, waitlist | Education ministry recognition not required for private tutoring; child data - parental consent, no ad targeting, deletion on request |

Honestly out of scope at launch (noted, not hidden): placing-online-only ventures (pure e-commerce, affiliate), manufacturing/production modules (heavy ERP, later), churches/mosques/charities (donations module later if a real user asks), banks/microfinance (regulated lending, never without counsel), gambling/points-as-currency (legal in Egypt; loyalty points are never exchangeable for cash). ETA e-invoice/e-receipt claims and ZATCA stay "pending spec reading + owner onboarding" until signed off by the accountants/lawyer named in section 15.

## 5. The common engine every sector reuses

One `packages/core` tenanted platform. Every sector template is a thin, typed layer over it; every line of code here is built once and paid for once. Interfaces are stable enough for AI scaffolding of new sectors later.

1. **Tenant and business entity**: Firestore hierarchy `organizations` (owner account) → `businesses` (one owner, several businesses) → `branches` (optional, default 1) → `memberships` (user ↔ business with role). Every document carries `orgId`, `businessId` (and `branchId` where relevant); security rules deny cross-tenant reads/writes by default (emulator tests required, see M3). Custom claims on the Firebase token: `role` per business via membership docs, `company_owner` for the analytics page. No tenant uses another tenant's data, ever - the Firestore rules are the boundary, not client code.
2. **Team and workers**: roles per business: `owner`, `manager`, `cashier`, `staff` + sector-specific (`pharmacist`, `technician`, `waiter`, `librarian`, `stylist`, `trainer`, `driver`, `agent`). Granular permissions (pos.sell, inventory.read, reports.finance, team.manage, settings.billing, devices.manage, audit.read). Owner can delegate: manager gets everything except billing/export. Staff invite links with expiry; deactivation instant (JWT revoked by claim removal on next refresh + security rules check).
3. **Shifts and attendance**: shift open/close with counted cash, float, expected vs actual (over/short flagged), drop handover across shifts; attendance clock in/out (PIN on POS, QR badge, or web), breaks, late/absent rules, weekly summary; payroll export CSV (staffPayrollService ported, not payment-in-app at v1).
4. **Inventory and purchasing**: items with variants/units, stock per branch, low-stock and reorder-point alerts, FEFO batches (manufacturing/expiry from pharmacy), cycle counts, waste log, transfers between branches (with in-transit state), purchase orders (supplier, draft/sent/received/partial), goods receipt with discrepancies, purchase invoices later with ETA sign. Auto-reorder suggestion from 30-day velocity (usage only, opt-in).
5. **Sales and orders and POS**: fast cart (barcode, SKU search, favorites grid, quick-keys), discounts (line/bill, max by role), taxes (VAT included/excluded), mixed payments (cash, cards via Paymob, wallets, InstaPay QR at counter, credit book for B2B), held/parked orders, kitchen display fire (`kds.fire` for restaurant template), refunds/voids with reason + audit log + manager override PIN, receipts print via ESC/POS bridge or browser print, reprint from stored sale (money math in integer piasters; rounding tests).
6. **Customers and loyalty**: customer profiles (name, phone, WhatsApp opt-in flag), purchase history per business, points/tiers (visit-based and spend-based), coupons, memberships for service sectors (package sessions), credit/receivables ledger for B2B (wholesale, hardware, garage accounts), privacy: export/delete on request.
7. **Finance and expenses**: cash and bank ledger per business, petty cash, expenses with receipt photo + category, supplier payments, Z-report per shift and per day (total sales, taxes, discounts, over/short, open credit), profit & loss simple view, VAT summary for the accountant, bank reconciliation CSV import later. Not full accounting (Zoho/Daftra stay for books) - we do the shop's operating P&L and hand off exports cleanly.
8. **Suppliers**: supplier 360 (contact, payment terms, price list history, last order, average lead time), price comparison across suppliers, returns/defects log; purchase invoices emailed watchers later.
9. **Reports and dashboards**: sales by hour/day/week/month, by item/category, by employee, by payment method; inventory valuation; low stock and expiry expiring soon; loyalty cohort; cash reconciliation report; owner "today vs yesterday" card; scheduled weekly Telegram digest (opt-in); export CSV/PDF.
10. **Notifications**: one SIR Business Telegram bot (user links own account, BOT_ARCHITECTURE): digest per business (sales, shifts open/close variance, low stock, new review on Google later), alerts (license about to expire, failed sync). In-app notification center, email for receipts/invoices, WhatsApp deep links for customer messaging (owner's own account, read-only phone API - never scraped).
11. **Offline mode**: POS PWA keeps selling with zero connectivity: local IndexedDB/fast cache of catalog + cart + queued mutations; Firestore offline persistence as the sync layer; conflict rule (documented in ADR): server-order timestamps win per field for quantities where both changed; money values are never merged - a sale is one atomic local-then-server commit with idempotency keys (`lib/idempotency.ts` pattern ported), so double-submits and retries never double-charge; receipt reprint works offline from the queued sale; sync status chip always visible (synced/syncing/offline 3 pending).
12. **Hardware**: hardware abstraction (`PerDevice`): ESC/POS printers (thermal, cut command), barcode scanners (HID keyboard emulation, wedge mode), cash drawers (kick on sale), kitchen displays, scales (weighed items), customer display (cart on second screen), kiosk self-order. Every device behind an interface with a simulated driver for CI + a golden-file test suite; real-device tests are owner steps with real hardware.
13. **Kiosk and customer-facing**: tablet kiosk mode (fullscreen, no browser chrome, attract loop showing neutral branded slides - no fake customers), order tracking screen for customers, QR menu for restaurant template, self-checkout later. Customer display: live cart, totals, thank-you with points earned.
14. **AI copilot**: "اسأل نشاطك" / "Ask your business": answers computed from the business's own Firestore (via allowed query whitelist), the model only phrases the numbers (numeric-accuracy eval gate: answer must equal the SQL/Firestore result, eval set of 50 Q/A, 100% gate before shipping; free tier cap 100 questions/mo, owner unmetered). Support assistant grounded in `docs/help`. Chain: `ai-proxy` from SHARED_PLATFORM_KIT (Gemini flash-lite → flash → any Gemini → OpenRouter free → local; one key per project on our own GCP project). AI keys never in the client.
15. **Security and compliance plumbing**: encrypted field set for health data (pharmacy/clinic) and tax IDs (AES-GCM with per-tenant wrapped key, KMS later), audit log (who/what/when, immutable append), export (JSON + CSV per business: products, sales 90d, customers, expenses - self-serve in settings), deletion (soft delete → 30-day grace → purge; backups 90 days then gone), per-tenant isolation tests, secrets only in ignored files/env vars, Egyptian PDPL + consumer law pack in `legal-pack`, ETA/ZATCA e-receipt pipeline (spec-gated).
16. **Owner-only analytics** (`/owner`): see section 2 and section 9; server-verified `company_owner` claim; aggregates only; audit-logged views; no PII drill-down without break-glass.

## 6. Sector templates and the legacy feature map

The four legacy apps become templates 1-4. Ported means: code rewritten against `packages/core` (never copy-pasted), mock data removed, auth/billing/AI re-wired to the platform. Nothing from legacy ships with its flaws: no hard-coded PINs/emails, no client-side keys, no fake payments, no in-memory DB fallback, no canned AI answers, no false legal claims (SOC 2 / ISO 27001 were claimed without evidence), no kill switch (remote vendor lockout), no "anti-piracy" gimmicks.

Verdicts: **port** = rewrite into `packages/core` or template; **drop** = gone for good (reason in the row); **defer** = after M6 with legal/licensing gates.

### 6.1 Restaurant template (from legacy `SIR Restaurant`, repo `restaurant-os`, HEAD 17e6d84, read-only)

| Legacy feature (source) | Lands in | Verdict |
|---|---|---|
| PosModule, PosStore, tableOrderService (`components/modules/PosModule.tsx`, `stores/usePosStore.ts`, `services/tableOrderService.ts`) | `packages/core` POS + restaurant template | port (integer piasters, idempotency, offline queue) |
| KdsModule, useKdsStore (`KdsModule.tsx`, `useKdsStore.ts`) | restaurant template | port |
| FloorPlanModule + types/floorplan (`FloorPlanModule.tsx`, `types/floorplan.ts`) | restaurant template | port |
| WaiterModule (`WaiterModule.tsx`) | restaurant template | port (order from phone/tablet in the hall) |
| KioskModule (`KioskModule.tsx`) | core kiosk | port |
| TableGuestPortalModule + CustomerPortalView (`TableGuestPortalModule.tsx`, `components/customer/CustomerPortalView.tsx`) | restaurant template | port |
| DeliveryHubModule + deliveryAggregatorService (`DeliveryHubModule.tsx`, `services/deliveryAggregatorService.ts`, `types/delivery.ts`) | restaurant template | port (aggregator webhooks server-side later) |
| RecipeStudioModule + recipeService + recipeStudioService + marketingRecipe (`RecipeStudioModule.tsx`, `services/recipeService.ts`, `services/recipeStudioService.ts`, `__tests__/orderRecipe.test.ts`) | restaurant template (food costing) | port |
| InventoryModule + useInventoryStore + ProcurementModule + procurementService (`InventoryModule.tsx`, `useInventoryStore.ts`, `components/modules/ProcurementModule.tsx`, `services/procurementService.ts`, `types/procurement.ts`) | `packages/core` inventory | port (FEFO added from market) |
| ShiftModule + useShiftStore + shiftService + staffPayrollService + StaffModule + useStaffStore (`ShiftModule.tsx`, `shiftService.ts`, `staffPayrollService.ts`, `useStaffStore.ts`) | `packages/core` shifts/attendance | port |
| CustomersModule + customer360Service (`CustomersModule.tsx`, `customer360Service.ts`) | `packages/core` customers | port |
| ReportsModule (`ReportsModule.tsx`) | `packages/core` reports | port |
| SuperAdminModule + useSuperAdminStore + types/superAdmin (`SuperAdminModule.tsx`, `useSuperAdminStore.ts`) | replaced by owner-only analytics (section 8) + per-business settings | port as settings only; company analytics new-built |
| SettingsModule + useSystemStore (`SettingsModule.tsx`, `useSystemStore.ts`) | settings screens | port |
| OwnerAppPortal + OwnerControlBar + SubscriptionUpgradeModal + subscription.ts + lib/subscription + licenseEngine + subscription gating tests (`components/owner/OwnerAppPortal.tsx`, `components/ui/OwnerControlBar.tsx`, `components/subscription/SubscriptionUpgradeModal.tsx`, `services/licenseEngine.ts`, `lib/subscription.ts`) | billing via SHARED_PLATFORM_KIT `signed-webhook` + `billing-fallback` | port; kill-switch mechanics dropped |
| Security: killSwitch, canaryToken, clockGuard, hardwareDna, licenseValidator, security/index (`services/security/*.ts`) | nothing | drop (remote client lockout + hardware DNA are anti-patterns; replaced by server-verified license with grace and audited legal flow) |
| AI: AiCopilotModule + AiVisionModule + aiRouter + visionScannerService + smartRoutingService + AIStore + GlobalAIChatbot (`components/*/Ai*.tsx`, `services/aiRouter.ts`, `visionScannerService.ts`, `smartRoutingService.ts`, `stores/useAIStore.ts`, `components/ui/GlobalAIChatbot.tsx`) | AI copilot via `ai-proxy` chain (section 14) | port architecture; rebuild against proxy; client keys removed |
| OnlineStoreModule (`OnlineStoreModule.tsx`) | online ordering (web/QR) | port (later, after core POS green) |
| MarketingModule + marketingService + useMarketingStore + marketingRecipe test (`MarketingModule.tsx`, `marketingService.ts`, `useMarketingStore.ts`) | notifications + coupons module later | defer |
| HardwareHubModule + printerService + soundEngine + voiceAnnouncerService + IntercomModule (`HardwareHubModule.tsx`, `printerService.ts`, `soundEngine.ts`, `voiceAnnouncerService.ts`, `IntercomModule.tsx`) | hardware layer (section 5.12) | port printer/drawer; sounds optional; intercom drop |
| ZatcaComplianceModule + zatcaPhase2Service + ZatcaQr test (`ZatcaComplianceModule.tsx`, `services/zatcaPhase2Service.ts`, `types/zatca.ts`) | ETA/ZATCA pipeline | defer (spec-gated, section 15) |
| WhatsAppBotService (`services/whatsappBotService.ts`) | dropped for v1; Telegram bot (section 5.10) instead | drop |
| whatsappBotService tests, tableGuestPortal tests, onboardingWizard (`__tests__/*.test.ts`, onboarding wizard) | test strategy ported | port intent (tests re-created around new code) |
| Onboarding: onboardingService (`services/onboardingService.ts`) | linear wizard (section 2) | rebuild (stepper rule is new) |
| Auth: BusinessAuthScreen, LockScreen, TenantAuthModal, WelcomeLandingScreen (`components/auth/*`) | auth scaffold (Google + phone OTP + PIN for staff) | rebuild |
| Layout: AppShell, Header, Sidebar, QuickSearchModal, ErrorBoundary, NotFoundPage, ServerErrorPage (`components/layout/*`, `components/ui/ErrorBoundary.tsx`) | `packages/ui` with five-state primitives | rebuild |
| Legal: LegalModal, CookieConsentBanner, FormConsentCheckbox (`components/legal/*`) | `legal-pack` (shared kit) | port |
| Stores: useMenuStore, useOrderStore, useTableStore, useSystemStore (`stores/*`) | core kitchen/table/order stores | port semantics |
| db/schema.ts, db/mock-data.ts, db/index.ts, lib/* (crypto, ids, logger, money, onlineSync, rbac, sanitize, idempotency, validation, consent, subscription) | `packages/core` modules | money/ids/idempotency/validation/rbac port; crypto re-backed by libsodium/KMS; mock-data dropped; storage.ts dropped (no localStorage sessions) |
| weatherService, cloudinaryService, eventBus, smartRoutingService (`services/*`) | - | drop (unused/weather gimmick); cloudinary → Firebase Storage signed uploads |
| Electron/vite packaging, unsigned NSIS | Windows app via `plans/WINDOWS_APP_STANDARD.md` | defer to M5-M6 (web first) |

### 6.2 Market template (from legacy `SIR Market`, master dfd49a9)

| Legacy feature (source) | Lands in | Verdict |
|---|---|---|
| POSOperatorView + POSKeypad + cart contexts (`renderer/views/POSOperatorView.tsx`, `components/ui/POSKeypad.tsx`, `context/CartContext.tsx`) | `packages/core` POS | port (presentation rebuilt; cart logic remade in core) |
| FEFOInventoryView + fefoInventoryService (`FEFOInventoryView.tsx`, `services/fefoInventoryService.ts`) | core inventory | port |
| ProcurementView + procurementService + PurchaseOrder (`ProcurementView.tsx`, `services/procurementService.ts`) | core purchasing | port |
| Customer360View + customer360Service (`Customer360View.tsx`, `services/customer360Service.ts`) | core customers | port |
| Staff360View + staff360Service (`Staff360View.tsx`, `services/staff360Service.ts`) | core team | port |
| SuperAdminView + superAdminService (116 KB monolith → rebuilt) | settings + `/owner` | rebuild small |
| ShiftManagementView + shiftManagementService (`ShiftManagementView.tsx`, `shiftManagementService.ts`) | core shifts | port |
| OnlineStoreView + ecommerceService + OrderTrackerView (`OnlineStoreView.tsx`, `ecommerceService.ts`, `renderer/components/OrderTrackerView.tsx`, `views/OrderTrackerView.tsx`) | online ordering (web) | defer (after core POS) |
| AIRouterView + dualAIRouter + voicePOSParser + demandForecastEngine + marketBasketEngine (`AIRouterView.tsx`, `services/dualAIRouter.ts`, `voicePOSParser.ts`, `demandForecastEngine.ts`, `marketBasketEngine.ts`) | AI proxy + analytics later | defer AI; basket/demand defer to M6+ |
| ComplianceView + egyptETASigner + saudiZATCAEngine + subscriptionGatingService + universalPlatform (`ComplianceView.tsx`, `services/egyptETASigner.ts`, `saudiZATCAEngine.ts`, `subscriptionGatingService.ts`, `universalPlatform.ts`) | ETA/ZATCA pipeline (spec-gated) + kit billing | ETA signer port behind server; ZATCA defer |
| Hardware: HardwareManagementView + barcodeScanner + escposPrinter + scaleDriver + labelPrinter + hardwareMockAdapter + priceBarcodeDecoder + main/barcodeSerialManager + scaleSerialManager + hardwareAutoConnect + trayManager + updateManager (`renderer/views/HardwareManagementView.tsx`, `services/*`, `main/*`, `preload/index.ts`) | hardware layer | port native-bridge later; web POS uses HID wedge + print API |
| Security: antiPiracyShield (preset PINs, MOCK_KEY PEM) | nothing | drop (documented red flags; replaced by kit billing-fallback) |
| Auth: StoreAuthLanding, StoreLoginModal, LockScreen, context/AuthContext (hard-coded owner emails) | auth scaffold | rebuild |
| Onboarding: OnboardingWizardModal, PersonalizedOnboardingModal (`components/OnboardingWizardModal.tsx`, `PersonalizedOnboardingModal.tsx`) | linear wizard | rebuild (stepper law) |
| db/schema.ts + migrator + connection (in-memory fallback) | Firestore + local IndexedDB queue | rebuild (fail loudly, never silent in-memory) |
| services/logger, universalPlatform, whatsappMarketingService | kit logger; drop whatsapp | drop marketing bot |
| Data egress surface: 53 test files / ~1,367 cases unverified | test suite rebuilt | port intent |

### 6.3 Library template (from legacy `SIR Library`, main, 91 files)

| Legacy feature (source) | Lands in | Verdict |
|---|---|---|
| CatalogModule + useLibraryStore + citationGenerator (`CatalogModule.tsx`, `stores/useLibraryStore.ts`, `domain/citationGenerator.ts`, `types/library.ts`) | library template | port |
| BorrowingModule + useBorrowingStore (`BorrowingModule.tsx`, `stores/useBorrowingStore.ts`, `__tests__/borrowingRules.test.ts`) | library template | port |
| MembersModule + useMemberStore (`MembersModule.tsx`, `stores/useMemberStore.ts`) | library template | port |
| StudySpaceModule + useStudySpaceStore (`StudySpaceModule.tsx`, `stores/useStudySpaceStore.ts`) | library template (desk booking) | port |
| ReaderPortalModule (`ReaderPortalModule.tsx`, public OPAC + holds) | library template (member portal) | port |
| PosModule + usePosStore + ReceiptPreviewModal (`PosModule.tsx`, `usePosStore.ts`, `components/ui/ReceiptPreviewModal.tsx`) | core POS | port |
| ProcurementModule (`ProcurementModule.tsx`) | core purchasing | port |
| KioskModule (`KioskModule.tsx`) | core kiosk | port |
| ShiftModule + useShiftStore (`ShiftModule.tsx`, `useShiftStore.ts`) | core shifts | port |
| ReportsModule (`ReportsModule.tsx`) | core reports | port |
| AiCopilotModule (canned, claims "GPT-4o") | AI proxy copilot | rebuild |
| OwnerAppPortal (`components/modules/OwnerAppPortal.tsx`) | owner analytics | rebuild |
| SuperAdminModule (`SuperAdminModule.tsx`) | settings | port small |
| HardwareHubModule (`HardwareHubModule.tsx`) | hardware layer | port |
| Auth: WelcomeLandingScreen, UserProfileModal ("Google login sets admin") | auth scaffold | rebuild |
| mock-data (seeder) | removed | drop |
| Legal: PRIVACY/TERMS/EULA/REFUND/COOKIE docs + modals | `legal-pack` | rebuild honest (no SOC 2 claims) |

### 6.4 Pharmacy template (from legacy `SIR Pharmacy`, main, 15 commits)

| Legacy feature (source) | Lands in | Verdict |
|---|---|---|
| PosModule + usePosStore (`PosModule.tsx`, `stores/usePosStore.ts`) | core POS | port |
| FefoModule + expiry radar (`FefoModule.tsx`, `__tests__/fefoExpiry.test.ts`, email "expiryRadar" behaviour) | core inventory | port |
| ClinicalDdiModule + useClinicalStore + drugInteractions (`ClinicalDdiModule.tsx`, `useClinicalStore.ts`, `domain/drugInteractions.ts`, `__tests__/ddiRadar.test.ts`) | pharmacy template | port algorithm; **drug data must be licensed or labeled "(unsourced, verify)"; the hand-typed 8 DDI rules stay internal test fixtures only - never presented as clinical truth** |
| ControlledDrugsModule (`ControlledDrugsModule.tsx`) | pharmacy template | port (append-only log, role-gated, audit) |
| PatientsModule + usePatientStore (`PatientsModule.tsx`, `usePatientStore.ts`) | pharmacy template | port with encryption (health data) |
| SuppliersModule (`SuppliersModule.tsx`) | core suppliers | port |
| DeliveryModule (`DeliveryModule.tsx`) | delivery module | port (v1 manual assignment) |
| KioskModule (`KioskModule.tsx`) | core kiosk | port |
| ShiftModule + useShiftStore (`ShiftModule.tsx`, `useShiftStore.ts`) | core shifts | port |
| ReportsModule (`ReportsModule.tsx`) | core reports | port |
| AiCopilotModule (invents stock answers) | AI proxy copilot | rebuild with numeric-eval gate; zero-stock test mandatory |
| OwnerAppPortal (`OwnerAppPortal.tsx`) | owner analytics | rebuild |
| SuperAdminModule (`SuperAdminModule.tsx`) | settings | port small |
| HardwareHubModule (`HardwareHubModule.tsx`, `PharmacyReceiptModal.tsx`, `DdiAlertModal.tsx`) | hardware layer + UI | port |
| Auth: UserProfileModal hard-coded admin | auth scaffold | rebuild |
| mock-data (13 medicines) | removed | drop |
| Legal (false SOC 2 claims) | `legal-pack` | rebuild honest |
| Electron devDeps missing; node_modules symlink into Restaurant | rebuilt toolchain | n/a |

**Cross-cutting legacy rulings**: fake payments (SubscriptionUpgradeModal success screens) → replaced by `signed-webhook`; fake AI → proxy + eval; client-owned AI keys → server proxy; localStorage sessions → Firebase Auth tokens; seeded mock data everywhere → removed, empty states only; unsigned installers → Windows app standard at M6; kill switches → deleted; ETA/ZATCA "implemented" claims → spec-gated and honest in the store listing until signed.

## 7. Data model and privacy

**What we hold**: business records (products, prices, sales, stock, expenses), employee records (names, phones, roles, shifts, attendance, PIN hashes - never raw PINs), usage records (which features are used, error rates), and billing metadata (plan, seats, invoices). We never hold card numbers (Paymob/Fawry tokens only) and never hold content of customer chats.

**Entities (Firestore paths)**:
`organizations/{orgId}` (owner account, plan, billing, locale) · `businesses/{businessId}` (name, sector template key, currency, tax IDs encrypted) · `organizations/{orgId}/businesses/{businessId}/branches/{branchId}` · `memberships/{membershipId}` (orgId, businessId, userId, role, invitedBy, status) · `users/{userId}` (private profile; phone/email only in private doc) · `roles` (fixed enum + sector-specific) · `products/{productId}` (sku, barcode, categoryId, unit, taxRate, costCents, priceCents, reorderPoint, fefo flag) · `batches/{batchId}` (productId, branchId, qty, expiry, supplierId) · `sales/{saleId}` (branchId, cashierId, lines[], totals in integer piasters, payment[], status, idempotencyKey, createdAt server) · `saleLines`, `payments/{paymentId}` · `shifts/{shiftId}` (open/close cash) · `attendance/{doc}` · `customers/{customerId}` (owner-consented marketing flag) · `loyaltyAccounts/{membershipId}` · `suppliers/{supplierId}` · `purchaseOrders/{poId}` · `expenses/{expenseId}` · `devices/{deviceId}` (branch, type, lastSeen, token hash) · `subscriptions/{subId}` (plan, seats, businesses, status, currentPeriodEnd, provider ids) · `auditLogs/{logId}` (append-only, who/what/when/entity) · `usageEvents/{eventId}` (feature name, businessId, count - no payloads with PII) · `notifications/{doc}`.
Indexes: branch+createdAt, business+sku, org+user, product+barcode. All IDs client-generated UUIDv7 (sortable).

**Privacy engineering**:
- Per-tenant isolation: deny-by-default security rules (`request.auth != null && isMember(businessId)`); composite rules per role; 50+ emulator assertions (user of shop A cannot read shop B's sales, staff cannot read owner-only reports, cashier cannot edit a closed sale) committed as `firestore.rules.test.ts` and run in every CI verify.
- Encryption: Firestore at rest (Google-managed) plus field-level AES-256-GCM for health data (pharmacy patients) and tax IDs, wrapped per tenant (env-held kek for v1; Cloud KMS when Blaze is enabled). Never logged, never in analytics.
- Export: self-serve in Settings → Data: full business export (JSON zip + CSV per entity); available even in grace period; scheduled emailed export later.
- Deletion: soft-delete (hidden, 30-day restore window) → purge jobs; backups retained 90 days max then destroyed; deletion propagates to sub-processors via retention contracts.
- Residency: default `me-central1` (Doha) Firestore + `europe-west1` storage bucket; PDPL-aligned; Egypt regions unavailable in Firebase today (verify at create, record in CHECKPOINT).
- Access: support staff (us) read nothing without break-glass ticket, reason and owner approval; every access audit-logged and shown to the business owner in Settings → Security → Recent access.
- Health data (pharmacy/clinic): excluded from product analytics, never in AI prompts, encrypted separately, retention capped at the license minimum (pharmacy: as long as the pharmacy license requires - configurable 5 years default, pharmacist decides; deletion request honored within the law).
- Children: tutoring/nursery/school-shop templates: parent-linked accounts only, no behavioural ads, minimal fields (name, class, guardian phone), deletion on request.
- DPA: every business gets a downloadable data-processing addendum (we are processor, they are controller of their employee/customer data); sub-processors list: Firebase/Google, Vercel (hosting), Paymob/Fawry (payments), Telegram (notifications, user opt-in), email provider. Updated before launch.
- Marketing: analytics cookies off until consent (legal-pack banner), product analytics only on our own domain, opt-out honored.

**Our own data use**: aggregate stats for the owner-only page (section 8); never sold, never shared, never used to train public models; on-device models only if local wins later; crash reports consent-based.

## 8. Owner-only analytics page (company side, `/owner`)

Route `/owner` on the web portal. Protection: `company_owner` custom claim verified in a server route (not client); session IP+UA binding; audit-logged on every view; break-glass documented in `SYSTEM.md`. Content (all real, nothing invented; empty states if zero data):
- Fleet overview: total businesses, paying vs trial, by sector (bar), by governorate (map later), new this month.
- Funnel: signed up → sector chosen → setup completed → first sale → day-7 active → trial converted; cohort curves.
- Money: MRR (EGP and USD), ARR, ARPU, expansion from additional business seats, failed payments (billing-fallback log), refunds.
- Health: median time-to-first-sale, error rate per business, sync failure rate (alert > 2%), support tickets, top 5 errors.
- Churn: monthly logo churn, reason tags (price/feature/competitor), win-back hooks status.
- Product: sector template adoption, module toggles, AI usage and eval accuracy drift, TV-monthly export.
Nothing shown here leaves the company. No employee names, no sale lines, no customer personal data - ever, unless break-glass (audited, 30-minute expiry, owner-visible counter).

## 9. Pricing (free trial first, then subscription; EGP and USD)

All figures are **proposed, 2026-11-12, unsourced until 5 pilot interviews re-price them** and must not appear in public copy before then (verify in section 18). Auto-detect currency from locale/IP with manual override (OWNER_DEFAULTS 16); EGP shown to Egyptian visitors, USD otherwise. Tax line added at invoice per local law. Owner (Ahmed) has all features free forever (his account claim `company_owner`).

| Plan | Price (EGP / month) | Price (USD / month) | Includes |
|---|---|---|---|
| **Free (forever)** | 0 | 0 | 1 business, 1 branch, 2 seats, POS + inventory + shifts + 30-day history, basic reports, offline mode, community support (docs + Telegram community). Fair: no card, no expiry, real value for a one-till shop |
| **Trial** | 0 for 30 days | 0 | Everything in Pro while trial lasts: all sector modules, up to 15 seats, AI (metered fair-use), Telegram digests. No card required; converts or downgrades with zero data loss |
| **Starter** | 299 | $9 | 1 business, 1 branch, 5 seats, 1-year history, full sector modules, exports, email support |
| **Business** | 599 | $19 | 1 business, 3 branches, 15 seats, loyalty, multi-branch, inventory transfer, 2 years history, priority support (next business day) |
| **Pro** | 1 199 | $39 | 1 business, unlimited branches, 50 seats, all modules incl. pharmacy FEFO + clinic plans, AI 500 questions/mo, dedicated Telegram support |
| Extra business | +50% of base price | +50% of base price | Up to 5 businesses per owner |
| Extra seat | +60 | $2 | Beyond included seats |
| Annual | 10 months paid, 2 free | same | Any plan |

Rationale against competitors: the r61 addendum in `ops/competitors/sir-business.md` corrects the r53 read. Foodics now publishes Egypt bundles from about EGP 2,849-3,958/mo billed annually depending on bundle and promotion; inyad publishes retail plans from EGP 599/mo and food plans from EGP 799/mo; Daftra's accounting-led plans start around EGP 489.50/mo yearly-billed per dated third-party reads; Circle is a free Arabic-first shop app; Geidea is payments-led with no public price; Loyverse still charges US$5-25/mo add-ons; Shopify POS Pro is US$89/location; Square is not Egypt-native; Odoo and Zoho remain per-user/accounting-led. Our 3-user shop pays EGP 599/mo total, not per module. Prices exclude ETA/ZATCA compliance fees (compliance is a cost to onboard your tax registration, not a paywall).

Old prices (Restaurant 450/750/1950; Market 950/2450/4900; Pharmacy Pro 999/Ent 2,499 - 2026-10-29 inventory) are history: superseded by this table; all tagged "(unsourced, verify)" in any external copy until interviews complete.

## 10. Platform matrix

| Platform | Status | Notes |
|---|---|---|
| Web PWA (Chrome/Edge/Safari) | **Now, primary** | Next.js 15 + React 19, RTL-first, offline shell, installable. Serves the cashier tablet, manager laptop, owner phone |
| Android (Capacitor) | M3 | Same codebase; POS terminals and owner phone |
| iOS (Capacitor) | M4 | Same codebase; owner phone; no App Store promise until tested |
| Windows (Electron) | M5 | `WINDOWS_APP_STANDARD.md`: real installer, Firebase sign-in, self-update, download page; only after web is stable |
| macOS / Linux | M6+ if a business asks | Same Electron; deferred honestly |
| Kiosk hardware (self-order tablet) | M5 | Locked browser profile on the PWA; BYO Android tablet |
| TV / watch / car | Skipped | No business case; skipped honestly |
| Browser extension | Skipped | No business case |
| ETA e-receipt hardware fiscalisation (BTC keyboards) | Not in v1 | Generic ESC/POS only; fiscal hardware is sector/ETA specific, researched at M2 spec read |

## 11. Architecture on Firebase plus Vercel now

Merged from the old Electron/SQLite/Cloudflare sketch and the 2026-11-12 direction (Firebase + Vercel). Honest constraints kept in view:

- **Firebase project** `sir-business` (Spark now): Auth (Google, phone OTP, email/password), Firestore (default `me-central1` verify; fallback `europe-west1`), Cloud Storage (receipts, logos) with signed URLs, FCM (push), Analytics (product analytics, consent-gated), Crashlytics via web SDK; Spark free tier (50k reads/20k writes/20k deletes per day, 1 GiB storage) covers pilot; Blaze needed for Cloud Functions billing/SMS later (owner adds a card - OWNER_ACTIONS).
- **Web**: `apps/web` Next.js 15 App Router, exported as static export where possible (marketing, docs) + dynamic routes as serverless API route handlers on **Vercel** (Hobby? Commercial use demands Vercel Pro - owner decision; interim: Firebase App Hosting or Vercel Hobby as preview only) AND deployed to **Firebase** (App Hosting supports Next.js or static Hosting behind rewrite rules; curl-check both hosts after each deploy, retry once on timeout; own domain later).
- **Server ops** (AI proxy, billing webhooks, ETA/ZATCA signer, owner analytics API, Telegram webhook): Next.js Route Handlers on Vercel; duplicated as Firebase Cloud Functions when Blaze is on - one codebase via shared package, two thin wrappers. Keep secrets in env only; `.env*.local` gitignored; same env vars on both hosts.
- **Data plane live paths**: POS offline queue in IndexedDB; server validation via rules + server functions (price/total checks server-side, totals recomputed piasters); Firestore listeners for KDS/orders; scheduled function (cron `:00`) for nightly roll-ups and weekly digest.
- **Local**: money, inventory FEFO, receipt ESC/POS bytes, sync conflict - pure functions in `packages/core`, unit-tested without I/O; emulator-tested rules; Vitest + emulator in CI.
- **Windows later**: Electron shell loads the same deployed app (like SIR Laptop Manager), ESC/POS via local bridge; not before M5.
- **Monorepo**: npm workspaces (`apps/web`, `apps/portal` later merges into `web`, `packages/core`, `packages/ui`); Turborepo cache; TypeScript strict everywhere; absolute imports; files < 300 lines; layered core/domain/data/presentation.

### 11.1 API surface (server + client)

All tenant reads/writes are Firestore with deny-by-default rules; the HTTP API exists for operations that must be server-side or secret-bearing. Every endpoint is versioned under `/api/v1`, requires a Firebase ID token, re-checks membership/role server-side for mutations, and writes an audit event for sensitive actions.

| Surface | Methods | Purpose | Notes |
|---|---|---|---|
| `/api/v1/businesses` | GET, POST, PATCH | List/create/update business profile, sector pack, locale, currency | Owner/manager only; sector pack change is audited and never silently rewrites history |
| `/api/v1/businesses/:id/branches` | GET, POST, PATCH | Branch CRUD, address, working hours, default printer | Branch-scoped roles enforced |
| `/api/v1/businesses/:id/members` | GET, POST, PATCH, DELETE | Invite, role change, deactivate member | Invite link is single-use, expiring; role change writes audit |
| `/api/v1/businesses/:id/pos/sales` | POST | Validate and commit a sale after offline sync | Idempotency key required; server recomputes totals in integer piasters; returns canonical sale doc |
| `/api/v1/businesses/:id/pos/receipts/:saleId` | GET, POST | Fetch receipt payload, queue ETA/ZATCA submission when enrolled | Never claims compliance; returns signer status honestly |
| `/api/v1/businesses/:id/inventory/:productId/batches` | GET, POST, PATCH | FEFO batches, expiry, receiving, adjustments | Pharmacy/food packs require reason codes; controlled log is append-only |
| `/api/v1/businesses/:id/purchasing/orders` | GET, POST, PATCH | PO lifecycle, goods receipt, supplier invoices | B2B ETA e-invoice path is spec-gated |
| `/api/v1/businesses/:id/customers` | GET, POST, PATCH | Customer profile, consent flags, credit ledger | Export/delete endpoints share the same consent rules |
| `/api/v1/businesses/:id/reports/:slug` | GET | Owner/manager report snapshots | Cashier cannot read finance reports; reports are computed from Firestore, not cached PII |
| `/api/v1/billing/checkout` | POST | Create Paymob/Fawry subscription checkout | Server holds merchant secrets; returns hosted payment URL or tokenized intent |
| `/api/v1/billing/webhook/:provider` | POST | Signed webhook receiver | HMAC verification, replay protection, idempotent plan transitions |
| `/api/v1/billing/portal` | GET, POST | Customer portal link for plan/cancel/update | Cancels via provider portal; no dark patterns |
| `/api/v1/ai/ask` | POST | "Ask your business" natural-language query | Whitelisted read-only query set; LLM phrases only; metered per plan; no patient/secret rows |
| `/api/v1/ai/support` | POST | Grounded help assistant | Free tier daily cap; cites docs/help pages only |
| `/api/v1/eta/receipts` | POST, GET | Queue/fetch ETA e-receipt submission status | Only active after business enrollment and signer onboarding; otherwise returns `not_enrolled` |
| `/api/v1/zatca/invoices` | POST, GET | Queue/fetch ZATCA invoice status for KSA businesses | Spec-gated; same honest status model |
| `/api/v1/telegram/webhook` | POST | Bot updates for digest, alerts, support links | Verifies Telegram secret; maps chat to membership by one-time code |
| `/api/v1/owner/metrics` | GET | Company owner analytics | Requires `company_owner` claim; every view audit-logged; no tenant PII |
| `/api/v1/devices` | GET, POST, PATCH | Register POS/kiosk/device, rotate token hash, revoke | Device tokens are hashed; kiosk lock state is server-authoritative |
| `/api/v1/privacy/export` | POST, GET | Start and download full business export | Available in grace period; job writes zip to Storage with expiring signed URL |
| `/api/v1/privacy/delete` | POST | Schedule deletion/purge workflow | Soft-delete first; owner confirmation; purge job documented |

Client-side reads use Firestore listeners for live screens (POS cart, KDS, owner dashboard); mutations that touch money, stock, roles, billing or health data go through the server endpoints above or Firestore transactions with rules that mirror the same checks.

## 12. Competitor matrix (full study: `ops/competitors/sir-business.md`, r53, 2026-11-12)

Summary of the thirteen (r53 globals plus r61 Egypt-local reads; sources and dates in `ops/competitors/sir-business.md`):

| # | Competitor | Their price (source, opened 2026-10/11) | One-line flaw | We beat them by |
|---|---|---|---|---|
| 1 | Odoo | One App Free US$0; Standard about US$8.95-20.90/user/mo depending apps (odoo.com/pricing via r53) | USD pricing + complexity; POS is partner-shaped | Egyptian Arabic POS at one price, five-state UX, sector packs day one |
| 2 | Square | Free processing-only; Plus US$49/mo; Premium US$149/mo per location (squareup.com via r53) | Not in Egypt, no Arabic, no ETA | Egypt-native rails + Arabic + ETA-ready + fair free tier |
| 3 | Toast | Quote-only; hardware lock-in (toasttab.com via r53) | Restaurant-only | Every sector, BYO hardware, transparent EGP |
| 4 | Foodics (فودكس) | Egypt page publishes bundles: Basic EGP 2,848.95-3,019.89/mo and Advanced EGP 3,733.67-3,957.69/mo billed annually; promos lower (foodics.com Egypt pricing, 2026-11-12) | Restaurant-led, hardware/payment bundle pressure, premium price band | Same Arabic depth, 41 sector packs, public EGP tiers, payment-agnostic |
| 5 | Loyverse | Free POS; add-ons US$5 history, US$5/employee, US$25 inventory per store (loyverse.com via r53; Circle comparison 2026-10-28) | Add-on ladder + USD; no ETA; weak Arabic | EGP tiers, history included, ETA-ready |
| 6 | Zoho Books | Free small tier; US$10-249/mo accounting plans (zoho.com via r53) | Not a POS; inventory behind higher tiers | Real POS with offline, books handed to accountants |
| 7 | Lightspeed | Basic/Core/Plus US$89/149/289/mo (lightspeedhq.com via r53) | 10-30x Egyptian SME budget; US/EU focus | Right price band for Egypt |
| 8 | Shopify POS | Basic US$27; Grow US$72; POS Pro +US$89/location (shopify.com via r53) | Shopify Payments not fully in Egypt; per-location Pro wall | One per-business price, InstaPay/wallets |
| 9 | Daftra (دفترة) | Accounting-led; dated third-party reads show Basic EGP 489.50/mo yearly or EGP 733 monthly, Advanced EGP 977.58/1,225, Comprehensive EGP 1,960/2,448 (verify on daftra.com) | Cluttered UI; accounting-first; POS depth varies by plan | Apple-grade Arabic UX, modern tenancy, POS-first free tier |
| 10 | Qoyod (قيود) | 14-day trial; Saudi-first; Egypt "قريبًا" (qoyod.com via r53) | ZATCA-only compliance; Saudi-first; POS separate | ETA-ready from M2, one unified product |
| 11 | Circle (DcodZ) | Free today, no subscription or card; offline selling syncs later; one shop per account; VAT receipts but not certified e-invoicing (justacircle.com, 2026-11-12) | Single-shop scope, no branches, no sector depth, no certified ETA | Multi-business tenancy, 41 packs, team roles, ETA pipeline, owner analytics |
| 12 | inyad | Free POS/Invoicing at 0 EGP; retail from EGP 599/mo, food from EGP 799/mo, platinum to EGP 2,199-3,199/mo; Classic one-time licenses EGP 9,199-12,099 (inyad.com Egypt pricing, 2026-11-12) | Broad suite but shallower per sector; payments/product breadth can feel like a bundle | Sector-specialised packs, fair free tier, clearer ETA wording, multi-business owner model |
| 13 | Geidea POS | No public Egypt price; payments-led POS with offline mode, 100+ reports, own terminals and acquiring (geidea.net, 2026-11-12) | Tied to Geidea acquiring/hardware; restaurant/retail generalist | Software-first, payment-agnostic (Paymob/Fawry/InstaPay/QR), sector packs |

Adopted ideas (cite): per-location Pro unlock (Shopify) as our per-business/per-seat model; Odoo light-user as cashier role without back-office; Loyverse/Qoyod/inyad free or trial shape -> our 30-day trial plus forever-free tier; Square/Circle offline selling -> our offline queue with honest sync states; Toast/Geidea hardware bundles -> BYO devices first; Foodics KDS/floor flow -> restaurant pack only, not every sector; Qoyod/Circle honest compliance limits -> our "not ETA certified until enrolled" badge. Original: stepper sector wizard, numeric-eval AI, encrypted health data, Telegram linkage, per-tenant isolation tests.

## 13. Quality bar and screens (premium, Apple-level, Arabic RTL)

Design system in `packages/ui`: tokens (color/spacing/radius/shadow), springs (stiffness 170/damping 26 default; close matches open), logical CSS properties only; themes light/dark/system/high-contrast; RTL-first with bidi auto-detect per input run (L8); icons: Phosphor (single license, tree-shaken); touch targets ≥ 44px; layout safe at 320/390/768/1280/1920; no emoji headers, no gradient hero text, no pill-everything; five states on every view (idle, skeleton, empty + one action, error + retry, populated); 120 Hz transforms only; no fake numbers anywhere; Arabic copy first, English mirrored (no "(RTL)" labels); 44px swipe tabs/bottom nav with `scrollIntoView` on mount (L1); tab bar never unmounts on navigation (L28); reduced-motion honored. Screens: Signup, Sector catalogue, Linear setup wizard (8 steps), Lock/PIN, POS, Orders + KDS, Inventory (FEFO radar), Purchasing (PO + receiving), Customers + loyalty, Finance (shifts, Z-report, expenses), Reports, Team & permissions, Devices, Settings, Billing, Owner analytics (company), Kiosk, Customer display, Receipt print, Onboarding resume, Empty states everywhere. All screenshots at 320/390/768/1280 (+1920 spot) in both languages both themes before any "done" (L33).

## 14. AI and support

Flagship: "اسأل نشاطك" / "Ask your business" - owner asks in Arabic or English ("إيه أكتر حاجة اتباعت النهاردة؟"); the answer is computed from a whitelisted read-only query set (sales by item/hour/method/cashier, expiry next 7 days, low stock, best-selling week); the LLM phrases, never invents; numeric-accuracy eval gate (50 pinned questions, 100% match required pre-ship; drift monitored weekly via Telegram report). Metered: free tier cap 100 questions/business/mo; plan questions included (Pro 500); overage disabled in v1 (no surprise bills). AI keys server-side only (`ai-proxy` pattern, OWNER_DEFAULTS 11) with Gemini flash-lite → flash → any Gemini → OpenRouter free → local; kill switch in settings. Support assistant grounded in `docs/help` + shipping changelogs; free-tier 5 questions/day; Arabic Egyptian dialect; five states; refuses to invent policy - links to pages. Benchmark: zero tolerance for invented stock/prices (a pharmacy answer of "12" when stock is 0 is a release blocker).

## 15. Security, legal and compliance

Deny-by-default everywhere; server checks never client flags. PINs hashed (argon2), 5 attempts lockout, manager override is a separate hashed PIN with audit. Phone OTP and Google only for customers; staff PINs never leave the device as plaintext. Pharmacy: controlled-drug log append-only (no edit, only void-with-reason), health data AES-256-GCM field-level, pharmacist license number captured at onboarding (verified manually v1), drug interaction data labeled "(unsourced, verify)" until licensed, DDI warnings phrased as "discuss with your pharmacist" never advice. Food: ETA e-receipt fields printed (seller VAT number placeholder until onboarding; spec read first). Tax claims: no public ETA/ZATCA "compliant" claim until accountants + lawyer sign (see section 22). Egyptian consumer law + PDPL: privacy notice, refund policy, cookie banner with Reject, data export/delete buttons, DPA for business customers. Logging: audit trail of reads of health data; error reporting opt-in; security.txt. Breach runbook; incident contact; public status page later. No AHome data ever touches this product; no Habiba anything; no fake reviews; marketing only after first 3 consenting pilot testimonials.

## 16. Milestones M0 → M6 (acceptance tests are commands, not adjectives)

**M0 - Foundations (target: 1 week).** Desktop folder kit recreated from scratch (`SIR Project Kit` generator): `D:\Projects\SIR Business\folder.ico` (real icon, exists), Desktop `SIR Projects/SIR Business/` with shortcuts (Web, Vercel, Start dev, Stop dev, Windows app - skipped but placeholder not allowed: omit until exists), `Versions.txt` (1.0.0 + plain status). `.sir/` files refreshed (`PLAN_REFRESH.md`, `CHECKPOINT.md`). GitHub repo public-proof kept private, clean main. Firebase project `sir-business` created (Spark, me-central1 or fallback recorded); Vercel project imported; env vars on both hosts; both URLs curl 200.
*Acceptance*: `ls Desktop/SIR Projects/SIR Business` shows kit; `gh repo view sirahmed8/sir-business`; `curl -s -o /dev/null -w "%{http_code}" https://sir-business.web.app` → 200; `curl -s -o /dev/null -w "%{http_code}" https://sir-business.vercel.app` → 200; `.sir/CHECKPOINT.md` records both URLs + region.

**M1 - Common engine core (target: 3 weeks).** Tenancy (org/business/branch/membership), RBAC with sector role templates, auth scaffold (Google + phone OTP + staff PIN, hashed), products + inventory FEFO, POS sale end-to-end on emulator + web PWA (cash sale persists through reload), money module integer piasters, offline queue design ADR (`docs/adr/001-offline-sync.md` conflict rule), five-state primitives in `packages/ui`.
*Acceptance*: `npm run verify` green (tsc, lint, vitest); POS e2e: create sale offline → reload browser → sale present; rules emulator suite green (`firebase emulators:exec --only firestore "pnpm test:rules"`); `npm run build` exits 0; PWA manifest installable; screenshot at 320/390/768/1280 ar+en light+dark.

**M2 - Restaurant + Market templates (target: 3 weeks).** Both templates from section 6.1/6.2 maps: floor plan/KDS/waiter/kiosk for restaurant; FEFO radar, barcode POS, procurement, customer 360 for market. Legacy parity table filled in `.sir/reports/parity.md` with per-module verdict. Onboarding wizard (linear stepper) ships.
*Acceptance*: template smoke suite (`pnpm test:sectors -- restaurant market`) green; wizard e2e refuses to advance with invalid branch form (test asserts disabled Next); receipt reprint byte-golden test green; manual script: fresh signup → restaurant sector → add 3 items → cash sale → Z-report shows it.

**M3 - Subscriptions, owner page, hardening (target: 2 weeks).** Billing on Paymob test keys behind `signed-webhook` + `billing-fallback` (14-day grace, never locks out mid-shift); 30-day trial counter; `/owner` analytics live (claim-verified); Firestore rules in production mode with emulator coverage; export/delete in settings; legal-pack pages (privacy, terms, refund, cookies with Reject); Telegram bot linked per user with digest.
*Acceptance*: pay-to-pro webhook replay test asserts plan upgrade + downgrade path; `/owner` without claim → 403 page; rules tests green in CI; `GET/POST /api/owner/metrics` requires claim (integration test); DPA PDF downloads; Telegram `/start <code>` links account (manual proof screenshot).

**M4 - Library + Pharmacy templates (target: 3 weeks, Pharmacy last).** Library: catalog/OPAC/memberships/borrowing/desk booking/citations. Pharmacy: FEFO radar, patients encrypted, controlled-drugs log, DDI warnings "(unsourced, verify)" badge in UI, zero-stock refusal test.
*Acceptance*: pharmacy smoke suite green; controlled-drug append-only rule test (edit attempt rejected); patient record decrypt round-trip test; DDI alert shows source disclaimer; zero-stock question returns "0" in AI eval (gate).

**M5 - Hardware, AI, polish (target: 2 weeks).** ESC/POS bridge (golden bytes), barcode wedge, cash drawer kick test, customer display live cart, kiosk locked mode, AI "ask your business" with eval gate, 120 Hz audit, reduced-motion pass, 320–1920 px audit both directions.
*Acceptance*: `pnpm test:print` golden equal; eval report shows 50/50; lighthouse PWA ≥ 90; audit script (click-target + WCAG composite probe from L50) zero blockers; five states on 30 screens verified.

**M6 - Pilot, production, archive (target: 3 weeks).** Three consenting real Egyptian businesses on 14-day monitored pilot (written consent, no secrets); bugfix week; production readiness checklist; dual hosting curl-verified after deploy; Windows app only if a customer has Windows kiosk hardware (otherwise skipped honestly); legacy folders moved to `D:\Projects\old projects\SIR Business legacy\` with a note in `MERGE_RECORD`; LAUNCH_CHECKLIST items ticked; store listings draft (no publication until owner approves).
*Acceptance*: pilot report (3 businesses × 2 weeks) with zero P0s; rollback rehearsal (Vercel promote previous + Firebase Hosting previous); legacy folders present under `old projects\` with `README.md` mapping; both hosts 200; sign-off written in `.sir/EVIDENCE/`.

## 17. Task queue (ready to hand to agents)

`ops/briefs/sir-business-tasks.md` (r61, 2026-11-12) now carries 48 smaller tasks. Tasks 1-10 stay ready to queue for M0/M1/M2 foundations; tasks 11-48 are gated follow-ons covering the API surface, sector pack registry, wave-1 packs, service/retail/production packs, hardware, owner analytics, legal/privacy, launch instrumentation and pilot readiness. Every task has Brief, Files, Done when, Check and applicable skills from `ops/SKILLS_INDEX.md`. Per-sector first-ten tasks also exist under `ops/briefs/business-<slug>-tasks.md` for all 41 packs.

## 18. Risks and open questions (defaults chosen; review at milestone starts)

ETA/ZATCA: nobody claims compliance until official specs are read by an Egyptian accountant; default = ship without, show honest "e-invoice on the way" badge, build after spec read. Pharmacy data: default = encrypt + no-AI + pharmacist review before any real pharmacy pilots (3 pharmacists on advisory board, owner step). Drug data: default = licensed Egyptian drug DB or curated seed with visible "(unsourced, verify)" until licensed. DDI accuracy: no medical advice, phrased "ask your pharmacist". Hardware: web-first; ESC/POS via print bridge M5; fiscal hardware not in v1. Concurrency: Firestore transaction budget per sale; stress tests at M2. Costs: free tiers first; Blaze (Cloud Functions) requires owner card; Vercel Pro required for commercial terms - decision owner, default interim = Firebase App Hosting for production and Vercel for preview. Localization: Arabic MSA + Egyptian dialect UI copy deck; legal English. Retention: 90-day backups; purge jobs tested. Data migration from four legacy apps: none (they never worked on real data); pilot shops start empty with catalog import. Multi-currency accounts: EGP and USD only in v1. Security: no bug bounty until public; responsible disclosure email placeholder. Talent: founder is a student; everything documented here and in `.sir/` so any free model can continue from cold start.

## 19. Only the owner can do

1. Create `firebase projects:create sir-business` and the `sir-business` GitHub repo remotes are already wired (`gh repo view sirahmed8/sir-business`); Firebase console needs his clicks for the first project creation.
2. Add billing card for Blaze (when Cloud Functions are needed) and decide Vercel Hobby vs Pro.
3. Buy domain `sirbusiness.app` (or an `.eg`) and the code-signing cert; set DNS on both hosts.
4. Create Paymob + Fawry merchant accounts; paste live keys (never in git; env + Vercel env).
5. Accountant (ETA specs read, pricing sanity-check, e-invoice wording) and pharmacist review (pharmacy pilot go/no-go, drug seed source).
6. ETA/ZATCA sandbox onboarding when phase 2 applies to us; lawyer for DPA + terms; pilot consent letters from 3 shops.
7. Telegram BotFather chat to hand over bot username `@SIRBusinessBot` (or chosen name) and set privacy policy link.

## 20. Feature parity target (best-in-category, honest)

Match or exceed, with eyes open: Loyverse (free POS, global) for setup speed; Foodics (Arabic restaurant) for floorflow and KDS; Daftra (Egyptian sectors) for catalogue breadth; Odoo (modules) for multi-company; Zoho (books) for accountant handoff files; Square (simplicity + free tier) for time-to-first-sale; Lightspeed (retail) for reporting. We do **not** copy their moats blindly: no hardware lock-in, no quote-only pricing, no fake compliance, no mock data, no Windows-only desktop hostage.

## 21. Verification and definition of done

Nothing is done until: `npm run verify` green; both hosts curl 200; screenshots at 5 widths both directions both themes; five states on all shipped screens; rules emulator suite green; eval 100% where AI ships; report in `.sir/evidence/` + `ops/agy-runs/reports/`; pushes to `main`; CI note per rule 18 (quota flag) or green CI after 2026-12. Milestone M0 also refreshes `plans/PRODUCT_DIRECTION_2026-11-12.md` references in this file if it moves.

## 22. Anchor decisions (2026-11-12, logged)

Firebase project name: `sir-business` (OWNER_DEFAULTS 2). Repo: existing `sirahmed8/sir-business` reused. Region default: `me-central1` verify, else `europe-west1`. Currency: EGP default, USD auto for non-ar-EG. Trial: 30 days. Free tier: §9. Bot: single `@SIRBusinessBot`. ETA/ZATCA: spec-gated, off by default. Windows: M5+. Arabic: Egyptian dialect voice, RTL-first. Version: 1.0.0 until GA.

## 23. Launch and marketing (M5 to M6, then post-launch)

**Positioning**: one owner, many businesses, each with its own specialised software and site on one engine. The public promise is operational, not magical: sell faster offline, know stock before it expires, see profit per shift, keep each shop's team and data separate, and pay one fair EGP price instead of a stack of per-module fees.

**Launch surfaces**
- Marketing site (same Next.js app, `/` and `/ar`): hero states the end state in one sentence, sector picker shows all 41 packs with honest status (ready, in pilot, on the way), pricing shows Free/Trial/Starter/Business/Pro in EGP with USD toggle, and every competitor claim links to `ops/competitors/sir-business.md` sources or says "(unsourced, verify)".
- Sector landing pages: one indexable page per pack at `/sectors/<slug>` and `/ar/sectors/<slug>`, generated from the same JSON that feeds `plans/business-sectors/<slug>.md` so copy cannot drift. Each page has operator pain, three concrete workflows, screenshots only after a real pilot or demo tenant exists, FAQ, and a CTA to start free.
- In-product onboarding: linear wizard (unavailable future steps stay disabled), sector pack choice, branch setup, first product import (CSV/template), first sale rehearsal, receipt print test, team invite, and a "what is not included yet" honesty card.
- Docs and help: `docs/help/<slug>.md` bilingual, searchable by the support assistant; changelog per pack; status page when public.

**Channels, in order**
1. Direct outreach to the 3 pilot businesses and their street networks; no paid ads until at least one pilot can be named with permission.
2. Arabic SEO pages for high-intent queries ("نظام كاشير للسوبر ماركت", "برنامج صيدلية FEFO", "إدارة حجوزات صالون") once sector pages exist; English pages for GCC expats and franchise owners.
3. WhatsApp/Telegram community for Egyptian shop owners; weekly Egyptian-dialect tip tied to a real feature, never engagement bait.
4. Accountant and pharmacist referrals for pharmacy/clinic packs; hardware-store and print-shop associations for B2B packs.
5. App stores only after PWA metrics justify native shells; store copy must match the honest compliance badges.

**Launch gates (no public claims before these pass)**
- ETA wording reviewed by the Egyptian accountant; public pages may say "ETA-ready workflow" only after spec read and pilot validation, never "ETA compliant" for a business that is not enrolled.
- Pharmacy pack gated by pharmacist review, encrypted patient fields, licensed drug-data source or visible "(unsourced, verify)" seed, and controlled-drug append-only tests.
- Pricing copy uses the dated competitor file and says prices exclude tax and compliance onboarding unless the invoice shows otherwise.
- All screenshots use demo tenants with obviously sample data or real consenting pilots; no stock-photo "live dashboard" pretending to be customer data.
- Free tier is genuinely useful: offline POS, one business, two seats, receipts, basic reports, export. Paid tiers add history, branches, seats, sector depth, AI quota and priority support.

**Metrics that decide the next milestone**
- Activation: signup -> sector chosen -> first product -> first sale -> second day active.
- Retention: day-7 and day-30 active businesses; sector mix; offline sync success rate; support tickets per business.
- Money: trial-to-paid conversion, MRR by plan and sector, failed-payment rate, refund rate, expansion (extra business/seat).
- Trust: export/delete requests completed inside SLA, ETA/ZATCA status accuracy, AI eval drift, security incidents (target zero P0/P1).
- Owner page shows only aggregate, non-PII metrics; tenant-level drill-down requires break-glass and is owner-visible.

## 24. r61 refresh changes (2026-11-12)

This pass kept the r53/r56 architecture and made the plan executable for a planning-only round:

- Rescanned the merged plan, the SIR Business `.sir` deep scan, legacy verdicts, competitor file, owner direction and sector catalogue.
- Added the r61 competitor addendum with Egypt-local reads: Circle, inyad and Geidea; corrected Foodics and Daftra price statements; verified ETA e-invoice/e-receipt conditions, ETA SDK portal, ETA Decision 361/2025 phase-nine timing, Paymob/Fawry published fee snippets and Firestore free-tier/location facts.
- Raised the sector catalogue from the r53 grouped view to the authoritative 41-pack catalogue in `plans/business-sectors/`, with `_ENGINE.md`, per-sector plans and per-sector task briefs generated from `_data/*.json`.
- Added the API surface table under architecture so server/client boundaries, money/idempotency, billing webhooks, AI metering, ETA/ZATCA honesty, privacy export/delete and owner analytics are explicit before build starts.
- Added launch/marketing gates so public copy cannot outrun pilots, accountant review, pharmacist review or honest compliance status.
- Expanded `ops/briefs/sir-business-tasks.md` from 10 build briefs to 40+ smaller tasks with acceptance checks and applicable skills, while keeping the first 10 ready for agents.
- Kept every price, law, certification and competitor claim tied to a dated source or "(unsourced, verify)"; nothing in this round created product code, Firebase projects, repositories or store listings.

*Every claim in this plan about a competitor, a price, a market size, a law or a certification carries a source or "(unsourced, verify)"; see `ops/competitors/sir-business.md` and section 18. This plan merges and supersedes the 2026-11-10 draft; git history preserves it.*
