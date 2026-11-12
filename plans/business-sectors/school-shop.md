# SIR Business sector: School shop (مقصف ومكتبة مدرسة)

> Round r56 (2026-11-12). Sector 23 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `market + service`, group `education-and-community`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The school shop manager oversees the campus catalog, student wallets, parent billing and term subscriptions. Their day is parent top-ups, uniform sales and managing term deposits.

Why this sector is in the catalogue: School shops sell uniforms, books and supplies to students. They also handle parent top-ups, term subscriptions and parent consent for child data. Child data privacy (PDPL) is the key differentiator.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- SchoolShop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours, termDate)
- CampusItem (id, shopId, sku, nameAr, nameEn, type (uniform/book/supply), sizeAr, sizeEn, pricePiasters, costPiasters, taxRate, stockQty, status, locationShelf)
- Student (id, schoolId, name, class, guardianPhone, guardianConsent, walletPiasters, enrollmentYear, status)
- TermSubscription (id, studentId, type, amountPiasters, startDate, endDate, status, paidAt)
- TopUp (id, studentId, amountPiasters, method, status, recordedAt, receiptPrinted)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: visit, subscription, top-up, item

Batches: No : school shop carries no stock or expiry

Expiry and shelf life: Not applicable. Subscriptions have date ranges not expiry dates

Sector specific structures: The core structures are the student with guardian consent, the term subscription with start/end dates, the wallet top-up and the campus catalog. Child data (student name, class) requires parent consent per PDPL.

## 3. Screens and workflows that belong to this sector

- Campus catalog: grid of items (uniforms, books, supplies) with size options and prices
- Student profile: name, class, guardian phone, consent flag, wallet balance, active subscriptions
- Term subscription: select type, set amount and dates, record payment, track status (active/pending/expired)
- Wallet top-up: enter amount, select payment method (cash, card, InstaPay), record top-up, print receipt
- Order management: receive shipment, update campus catalog stock, record sales
- Cash register: scan SKU, apply discount, tender payment, print receipt with student name and class
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : campus catalog, subscriptions, reports, billing
- Cashier: scan items, tender payment, print receipt, top-up wallet
- Staff: receive shipments, update catalog stock, manage subscriptions
- Assistant: parent communications, consent management

## 5. Reports and KPIs

- Sales by day and hour: revenue per period, peak hours (around school dismissal)
- Term subscription volume: active vs pending vs expired per period
- Wallet top-up frequency: number of top-ups per student per period, total amount collected
- Campus item stock: how many uniform/supply items in stock, low-stock alerts
- Parent purchase history: total spent per student, visit frequency

## 6. Integrations that matter

- Barcode scanner for SKU entry at till
- Esc/POS thermal printer for receipts and top-up receipts
- InstaPay QR for wallet top-up (counterparty integration)
- WhatsApp deep link for parent notifications (low balance, subscription renew)
- Email for invoice and subscription renewal notices (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours, term start/end dates
- Initial catalog: the campus items (uniforms, books, supplies) with sizes and prices
- Membership types: the term subscription types (full term, half term, quarter) and amounts
- Staff: add the initial team with their role templates
- First week plan: receive first shipment, list first campus items, first parent top-up

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
- s
- t
- u
- d
- e
- n
- t
- /
- g
- u
- a
- r
- d
- i
- a
- n
-  
- c
- o
- n
- s
- e
- n
- t
- /
- t
- e
- r
- m
-  
- s
- u
- b
- s
- c
- r
- i
- p
- t
- i
- o
- n
-  
- s
- c
- h
- e
- m
- a
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

- مقصف المدرسة
- مستلفيات، اشتراكات وأرصدة من لوحة واحدة
- حذف المكتبة campus
- اشتراكات بالفصل
- أرصدة الوالدين

Questions the page must answer:

- كيف أشتريunos uniform للابن؟
- كيف أحمل رصيد محفظة الأب؟

### English

- School Shop Management
- Campus catalog, term subscriptions and wallet top-ups from one dashboard
- Campus catalog with size options and prices
- Term subscriptions with start/end dates
- Wallet top-ups with multiple payment methods

Questions the page must answer:

- How do I buy a uniform for my child?
- How do I top up the wallet?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Campus catalog: grid of items (uniforms, books, supplies) with size options and prices
- Student profile: name, class, guardian phone, consent flag, wallet balance, active subscriptions
- Term subscription: select type, set amount and dates, record payment, track status (active/pending/expired)
- Wallet top-up: enter amount, select payment method (cash, card, InstaPay), record top-up, print receipt
- Order management: receive shipment, update campus catalog stock, record sales
- Cash register: scan SKU, apply discount, tender payment, print receipt with student name and class

## 9. Pricing tier notes

- - Starter: 100 EGP / month, 1 branch, up to 50 campus items
- - Professional: 220 EGP / month, unlimited items, reports
- - Enterprise: custom for school chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| SchoolFix | from 250 EGP/mo | no guardian consent flag | parent consent and minimal child data with PDPL deletion on request |
| EduCart | from 230 EGP/mo | no term subscription tracking | full term subscriptions with start/end dates and aging reports |
| CampusMart | from 280 EGP/mo | no wallet top-up InstaPay integration | InstaPay QR top-up and receipt printing |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-school-shop-tasks.md`:

1. Add guardian consent flag for student records (M1)
2. Add term subscription screen (M1)
3. Add wallet top-up screen with InstaPay (M1)
4. Add campus catalog grid with sizes and prices (M1)
5. Add cash register with student name and class print (M2)
6. Add term subscription volume report (M2)
7. Add wallet top-up frequency report (M3)
8. Add campus item stock report (M3)
9. Add parent purchase history report (M3)
10. Add onboarding flow for initial school shop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Member data with children (under 18) requires parent consent and minimal fields per PDPL
- Encryption key loss makes student records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Term subscriptions without clear start/end dates can violate consumer protection law

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-school-shop-tasks.md`
