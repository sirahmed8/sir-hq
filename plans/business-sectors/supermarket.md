# SIR Business sector: Supermarket (سوبر ماركت)

> Round r56 (2026-11-12). Sector 1 of 41 in `plans/business-sectors/_INDEX.md`, wave 1.
> Base template `market`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner runs a supermarket with three to twelve staff across a morning and an evening shift. Their day is dominated by three things: the queue at the till, perishable stock that has to be rotated before it spoils, and suppliers who change prices by phone. The money leaks in two places nobody measures: expired dairy and meat, and shrink on the shelf. There is usually no stock system at all, so reorder is a phone call and the end of day cash is counted from memory.

Why this sector is in the catalogue: It is the anchor shop of every retail street in Egypt and the hardest test of the point of sale: real speed, real queues, perishable stock and a supplier who calls with a price change mid-morning.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Store (id, name, branchId, areaSquareMeters, openingHours, workingDays, taxRegistration, receiptHeader, currency)
- Product (id, sku, barcode, nameAr, nameEn, categoryId, unit, unitPricePiasters, costPiasters, taxRate, brandId, supplierId, reorderPoint, isWeighed, isBatch, taxExempt)
- Category (id, nameAr, nameEn, parentId, shelfOrder, colorToken, iconKey)
- Shelf (id, categoryId, label, position, capacityUnits)
- Batch (id, productId, supplierId, quantity, receivedAt, expiryAt, costPiasters, locationCode)
- Supplier (id, nameAr, phone, paymentTerms, visitDays, priceListId, lastOrderAt, rating)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, receivedAt, totalPiasters)
- GoodsReceipt (id, purchaseOrderId, receivedBy, lines, discrepancies, note, createdAt)
- Sale (id, branchId, cashierId, lines, payments, totalsPiasters, discountsPiasters, taxPiasters, createdAt, idempotencyKey)
- SaleLine (id, saleId, productId, batchId, quantity, unitPricePiasters, weightGrams, discountPiasters, isWeighed)
- Customer (id, name, phone, whatsappOptIn, loyaltyPoints, tier, creditLimitPiasters, balancePiasters, lastVisitAt)
- LoyaltyTransaction (id, customerId, saleId, points, tierAfter, reason)
- Shift (id, branchId, openedBy, openedAt, floatPiasters, closedAt, countedPiasters, expectedPiasters)
- StockCount (id, branchId, countedBy, lines, variancePiasters, status, countedAt)
- Waste (id, productId, batchId, quantity, reason, loggedBy, createdAt)
- Employee (id, name, phone, role, branchId, hireDate, hourlyRatePiasters, status)

Units in use: piece, pack, box, kilogram, gram, litre, millilitre, and weight based selling where the price is per kilogram and the number comes from the scale

Batches: Yes for everything dated: dairy, meat, frozen, bread, juice. Every batch keeps supplier, received date, expiry date and cost, so the shop can sell by batch, claim credit and see the real margin per batch instead of per item

Expiry and shelf life: Expiry is a radar, not a report: 7 days critical, 30 days watch, 90 days plan. The shelf list shows the earliest expiry first inside each category, and a one tap discount on a batch is written to the audit log with who did it and when

Sector specific structures: No tables, no appointments and no prescriptions. The structures specific to this sector are the shelf life per category, the produce and butchery area with its own price list per kilogram, the weighing and labelling station, and the customer 360 with the credit book for regulars who pay at the end of the month

## 3. Screens and workflows that belong to this sector

- Till: the fastest screen in the product. Barcode scanner, quick keys grid for the top twenty items, a held basket, mixed payment, and a weight button that opens the scale for produce
- Weigh and label: the cashier puts the item on the scale, the weight lands in the cart, and a label with the product name, the weight and the price prints for the bag
- Fresh list: the produce and meat wall with the price per kilogram, the batch behind each item and a one tap change of price for today only
- Shelf and expiry: the oldest batch first, with the quantity left, the cost and the shelf it is on, and a button to discount or to write it off as waste
- Goods receipt: the delivery arrives, the cashier scans the barcode and counts, the screen shows the difference between what was ordered and what arrived, and the receipt closes the purchase order
- Purchase order: the owner writes the order to a supplier from the reorder suggestion, with the last price of every item shown next to the new one
- Stock count: count the shelf with the phone camera or a scanner, see the difference against the system per item, and post the count with a reason
- Customer 360: what this customer buys, when, how much they owe, their points, and one tap to send a WhatsApp message with the receipt
- Shift close: count the drawer, compare with the expected cash, see the difference before it becomes a fight, print the Z report and hand over to the next shift

## 4. Roles and permissions

- Owner: everything, including billing, exports and the staff list
- Manager: everything except billing and export; approves discounts above the cashier limit; receives goods
- Cashier: sells, takes payment, prints receipts, cannot void a line without the manager override
- Stock controller: receives deliveries, counts stock, writes waste, sets reorder points, cannot sell
- Shelf filler: stock counts and expiry checks, no pricing and no cash
- Supplier buyer: creates purchase orders, sees supplier price lists, no access to customer data

## 5. Reports and KPIs

- Sales by hour: where the money comes from across the day, so the shift plan matches the real queue
- Sales by category and by item: which shelf pays for the rent
- Expiry loss in piasters per day: the number the owner has never seen before
- Stock valuation at cost and at retail: what the shop really holds
- Low stock list with the reorder suggestion: what to order tomorrow
- Shrink: counted difference against the system per item, with the value
- Cash reconciliation per shift: expected against counted, with the over and short
- Top customers and loyalty: who comes back, who is owed

## 6. Integrations that matter

- Thermal receipt printer through ESC/POS over USB, Bluetooth or the local network, with a golden file test for the 58 mm and 80 mm layouts
- Electronic weighing scale through the local bridge or WebSerial, with the weight landing in the cart
- Barcode scanner in keyboard mode, with a camera scanner on the phone for stock counts
- Cash drawer kicked on a cash payment
- WhatsApp receipt for the customer through the shop own account, with the shop choosing paper, message or both
- ETA e receipt and e invoice pipeline behind one server side signer, only after the official specification is read

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, city, phone, currency, working hours and the number of tills
- Categories: pick the shelves the shop really has from the seeded list, and set the order of the aisles
- Weighed items: mark the produce and meat as sold by weight and set the price per kilogram
- Supplier: add the main supplier with the visit days and the payment terms
- Team: add the staff with the role template and the till PIN
- First week plan: print a test receipt, count one shelf, receive one delivery, set the tax rate, choose the receipt layout
- Review and finish: the business opens in trial mode with a days left chip

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Category tree in Arabic with the usual Egyptian supermarket shelves: vegetables, fruit, meat, fish, dairy, bread, dry goods, drinks, household, personal care, baby
- Unit set with weight and pack conversions, and a quick key grid of the twenty most scanned items the shop can rename in one tap
- Shelf life per category that the shop can change per product, marked as a starting point
- Receipt layout for 80 mm with the store header, the tax line, the loyalty line and the QR for the receipt lookup
- Role templates with the permissions above and a PIN policy for the till
- Reorder points per category left empty on purpose, so the shop sets them from its own velocity after a week of sales

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- سوبر ماركت بيتظبط في يوم واحد: باركود، ميزان، وتالف بيتعرف قبل ما يبقى خسارة
- كاشير بيشتغل من غير نت، مخزون بالتاريخ، واستلام بيفرق بين اللي اتبعت واللي وصل
- الكاشير بيلمس الباركود والميزان: الصنف بيتحسب في ثانية بدون كتابة
- التالف بيتعرض بالأيام مش بالتقرير: كل صنف بتاريخه وكمية منه
- المالك بيعرف خسارة التالف بالجنيه قبل نهاية الشهر

Questions the page must answer:

- هي شغال من غير نت؟ أيوه: الكاشير بيكمّل لحد ما يرجع الاتصال، والطباعة بتطلع من الجهاز نفسه
- كل فاتورة بتطلع برقم ورسوم ضريبية صح؟ الأرقام بتبقى بالجنيه المئوي وبتتراجع في الـZ report، والتوقيع الضريبي بيتبني بعد ما نقرأ المواصفة الرسمية

### English

- A supermarket that sorts itself out in one day: barcode, scale, and expiry you can see before it becomes a loss
- A till that works with no connection, stock that knows its date, and a goods receipt that shows the difference between what was ordered and what arrived
- The cashier touches the barcode and the scale: the item is priced in a second with no typing
- Expiry is a live list, not a report: every dated item with how many are left
- The owner sees the cost of expired stock in pounds before the month ends

Questions the page must answer:

- Does it work without internet? Yes: the till keeps selling and the receipt prints from the device, then the queue syncs when the connection is back
- Is every receipt numbered and does the tax line add up? The money is kept in integer piasters and reconciled in the Z report, and the tax signer is built only after the official specification is read

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Till: the fastest screen in the product. Barcode scanner, quick keys grid for the top twenty items, a held basket, mixed payment, and a weight button that opens the scale for produce
- Weigh and label: the cashier puts the item on the scale, the weight lands in the cart, and a label with the product name, the weight and the price prints for the bag
- Fresh list: the produce and meat wall with the price per kilogram, the batch behind each item and a one tap change of price for today only
- Shelf and expiry: the oldest batch first, with the quantity left, the cost and the shelf it is on, and a button to discount or to write it off as waste
- Goods receipt: the delivery arrives, the cashier scans the barcode and counts, the screen shows the difference between what was ordered and what arrived, and the receipt closes the purchase order
- Purchase order: the owner writes the order to a supplier from the reorder suggestion, with the last price of every item shown next to the new one

## 9. Pricing tier notes

- Free tier fits a one till shop: one business, one branch, two seats, the till, the stock list and thirty days of history
- The Starter tier adds one year of history and five seats, which is where a supermarket with three tills lives
- The Business tier is the one to watch: weigh and label, purchasing, transfers between branches and the expiry loss report sit behind it, because that is where the work is
- Extra branches and extra seats are priced separately, and the annual price is ten months paid for twelve

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Loyverse | Free POS, add-ons from US$5 per store per month for unlimited history (loyverse.com/pricing, opened 2026-11-12) | Advanced inventory, purchase orders and transfers are paid add-ons, and there is no expiry or batch handling to buy | The expiry radar, FEFO and the goods receipt with the difference are part of the pack, in Arabic, priced in pounds |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | Needs an implementation partner for anything real, and the price is in dollars | One price for the whole shop, ready on day one, with the Arabic cashier flow that Odoo never had |
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | Cluttered legacy interface and a quote led sales motion | Same sector depth with an Apple grade Arabic interface, offline in the browser and a fair free tier |
| Square | Free with processing fees, Plus US$49 per month per location (squareup.com, opened 2026-11-12) | Not offered in Egypt and no Arabic, so no local payment rails and no local tax story | Built for the Egyptian till: cash, wallet, InstaPay and card through Paymob, with the ETA receipt pipeline |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-supermarket-tasks.md`:

1. Register the supermarket pack in the sector registry (M1)
2. Write the supermarket data model and its validation (M1)
3. Build the supermarket catalog seed with units and shelf lives (M1)
4. Write the supermarket terminology map in Arabic and English (M1)
5. Build the weigh and label screen for the produce wall (M2)
6. Build the expiry and shelf screen for the stock controller (M2)
7. Build the goods receipt screen with the difference (M2)
8. Write the supermarket receipt layout and the golden file (M2)
9. Build the supermarket report pack and the dashboard cards (M2)
10. Publish the supermarket landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The expiry radar is a safety tool, so the seed shelf lives are starting points only and the shop must confirm them from the real packaging labels
- Weight based selling depends on the scale being right, so a manual weight entry stays available and the printed label shows the weight
- Credit for regulars is a shop ledger and not a lending product, so no interest, no instalments and no collections are built
- The tax line is calculated in integer piasters and reconciled, but the official ETA signer stays off until the specification is read and signed off by the accountant

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-supermarket-tasks.md`
