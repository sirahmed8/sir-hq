# SIR Business sector: Wholesale and distribution (جملة وتوزيع)

> Round r56 (2026-11-12). Sector 19 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `market + b2b`, group `retail-and-commerce`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The wholesale distributor manages bulk inventory, customer credit accounts and ETA e-invoices. Their day is price tiers, outstanding receivables and compliance with ETA invoicing rules.

Why this sector is in the catalogue: Wholesale distributors sell to other businesses (restaurants, shops, pharmacies). They need tiered pricing, large-quantity discounts, receivables/credit book and B2B invoicing (ETA).

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Distributor (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Customer (id, distributorId, name, phone, creditLimitPiasters, creditUsedPiasters, paymentTerms, isB2B, status, repAssigned)
- Product (id, distributorId, sku, nameAr, nameEn, category, unitPricePiasters, costPiasters, taxRate, unit (box,pack,litre), minOrderQty, maxOrderQty, status, locationShelf)
- PriceTier (id, productId, minQty, maxQty, discountPercent, isActive)
- Receivable (id, customerId, amountPiasters, dueDate, status, createdAt, lastPaymentAt, notes)
- B2BInvoice (id, saleId, etaSigned, qrCode, sealHash, status, issuedAt, notes)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, distributorId, name, phone, role, hourlyRatePiasters, status)

Units in use: box, pack, crate, litre, tonne, piece

Batches: No : wholesale carries no stock or expiry

Expiry and shelf life: Not applicable. Receivables have due dates not expiry dates

Sector specific structures: The core structures are the price tier system (min qty / max qty / discount), the receivable tracking with due dates and the B2B invoice with ETA signing and QR code. Tiered pricing by volume is the key differentiator.

## 3. Screens and workflows that belong to this sector

- Product catalogue: grid of products with name, price per unit, min/max order qty, price tier badge
- Product detail: full info, all active price tiers, cost, min/max qty
- Customer account: credit limit, credit used, payment terms, status, rep assigned, receivables list
- Price tier manager: add/edit tier (minQty, maxQty, discount%), set active, compute discounts
- Receivable tracker: list of outstanding receivables, due dates, aging, receive payment, mark paid
- B2B invoice: generate ETA-compliant invoice with QR code and seal hash, sign, send to customer
- Purchase order: receive from supplier, update stock, record cost
- Cash register: scan SKU, apply price tier discount, tender payment, print receipt with invoice
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : inventory, pricing, customers, invoices, reports, billing
- Sales rep: manage customers, create price tiers, approve receivables, generate invoices
- Cashier: scan items, apply price tier discount, tender payment, print receipt
- Accountant: receivables aging, invoice verification, ledger export

## 5. Reports and KPIs

- Sales by day and hour: revenue per period, peak hours
- Price tier performance: which tiers are active, how much volume each tier drives
- Receivables aging: total outstanding, by due date bucket, collection rate per period
- B2B invoice volume: invoices issued, paid, outstanding per period
- Customer credit: total credit used vs limit, top customers by volume

## 6. Integrations that matter

- ETA e-invoice signer (server-side) for generating QR code and seal hash
- Esc/POS thermal printer for receipts and invoices
- WhatsApp deep link for customer receivable notifications and invoice copies
- Email for invoice delivery (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Distributor basics: name, branch, address, phone, currency, working hours
- Initial product list: the starting catalogue with SKU, prices and price tier structure
- Price tier scheme: the min/max qty and discount levels the distributor uses
- Customer setup: the first B2B customer with credit limit and payment terms
- First week plan: add first product, set first price tier, first customer, first invoice

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
- i
- c
- e
-  
- t
- i
- e
- r
-  
- s
- y
- s
- t
- e
- m
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

- جملة وتوزيع
- أسعار متدرجة، ذمم مدينة وفواتيرETA من لوحة واحدة
- أسعار متدرجة حسب الكمية
- متابعة الذمم المدينة
- فواتير ETA التلقائية

Questions the page must answer:

- كيف أُنشئ سعراً متدرجاً؟
- ما هي شروط الائتمان للعملاء؟

### English

- Wholesale & Distribution Management
- Tiered pricing, receivables and B2B invoicing from one dashboard
- Tiered pricing by volume with min/max qty and discount
- Receivables aging and collection tracking
- ETA-compliant B2B invoicing with QR code

Questions the page must answer:

- How do I create a price tier?
- What are the credit terms for customers?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Product catalogue: grid of products with name, price per unit, min/max order qty, price tier badge
- Product detail: full info, all active price tiers, cost, min/max qty
- Customer account: credit limit, credit used, payment terms, status, rep assigned, receivables list
- Price tier manager: add/edit tier (minQty, maxQty, discount%), set active, compute discounts
- Receivable tracker: list of outstanding receivables, due dates, aging, receive payment, mark paid
- B2B invoice: generate ETA-compliant invoice with QR code and seal hash, sign, send to customer

## 9. Pricing tier notes

- - Starter: 200 EGP / month, 1 branch, up to 150 products
- - Professional: 450 EGP / month, unlimited products, receivables module
- - Enterprise: custom for wholesale distributor networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Dukaan | from 500 EGP/mo | no price tier system | full tiered pricing by volume with min/max qty and auto discount |
| Watania | from 480 EGP/mo | no receivables aging | full receivables aging with due date buckets and collection rate |
| Tasheel | from 520 EGP/mo | no ETA B2B invoice | full ETA invoicing with QR code and seal hash |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-wholesale-distribution-tasks.md`:

1. Add product catalogue with price tier badges (M1)
2. Add price tier manager (M1)
3. Add customer account with credit and receivables (M1)
4. Add receivable tracker with due dates and aging (M1)
5. Add B2B invoice generator with ETA signing (M2)
6. Add cash register with price tier discount (M1)
7. Add receivables aging report (M2)
8. Add B2B invoice volume report (M2)
9. Add customer credit report (M2)
10. Add onboarding flow for initial wholesale setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes customer and receivable records unrecoverable
- WhatsApp template rejection if not approved by Meta
- ETA invoicing without proper spec sign-off can violate tax law
- Credit extended without clear limits and terms can violate consumer protection law

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-wholesale-distribution-tasks.md`
