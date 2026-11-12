# SIR Business sector: Restaurant (مطعم)

> Round r56 (2026-11-12). Sector 3 of 41 in `plans/business-sectors/_INDEX.md`, wave 1.
> Base template `restaurant`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner stands between the kitchen and the floor, and their day is a sequence of small fires: a table that waited too long, a dish that came out wrong, a delivery order that the driver is waiting for, and the cost of the food against the price on the menu. They know the menu by heart and the stock by guess. The two things they cannot see are which dish actually makes money once the waste and the labour are counted, and how many covers the second shift really served.

Why this sector is in the catalogue: It is the deepest existing competition in the market and the sector that needs the most from the engine: tables, a kitchen, a waiter, a delivery app and a food cost that has to be exact.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Restaurant (id, name, branchId, address, phone, currency, seats, openingHours, taxRegistration, serviceChargePercent)
- Table (id, branchId, label, seats, zone, status, shape, positionX, positionY, mergedWithTableId)
- Zone (id, nameAr, nameEn, kind, order)
- MenuSection (id, nameAr, nameEn, order, isHidden)
- MenuItem (id, sectionId, nameAr, nameEn, pricePiasters, costPiasters, taxRate, isAvailable, station, prepMinutes, allergens)
- MenuItemVariant (id, menuItemId, nameAr, nameEn, priceDeltaPiasters, isDefault)
- Recipe (id, menuItemId, yield, lines with productId and quantity, wastePercent)
- Order (id, branchId, tableId, serviceType, status, openedBy, openedAt, lines, totalsPiasters, guestCount, discountPiasters, serviceChargePiasters, idempotencyKey)
- OrderLine (id, orderId, menuItemId, variantId, quantity, unitPricePiasters, note, status, firedAt, station)
- KitchenTicket (id, orderId, station, status, firedAt, readyAt, note)
- Sale (id, branchId, orderId, payments, totalsPiasters, closedAt)
- Payment (id, saleId, method, amountPiasters, reference, cashGivenPiasters, changePiasters)
- DeliveryOrder (id, orderId, channel, driverName, driverPhone, address, status, promisedAt, deliveredAt, pickupAt)
- Supplier (id, nameAr, phone, paymentTerms, visitDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters, covers, labourCostPiasters)
- Employee (id, name, phone, role, station, hourlyRatePiasters, status)
- StockItem (id, nameAr, unit, costPiasters, quantity, isBatch, supplierId, reorderPoint)

Units in use: portion, plate, piece, kilogram, gram, litre, shot, cup, and recipe quantities that are converted into the cost of one portion

Batches: Yes for anything that arrives dated: dairy, meat, frozen, sauces. The kitchen consumes the oldest batch first, so the cost of a dish is the cost of the batch that was actually used

Expiry and shelf life: The kitchen sees a simple alert for the items that expire in three days, and the waste log records what was thrown out with the reason. A full expiry radar belongs to the supermarket pack, not here

Sector specific structures: The structures specific to this sector are tables and zones with the floor plan, the kitchen stations and the kitchen display, the recipe and the food cost, the split bill, the waiter and the handheld order, and the delivery order that leaves the building

## 3. Screens and workflows that belong to this sector

- Floor plan: the tables on a map with their state (free, seated, ordered, ready to serve, bill asked), the time since seated, and the order total, so the floor is read in one glance
- Table order: the waiter opens a table, adds items with the modifiers and the note, sends to the kitchen with one tap, and the table state changes
- Kitchen display: the tickets by station, the time on each one with the colour, and the buttons for ready and served, so the cook sees only what is cooking
- The till: the sale that closes the table, the split by guest or by item, the service charge, the discount with the manager override, and the receipt
- Menu and availability: the owner marks a dish as sold out and every till, the QR menu and the delivery screen lose it at once
- Food cost: what each dish really costs after the recipe and the waste, against the price on the menu, with the margin
- Delivery orders: the orders from the delivery apps and the own delivery, the driver, the promise time, and the handover
- Shift and covers: the shift with the number of covers served, the labour cost and the sales per hour
- Stock and purchase: what the kitchen consumed today from the stock, what ran low, and the order to the supplier

## 4. Roles and permissions

- Owner: everything, including the menu, the prices, the staff and the reports
- Manager: everything except billing; approves discounts, voids and free items
- Waiter: opens tables, takes orders, sends to the kitchen, prints the bill
- Cashier: takes the payment, closes the table, opens and closes the shift
- Cook (kitchen): the kitchen display only, marks ready, cannot see the money
- Delivery driver: only the orders assigned to him, with the status buttons and the handover

## 5. Reports and KPIs

- Sales by hour and covers per hour: the truth about the second shift
- Food cost and margin per dish: which dishes pay for the kitchen
- Best and worst sellers: what to push and what to drop from the menu
- Kitchen time: how long each station takes, from fired to ready
- Table turn time: how long a table sits before it is closed
- Delivery orders: how many, how late, per channel
- Waste per day with the reason: what was thrown out and why
- Shift summary: sales, covers, discounts, labour and cash variance

## 6. Integrations that matter

- Kitchen display: any Android tablet or a spare screen on the same network, with a simulated driver in the tests
- Thermal receipt printer through ESC/POS and a customer display on a second screen
- Delivery apps: read only status and order intake through each provider own connection, marked as a manual link until the provider API is confirmed
- WhatsApp for the customer confirmation and the delivery order update through the restaurant own account
- Card terminal through Paymob and the local wallet and InstaPay on the counter
- ETA e receipt and e invoice behind the server side signer, off until the specification is read

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency and the opening hours
- Floor: the zones and the tables, with the seats and the layout on the map
- Menu: import the dishes from a spreadsheet or add them one by one, with the price and the station
- Kitchen stations: the stations the kitchen works with (grill, fryer, cold, pastry, bar)
- Team: the staff with their role template and the station or the zone they work
- Stock: the main ingredients with the cost, and the recipes for the top dishes
- First week plan: open a table, send an order to the kitchen, print a bill, close the shift, and set the service charge
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Menu sections in Arabic: starters, salads, main courses, grills, sides, desserts, drinks and shisha when the shop serves it
- A station list with the usual kitchen stations and a ready made table shape set for two, four and six seats
- Role templates with the waiter, the cook and the driver permissions
- A receipt layout with the table number, the service charge line and the kitchen ticket number
- An empty recipe book and an empty stock list, so the shop enters its own dishes and real costs

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- مطعم بيتحكم فيه: الترابيزة، المطبخ، والدليفري في شاشة واحدة
- كاشير وأرضية ومطبخ، من غير نت، وكل وصفة بتعرف تكلفتها الحقيقية
- الترابيزة على خريطة: كام واحد قاعد ولسه مستني إيه من ساعة
- المطبخ شاشته بتوصله تيكيت واحد وتفضل لايك
- بتعرف تكلفة كل أكلة في المنيو من غير ما تخمّن

Questions the page must answer:

- لو النت مقطوع؟ الكاشير والأرضية والمطبخ بيفضلوا شغالين، وبعدين بيتبعتوا لما يرجع الاتصال
- الدليفري Apps بتتعمل معاه؟ أيوه، بس لحد ما نتأكد من واجهة كل تطبيق هنعملها ربط يدوي بدل ما نعتمد على كلام غير متأكد

### English

- A restaurant you can actually run: the floor, the kitchen and the delivery on one screen
- Till, floor and kitchen with no connection, and every dish that knows its real food cost
- The tables on a map: how many are seated, how long they have waited, and what is on the table
- The kitchen gets one ticket and stops shouting
- You see the real cost of every dish on the menu, not a guess

Questions the page must answer:

- What if the connection drops? The till, the floor and the kitchen keep working, and everything syncs when the connection is back
- Do the delivery apps work with it? Yes, but until each provider interface is confirmed we do it as a manual link rather than pretend an integration we have not verified

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Floor plan: the tables on a map with their state (free, seated, ordered, ready to serve, bill asked), the time since seated, and the order total, so the floor is read in one glance
- Table order: the waiter opens a table, adds items with the modifiers and the note, sends to the kitchen with one tap, and the table state changes
- Kitchen display: the tickets by station, the time on each one with the colour, and the buttons for ready and served, so the cook sees only what is cooking
- The till: the sale that closes the table, the split by guest or by item, the service charge, the discount with the manager override, and the receipt
- Menu and availability: the owner marks a dish as sold out and every till, the QR menu and the delivery screen lose it at once
- Food cost: what each dish really costs after the recipe and the waste, against the price on the menu, with the margin

## 9. Pricing tier notes

- The free tier runs a small cafe counter: one business, one branch, two seats, the till and the shift
- Starter adds the floor plan, the waiter handheld and a year of history for a restaurant with five seats
- The Business tier adds the kitchen display, the delivery orders, the recipes and the food cost, which is the difference between running a restaurant and guessing
- Kiosk and the customer display are priced per device, never as a forced hardware bundle

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Foodics (فودكس) | Quote only, no rate card published; claims 40,000 or more restaurants (foodics.com, opened 2026-11-12) | Restaurant only, quote led sales and an opaque price | The same Arabic depth at a published price, and every other sector on the same account |
| Toast | Quote only, hardware lock in (pos.toasttab.com/pricing, opened 2026-11-12) | Approved hardware only and a United States payments model | Any Android tablet works, and the payment rails are the Egyptian ones |
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | A wide ERP where a restaurant wants a floor and a kitchen | The floor, the kitchen and the delivery are the product, in a fast Arabic interface |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | The restaurant is a separate app from the shop, and the price is in dollars | One account for the restaurant and the shop next door, priced in pounds |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-restaurant-tasks.md`:

1. Register the restaurant pack in the sector registry (M1)
2. Write the restaurant data model with tables, zones and recipes (M1)
3. Build the restaurant seed with the Arabic menu sections and the floor tables (M1)
4. Write the restaurant terminology map in Arabic and English (M1)
5. Build the interactive floor plan (M2)
6. Build the kitchen display and the ticket routing (M2)
7. Build the waiter order flow with modifiers and notes (M2)
8. Build the food cost and the recipe cost screen (M2)
9. Build the delivery order screen with the manual link (M2)
10. Build the restaurant report pack and the shift summary (M2)

## 12. Risks, unknowns and what we refuse to fake

- Food cost is only as honest as the purchase prices, so an item without a real cost is flagged and never treated as free
- Delivery app interfaces change often, so the first release keeps a clearly labelled manual entry instead of pretending an integration we have not verified
- Service charge and tax rules differ between the cities, so the percentages are set per business and never assumed by the product
- Allergens are shown as the shop wrote them, and the product never decides that a dish is safe for a guest

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-restaurant-tasks.md`
