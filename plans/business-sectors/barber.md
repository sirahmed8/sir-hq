# SIR Business sector: Barber (حلاقة رجالي)

> Round r56 (2026-11-12). Sector 9 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `service`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner cuts hair all day and the queue is the whole management problem. Two chairs, one barber, and the person who walks in and expects to be next. The money is small but steady, and the pain is short: the wait is too long, the barber is alone, and the daily total is in a notebook.

Why this sector is in the catalogue: It is the smallest service shop that still needs a queue: a walk in, a ticket, a chair and a fast sell, with the lowest data risk in the catalogue.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, name, branchId, address, phone, currency, openingHours, taxRegistration)
- Barber (id, name, phone, role, chairId, commissionPercent, serviceIds, status)
- Chair (id, branchId, label, status)
- Service (id, nameAr, nameEn, durationMinutes, pricePiasters, commissionPercent, isActive)
- Ticket (id, branchId, number, clientName, clientPhone, barberId, serviceIds, issuedAt, calledAt, servedAt, status, source)
- WalkIn (id, branchId, clientName, clientPhone, arrivedAt, calledAt, status)
- Client (id, name, phone, whatsappOptIn, lastVisitAt, visitCount)
- Sale (id, branchId, clientId, barberId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- SaleLine (id, saleId, serviceId, barberId, quantity, unitPricePiasters, commissionPiasters)
- RetailProduct (id, nameAr, unit, pricePiasters, costPiasters, quantity, isBatch, openedAt)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)

Units in use: service, session, piece and minute as the booked duration

Batches: Only for the retail shelf (the shave cream, the oil, the tonic): the opening date is recorded so the shelf knows what is fresh

Expiry and shelf life: The opened retail products show the days left, and nothing else in this sector expires

Sector specific structures: The structures specific to this sector are the queue and the ticket: the walk in arrives, takes a number, is called, and the ticket turns into a sale

## 3. Screens and workflows that belong to this sector

- The queue: the waiting list with the names and the wait time, and the call button that puts the next person on the chair
- Ticket display: the big number on the screen for the customer to watch
- The chair view: the barber sees his day, his client and the service
- Fast sell: the service, the price and the payment in two taps
- Retail shelf: the products sold next to the cut, with the opening date
- End of day: the money counted, the clients served, the average wait and the empty slots

## 4. Roles and permissions

- Owner: everything, including the prices, the staff and the reports
- Barber: the queue, his clients, the sale of his services
- Cashier: takes the payment and closes the shift when there is a second person

## 5. Reports and KPIs

- Clients served per barber per day and the average wait
- Revenue per service and per barber with the commission
- Empty slots by hour
- The walk in share against the booked clients
- Cash reconciliation per shift

## 6. Integrations that matter

- Thermal printer through ESC/POS for the receipt and the ticket
- WhatsApp for the ticket number and the reminder of the next visit through the shop own account
- Card terminal through Paymob and the mobile wallets at the counter
- A tablet on the wall in a browser full screen for the ticket display

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Chairs: the number of chairs and their labels
- Services: the cuts with the duration and the price
- Team: the barbers with the commission percentage
- Queue: the way the shop calls the clients (a number on the screen, a name, or a voice)
- Retail shelf: the products sold next to the cut
- First week plan: issue a ticket, serve a client, close the shift, print the end of day
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Service categories in Arabic: قص شعر, حلاقة, لحية, غسيل, صبغة, وعناية
- Chair labels and the ticket display layout
- Role templates for the barber and the cashier
- A receipt layout with the barber, the service and the wait time

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- حلاقة بنظام أرقام: الزبون يدخل، ياخد رقم، ويتنادى عليه
- طابور واضح على الشاشة، بيع سريع، وختام يوم بيقول كام قصّيت وكم استنيت
- الزبون بيشوف رقمه على الشاشة بدل ما يسأل
- الكوافير بياخد الطابور كله في شاشة واحدة
- بتعرف أكتر وقت الإشغال وأكتر وقت فاضي

Questions the page must answer:

- ينفع من غير نت؟ أيوه: التذاكر والبيع والطباعة بيفضلوا شغالين
- الزبون بينسى ميعاده؟ رقم التذكرة على واتساب وبتتقدر تتابعه

### English

- A barber shop with a number system: the client walks in, takes a number and is called
- A clear queue on the screen, a fast sell, and an end of day that says how many you cut and how long people waited
- The client watches the number on the screen instead of asking
- The barber sees the whole queue on one screen
- You see the busiest hour and the hour you lose

Questions the page must answer:

- Does it work with no connection? Yes: the tickets, the sale and the printing keep working
- What if a client forgets the appointment? The ticket number goes on WhatsApp and you can follow up

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- The queue: the waiting list with the names and the wait time, and the call button that puts the next person on the chair
- Ticket display: the big number on the screen for the customer to watch
- The chair view: the barber sees his day, his client and the service
- Fast sell: the service, the price and the payment in two taps
- Retail shelf: the products sold next to the cut, with the opening date
- End of day: the money counted, the clients served, the average wait and the empty slots

## 9. Pricing tier notes

- The free tier fits a one barber shop: one business, one branch, two seats, the queue and the fast sell
- Starter adds the ticket display, the reminders and a year of history
- The Business tier adds the retail shelf, the commissions and the reports
- The extra barber is priced as a seat, not as a new business

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | An ERP where a barber needs a number and a chair | A queue flow built for the walk in, in Arabic, at a price a one chair shop can pay |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | A retail till with no queue and no barber commission | The queue, the ticket and the commission per barber |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | A partner project for a queue that should take an hour to set up | Ready in one hour on any tablet, in Arabic |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-barber-tasks.md`:

1. Register the barber pack in the sector registry (M1)
2. Write the barber data model with the queue and the tickets (M1)
3. Build the barber seed with the Arabic service categories (M1)
4. Write the barber terminology map in Arabic and English (M1)
5. Build the queue screen with the call button (M2)
6. Build the ticket display for the wall (M2)
7. Build the fast sell with the service and the payment (M2)
8. Build the retail shelf with the opening date (M2)
9. Build the barber report pack (M2)
10. Publish the barber landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The client name and the phone are optional at the till and belong to the shop, so they never enter our analytics
- The queue order is the shop own rule, and the app never reorders the clients by its own idea
- The retail products of a barber shop are a small shelf, so no expiry rule is applied to anything that has no opening date

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-barber-tasks.md`
