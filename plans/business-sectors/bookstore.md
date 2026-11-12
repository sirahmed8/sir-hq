# SIR Business sector: Bookstore (مكتبة بيع)

> Round r56 (2026-11-12). Sector 21 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `retail`, group `education-and-community`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The bookstore owner manages inventory, purchases from suppliers and customer wish lists. Their day is receiving shipments, pricing copies and matching customers to books they want.

Why this sector is in the catalogue: A bookstore sells books by ISBN, tracks second-hand stock and manages customer wishes. Distinct from the library circulation model: this is a sales model, not a lending model.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Bookstore (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Product (id, bookstoreId, sku, isbn, titleAr, titleEn, authorAr, authorEn, category, unitPricePiasters, costPiasters, taxRate, condition, status, locationShelf)
- Customer (id, bookstoreId, name, phone, whatsAppOptIn, purchaseHistoryCount, totalSpentPiasters)
- Wishlist (id, customerId, productId, notes, createdAt, notified)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, bookstoreId, name, phone, role, hourlyRatePiasters, status)

Units in use: piece, copy, set

Batches: No : bookstore carries no stock or expiry (condition indicates wear, not expiry)

Expiry and shelf life: Not applicable. Books have condition states not expiry dates

Sector specific structures: The core structures are the product catalogue with condition states, the wishlist system and the customer purchase history. Condition (new/used) replaces expiry for second-hand stock.

## 3. Screens and workflows that belong to this sector

- Product catalogue: grid of books with title, author, ISBN, price, condition (new/used), availability
- Product detail: full book info, edition notes, condition description, purchase options
- Wishlist manager: customer wishes, notify when available, prioritise purchases
- Customer profile: purchase history, total spent, wishlist, opt-in status
- Purchase order: receive shipment from supplier, record items, update stock
- Cash register: scan SKU, apply discount, tender payment, print receipt
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : inventory, pricing, reports, billing
- Cashier: scan items, apply discounts, tender payment, print receipt
- Stock clerk: receive shipments, update stock, relocate products
- Assistant: customer wishlist management, special orders

## 5. Reports and KPIs

- Sales by day and hour: revenue per period, peak hours
- Product popularity: most sold books, editions, authors per period
- Customer lifetime value: total spent, visit frequency, average ticket
- Wishlist conversion: how many wishes turned into purchases
- Inventory aging: how long copies have been in stock by condition

## 6. Integrations that matter

- Barcode scanner for SKU entry at till
- Esc/POS thermal printer for receipts and special orders
- WhatsApp deep link for customer notifications (new arrivals, wished-back-in-stock)
- Email for invoice and special order updates (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial inventory: the starting book list with ISBN, titles, prices and condition
- Product categories: fiction, non-fiction, children, academic, second-hand
- Staff: add the initial team with their role templates
- First week plan: receive first shipment, list first products, first customer sale

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
- p
- r
- o
- d
- u
- c
- t
-  
- c
- a
- t
- a
- l
- o
- g
- u
- e
-  
- w
- i
- t
- h
-  
- c
- o
- n
- d
- i
- t
- i
- o
- n
-  
- s
- t
- a
- t
- e
- s
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

- مكتبة بيع
- كتب جديدة وكتب قديمة من لوحة واحدة
- كتالوج كتب بال ISBN والسعر
- قوائم Wunsch (wishlist) للعملاء
- تاريخ المشتريات لكل عميل

Questions the page must answer:

- هل tienen كتب قديمة؟
- كيف أحجز كتاباً ليس موجوداً؟

### English

- Bookstore Management
- ISBN catalogue, wishlists and customer purchase history from one dashboard
- ISBN-tracked product catalogue with condition
- Wishlist system with notification
- Customer purchase history and LTV

Questions the page must answer:

- Do you have second-hand books?
- How do I order a book not in stock?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Product catalogue: grid of books with title, author, ISBN, price, condition (new/used), availability
- Product detail: full book info, edition notes, condition description, purchase options
- Wishlist manager: customer wishes, notify when available, prioritise purchases
- Customer profile: purchase history, total spent, wishlist, opt-in status
- Purchase order: receive shipment from supplier, record items, update stock
- Cash register: scan SKU, apply discount, tender payment, print receipt

## 9. Pricing tier notes

- - Starter: 100 EGP / month, 1 branch, up to 50 products
- - Professional: 220 EGP / month, unlimited products, reports
- - Enterprise: custom for bookstore chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Nas | from 250 EGP/mo | no condition tracking (new/used) | condition-aware catalogue with new/used pricing |
| Dar Al-Kitab | from 230 EGP/mo | no wishlist system | full wishlist with notification when back in stock |
| Rawy | from 280 EGP/mo | no customer LTV reports | customer lifetime value and purchase history reports |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-bookstore-tasks.md`:

1. Add product catalogue grid with condition states (M1)
2. Add wishlist manager per customer (M1)
3. Add customer profile with purchase history (M1)
4. Add purchase order receipt screen (M2)
5. Add cash register with SKU scanning (M2)
6. Add customer lifetime value report (M3)
7. Add wishlist conversion report (M3)
8. Add inventory aging report by condition (M4)
9. Add onboarding flow for initial bookstore setup (M1)
10. Add personalisation engraving flow (M1)

## 12. Risks, unknowns and what we refuse to fake

- No special-category data risks (this is a retail sales model)
- Encryption key loss makes product records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Second-hand condition descriptions must not mislead buyers consumer-protection law

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-bookstore-tasks.md`
