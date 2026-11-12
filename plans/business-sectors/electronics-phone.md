# SIR Business sector: Electronics and mobile (إلكترونيات وموبايلات)

> Round r56 (2026-11-12). Sector 17 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `retail`, group `retail`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The electronics shop owner manages a serialised inventory of phones and accessories, warranty claims and repair jobs. Their day is receiving new stock, tracking warranty expiry and handling repair quotes.

Why this sector is in the catalogue: Electronics shops sell phones and accessories with IMEI tracking, warranty dates and service/repair intake. Each phone is a serialised unit with its own warranty claim.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- PhoneUnit (id, shopId, imei, model, colour, storage, warrantyStart, warrantyEnd, costPiasters, pricePiasters, status, locationShelf, faultNote)
- Accessory (id, shopId, name, type, pricePiasters, costPiasters, stockQty, status, locationShelf)
- RepairJob (id, phoneId, customerName, customerPhone, complaint, quotePiasters, approvedBy, status, completedAt, notes)
- WarrantyClaim (id, phoneId, customerName, customerPhone, issue, status, claimedAt, resolvedAt, authorisedBy)
- Supplier (id, nameAr, phone, paymentTerms, visitDays, leadTimeDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: piece, unit, set

Batches: No : electronics shop carries no stock or expiry (IMEI is serial number not batch)

Expiry and shelf life: Warranty has start and end dates, not product expiry

Sector specific structures: The core structures are the IMEI-tracked phone unit, the repair job with quote and status, and the warranty claim lifecycle. IMEI is equipment data not personal data but receipts carry buyer phone if captured.

## 3. Screens and workflows that belong to this sector

- Phone catalogue: grid of phone units with IMEI, model, colour, storage, price, warranty status, fault note
- Phone detail: full unit info, warranty dates, fault note, history of repairs
- Accessory catalogue: grid of accessories with name, type, price, stock
- Repair job creation: enter phone IMEI, complaint, generate quote, set status (draft/approved/in-progress/completed)
- Warranty claim creation: enter phone IMEI, customer details, issue, set status (open/pending/resolved)
- Repair status tracker: per job, view progress, mark completed, print completion receipt
- Warranty claim tracker: per unit, view status, resolution, update status
- Cash register: scan IMEI or SKU, apply discount, tender payment, print receipt with IMEI
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : inventory, repairs, warranties, reports, billing
- Sales rep: manage phone stock, create repair jobs, handle warranty claims
- Technician: view repair jobs, mark in-progress/completed, update warranty claims
- Cashier: scan IMEI/SKU, tender payment, print receipt

## 5. Reports and KPIs

- Phone inventory by model and storage: count per model/colour/storage, turnover rate
- Repair job pipeline: draft/approved/in-progress/completed counts, average duration
- Warranty claim rate: open/pending/resolved counts, resolution time, common issues
- Phone sales by model and period: volume and revenue per model per month
- Accessory sales by type and period: volume and revenue per accessory type per month

## 6. Integrations that matter

- Web API for IMEI validation (optional, carrier lookup)
- Esc/POS thermal printer for receipts and repair completion notes
- WhatsApp deep link for customer repair status updates and warranty notifications
- Email for warranty resolution notice (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial inventory: the starting phone list with IMEI, model, colour, storage, price and warranty dates
- Repair types: the repair categories (screen replacement, battery, charging port, water damage, others)
- Staff: add the initial team with their role templates
- First week plan: receive first phone stock, create first repair job, first warranty claim

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- N
- o
-  
- s
- e
- c
- t
- o
- r
- -
- s
- p
- e
- c
- i
- f
- i
- c
-  
- s
- e
- e
- d
-  
- d
- a
- t
- a
- .
-  
- T
- h
- e
-  
- e
- n
- g
- i
- n
- e
-  
- p
- r
- o
- v
- i
- d
- e
- s
-  
- t
- h
- e
-  
- I
- M
- E
- I
- -
- t
- r
- a
- c
- k
- e
- d
-  
- p
- h
- o
- n
- e
-  
- u
- n
- i
- t
-  
- a
- n
- d
-  
- r
- o
- l
- e
-  
- t
- e
- m
- p
- l
- a
- t
- e
- s
- .

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- إلكترونيات وموبايلات
- هواتف، ضمانات وإصلاح من لوحة واحدة
- تتبع IMEI لكل وحدة
- إدارة Claims الضمان
- ملفات الصيانة

Questions the page must answer:

- كيف أتبع الوحدة ب IMEI ?
- كم مدة الضمان؟

### English

- Electronics & Mobile Management
- IMEI-tracked units, warranties and repairs from one dashboard
- IMEI tracking per unit
- Warranty claim lifecycle
- Repair job pipeline

Questions the page must answer:

- How do I track a unit by IMEI?
- What is the warranty period?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Phone catalogue: grid of phone units with IMEI, model, colour, storage, price, warranty status, fault note
- Phone detail: full unit info, warranty dates, fault note, history of repairs
- Accessory catalogue: grid of accessories with name, type, price, stock
- Repair job creation: enter phone IMEI, complaint, generate quote, set status (draft/approved/in-progress/completed)
- Warranty claim creation: enter phone IMEI, customer details, issue, set status (open/pending/resolved)
- Repair status tracker: per job, view progress, mark completed, print completion receipt

## 9. Pricing tier notes

- - Starter: 200 EGP / month, 1 branch, up to 50 phone units
- - Professional: 450 EGP / month, unlimited units, repair module
- - Enterprise: custom for electronics chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| GadgetPro | from 550 EGP/mo | no IMEI tracking | full IMEI per unit with warranty and repair lifecycle |
| PhoneCare | from 520 EGP/mo | no repair job pipeline | full repair job from quote to completion with status tracking |
| Mobility | from 580 EGP/mo | no warranty claim lifecycle | full warranty claim open/pending/resolved with resolution tracking |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-electronics-phone-tasks.md`:

1. Add IMEI-tracked phone catalogue (M1)
2. Add repair job creation and status tracker (M1)
3. Add warranty claim creation and tracker (M1)
4. Add repair status tracker per job (M1)
5. Add warranty claim tracker per unit (M1)
6. Add cash register with IMEI/SKU scanning (M1)
7. Add phone inventory by model report (M2)
8. Add repair pipeline report (M2)
9. Add warranty claim rate report (M2)
10. Add onboarding flow for initial electronics shop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes phone unit and warranty records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Warranty claims without clear start/end dates can violate consumer protection law
- IMEI data stored without proper consent can raise privacy concerns if receipts expose buyer phone

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-electronics-phone-tasks.md`
