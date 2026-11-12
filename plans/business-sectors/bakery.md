# SIR Business sector: Bakery (مخبز وحلواني)

> Round r56 (2026-11-12). Sector 6 of 41 in `plans/business-sectors/_INDEX.md`, wave 1.
> Base template `restaurant`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner is in the shop at four in the morning while the first batch bakes, then at the counter at seven with the queue of the commuters. Their pain is the weight and the price: the customer asks for three quarters of a kilo and the shop has to be fast and exact. The second pain is yesterday bread: it is good food on the second day and a loss on the third, and the owner decides the discount by feel.

Why this sector is in the catalogue: It sells by weight and it produces during the night, so it needs the kitchen of the restaurant and the costing of the retail sector at the same time.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Bakery (id, name, branchId, address, phone, currency, openingHours, taxRegistration)
- Product (id, sku, nameAr, nameEn, categoryId, unit, unitPricePiasters, costPiasters, taxRate, isWeighed, isBatch, shelfLifeDays)
- Category (id, nameAr, nameEn, order, iconKey)
- ProductionBatch (id, productId, producedAt, quantity, costPiasters, expiresAt, status, note)
- DailyPrice (id, productId, date, pricePiasters, reason)
- Sale (id, branchId, cashierId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- SaleLine (id, saleId, productId, quantity, weightGrams, unitPricePiasters, discountPiasters, isWeighed)
- Waste (id, productId, productionBatchId, quantity, reason, loggedBy, createdAt)
- Supplier (id, nameAr, phone, paymentTerms, visitDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)
- Employee (id, name, phone, role, station, hourlyRatePiasters, status)
- StockItem (id, nameAr, unit, costPiasters, quantity, supplierId, reorderPoint)

Units in use: piece, kilo, gram, portion, pack, tray, dozen, with the weight sold per kilogram and the pastries sold per piece

Batches: Yes for everything made in house: each production batch carries the date, the quantity, the cost of the ingredients and the expiry, so the owner knows what yesterday bread cost him

Expiry and shelf life: The day old rules are per product: the shelf life, the day it becomes discounted and the day it is written off. The screen shows the batches that expire today with the quantity, and one tap writes them off with a reason

Sector specific structures: The structures specific to this sector are the production batches from the night shift, the weight based selling with the scale, the daily price changes for a holiday or a promotion, and the day old discount rule

## 3. Screens and workflows that belong to this sector

- Weighed till: the pastries and the bread by the weight, with the scale value and the price per kilogram, and the quick keys for the most sold items
- Production plan: what the night shift bakes, how much, and what was actually produced against the plan
- Day old screen: the batches that expire today, the quantity, and the discount rule or the write off
- Stock: the flour, the sugar, the butter, the fillings and the packaging, with the last count and the reorder point
- Daily price: change the price of an item for today only, with the reason written in the audit log
- Purchasing: the order to the supplier with the last price and the quantity
- Shift and the end of day: the money counted, the waste of the day in money and the number of pieces sold

## 4. Roles and permissions

- Owner: everything, including the prices and the staff
- Manager: everything except billing, approves the write offs and the price changes
- Baker: the production plan and the batches, no cash
- Cashier: the counter, the scale, the payment and the shift close
- Assistant: the counter and the stock count, no price change

## 5. Reports and KPIs

- Sales by product and by hour: the morning rush measured
- Day old waste in money per day: the loss the owner never measured
- Margin per product after the real batch cost
- Production against the plan: what was baked and what was sold
- Stock of the raw material with the days left
- Cash reconciliation per shift

## 6. Integrations that matter

- Weighing scale through the local bridge or WebSerial, with a manual weight entry as a fallback
- Thermal printer through ESC/POS for the receipt and for the batch label with the date
- Camera scanner on the phone for the stock count of the flour and the packaging
- WhatsApp for the order confirmation and for the day old offer to the regulars through the bakery own account

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Products: the items the shop sells, with the ones sold by weight marked
- Shelf life: the number of days each item stays fresh, and the rule for the day old discount
- Raw material: the flour, the sugar, the butter and the packaging with the counts
- Team: the baker, the cashier and the assistant
- Suppliers: the main suppliers with the visit days
- First week plan: weigh one item, produce one batch, close the shift, set the day old rule
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Category list in Arabic: عيش, معجنات, بيتزا, كيك, حلويات, بسكويت, كرواسون, سندويتشات
- A weight and piece unit set with the price per kilogram
- A shelf life list per category as a starting point, marked to be confirmed by the shop
- A receipt layout with the weight line and the production date for the items that are made in house
- Role templates for the baker, the cashier and the assistant

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- مخبز بيحسب بالوزن، وبيعرف خسران امبارح بالجنيه
- كاشير بالميزان، دفعات إنتاج بالليل، وقاعدة خصم اليوم التاني
- الوزن بيتحسب من الميزان والسعر للكيلو واضح على الشاشة
- دفعة الإنتاج بالليل مسجلة بالتاريخ والكمية والتكلفة
- خصم اليوم التاني قاعدة بتتحط مرة وتطبّق لوحدها

Questions the page must answer:

- الخبز التاني بيتحوّل لخصم تلقائي قبل ما يبقى هدر، والقاعدة بتحدد يوم الخصم
- ينفع أكسر الماكينة؟ لأ: الكاشير بيفضل شغال والطباعة بتطلع من الجهاز

### English

- A bakery that sells by weight and knows what yesterday bread cost
- A till with the scale, night production batches, and a day old rule you set once
- The weight comes from the scale and the price per kilo is on the screen
- The night batch is recorded with its date, its quantity and its cost
- The day old discount rule is set once and applies itself

Questions the page must answer:

- Is the day old bread thrown away? It is converted by the rule before it becomes waste, and the rule decides the discount day
- Does it work with a broken connection? Yes: the till keeps selling and the receipt prints from the device

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Weighed till: the pastries and the bread by the weight, with the scale value and the price per kilogram, and the quick keys for the most sold items
- Production plan: what the night shift bakes, how much, and what was actually produced against the plan
- Day old screen: the batches that expire today, the quantity, and the discount rule or the write off
- Stock: the flour, the sugar, the butter, the fillings and the packaging, with the last count and the reorder point
- Daily price: change the price of an item for today only, with the reason written in the audit log
- Purchasing: the order to the supplier with the last price and the quantity

## 9. Pricing tier notes

- The free tier fits a small bakery with one counter: one business, one branch, two seats, the weighed till and the shift
- Starter adds the production plan, the day old rule and a year of history
- The Business tier adds the purchasing, the raw material stock and the waste report
- The kiosk for the self service bread shelf is priced per device

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Foodics (فودكس) | Quote only, no rate card published (foodics.com, opened 2026-11-12) | Restaurant shaped, with no weight based bakery flow | The weight, the production batch and the day old rule as first class screens |
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | A general ERP where a baker needs a scale and a batch | A bakery flow with the scale, the batches and the Arabic words of the trade |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | No production batches, no day old rule and no weight pricing | The production and the expiry life of the shop, priced in pounds |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-bakery-tasks.md`:

1. Register the bakery pack in the sector registry (M1)
2. Write the bakery data model with the production batches (M1)
3. Build the bakery seed with the Arabic categories and the shelf lives (M1)
4. Write the bakery terminology map in Arabic and English (M1)
5. Build the weighed till and the scale driver (M2)
6. Build the production plan and the night batches (M2)
7. Build the day old screen with the discount rule (M2)
8. Build the raw material stock and the purchasing (M2)
9. Build the bakery report pack (M2)
10. Publish the bakery landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The shelf life list is a starting point and the shop must confirm it from the real product, because a wrong shelf life is a food safety question
- The scale is the source of the price, so the manual entry is always available and marked as manual in the receipt
- The day old rule never disposes stock on its own without the owner seeing the amount and pressing the button
- Allergen labelling is the shop own text: the product never decides that an item is safe for someone

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-bakery-tasks.md`
