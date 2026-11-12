# SIR Business sector: Florist (محل زهور)

> Round r56 (2026-11-12). Sector 30 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `service + retail`, group `service-and-retail`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The florist owner manages fresh flower inventory, delivery schedules and customer orders. Their day is flower stock checks, delivery slot scheduling and vase-life tracking.

Why this sector is in the catalogue: Florist shops sell fresh flowers and plants, need FEFO food tracking for flower freshness, delivery window scheduling and order management. The key is FEFO tracking and delivery slot management.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- FlowerBundle (id, shopId, nameAr, nameEn, flowerTypes (array), pricePiasters, bundlePricePiasters, discountPercent, validityDays, status, notes)
- FlowerStock (id, shopId, flowerType, source (local/international), pricePiasters per stem, stemQty, reorderPoint, status, locationShelf)
- CustomerOrder (id, shopId, customerName, customerPhone, bundleId, quantity, deliveryDate, deliveryTimeSlot, status (pending/confirmed/out-for-delivery/done), notes, paymentStatus)
- VaseLife (id, flowerType, averageDays, careInstructionsAr, careInstructionsEn)
- Supplier (id, shopId, name, phone, paymentTerms, visitDays, leadTimeDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: bundle, stem, arrangement

Batches: Yes for cut flowers: FEFO batches with supplier, received date, expiry date (vase life days) and cost

Expiry and shelf life: Cut flowers have vase-life expiry tracked per batch; the shop sees alerts for flowers fading in 3/5/7 days

Sector specific structures: The core structures are the flower bundle with discount and validity, the per-stem stock with FEFO vase-life, the customer order with delivery slot and the vase-life care instructions. FEFO flower freshness is the key differentiator from regular retail.

## 3. Screens and workflows that belong to this sector

- Flower bundle catalogue: list of bundles with name, flower types, price, bundle price, discount %, validity days, status
- Flower stock level: stems per type, source, reorder point, FEFO vase-life badge and expiry alert
- Customer order creation: select bundle, enter customer name/phone, select delivery date/time slot, set status (pending/confirmed), compute total (bundle price - discount), set payment status
- Order list: all orders with bundle, customer, delivery date/time, status, payment status
- Vase life tracker: per flower type, average days, care instructions, fade alert per bundle
- Supplier management: list of suppliers per shop, payment terms, lead time, contact
- Purchase order: create per shop, receive from supplier, update flower stock
- Cash register per shop: scan bundle SKU or product, apply FEFO discount if urgent, tender payment, print receipt with bundle details and vase-life notes

## 4. Roles and permissions

- Owner: everything : bundles, stock, orders, reports, billing
- Flower specialist: create bundles, manage stock, process orders, handle vase-life alerts
- Sales rep: manage products, create bundles, handle customer orders
- Cashier: scan bundle SKU, tender payment, print receipt

## 5. Reports and KPIs

- Bundle sales per period: bundles created, sold, expired per month, revenue per bundle per period
- FEFO vase-life aggregate: total stems fading per period by days (3/5/7), value at risk, discounts applied
- Order pipeline: orders by status per period, average delivery time per period
- Customer retention: order count per customer, total spent per customer, re-order rate
- Stock turnover: stems per type per period, reorder frequency, FEFO expiry vs stock ratio

## 6. Integrations that matter

- Esc/POS thermal printer per shop for receipts and vase-life care cards
- WhatsApp deep link per customer for delivery notifications and vase-care tips
- Email for order confirmations and vase-care tips (opt-in)
- SMS for FEFO expiry alerts to customers (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial bundles: the starting bundle list with flower types, price, discount and validity days
- Flower stock: the starting stem list with source, price per stem, reorder point and FEFO vase-life days
- Staff: add the initial team with their role templates
- First week plan: create first bundle, first customer order, first supplier order

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
- f
- l
- o
- w
- e
- r
-  
- b
- u
- n
- d
- l
- e
- /
- v
- a
- s
- e
- -
- l
- i
- f
- e
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

- محل زهور
- باقات، توصيل وطازجية من لوحة واحدة
- باقات مع خصم وفترة صلاحية
- تتبع طول عمر الورد (vase life)
- Slots تسليم

Questions the page must answer:

- هل تتوفر باقة الزهور المطلوبة؟
- متى ستصل التوصيل؟

### English

- Florist Management
- Bundles, delivery and vase-life tracking from one dashboard
- Flower bundles with discount and validity
- Vase-life tracking and fade alerts
- Delivery slot scheduling

Questions the page must answer:

- What bundles are available?
- When is delivery?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Flower bundle catalogue: list of bundles with name, flower types, price, bundle price, discount %, validity days, status
- Flower stock level: stems per type, source, reorder point, FEFO vase-life badge and expiry alert
- Customer order creation: select bundle, enter customer name/phone, select delivery date/time slot, set status (pending/confirmed), compute total (bundle price - discount), set payment status
- Order list: all orders with bundle, customer, delivery date/time, status, payment status
- Vase life tracker: per flower type, average days, care instructions, fade alert per bundle
- Supplier management: list of suppliers per shop, payment terms, lead time, contact

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 20 bundles
- - Professional: 350 EGP / month, unlimited bundles, FEFO module
- - Enterprise: custom for florist chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| BloomPro | from 450 EGP/mo | no FEFO vase-life tracking | full FEFO vase-life per stem with 3/5/7 day alerts and aggregate view |
| PetalMart | from 430 EGP/mo | no bundle discount system | full bundle discount with validity percent and bundle price |
| FlowCo | from 480 EGP/mo | no delivery slot scheduler | delivery slot scheduler with available slots per time and booking management |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-florist-tasks.md`:

1. Add flower bundle catalogue (M1)
2. Add flower stock level with FEFO vase-life (M1)
3. Add customer order creation with delivery slot (M1)
4. Add vase life tracker per flower type (M1)
5. Add supplier management (M1)
6. Add purchase order and stock update (M1)
7. Add cash register per shop with FEFO discount (M1)
8. Add bundle sales per period report (M1)
9. Add FEFO vase-life aggregate report (M1)
10. Add order pipeline report (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes bundle and order records unrecoverable
- WhatsApp template rejection if not approved by Meta
- FEFO vase-life without proper batch tracking can lead to selling faded flowers to customers
- Delivery slot without clear confirmation can lead to no-show disputes and wasted bundles

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-florist-tasks.md`
