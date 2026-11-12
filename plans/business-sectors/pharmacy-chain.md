# SIR Business sector: Pharmacy chain (سلسلة صيدليات)

> Round r56 (2026-11-12). Sector 41 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `pharmacy + branches`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The pharmacy chain owner manages multiple branch pharmacies under one account. Their day is branch stock visibility, centralised purchasing and ensuring each branch FEFO compliance and controlled-drug log.

Why this sector is in the catalogue: Pharmacy chains are common in Egypt. They need multi-branch support, centralised buying and the same FEFO/expiry/controlled-drug logic as a single pharmacy but across many locations. The owner owns several businesses on one bill.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Chain (id, nameAr, nameEn, ownerId, taxRegistration, currency, openingHours, branchesCount, isActive)
- Branch (id, chainId, nameAr, nameEn, address, phone, currency, taxRegistration, openingHours, fe4oEnabled, controlledDrugEnabled)
- PharmacyProduct (id, branchId, sku, nameAr, nameEn, activeIngredient, pricePiasters, costPiasters, taxRate, fe4oFlag, expiryDate, supplierId, status, locationShelf)
- Supplier (id, chainId, name, phone, paymentTerms, visitDays, leadTimeDays, isPreferred)
- PurchaseOrder (id, branchId, supplierId, status, lines, expectedAt, totalPiasters)
- ControlledDrugLog (id, branchId, drugName, batchId, quantityPiasters, dateIn, dateOut, authorisedBy, reason, status (administered/sold/wasted))
- Employee (id, branchId, name, phone, role, hourlyRatePiasters, status)
- ChainAuditLog (id, chainId, action, performedBy, performedAt, notes)

Units in use: batch, box, bottle, tube

Batches: Yes for all drugs and food: batches with supplier, received date, expiry date and cost, so each branch can sell by batch and claim credit

Expiry and shelf life: Each branch sees alerts for items expiring in 30/60/90 days; central view shows aggregate expiry across all branches

Sector specific structures: The core structures are the chain with branches, the per-branch pharmacy product with FEFO and the centralised controlled-drug log per branch. Multi-branch support with shared central buying is the key differentiator from a single pharmacy.

## 3. Screens and workflows that belong to this sector

- Chain overview: all branches, branch stock summary, central buying dashboard, expiry aggregate view
- Branch selector: switch between branches, view branch-specific data (products, controlled log, staff)
- Product catalogue per branch: grid of pharmacy products with name, active ingredient, price, FEFO badge, expiry date badge, stock qty
- FEFO food radar per branch: items expiring in 30/60/90 days, value at risk, one-tap discount tag
- Controlled drug log per branch: append-only list of administered/sold/wasted drugs with date, batch, quantity, authorised user
- Supplier management: list of suppliers per chain, preferred flag, lead time, contact
- Purchase order: create per branch, receive from supplier, update branch stock
- Cash register per branch: scan SKU or product, apply FEFO discount if urgent, tender payment, print receipt with branch name

## 4. Roles and permissions

- Owner: everything : chain, branches, products, controlled logs, reports, billing across all branches
- Branch manager: manage branch products, controlled log, staff, purchase orders, view chain overview
- Pharmacist: per branch - manage products, controlled drug log, approve administration,
- Cashier: per branch - scan products, tender payment, print receipt

## 5. Reports and KPIs

- Chain-wide expiry aggregate: items expiring in 30/60/90 days across all branches, total value at risk
- Branch product sales: which products sell most per branch, revenue per branch per period
- Controlled drug log per branch: administered vs sold vs wasted counts per period, audit trail per branch
- Centralised buying: purchase orders created, received, total spend per period, preferred supplier performance
- FEFO food radar aggregate: total items expiring across all branches, discounts applied across chain

## 6. Integrations that matter

- Esc/POS thermal printer per branch for receipts and controlled log records
- WhatsApp deep link per branch for stock alerts and supplier contact
- Email for purchase order updates and supplier contracts (opt-in)
- Centralised dashboard: Firebase for chain-wide data, branch-level IndexedDB for local ops

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Chain basics: name, owner, tax registration, currency, opening hours, initial branch count
- Initial branch: the first branch address, phone, currency, opening hours, FEFO and controlled drug enabled flag
- Initial product list: the starting pharmacy product list per branch with SKU, active ingredient, price and FEFO flag
- Supplier list: the first preferred supplier with terms and lead time
- First week plan: create first branch, first product, first purchase order

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
- h
- a
- i
- n
- /
- b
- r
- a
- n
- c
- h
- /
- p
- h
- a
- r
- m
- a
- c
- y
-  
- p
- r
- o
- d
- u
- c
- t
- /
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

- سلسلة صيدليات
- فروع، مشتريات مركزية وتracking FEFO من لوحة واحدة
- عرض مركزي لجميع الفروع
- مشتريات مركزية
- Tracking FEFO مركزي

Questions the page must answer:

- كيف أضيف فرع جديد؟
- كيف أشرف على المشتريات المركزية؟

### English

- Pharmacy Chain Management
- Chain, branches, central buying and FEFO tracking from one dashboard
- Chain overview with all branches
- Centralised buying and supplier management
- FEFO tracking across all branches

Questions the page must answer:

- How do I add a new branch?
- How do I manage central buying?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Chain overview: all branches, branch stock summary, central buying dashboard, expiry aggregate view
- Branch selector: switch between branches, view branch-specific data (products, controlled log, staff)
- Product catalogue per branch: grid of pharmacy products with name, active ingredient, price, FEFO badge, expiry date badge, stock qty
- FEFO food radar per branch: items expiring in 30/60/90 days, value at risk, one-tap discount tag
- Controlled drug log per branch: append-only list of administered/sold/wasted drugs with date, batch, quantity, authorised user
- Supplier management: list of suppliers per chain, preferred flag, lead time, contact

## 9. Pricing tier notes

- - Starter: 300 EGP / month, 1 branch, up to 20 products per branch
- - Professional: 600 EGP / month, unlimited products per branch, centralised buying module
- - Enterprise: custom for pharmacy chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| ChainCare | from 700 EGP/mo | no centralised buying module | full centralised buying with supplier management and purchase orders per branch |
| Pharmachain | from 680 EGP/mo | no FEFO aggregate view | chain-wide FEFO aggregate: items expiring across all branches and total value at risk |
| Medichain | from 720 EGP/mo | no branch switching | single UX to switch between all branches with all data per branch |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-pharmacy-chain-tasks.md`:

1. Add chain overview with branch switching (M1)
2. Add branch-specific product catalogue with FEFO (M1)
3. Add FEFO food radar per branch (M1)
4. Add controlled drug log per branch (M1)
5. Add supplier management per chain (M1)
6. Add purchase order per branch (M1)
7. Add cash register per branch with FEFO discount (M1)
8. Add chain-wide expiry aggregate report (M1)
9. Add branch product sales report (M1)
10. Add controlled drug log per branch audit report (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes chain and branch records unrecoverable across all branches
- WhatsApp template rejection if not approved by Meta
- FEFO expiry without proper batch tracking can safety-compromise patients across branches
- Centralised buying without clear audit per branch can violate legal requirements on per-branch reporting

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-pharmacy-chain-tasks.md`
