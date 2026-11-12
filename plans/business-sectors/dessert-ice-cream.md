# SIR Business sector: Dessert and ice cream (حلويات وأيس كريم)

> Round r56 (2026-11-12). Sector 35 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `restaurant + retail`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The dessert shop manager manages flavour variants, marble-slab assembly and delivery bundles. Their day is flavour selection, assembly instructions and bundle creation.

Why this sector is in the catalogue: Dessert and ice cream shops need a flavour matrix (variants), marble-slab style assembly notes and delivery promo bundles. The key is the flavour variants and assembly notes.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Flavour (id, shopId, nameAr, nameEn, variantAr (comma-separated), variantEn (comma-separated), baseType (iceCream/sorbet), pricePiasters, costPiasters, taxRate, isAvailable, isDefault)
- AssemblyNote (id, shopId, flavourId, stepsAr (comma-separated), stepsEn (comma-separated), isDefault)
- Order (id, shopId, lines with flavourId, quantity, totalPiasters, status, openedAt, closedAt)
- DeliveryBundle (id, shopId, flavourIds (comma-separated), discountPercent, bundlePricePiasters, status, createdAt)
- MenuItem (id, sectionId, nameAr, nameEn, pricePiasters, costPiasters, taxRate, isAvailable, station, prepMinutes)
- StockItem (id, nameAr, unit, costPiasters, quantity, isBatch, supplierId, reorderPoint)

Units in use: portion, scoop, bundle

Batches: Yes for dairy and cream: batches with supplier, received date, expiry date and cost

Expiry and shelf life: Dairy and cream have expiry dates tracked per batch; the shop sees alerts for items expiring in three days, and the waste log records what was thrown out

Sector specific structures: The core structures are the flavour matrix with variants, the assembly notes per flavour and the delivery bundle system. Flavour variants are the key differentiator from standard restaurant template.

## 3. Screens and workflows that belong to this sector

- Flavour catalogue: grid of flavours with name, variants (Ar/En), base type, price, default flag
- Assembly notes editor: select flavour, enter steps Ar/En (marble-slab style), set as default
- Order creation: select flavour, set quantity, compute total, apply bundle discount if applicable, set status
- Bundle manager: select flavour IDs, set discount percentage, set bundle price, set status (active/inactive)
- Order list: all orders with flavour, quantity, total, status, opened/closed time
- Flavour popularity: which flavours sell most, revenue per flavour per period
- Stock and waste: current stock levels, waste log per day, expiry alerts for batches
- Cash register: select flavour, set quantity, apply bundle if applicable, tender payment, print receipt

## 4. Roles and permissions

- Owner: everything : flavours, assembly notes, bundles, reports, billing
- Prep staff: follow assembly notes, prepare marble-slab, record waste
- Cashier: select flavour, set quantity, apply bundle if applicable, tender payment, print receipt
- Manager: create flavours and assembly notes, set bundles, approve waste adjustments

## 5. Reports and KPIs

- Flavour sales per period: which flavours sell most, revenue per flavour per month
- Bundle volume per period: how many bundles created, revenue per bundle per period
- Daily waste log: waste in piasters per period, reasons, trends
- Flavour popularity trend: which flavours gaining/losing popularity per month
- Stock turnover: current stock levels, reorder frequency, waste vs stock ratio

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and bundle notes
- WhatsApp deep link for bundle ready-notice and flavour shortage alerts
- Email for inventory reorder requests (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial flavours: the starting flavour list with variants and default flag
- Assembly notes: the starting marble-slab assembly steps per flavour
- Bundle structure: the initial bundle (which flavours, discount percent, bundle price)
- Staff: add the initial team with their role templates
- First week plan: create first flavour, first assembly notes, first bundle

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
- a
- v
- o
- u
- r
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

- حلويات وأيس كريم
- نكهات، تركيبات وتجميعات من لوحة واحدة
- مصفوفة نكهات بمتغيرات
- ملاحظات التجميع marble-slab style
- حزم التوصيل مع خصم

Questions the page must answer:

- ما النكهات المتوفرة؟
- هل هناك حزم توصيل؟

### English

- Dessert & Ice Cream Management
- Flavour matrix, assembly notes and delivery bundles from one dashboard
- Flavour matrix with variants and defaults
- Marble-slab assembly notes per flavour
- Delivery bundle system with discount

Questions the page must answer:

- What flavours are available?
- Are there delivery bundles?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Flavour catalogue: grid of flavours with name, variants (Ar/En), base type, price, default flag
- Assembly notes editor: select flavour, enter steps Ar/En (marble-slab style), set as default
- Order creation: select flavour, set quantity, compute total, apply bundle discount if applicable, set status
- Bundle manager: select flavour IDs, set discount percentage, set bundle price, set status (active/inactive)
- Order list: all orders with flavour, quantity, total, status, opened/closed time
- Flavour popularity: which flavours sell most, revenue per flavour per period

## 9. Pricing tier notes

- - Starter: 140 EGP / month, 1 branch, up to 25 flavours
- - Professional: 300 EGP / month, unlimited flavours, bundle module
- - Enterprise: custom for dessert shop chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| SweetSpot | from 400 EGP/mo | no flavour variants | full flavour variants (Ar/En) with base type and default flag |
| CoolBite | from 380 EGP/mo | no assembly notes | marble-slab assembly notes per flavour with Ar/En steps |
| TreatCo | from 420 EGP/mo | no bundle system | full bundle system with discount percent and bundle price |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-dessert-ice-cream-tasks.md`:

1. Add flavour catalogue with variants (M1)
2. Add assembly notes editor (M1)
3. Add bundle manager (M1)
4. Add order creation with bundle discount (M1)
5. Add flavour popularity report (M1)
6. Add bundle volume report (M1)
7. Add daily waste log report (M1)
8. Add stock turnover report (M1)
9. Add onboarding flow for initial dessert shop setup (M1)
10. Add flavour popularity trend report (M2)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes flavour and order records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Bundle discount without clear criteria can lead to revenue loss
- Flavour variant descriptions that mislead consumers can violate consumer protection law

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-dessert-ice-cream-tasks.md`
