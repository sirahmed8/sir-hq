# SIR Business sector: Hardware and materials (عدد ومواد بناء)

> Round r56 (2026-11-12). Sector 18 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `market + b2b`, group `retail-and-commerce`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The hardware store owner manages a large inventory of building materials, contractor credit accounts and delivery scheduling. Their day is price lists, credit terms and delivery run planning.

Why this sector is in the catalogue: Hardware stores sell building materials to contractors and DIY customers. They need bulk pricing, contractor accounts with credit/postpay, delivery scheduling and BOM-style quotes.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Store (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Product (id, storeId, sku, nameAr, nameEn, category, unitPricePiasters, costPiasters, taxRate, unit (kg,litre,piece,box), stockQty, status, locationShelf, isContractor)
- Contractor (id, storeId, name, phone, creditLimitPiasters, creditUsedPiasters, paymentTerms, status, assignedRep)
- Quote (id, storeId, contractorId, lines, validUntil, totalPiasters, status, approvedBy)
- DeliveryRun (id, storeId, orderIds, waypoints, estimatedDuration, actualDuration, status)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, storeId, name, phone, role, hourlyRatePiasters, status)

Units in use: kg, litre, piece, box, bundle, roll

Batches: No : hardware store carries no stock or expiry

Expiry and shelf life: Not applicable. Products have no expiry

Sector specific structures: The core structures are the contractor credit account with limit and terms, the quote system with validity period, and the delivery run scheduling. Bulk pricing per unit is the key differentiator.

## 3. Screens and workflows that belong to this sector

- Product catalogue: grid of materials with name, price per unit, unit measure, contractor badge
- Product detail: full info, bulk price breaks, supplier, reorder point
- Contractor account: credit limit, credit used, payment terms, status, assigned rep, history
- Quote editor: select lines, set valid until, compute total, approve/reject
- Delivery scheduler: assign orders to run, view waypoints, ETA, update status
- Purchase order: receive from supplier, update stock, record costs
- Cash register: scan SKU, apply contractor discount, tender payment, print receipt
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : inventory, pricing, contractors, reports, billing
- Sales rep: manage contractors, create quotes, approve deliveries
- Cashier: scan items, apply contractor discount, tender payment, print receipt
- Stock clerk: receive shipments, update stock, create quotes

## 5. Reports and KPIs

- Sales by day and hour: revenue per period, peak hours
- Contractor credit: total credit used vs limit, aging of outstanding, top contractors
- Quote volume: quotes created, approved, rejected per period
- Delivery run efficiency: orders per run, on-time rate, average duration
- Inventory aging: items in stock by category and how long

## 6. Integrations that matter

- SMS gateway for contractor notifications (credit reminder, delivery ETA)
- Esc/POS thermal printer for receipts and quotes
- WhatsApp deep link for contractor order status and delivery updates
- Google Maps for delivery route planning

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial inventory: the starting material list with SKU, prices and contractor flag
- Contractor types: the contractor categories (construction, plumbing, electrical, renovation) and credit terms
- Staff: add the initial team with their role templates
- First week plan: receive first shipment, create first contractor, first quote

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
- c
- o
- n
- t
- r
- a
- c
- t
- o
- r
-  
- c
- r
- e
- d
- i
- t
-  
- f
- l
- a
- g
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

- أدوات ومواد بناء
- أسعار الجملة، الحسابات وتصميم الحصص من لوحة واحدة
- أسعار بالجملة للكميات الكبيرة
- حسابات المقاولين مع مدة الائتمان
- جدولة توصيل الطلبات

Questions the page must answer:

- كيف أفتح حساب مقاول؟
- ما هي مدة الائتمان المتاحة؟

### English

- Hardware & Materials Management
- Bulk pricing, contractor accounts and delivery scheduling from one dashboard
- Bulk pricing per unit with price breaks
- Contractor credit accounts with limits and terms
- Delivery run scheduling and tracking

Questions the page must answer:

- How do I open a contractor account?
- What credit terms are available?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Product catalogue: grid of materials with name, price per unit, unit measure, contractor badge
- Product detail: full info, bulk price breaks, supplier, reorder point
- Contractor account: credit limit, credit used, payment terms, status, assigned rep, history
- Quote editor: select lines, set valid until, compute total, approve/reject
- Delivery scheduler: assign orders to run, view waypoints, ETA, update status
- Purchase order: receive from supplier, update stock, record costs

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 100 products
- - Professional: 320 EGP / month, unlimited products, contractor module
- - Enterprise: custom for hardware chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| HardwarePro | from 380 EGP/mo | no contractor credit module | full contractor credit with limits, terms and usage history |
| BldgMart | from 350 EGP/mo | no quote system with validity | full quote editor with validUntil and approve/reject |
| Sico | from 400 EGP/mo | no delivery scheduler | delivery run scheduling with waypoints and ETA tracking |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-hardware-materials-tasks.md`:

1. Add product catalogue with contractor flag (M1)
2. Add contractor account screen (M1)
3. Add quote editor with validity and approval (M1)
4. Add delivery scheduler with waypoints and ETA (M1)
5. Add cash register with contractor discount (M2)
6. Add contractor credit aging report (M2)
7. Add quote volume report (M2)
8. Add delivery run efficiency report (M2)
9. Add inventory aging report by category (M3)
10. Add onboarding flow for initial hardware store setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes contractor records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Credit extended without clear limits and terms can violate consumer protection law
- SMS template rejection if not approved by mobile carrier

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-hardware-materials-tasks.md`
