# SIR Business sector: Juice and drinks (عصائر ومشروبات)

> Round r56 (2026-11-12). Sector 34 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `restaurant`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The juice shop owner manages a modifier-heavy POS, flavour recipes and daily fresh prep. Their day is size/extras selection, recipe adherence and waste tracking.

Why this sector is in the catalogue: Juice and beverage quick-service shops need a modifier-heavy POS (sizes, extras), daily fresh prep checklist and flavour matrix. The key is the modifier grid and daily prep checklists.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Flavour (id, shopId, nameAr, nameEn, ingredientsAr, ingredientsEn, priceDeltaPiasters, isDefault, isAvailable)
- Modifier (id, shopId, nameAr, nameEn, isRequired, optionsAr (comma-separated), optionsEn (comma-separated), priceDeltaPiasters, isAvailable)
- DailyPrep (id, shopId, date, flavoursPrepared (array), modifiersUsed (array), wastePiasters, notes)
- Order (id, shopId, lines with menuItemId, modifiers, quantity, totalPiasters, status, openedAt, closedAt)
- MenuItem (id, sectionId, nameAr, nameEn, pricePiasters, costPiasters, taxRate, isAvailable, station, prepMinutes, allergens)
- StockItem (id, nameAr, unit, costPiasters, quantity, isBatch, supplierId, reorderPoint)

Units in use: portion, glass, litre, shot, cup

Batches: Yes for fresh produce: dairy, fruit juices, shot syrups. The shop consumes the oldest batch first

Expiry and shelf life: Fresh produce has expiry dates tracked per batch; the shop sees alerts for items expiring in three days, and the waste log records what was thrown out

Sector specific structures: The core structures are the modifier-heavy POS (sizes, extras), the flavour matrix and the daily prep checklist. Modifier grid is the key differentiator from standard restaurant template.

## 3. Screens and workflows that belong to this sector

- Menu catalogue: grid of items with name, price, station, availability
- Modifier grid: sizes (small/medium/large), extras (extra shot, syrup, whipped cream), price delta per modifier, required/optional flag
- Flavour matrix: list of flavours with ingredients and price delta, default flavour flag
- Daily prep checklist: date, flavours prepared (array), modifiers used (array), waste in piasters, notes
- Order creation: select menu item, add modifiers from the grid, set quantity, compute total with modifier deltas, set status
- Order list: all orders with item, modifiers, quantity, total, status, opened/closed time
- Stock and waste: current stock levels, waste log per day, expiry alerts for batches
- Cash register: scan menu item, add modifiers, tender payment, print receipt

## 4. Roles and permissions

- Owner: everything : menu, modifiers, daily prep, reports, billing
- Cashier: scan menu item, add modifiers from grid, tender payment, print receipt
- Prep staff: follow daily prep checklist, prepare flavours and modifiers, record waste
- Manager: create modifiers and flavours, set daily prep, approve waste adjustments

## 5. Reports and KPIs

- Sales by hour and day: revenue per period, peak hours for juice sales
- Flavour popularity: which flavours sell most, revenue per flavour per period
- Modifier performance: which sizes and extras are most added, revenue per modifier per period
- Daily waste log: waste in piasters per period, reasons, trends
- Stock turnover: current stock levels, reorder frequency, waste vs stock ratio

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and waste logs
- WhatsApp deep link for daily waste summary and modifier shortages
- Email for inventory reorder requests (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial menu: the starting menu items with price, station and availability
- Modifier grid: the sizes and extras the shop uses with price deltas
- Flavour matrix: the starting flavours with ingredients and price deltas
- Daily prep checklist: the first date and the flavours to prepare
- Staff: add the initial team with their role templates
- First week plan: create first modifier, first flavour, first daily prep checklist

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
- m
- o
- d
- i
- f
- i
- e
- r
-  
- g
- r
- i
- d
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

- عصائر ومشروبات
- مقاسات وإضافات من لوحة واحدة
- مصفوفة المقاسات والإضافات
- مصفوفة النكهات
- قائمة التحضير اليومية

Questions the page must answer:

- ما المقاسات المتوفرة؟
- ما النكهات المتوفرة؟

### English

- Juice & Drinks Management
- Modifier-heavy POS, flavour matrix and daily prep from one dashboard
- Modifier-heavy POS with sizes and extras
- Flavour matrix with ingredients and pricing
- Daily prep checklist and waste tracking

Questions the page must answer:

- What sizes are available?
- What flavours are available?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Menu catalogue: grid of items with name, price, station, availability
- Modifier grid: sizes (small/medium/large), extras (extra shot, syrup, whipped cream), price delta per modifier, required/optional flag
- Flavour matrix: list of flavours with ingredients and price delta, default flavour flag
- Daily prep checklist: date, flavours prepared (array), modifiers used (array), waste in piasters, notes
- Order creation: select menu item, add modifiers from the grid, set quantity, compute total with modifier deltas, set status
- Order list: all orders with item, modifiers, quantity, total, status, opened/closed time

## 9. Pricing tier notes

- - Starter: 130 EGP / month, 1 branch, up to 30 menu items
- - Professional: 280 EGP / month, unlimited items, modifier module
- - Enterprise: custom for juice shop chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| JuicePro | from 350 EGP/mo | no modifier grid | full modifier grid with sizes, extras and price deltas |
| FreshJuice | from 330 EGP/mo | no daily prep checklist | daily prep checklist with flavours, modifiers and waste tracking |
| DrinkPoint | from 380 EGP/mo | no flavour matrix | full flavour matrix with ingredients and price deltas |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-juice-beverage-tasks.md`:

1. Add modifier grid with sizes and extras (M1)
2. Add flavour matrix (M1)
3. Add daily prep checklist (M1)
4. Add order creation with modifiers (M1)
5. Add sales by hour report (M1)
6. Add flavour popularity report (M1)
7. Add modifier performance report (M1)
8. Add daily waste log report (M1)
9. Add stock turnover report (M1)
10. Add onboarding flow for initial juice shop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes menu and order records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Waste tracking without proper audit can lead to inventory discrepancies
- Modifier grid without price delta validation can cause revenue leakage

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-juice-beverage-tasks.md`
