# SIR Business sector: Salon (صالون)

> Round r56 (2026-11-12). Sector 8 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `service`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner runs chairs, not shelves. The day is a booking sheet with names on it, and the pain is the gap: an empty two o clock on a Tuesday, a client who wants the same stylist as last time and she is with someone else, and a stylist who asks for her commission at the end of the week and gets an argument about it. The second pain is the client who no shows and the slot is lost.

Why this sector is in the catalogue: It is a booking business that sells time, not goods: the chair, the stylist and the hour are the stock, and the owner loses money when the book is empty in the afternoon.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Salon (id, name, branchId, address, phone, currency, openingHours, taxRegistration)
- Stylist (id, name, phone, role, chairId, commissionPercent, serviceIds, workingHours, status)
- Chair (id, branchId, label, kind, status)
- Service (id, nameAr, nameEn, durationMinutes, pricePiasters, categoryId, commissionPercent, isActive)
- ServiceCategory (id, nameAr, nameEn, order)
- Appointment (id, branchId, clientId, stylistId, serviceIds, startsAt, endsAt, status, pricePiasters, depositPiasters, source, note)
- Client (id, name, phone, whatsappOptIn, notes, preferredStylistId, loyaltyPoints, lastVisitAt)
- Package (id, clientId, serviceId, sessionsTotal, sessionsUsed, pricePiasters, validUntil, status)
- Sale (id, branchId, clientId, stylistId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- SaleLine (id, saleId, serviceId, stylistId, quantity, unitPricePiasters, commissionPiasters)
- RetailProduct (id, nameAr, unit, pricePiasters, costPiasters, quantity, categoryId)
- Commission (id, stylistId, periodStart, periodEnd, servicePiasters, retailPiasters, totalPiasters, paidAt, status)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)
- NoShow (id, appointmentId, stylistId, minutes, penaltyPiasters, recordedAt)

Units in use: session, service, piece, box and minute as the booked duration, with the retail add ons sold by the piece

Batches: Only for the retail shelf (the dyes, the creams and the oils): the batch with the opening date so the shelf knows what is fresh, exactly like the pharmacy

Expiry and shelf life: The opened products on the shelf show the days left, and the packages of sessions show the last day they can be used

Sector specific structures: The structures specific to this sector are the chair, the stylist and the time slot, the appointment with a deposit and a no show penalty, the package of sessions with its expiry, and the commission of the stylist

## 3. Screens and workflows that belong to this sector

- The book: the day with the columns of the stylists and the slots, the booked, the free and the blocked, with the name and the phone
- New booking: the client, the service, the stylist, the time, the deposit and the reminder, in one flow that works on the phone
- Wait list: the clients who want a slot and accept a cancellation, called in order
- The stylist view: her day, her clients, the services, the times and the money she made that day
- Retail shelf: the products sold next to the service, with the opening date and the days left
- Packages: the sessions bought and used, with the expiry, for the client and for the salon
- Commission sheet: the period, the money per stylist, the retail share and the payout
- End of day: the money counted, the appointments served, the no shows and the empty slots

## 4. Roles and permissions

- Owner: everything, including the staff, the prices, the commissions and the reports
- Manager: everything except billing, approves a discount and a no show penalty
- Receptionist: the book, the walk in, the reminder and the payment
- Stylist: her day, her clients, the sale of her services and the retail she suggests
- Assistant: the shelf, the orders and the cleaning tasks

## 5. Reports and KPIs

- Booked hours per stylist per day: who is idle and who is full
- Empty slots by hour: the money the salon gave away by being quiet
- Revenue per service and per stylist, and the margin after the commission
- No show rate per stylist and per day
- Retail sales per stylist and the product that sells with a service
- Packages sold, used and expired
- Commission sheet per period

## 6. Integrations that matter

- WhatsApp for the booking confirmation, the reminder and the cancellation offer through the salon own account
- Thermal printer through ESC/POS for the receipt and the appointment card
- Google Calendar through the user own account as an optional second view, never as the source of truth
- Card terminal through Paymob and the mobile wallets at the reception

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Chairs: the chairs and the stations, with the label the salon uses
- Services: the services with the duration and the price, imported from a spreadsheet or added by hand
- Team: the stylists with their commission percentage and the working hours
- Clients: the first clients with a phone number and their preference
- Packages: the rules for the packages of sessions and how long they stay valid
- First week plan: book a client, send a reminder, sell a service, close the shift, run the commission sheet
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Service categories in Arabic: قص, صبغة, علاج, عناية, مكياج, nail, and the retail shelf
- A duration and commission field per service, left for the salon to fill
- Chair labels and a booking grid layout for one, three and six chairs
- Role templates for the receptionist, the stylist and the assistant
- A receipt layout with the stylist, the service, the duration and the deposit

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- صالون بمواعيد واضحة، والكراسي مشغولة في الوقت الصح
- دفتر مواعيد على الموبايل، عمولة واضحة للكوافيرة، وباقات جلسات لها تاريخ انتهاء
- دفتر المواعيد вид واضح: مين عندها وقت فاضية ومين مشغولة
- العمولة بتتحسب من كل خدمة تم بيعها فعلًا، والورقة بتطلع قبل آخر الشهر
- العميل بيجيله تذكير على واتساب ويقدر يلغي

Questions the page must answer:

- العميلة مش هتعرف تيجي؟ التذكير وقائمة الانتظار بيوصلوا حد بدل ما يقعد الوقت فاضي
- العمولات بتتحسب ازاي؟ من كل خدمة تم بيعها فعلًا في الفترة، والورقة بتطلع للفترة

### English

- A salon with a clear book, and chairs that are busy at the right hour
- The booking book on the phone, a commission the stylist agrees with, and session packages that expire on a date
- The book shows who is free and who is busy at a glance
- The commission is computed from the services really sold and the sheet comes out before the month ends
- The client gets a WhatsApp reminder and can cancel, which fills the slot instead of losing it

Questions the page must answer:

- What if the client does not show up? The reminder and the wait list fill the slot instead of losing it, and the no show is recorded with the minutes
- How are the commissions computed? From every service really sold in the period, and the sheet comes out for that period

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- The book: the day with the columns of the stylists and the slots, the booked, the free and the blocked, with the name and the phone
- New booking: the client, the service, the stylist, the time, the deposit and the reminder, in one flow that works on the phone
- Wait list: the clients who want a slot and accept a cancellation, called in order
- The stylist view: her day, her clients, the services, the times and the money she made that day
- Retail shelf: the products sold next to the service, with the opening date and the days left
- Packages: the sessions bought and used, with the expiry, for the client and for the salon

## 9. Pricing tier notes

- The free tier fits one chair: one business, one branch, two seats, the book and the till
- Starter adds the reminders, the wait list and a year of history
- The Business tier adds the packages, the retail shelf with the opening dates and the commission sheet
- The booking page on the public site is priced per business, not per stylist

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | An ERP where a salon needs a book, a chair and a commission | A salon flow built on the chair and the hour, with the commission the stylist can check |
| Square | Free with processing fees, Plus US$49 per month per location (squareup.com, opened 2026-11-12) | Bookings are an add on and there is no stylist commission model | The book, the wait list and the commission are part of the pack |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | A retail till with no appointments and no time based stock | The time is the stock here, so the whole product is built around it |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-salon-tasks.md`:

1. Register the salon pack in the sector registry (M1)
2. Write the salon data model with appointments, packages and commissions (M1)
3. Build the salon seed with the Arabic service categories (M1)
4. Write the salon terminology map in Arabic and English (M1)
5. Build the booking book grid (M2)
6. Build the new booking flow with the deposit and the reminder (M2)
7. Build the wait list and the no show flow (M2)
8. Build the packages with the expiry and the sessions used (M2)
9. Build the commission sheet (M2)
10. Build the salon report pack and the public booking page (M3)

## 12. Risks, unknowns and what we refuse to fake

- The client notes and the preferences are personal data of the salon, so they never enter our analytics and can be exported and deleted
- The reminder and the cancellation offer go through the salon own WhatsApp account, and the template rules of the platform apply to them
- The commission percentage is the salon own agreement, and the product never changes it
- Before and after photos of a client need a written consent, so the app asks for it before any photo is stored

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-salon-tasks.md`
