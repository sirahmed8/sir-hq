# SIR Business sector: Stationery and gifts (هدايا ومكتبة)

> Round r56 (2026-11-12). Sector 20 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `retail`, group `retail`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The gift and stationery shop owner manages a curated inventory of wrapping paper, greeting cards, engravable items and event souvenirs. Their day is custom orders, gift packing and personalisation requests.

Why this sector is in the catalogue: Gift shops and stationery stores need gift wrap, personalisation engraving and event management. Different from regular retail: the focus is on customisation and occasion-based selling.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Product (id, shopId, sku, nameAr, nameEn, category, unitPricePiasters, costPiasters, taxRate, isPersonalisable, personalisationNotes, condition, status, locationShelf)
- Customer (id, shopId, name, phone, whatsAppOptIn, purchaseHistoryCount, totalSpentPiasters, notes)
- Order (id, shopId, customerId, lines, totalsPiasters, discountPiasters, serviceChargePiasters, paymentMethod, status, createdAt, closedAt)
- OrderLine (id, orderId, productId, quantity, unitPricePiasters, personalisationDetails, note)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: piece, set, pack, meter

Batches: No : stationery shop carries no stock or expiry

Expiry and shelf life: Not applicable. Products have condition states not expiry dates

Sector specific structures: The core structures are the personalisable product flag, the order with personalisation details and the gift-wrap selection. Personalisation is the key differentiator from regular retail.

## 3. Screens and workflows that belong to this sector

- Product catalogue: grid of items with name, price, condition, personalisable badge
- Product detail: full item info, personalisation options, engraving text preview
- Gift wrap selector: wrapping paper, ribbon, card options, preview of packaged item
- Customer profile: purchase history, total spent, notes, opt-in status
- Order creation: add items, select gift wrap, add personalisation, apply discount, tender payment
- Cash register: scan items, apply gift wrap, tender payment, print receipt with gift note
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : inventory, pricing, reports, billing
- Cashier: scan items, apply gift wrap, tender payment, print receipt
- Stock clerk: receive shipments, update stock, relocate products
- Assistant: personalisation orders, special gift requests

## 5. Reports and KPIs

- Sales by day and hour: revenue per period, peak hours
- Personalisation volume: number of items with engraving per period, revenue from personalisation
- Customer lifetime value: total spent, visit frequency, average ticket
- Order average: items per order, gift wrap rate, personalisation rate
- Inventory aging: how long items have been in stock by category

## 6. Integrations that matter

- Barcode scanner for SKU entry at till
- Esc/POS thermal printer for receipts and gift notes
- WhatsApp deep link for customer notifications (ready order, personalisation complete)
- Email for invoice and special order updates (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial inventory: the starting product list with names, prices and personalisable flag
- Product categories: wrapping paper, greeting cards, engravable items, event souvenirs
- Staff: add the initial team with their role templates
- First week plan: receive first shipment, list first products, first customer sale with personalisation

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
- e
- r
- s
- o
- n
- a
- l
- i
- s
- a
- b
- l
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

- هدايا ومكتبة
- تفليف وهدايا من لوحة واحدة
- خيارات التغليف والتفليف
- خدمة النقش والنقش على الهدايا
- طلبات مناسبات مخصصة

Questions the page must answer:

- هل يمكن نقش اسم على الهدية؟
- ما هي خيوات التغليف المتوفرة؟

### English

- Stationery & Gifts Management
- Gift wrap, personalisation and event orders from one dashboard
- Gift wrap and packaging options
- Personalisation (engraving, monogramming)
- Occasion-based order management

Questions the page must answer:

- Can I engrave a name on the gift?
- What wrapping options are available?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Product catalogue: grid of items with name, price, condition, personalisable badge
- Product detail: full item info, personalisation options, engraving text preview
- Gift wrap selector: wrapping paper, ribbon, card options, preview of packaged item
- Customer profile: purchase history, total spent, notes, opt-in status
- Order creation: add items, select gift wrap, add personalisation, apply discount, tender payment
- Cash register: scan items, apply gift wrap, tender payment, print receipt with gift note

## 9. Pricing tier notes

- - Starter: 90 EGP / month, 1 branch, up to 30 products
- - Professional: 200 EGP / month, unlimited products, reports
- - Enterprise: custom for gift-and-stationery chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Giftify | from 220 EGP/mo | no personalisation engraving flow | full engraving/monogramming flow with text preview |
| Tahaddi | from 200 EGP/mo | no gift wrap selector | visual gift wrap selector with preview |
| Hadiyya | from 230 EGP/mo | no customer purchase history | customer LTV and order history reports |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-stationery-gifts-tasks.md`:

1. Add product catalogue with personalisable flag (M1)
2. Add gift wrap selector with preview (M1)
3. Add personalisation text preview (M1)
4. Add customer profile with purchase history (M1)
5. Add order creation with gift wrap and personalisation (M2)
6. Add cash register with gift wrap and scanning (M2)
7. Add customer LTV report (M3)
8. Add order average report (items, gift wrap, personalisation rates) (M3)
9. Add inventory aging report by category (M4)
10. Add onboarding flow for initial gift shop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- No special-category data risks (retail sales model)
- Encryption key loss makes product records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Personalisation text that violates consumer protection or contains disallowed content

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-stationery-gifts-tasks.md`
