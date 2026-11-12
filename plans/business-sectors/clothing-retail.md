# SIR Business sector: Clothing retail (ملابس)

> Round r56 (2026-11-12). Sector 16 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `retail`, group `retail`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The clothing shop owner manages a variant-heavy inventory of apparel, seasonal collections and markdowns. Their day is receiving new collections, pricing per variant and tracking exchanges.

Why this sector is in the catalogue: Clothing shops need size/color matrix, variants, seasonal collections, markdowns and exchange rules. The key is the variant matrix and markdown tracking.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Product (id, shopId, sku, nameAr, nameEn, category (tops/ bottoms/dresses/accessories), season, colorAr, colorEn, sizeAr, sizeEn, unitPricePiasters, costPiasters, taxRate, condition (new/used), stockQty, status, locationShelf)
- Variant (id, productId, colorId, sizeId, skuSuffix, priceDeltaPiasters, isDefault, stockQty)
- Customer (id, shopId, name, phone, whatsAppOptIn, purchaseHistoryCount, totalSpentPiasters)
- Order (id, shopId, customerId, lines with productId variantId, quantity, unitPricePiasters, discountPiasters, serviceChargePiasters, totalPiasters, paymentStatus, status, createdAt, closedAt)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: piece, set, pair

Batches: No : clothing retail carries no stock or expiry (condition indicates wear, not expiry)

Expiry and shelf life: Not applicable. Products have condition states not expiry dates

Sector specific structures: The core structures are the product variant matrix (color + size per SKU), the markdown tracker and the exchange log. Variant tracking per color/size is the key differentiator from regular retail.

## 3. Screens and workflows that belong to this sector

- Product catalogue: grid of items with name, price, color badge, size badge, condition (new/used), availability
- Product detail: full info, all color/size variants, stock per variant, markdown percentage, exchange policy
- Variant manager: add/edit variant (color, size, price delta, default flag, stock qty). Done when variant is saved and linked to product.
- Markdown tracker: set markdown % per product per period, track original price vs discounted price, apply at till
- Exchange log: record exchange reason (size/color/defect), update stock, issue refund note
- Customer profile: purchase history, total spent, notes, opt-in status
- Cash register: scan SKU or variant, apply markdown/discount, tender payment, print receipt
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : inventory, pricing, markdowns, exchanges, reports, billing
- Sales rep: manage products, create variants, apply markdowns, handle exchanges
- Cashier: scan items, apply markdown/discount, tender payment, print receipt
- Stock clerk: receive shipments, update stock, create variants, process exchanges

## 5. Reports and KPIs

- Sales by day and hour: revenue per period, peak hours
- Variant performance: which color/size combinations sell most, revenue per variant per period
- Markdown effectiveness: original price vs discounted price per period, sell-through rate at discount
- Exchange volume: exchanges per period, reasons, refund amount per period
- Customer repeat rate: visit count per customer, total spent per customer, re-book rate

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and exchange notes
- WhatsApp deep link for customer notifications (exchange ready, markdown alerts)
- Email for invoice and exchange confirmation (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial inventory: the starting product list with SKU, colors, sizes, prices and condition
- Product categories: tops, bottoms, dresses, accessories, seasonal collections
- Staff: add the initial team with their role templates
- First week plan: receive first collection, list first products, first customer sale with variant selection

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
- v
- a
- r
- i
- a
- n
- t
-  
- m
- a
- t
- r
- i
- x
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

- ملابس
- مقاسات وألوان وماركات من لوحة واحدة
- كتالوج منتجات ب Variants
- تعقّب الماركات
- خدمة الاستبدال

Questions the page must answer:

- هل تتوفر المقاس/اللون المطلوب؟
- كيف أقوم باستبدال المنتج؟

### English

- Clothing Retail Management
- Variant matrix, markdowns and exchanges from one dashboard
- Variant matrix (color + size per SKU)
- Markdown tracking with sell-through analysis
- Exchange log and refund processing

Questions the page must answer:

- What color/size combinations are available?
- How do I process an exchange?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Product catalogue: grid of items with name, price, color badge, size badge, condition (new/used), availability
- Product detail: full info, all color/size variants, stock per variant, markdown percentage, exchange policy
- Variant manager: add/edit variant (color, size, price delta, default flag, stock qty). Done when variant is saved and linked to product.
- Markdown tracker: set markdown % per product per period, track original price vs discounted price, apply at till
- Exchange log: record exchange reason (size/color/defect), update stock, issue refund note
- Customer profile: purchase history, total spent, notes, opt-in status

## 9. Pricing tier notes

- - Starter: 130 EGP / month, 1 branch, up to 50 products
- - Professional: 300 EGP / month, unlimited products, variant module
- - Enterprise: custom for clothing retail chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| FashionPro | from 400 EGP/mo | no variant tracking | full color/size variant tracking per SKU with price deltas |
| StyleMart | from 380 EGP/mo | no markdown tracker | full markdown tracker with original/discounted price and sell-through rate |
| Wardrobe | from 420 EGP/mo | no exchange log | full exchange log with reason, stock update and refund note |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-clothing-retail-tasks.md`:

1. Add product catalogue with color/size badges (M1)
2. Add variant manager (M1)
3. Add markdown tracker (M1)
4. Add exchange log (M1)
5. Add customer profile with purchase history (M1)
6. Add cash register with variant scanning and markdown (M1)
7. Add variant performance report (M2)
8. Add markdown effectiveness report (M2)
9. Add exchange volume report (M2)
10. Add onboarding flow for initial clothing shop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes product and order records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Markdown without clear criteria can lead to revenue loss and customer disputes
- Exchange descriptions that violate consumer protection law on refunds

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-clothing-retail-tasks.md`
