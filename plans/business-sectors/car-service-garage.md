# SIR Business sector: Car service and garage (صيانة سيارات)

> Round r56 (2026-11-12). Sector 11 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `garage`, group `services`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner runs a workshop with bays and mechanics. The car comes in with a complaint, the mechanic finds more, and the customer has to approve the extra work before it starts. The pain is the estimate that becomes an invoice nobody agreed to, the part that was not in stock, and the record of which car had which problem, because the same owner comes back next year.

Why this sector is in the catalogue: It is a workshop with a customer queue and a parts warehouse, so it needs the ticket, the estimate, the labour, the parts and the trust of the customer who left the car.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Garage (id, name, branchId, address, phone, currency, openingHours, taxRegistration)
- Bay (id, branchId, label, status)
- Customer (id, name, phone, whatsappOptIn, email)
- Vehicle (id, customerId, plate, make, model, year, colour, chassisLast4, notes, nextServiceAt)
- ServiceOrder (id, garageId, vehicleId, customerId, complaint, status, openedAt, promisedAt, deliveredAt, mileageKm, estimatePiasters, approvedPiasters, totalPiasters, advisorId)
- ServiceLine (id, serviceOrderId, type, nameAr, quantity, unitPricePiasters, kind, status)
- Part (id, sku, barcode, nameAr, nameEn, unit, costPiasters, pricePiasters, supplierId, reorderPoint, isBatch)
- Labour (id, serviceOrderId, mechanicId, minutes, hourlyRatePiasters, descriptionAr)
- Mechanic (id, name, phone, role, hourlyRatePiasters, commissionPercent, status)
- Estimate (id, serviceOrderId, status, lines, totalPiasters, sentAt, approvedAt, declinedAt, channel)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Supplier (id, nameAr, phone, paymentTerms, visitDays)
- Checklist (id, serviceOrderId, itemAr, state, note)
- Sale (id, branchId, customerId, serviceOrderId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- Warranty (id, serviceOrderId, itemAr, months, validUntil)

Units in use: piece, litre, filter, job, hour, minute and the labour hour

Batches: Only for the oils, the coolant and the brake fluid, where the shelf life matters; most parts are not batched

Expiry and shelf life: The oils and the fluids show the days left, and the service interval of the vehicle is the real date that matters here

Sector specific structures: The structures specific to this sector are the vehicle record with its plate and its service history, the estimate that the customer approves before the work starts, the labour of the mechanic, and the parts that come from the stock or are ordered for the customer

## 3. Screens and workflows that belong to this sector

- Job card: one screen for the car, the complaint, the inspection checklist, the photos, the estimate and the state of the work
- Intake: the customer, the plate, the car or a new vehicle record, the mileage and the complaint, with the photos
- Estimate: the lines with the parts and the labour, the total, and the approval link that the customer receives and presses
- Order desk: the parts to order for the jobs that wait, with the supplier and the expected day
- Bays and the workshop board: which car is on which bay, at which step, and who works on it
- Parts stock: the fast moving parts, the cost, the price, the reorder point and the barcode
- Handover: the finished work, the photos before and after, the invoice, the warranty and the next service date
- Customer and vehicle history: every visit, every problem and every part that was replaced

## 4. Roles and permissions

- Owner: everything, including the prices, the staff and the reports
- Manager: everything except billing, approves the estimate above a limit and the extra work
- Advisor (service reception): the intake, the estimate, the customer update and the handover
- Mechanic: the job card, the checklist, the parts request and the labour time
- Parts keeper: the stock, the orders and the deliveries
- Cashier: takes the payment and closes the shift

## 5. Reports and KPIs

- Jobs per bay and per mechanic, and the average job value
- The estimate to the approved ratio: how much extra work is found
- Turnaround time per job type against the promised day
- Parts sold per job and the fast moving parts with the reorder point
- Labour time per mechanic per day and the commission
- Return customers and the vehicles that came back within the warranty
- Cash reconciliation per shift

## 6. Integrations that matter

- Thermal printer through ESC/POS for the job card, the estimate and the invoice
- Phone camera for the photos of the car before and after the work
- WhatsApp for the estimate approval and the progress update through the garage own account
- Barcode scanner in keyboard mode for the parts in the stock and at the counter
- Card terminal through Paymob and the mobile wallets at the reception

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Bays: the number of bays and their labels
- Services: the jobs the garage offers with the price and the time, from the oil change to the full service
- Team: the advisors, the mechanics and the parts keeper with their roles
- Parts: the fast moving parts with the cost and the price
- Suppliers: the parts suppliers with the visit days
- First week plan: open a job card, send an estimate, get the approval, close a job and print the invoice
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Job type list in Arabic: زيت وفلاتر, تروس, بريك, Suspensions, كهرباء, تكييف, فحص كمبيوتر
- Part category list in Arabic with the units
- Role templates for the advisor, the mechanic, the parts keeper and the cashier
- A job card layout with the plate, the complaint, the mileage and the checklist
- An empty vehicle and customer list, never seeded with fake plates

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- صيانة سيارات: عرض سعر يتفق عليه العميل قبل الشغل، وسجل لكل عربية
- كرت صيانة لكل عربية، ووقت الشغل، وقطع الغيار بالمخزون
- العرض بيتبعت للعميل على واتساب ويتافق عليه بضغطة، فمفيش مفاجآت
- كل عربية ليها كارت بالتاريخ والأعطال والقطع اللي اتغيرت
- بتعرف الوقت المطلوب لكل شغل، والميكانيكي اللي عمله

Questions the page must answer:

- العميل مش موجود وقت الصيانة؟ عرض السعر بيتسجل والعقد بيتبعت، والموافقة من غير ما يحتاج يتصل بيه
- القطع مش موجودة؟ الطلب للمورد بيتبعت من شاشة الطلبات ومالك بتعرف يوم الوصول

### English

- A garage where the customer approves the estimate before the work starts, and every car has a record
- A job card per car, the time of the work, and the parts in the stock
- The estimate goes to the customer on WhatsApp and is approved with one tap, so there are no surprises
- Every car has a card with the history, the faults and the parts that were replaced
- You see the time each job really takes and who worked on it

Questions the page must answer:

- What if the customer is not there? The estimate is recorded and sent, and the approval is stored without needing a phone call
- What if the part is not in stock? The order to the supplier comes from the order screen and you see the expected day

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Job card: one screen for the car, the complaint, the inspection checklist, the photos, the estimate and the state of the work
- Intake: the customer, the plate, the car or a new vehicle record, the mileage and the complaint, with the photos
- Estimate: the lines with the parts and the labour, the total, and the approval link that the customer receives and presses
- Order desk: the parts to order for the jobs that wait, with the supplier and the expected day
- Bays and the workshop board: which car is on which bay, at which step, and who works on it
- Parts stock: the fast moving parts, the cost, the price, the reorder point and the barcode

## 9. Pricing tier notes

- The free tier fits a small workshop with one bay: one business, one branch, two seats, the job card and the till
- Starter adds the estimate approval, the parts stock and a year of history
- The Business tier adds the workshop board, the labour sheet, the warranty and the multi branch transfer
- The customer tracking link for the estimate is priced per branch, never per customer

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | An ERP where a garage needs a bay, a mechanic and an approved estimate | The job card, the estimate approval and the vehicle history as one flow |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | No garage workflow and a partner implementation cost | A garage flow that runs on a tablet in the bay, in Arabic |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | A retail till with no job cards, no estimate and no vehicle records | The job card and the customer approval are the product here |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-car-service-garage-tasks.md`:

1. Register the garage pack in the sector registry (M1)
2. Write the garage data model with the vehicles and the job cards (M1)
3. Build the garage seed with the Arabic job types (M1)
4. Write the garage terminology map in Arabic and English (M1)
5. Build the job card screen (M2)
6. Build the estimate and the customer approval (M2)
7. Build the parts stock and the order desk (M2)
8. Build the handover with the warranty and the next service (M2)
9. Build the garage report pack (M2)
10. Publish the garage landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The vehicle data (plate, chassis) belongs to the customer, so it never enters our analytics and can be exported and deleted
- The estimate approval is recorded with the channel and the time, because the dispute about extra work is a legal question the app never decides
- The parts are sold with the price the garage set, and the provenance of a part (original or copy) is stated as the garage states it
- No safety inspection result is certified by the product: the checklist is the garage own record

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-car-service-garage-tasks.md`
