# SIR Business sector: Laundry (مغسلة)

> Round r56 (2026-11-12). Sector 12 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `service`, group `services`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner receives a bag of clothes, and every piece has to be identified, counted, checked for stains, weighed, priced by rule and returned to the same customer. The pain is the lost piece: the customer comes back and one shirt is not in the bag. The second pain is the pricing, because the shop quotes by weight and by rule and the rules are in the owner head.

Why this sector is in the catalogue: It is a ticket business with a physical identity: every piece of clothing is tagged, weighed, priced by rule and tracked until the customer comes back for it.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, name, branchId, address, phone, currency, openingHours, taxRegistration)
- Ticket (id, branchId, number, customerId, receivedAt, promisedAt, dueAt, status, bagCount, weightGrams, totalPiasters, paidPiasters, note)
- TicketItem (id, ticketId, tagNumber, descriptionAr, categoryId, condition, stains, weightGrams, pricePiasters, serviceId, status)
- Tag (id, ticketId, tagNumber, barcode, printedAt)
- Service (id, nameAr, nameEn, kind, pricePerKgPiasters, pricePerPiecePiasters, turnaroundDays, isExpress)
- Category (id, nameAr, nameEn, order)
- Customer (id, name, phone, whatsappOptIn, lastVisitAt)
- ExpressTier (id, nameAr, priceDeltaPiasters, turnaroundHours)
- Sale (id, branchId, customerId, ticketId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- Supplier (id, nameAr, phone, paymentTerms, visitDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- StockItem (id, nameAr, unit, costPiasters, quantity, supplierId, reorderPoint)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)
- LostItem (id, ticketId, tagNumber, reason, reportedAt, resolvedAt)

Units in use: piece, kilogram, gram, and the bag as the intake unit for a customer

Batches: Not for the clothes. The stock of the shop (the detergent, the bags, the hangers) is a normal stock list with a reorder point

Expiry and shelf life: Not a driver here. What matters instead is the due date of each ticket: the promised day, and the reminder when the customer does not come back

Sector specific structures: The structures specific to this sector are the tag with a barcode per item, the ticket with the promised time, the express tier, the lost item record, and the customer who has three tickets open

## 3. Screens and workflows that belong to this sector

- Intake: the customer arrives, the bag is counted, every piece is tagged with a barcode and the photos of the stains are taken, and the ticket prints with the promised day
- The tag printer view: the list of the tags with their numbers, ready to print on the thermal printer
- The workshop board: the tickets by state (received, washing, ready, delivered) and the ones that are late
- Pricing: the weight per piece, the service per category, the express tier, and the total that the counter reads to the customer
- Ready for pickup: the tickets that are ready, the customer phone and one tap to call or to send the message
- Delivery on the bag: a service where a rider collects the bag and brings it back, with the driver and the time
- The customer: their tickets, their history and the unclaimed pieces that are still waiting
- End of day: the money, the tickets received, the tickets ready and the pieces not collected

## 4. Roles and permissions

- Owner: everything, including the prices, the rules and the reports
- Manager: everything except billing, approves the price exceptions and the refunds
- Counter: the intake, the tags, the payment and the handover
- Washer and ironer: the workshop board and the state of the tickets
- Rider: only the collections and the deliveries assigned to him

## 5. Reports and KPIs

- Tickets received, ready and delivered per day
- Revenue per service and per kilogram weight
- Late tickets: what was promised and what was delivered late
- Unclaimed pieces after fourteen days with their value
- Lost items and their resolution
- Wash and delivery cost per ticket
- Cash reconciliation per shift

## 6. Integrations that matter

- Thermal printer through ESC/POS for the ticket and the barcoded item tags
- Barcode scanner at the counter to read the tag back when the bag returns
- Phone camera for the stain photos, stored with the ticket
- WhatsApp for the ready message and the pickup reminder through the shop own account
- A weighing scale for the bulk weight

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Services: the categories of clothes and the price per piece and per kilogram, with the turnaround days
- Express: the express tiers with the price and the hours
- Rules: the stain rules, the excluded items and the turnaround the shop promises
- Team: the counter, the workshop and the rider
- Suppliers: the detergent, the bags and the hangers
- First week plan: receive a bag with three tags, price it, print the tags, mark one ticket ready, send the ready message
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Category list in Arabic for the clothes: قميص, بنطلون, جاكيت, فستان, بدلة, ملابس بيضاء, فرش, سجاد
- Service templates with the price per piece and the turnaround days
- Express tier presets
- A ticket layout with the bag count, the weight, the promised date and the total
- A tag layout with the barcode and the ticket number

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- مغسلة بكل قطعة تاغ بيتتبع لحد التسليم
- استلام وتغليف بالباركود، سعر بالكيلو أو بالقطعة، وميعاد تسليم واضح للزبون
- كل قطعة عليها تاج بباركود، فلو قطعة ناقصة بتعرف فورًا
- الميعاد بيتسجل مع الوقت السريع، والزبون بياخد رسالة لما تجهز
- القطع اللي ما رجعش بتظهر بقيمتها بعد 14 يوم

Questions the page must answer:

- الزبون نسي قطعة؟ كل قطعة مربوطة بالتذكرة وبالتاج، فياريع لصاحبه
- بتشتغل من غير نت؟ أيوه: الاستلام والطباعة بيفضلوا شغالين

### English

- A laundry where every piece is tagged and followed to the handover
- Intake with barcoded tags, a price by the kilogram or by the piece, and a clear promised day for the customer
- Every piece carries a barcoded tag, so a missing piece is found immediately
- The promised time is recorded with the express tier, and the customer gets a message when it is ready
- The pieces nobody collected show up with their value after fourteen days

Questions the page must answer:

- What if a customer loses a piece? Every piece is tied to the ticket and to the tag, so it is found and returned
- Does it work with no connection? Yes: the intake and the printing keep working

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Intake: the customer arrives, the bag is counted, every piece is tagged with a barcode and the photos of the stains are taken, and the ticket prints with the promised day
- The tag printer view: the list of the tags with their numbers, ready to print on the thermal printer
- The workshop board: the tickets by state (received, washing, ready, delivered) and the ones that are late
- Pricing: the weight per piece, the service per category, the express tier, and the total that the counter reads to the customer
- Ready for pickup: the tickets that are ready, the customer phone and one tap to call or to send the message
- Delivery on the bag: a service where a rider collects the bag and brings it back, with the driver and the time

## 9. Pricing tier notes

- The free tier fits one counter: one business, one branch, two seats, the intake, the tags and the till
- Starter adds the workshop board, the ready messages and a year of history
- The Business tier adds the express tiers, the pickup reminder, the lost item record and the multi branch collection
- The tag printing is priced per device, not per piece

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | An ERP without the tag and the workshop board of a laundry | The tag, the workshop board and the pickup reminder as one flow |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | A partner project for a counter that has to run tomorrow | Ready in an hour, in Arabic, with the thermal tag printer |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | A retail till with no tickets and no items that come back | The ticket, the tag and the promise date are the product here |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-laundry-tasks.md`:

1. Register the laundry pack in the sector registry (M1)
2. Write the laundry data model with the tickets and the tags (M1)
3. Build the laundry seed with the Arabic categories and the services (M1)
4. Write the laundry terminology map in Arabic and English (M1)
5. Build the intake screen with the tags and the photos (M2)
6. Build the workshop board with the states (M2)
7. Build the pickup reminder and the unclaimed list (M2)
8. Build the collection and delivery on the bag (M2)
9. Build the laundry report pack (M2)
10. Publish the laundry landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The stain photos and the condition of the clothes are personal data of the customer and belong to the shop, so they never enter our analytics and can be deleted on request
- The price rules are the shop own, so the app never invents a price for a piece the counter did not describe
- A lost piece is recorded as an incident with a reason, and the product never decides who pays
- The chemical and the waste rules of dry cleaning belong to the local authority, and the app records the work without advising on it

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-laundry-tasks.md`
