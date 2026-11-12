# SIR Business sector: Butcher and fresh grocery (ملحمة وخضار)

> Round r56 (2026-11-12). Sector 7 of 41 in `plans/business-sectors/_INDEX.md`, wave 1.
> Base template `market`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner buys at the market before dawn and cuts by hand all day. Their world is the cold chain: what must be sold today, what is at the end of its date, and what the customer will argue about on the scale. The third pain is the price list: the price of the cut changes with the market every week, and a printed board cannot keep up.

Why this sector is in the catalogue: It is the shop where the cold chain decides the profit: the meat and the dairy that must sell first, the cutting rules the customers argue about, and the weight price that has to be exact.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, name, branchId, address, phone, currency, openingHours)
- Product (id, sku, nameAr, nameEn, categoryId, cutName, unit, unitPricePiasters, costPiasters, taxRate, supplierId, reorderPoint, isWeighed, isBatch, shelfLifeDays)
- Category (id, nameAr, nameEn, order, iconKey)
- Cut (id, productId, nameAr, nameEn, yieldPercent, pricePerKgPiasters)
- Batch (id, productId, supplierId, quantity, receivedAt, expiryAt, costPiasters, coldChainTempCelsius)
- DailyPrice (id, productId, date, pricePiasters, reason)
- Sale (id, branchId, cashierId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- SaleLine (id, saleId, productId, batchId, cutId, quantity, weightGrams, unitPricePiasters, note)
- Waste (id, productId, batchId, quantity, reason, loggedBy, createdAt)
- Supplier (id, nameAr, phone, paymentTerms, visitDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)

Units in use: kilogram and gram for the weight, piece for the counted items, bunch for the vegetables and tray for the prepared mixes

Batches: Yes for everything perishable: the meat, the poultry, the fish and the dairy, each with the received date, the expiry and the purchase cost

Expiry and shelf life: The radar shows the batches that go first with the quantity and the cost, and the cold chain temperature is recorded at receiving so a broken chain is visible

Sector specific structures: The structures specific to this sector are the cuts and their yield, the daily price per kilogram that follows the market, the cold chain log at receiving, and the weight sale with the customer choosing the cut

## 3. Screens and workflows that belong to this sector

- Butcher till: the cut list with the price per kilogram, the scale value and the choice of cut for the customer
- Cold chain receiving: the delivery with the temperature, the expiry of every tray and the difference against the order
- Expiry radar: what must be sold today, tomorrow and this week, with the cost and the write off
- Daily price board: change the price per kilogram for today with the reason, and print the board for the shop
- Cutting list: the cuts of each animal with the yield and the price, so the owner knows what the piece is worth
- Stock: the raw material by batch with the days left and the reorder point
- End of day: the money counted, the waste of the day in money and the weight sold per category

## 4. Roles and permissions

- Owner: everything, including the prices, the suppliers and the staff
- Manager: everything except billing, approves the price change and the write off
- Butcher: the cuts, the stock and the receiving, no cash
- Cashier: the counter, the scale, the payment and the shift close

## 5. Reports and KPIs

- Weight sold per category per day
- Expiry loss in money per batch
- Margin per cut after the real purchase cost
- Price change history: what the price was and why it moved
- Cold chain record per delivery with the temperature at receiving
- Cash reconciliation per shift

## 6. Integrations that matter

- Weighing scale through the local bridge or WebSerial, with a manual weight entry as a fallback
- Thermal printer through ESC/POS for the receipt and the batch label
- A temperature probe recorded at receiving, typed in when the probe is not connected
- WhatsApp for the order confirmation and for the daily price board to the regulars through the shop own account

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Products: the cuts and the vegetables with the price per kilogram
- Shelf life: the days each item stays fresh, and the rule for the write off
- Suppliers: the market suppliers with the visit days
- Team: the butcher and the cashier with their roles
- Receiving: the first delivery with the batches, the expiry and the temperature
- First week plan: sell a weighed cut, receive a delivery, print the price board, close the shift
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Category list in Arabic: لحوم بقري, لحوم غنم, دواجن, سمك, خضار, فاكهة, ألبان, بيض
- A cut list with the common cuts and the yield field left empty for the shop to fill from its own experience
- Weight and piece units with the price per kilogram
- A receipt layout with the weight line and the cut name
- Role templates for the butcher and the cashier

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- ملحمة بتعرف التالف باليوم، والسعر بالكيلو بيتغير كل يوم
- استلام بيسجّل الحرارة والتاريخ، وميزان دقيق، ولوحة أسعار تتحدث
- شاشة التالف: كل دفعة بتاريخها وكميتها وتكلفتها
- الاستلام بيسجّل حرارة الشحنة، فلو في خلل بيبان
- لوحة الأسعار بتتحدث الصبح والزبون يشوف السعر الصح

Questions the page must answer:

- الزبون بيحتج على الوزن؟ الوزن من الميزان والإيصال فيه الوزن والسعر بالكيلو
- بتنفع من غير نت؟ أيوه: البيع والطباعة بيفضلوا شغالين

### English

- A butcher that sees the expiry by the day and follows the market price by the kilo
- Receiving records the temperature and the date, the scale is exact, and the price board updates itself
- The expiry screen shows every batch with its date, its quantity and its cost
- Receiving records the temperature of the delivery, so a broken cold chain is visible
- The price board updates in the morning and the customer sees the right price

Questions the page must answer:

- What if the customer argues about the weight? The weight comes from the scale and the receipt shows the weight and the price per kilo
- Does it work with no connection? Yes: selling and printing keep working

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Butcher till: the cut list with the price per kilogram, the scale value and the choice of cut for the customer
- Cold chain receiving: the delivery with the temperature, the expiry of every tray and the difference against the order
- Expiry radar: what must be sold today, tomorrow and this week, with the cost and the write off
- Daily price board: change the price per kilogram for today with the reason, and print the board for the shop
- Cutting list: the cuts of each animal with the yield and the price, so the owner knows what the piece is worth
- Stock: the raw material by batch with the days left and the reorder point

## 9. Pricing tier notes

- The free tier fits one counter: one business, one branch, two seats, the weighed till and the shift
- Starter adds the receiving with the cold chain, the expiry radar and a year of history
- The Business tier adds the daily price board, the cut yields and the purchasing
- The kiosk for the cuts board is priced per device

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | A general ERP with no weight flow for a butcher | The cuts, the yields, the daily price and the cold chain log as one flow |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | No batch expiry and no daily price for a market that moves every week | The batches, the daily price and the cold chain record |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | A partner project for a shop that needs the scale to work today | One price, ready today, in Arabic, with the scale and the printer |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-butcher-fresh-grocery-tasks.md`:

1. Register the butcher pack in the sector registry (M1)
2. Write the butcher data model with the cuts and the cold chain (M1)
3. Build the butcher seed with the Arabic categories (M1)
4. Write the butcher terminology map in Arabic and English (M1)
5. Build the weighed cut sale with the cut choice (M2)
6. Build the cold chain receiving screen (M2)
7. Build the expiry radar and the write off with a reason (M2)
8. Build the daily price board (M2)
9. Build the butcher report pack (M2)
10. Publish the butcher landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The cold chain record is only as good as the reading at receiving, so a missing temperature is blocked for the categories that need it instead of being invented
- The shelf life of the meat and the dairy comes from the packaging and the supplier, and the app never extends it
- Food safety rules belong to the health authority and the shop, so the product records and never advises
- The customer name on a weighed order is optional and is never required to sell

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-butcher-fresh-grocery-tasks.md`
