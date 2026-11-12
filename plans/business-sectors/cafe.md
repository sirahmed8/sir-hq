# SIR Business sector: Cafe (كافيه)

> Round r56 (2026-11-12). Sector 4 of 41 in `plans/business-sectors/_INDEX.md`, wave 1.
> Base template `restaurant`, group `food-and-drink`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner runs a small cafe with a barista, a waiter and a cash box. The day is a rush in the morning, a slower afternoon and a delivery peak at night. They lose money on the drinks they make wrong, on the ice and the milk that runs out at eight in the morning, and on the discount the waiter gives away to be nice. Their real question every day is which drink and which food carries the business.

Why this sector is in the catalogue: It is the second most common food business in Egypt and the hardest case for a fast till, because the order is modifiers and drinks with different sizes, ice and extras, and the queue is short and impatient.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Cafe (id, name, branchId, address, phone, currency, openingHours, serviceChargePercent, taxRegistration)
- Counter (id, branchId, label, kind, status)
- MenuSection (id, nameAr, nameEn, order, isHidden)
- MenuItem (id, sectionId, nameAr, nameEn, pricePiasters, costPiasters, taxRate, station, isAvailable)
- ModifierGroup (id, menuItemId, nameAr, nameEn, isRequired, maxChoices)
- Modifier (id, groupId, nameAr, nameEn, priceDeltaPiasters, isDefault, isAvailable, trackStock)
- Recipe (id, menuItemId, lines, yield, milkMl, iceGrams, caffeineGrams)
- Order (id, branchId, counterId, serviceType, status, lines, totalsPiasters, createdAt, idempotencyKey)
- OrderLine (id, orderId, menuItemId, modifiers, quantity, unitPricePiasters, note, status)
- StockItem (id, nameAr, unit, costPiasters, quantity, supplierId, reorderPoint, isBatch, expiryAt)
- PrepList (id, branchId, itemId, quantityNeeded, quantityDone, preparedAt)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)
- Employee (id, name, phone, role, hourlyRatePiasters, status)
- Customer (id, name, phone, whatsappOptIn, loyaltyPoints, tier)

Units in use: cup, portion, piece, gram, millilitre, shot, and the day parts that price a drink differently

Batches: Only for the dairy and the prepared bases: the milk, the cream and the syrups carry a batch with an opening date, so the morning stock knows what is fresh

Expiry and shelf life: A short alert for the opened milk and the bases, plus the daily preparation list, which is the real expiry problem in a cafe: what was prepared yesterday and what was sold

Sector specific structures: The structures specific to this sector are the modifier groups (size, ice, extras, syrup, milk type), the day parts with their own prices, the daily preparation list, and the order that has to be made in under a minute

## 3. Screens and workflows that belong to this sector

- Quick order: the grid of the top items with the modifiers one tap away, built for a queue that will not wait
- Drink builder: size, ice, milk, extra shot, syrup, with the price updating as the barista taps
- Till: the fast checkout with the card, the cash and the wallet, and the receipt that names the drink exactly as it was built
- Availability: one tap marks a drink as sold out and the grid, the QR menu and the delivery screen lose it at once
- Preparation list: what to prepare before opening and what to restock during the day, with the quantity done and the quantity left
- Stock for the bar: the milk, the beans, the syrups and the ice, with the last count and the reorder point
- Day parts: the prices for the morning, the afternoon and the evening, with what was sold in each
- Shift and the till report: the money counted against the sales, the discounts given and the waste of the day

## 4. Roles and permissions

- Owner: everything, including the menu, the prices and the staff
- Manager: everything except billing, approves discounts and voids
- Barista: makes the drinks, updates the availability, records the preparation list
- Cashier: takes the payment, closes the shift, hands over the drawer
- Waiter: takes the order for the table service, serves and closes the table

## 5. Reports and KPIs

- Sales and cups per hour: when the queue really happens
- The drink and the food that carry the business: margin per item
- Average ticket: the price of the basket, by day part
- Discounts given and who gave them: the number that hides in the margin
- Preparation waste: what was prepared and not sold, in money
- Stock of the bar: milk, beans and syrups with the days left

## 6. Integrations that matter

- Thermal printer through ESC/POS, and a customer display on the second screen for the waiting queue
- Barcode scanner in keyboard mode for the packaged items on the side
- Card terminal through Paymob, mobile wallets and InstaPay on the counter
- Delivery apps through a manual link first, with the channel shown honestly
- WhatsApp for the order confirmation through the cafe own account

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Counters: the number of counters and whether there is table service
- Menu: import the drinks and the food with the price and the modifiers
- Day parts: the morning, the afternoon and the evening with their prices
- Team: the barista, the cashier and the waiter with their roles
- Bar stock: the milk, the beans and the syrups with the counts
- First week plan: build one drink end to end, print a receipt, close the shift, set the day parts
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Menu sections in Arabic: espresso, brewed coffee, cold coffee, tea, matcha, juices, shakes, breakfast, sandwiches, sweets
- Modifier groups with the common sets: size, ice, milk type, extra shot, syrup, without sugar
- A day part preset with morning, afternoon and evening
- A receipt layout with the drink written the way it was built (size, ice and extras on separate lines)
- An empty stock list and an empty preparation list, so the shop enters its own milk and beans

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- كافيه بيشتغل في دقيقة: مشروبات بموديفايرز، والشغل من غير ما ينقطع
- كاشير سريع، شاشة تعديل المشروب، وقائمة تحضير الصبح قبل ما تفتح
- المشروب بيتظبط في 3 نقرات: حجم، تلج، حليب، زيادة
- بتعرف أنهي مشروب بيدفع الإيجار و أنهي بيضيع
- قائمة التحضير بتعرفك إحنا جبت كام قبل ما تفتح

Questions the page must answer:

- بيشتغل من غير نت؟ أيوه: الطلب والطباعة بيفضلوا شغالين والمزامنة بتتم بعدين
- الدليفري Apps متوصّلة؟ لحد ما نأكد من كل واجهة هنعملها إدخال يدوي مكتوب بوضوح

### English

- A cafe that runs in a minute: drinks with modifiers, and stock you can see
- A fast till, a drink builder screen, and the morning preparation list before you open the door
- A drink is built in three taps: size, ice, milk, extra shot
- You see which drink carries the rent and which one disappears
- The preparation list tells you how much to make before opening

Questions the page must answer:

- Does it work without a connection? Yes: orders and printing keep working and the sync happens after
- Are the delivery apps connected? Until each interface is confirmed they are a clearly labelled manual entry

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Quick order: the grid of the top items with the modifiers one tap away, built for a queue that will not wait
- Drink builder: size, ice, milk, extra shot, syrup, with the price updating as the barista taps
- Till: the fast checkout with the card, the cash and the wallet, and the receipt that names the drink exactly as it was built
- Availability: one tap marks a drink as sold out and the grid, the QR menu and the delivery screen lose it at once
- Preparation list: what to prepare before opening and what to restock during the day, with the quantity done and the quantity left
- Stock for the bar: the milk, the beans, the syrups and the ice, with the last count and the reorder point

## 9. Pricing tier notes

- The free tier fits a one person coffee bar: one business, one branch, two seats, the quick order and the shift
- Starter adds the drink builder, the day parts and a year of history
- The Business tier adds the preparation list, the stock for the bar and the waste report, which is where a cafe loses money quietly
- Kiosk and the customer display are priced per device

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Foodics (فودكس) | Quote only, no rate card published (foodics.com, opened 2026-11-12) | Built for the full service restaurant, heavier than a cafe counter needs | A cafe sized flow: the quick order, the modifiers and the preparation list, at a published price |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | A generic till with no modifiers and no recipe for the drink cost | The drink builder and the cost of every cup from the real recipes |
| Square | Free with processing fees, Plus US$49 per month per location (squareup.com, opened 2026-11-12) | Not offered in Egypt, no Arabic and no local payment rails | The Egyptian till with wallet and InstaPay, and the receipts in Arabic |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-cafe-tasks.md`:

1. Register the cafe pack in the sector registry (M1)
2. Write the cafe data model with modifiers and day parts (M1)
3. Build the cafe seed with the modifier groups (M1)
4. Write the cafe terminology map in Arabic and English (M1)
5. Build the quick order grid and the drink builder (M2)
6. Build the availability switch and the day parts (M2)
7. Build the morning preparation list (M2)
8. Write the cafe receipt layout and the golden file (M2)
9. Build the cafe report pack (M2)
10. Publish the cafe landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The drink cost depends on the real purchase prices of the milk, the beans and the syrups, so a missing cost is flagged and never counted as zero
- Delivery app interfaces are not confirmed, so the first release keeps a labelled manual entry instead of a fake integration
- The preparation waste report needs a real count of what was prepared, so the shop is asked for it once a day and the app never guesses it
- Nothing in this pack decides whether a drink is safe for a guest with an allergy: that stays with the shop

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-cafe-tasks.md`
