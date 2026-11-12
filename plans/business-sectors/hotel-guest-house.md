# SIR Business sector: Hotel and guest house (فندق وغرفة مفروشة)

> Round r56 (2026-11-12). Sector 37 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `hospitality`, group `hospitality`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The hotel owner manages room inventory, housekeeping board, reservations and deposits. Their day is room bookings, housekeeping status and invoice generation per stay with city tax.

Why this sector is in the catalogue: Hotels and guest houses need room calendar, housekeeping board, reservation window, deposits and refund rules, invoice per stay and city tax handling. The key is the room calendar with housekeeping status and deposit tracking.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Hotel (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours, cityTaxPercent)
- Room (id, hotelId, label, type (single/double/suite), capacity, pricePiasters per night, status (available/cleaned/occupied/inspected), housekeepingStatus (clean/dirty/inspected), lastCleanedAt)
- Reservation (id, hotelId, roomId, clientName, clientPhone, checkInDate, checkOutDate, depositPiasters, totalPiasters nightCount, status (confirmed/cancelled/noShow), notes, cityTaxStatus (paid/pending/unpaid))
- HousekeepingBoard (id, hotelId, roomId, status, task (checkout/clean/inspect), assignedTo, completedAt, notes)
- Invoice (id, reservationId, subtotalPiasters, cityTaxPiasters, totalPiasters, status (pending/paid/cancelled), issuedAt, notes)
- Staff (id, hotelId, name, phone, role, hourlyRatePiasters, status)

Units in use: room, night, reservation, invoice

Batches: No : hotel carries no stock or expiry

Expiry and shelf life: Not applicable. Reservations have check-in/out dates, invoices have status

Sector specific structures: The core structures are the room with housekeeping status, the reservation with deposit and city tax, the housekeeping board with task assignment and the invoice with city tax handling. Room status lifecycle (available→cleaned→occupied→inspected) is the key differentiator.

## 3. Screens and workflows that belong to this sector

- Room calendar: month view with room labels, status colours (available/cleaned/occupied/inspected), housekeeping status badge, reservation overlay
- Room detail: label, type, capacity, price per night, current status, housekeeping status, last cleaned, associated reservation
- Reservation creation: select room, enter client name and phone, check-in/check-out dates, set deposit % and amount, set total (nightCount × price), set status (confirmed/cancelled/noShow), set city tax status (paid/pending/unpaid)
- Housekeeping board: list of rooms with task (checkout/clean/inspect), assigned to, completed at, notes. Drag to reassign,
- Invoice editor: select reservation, compute subtotal (nightCount × price), city tax (percent of subtotal), total, set status (pending/paid/cancelled), issue, add notes
- Reservation list: all reservations with room, client, dates, status, deposit, city tax status
- Housekeeping task assign: select room, select task, assign to staff, set deadline, track completion
- Cash register: scan reservation reference, record payment, print receipt with invoice

## 4. Roles and permissions

- Owner: everything : rooms, reservations, housekeeping, invoices, city tax, reports, billing
- Front desk: create reservations, check-in/out, payment, invoice generation
- Housekeeping manager: assign tasks, track completion, status updates on board
- Cashier: record payments against invoices, print receipts

## 5. Reports and KPIs

- Occupancy rate per period: occupied rooms vs available rooms per day/week/month, occupancy %
- Revenue per period: total night revenue, total city tax collected, total revenue (nights + tax)
- Average daily rate (ADR): total night revenue / occupied rooms per period
- Housekeeping efficiency: rooms cleaned per day, average time in status, tasks completed per staff
- Reservation status: confirmed vs cancelled vs noShow counts per period, city tax collected vs pending

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and invoices
- WhatsApp deep link for reservation confirmations and city tax payment reminders
- Email for invoice delivery and city tax receipts (opt-in)
- Online booking platform integration (API, optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Hotel basics: name, branch, address, phone, currency, working hours, city tax percent
- Initial room types: the starting room types (single/double/suite) with capacity and price per night
- Housekeeping tasks: the standard tasks (checkout/clean/inspect) and assignment rules
- Staff: add the initial team with their role templates
- First week plan: create first room type, first reservation, first housekeeping task

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
- r
- o
- o
- m
- /
- h
- o
- u
- s
- e
- k
- e
- e
- p
- i
- n
- g
- /
- r
- e
- s
- e
- r
- v
- a
- t
- i
- o
- n
-  
- s
- c
- h
- e
- m
- a
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

- فندق وغرفة مفروشة
- تقويم غرف، housekeeping وفواتير من لوحة واحدة
- تقويم غرف مع حالة housekeeping
- حجوزات مع عربون ودفاتر مدينة
- فواتير وإيرادات مدينة

Questions the page must answer:

- كيف أحجز غرفة؟
- ما نسبة الضريبة المدينة؟

### English

- Hotel & Guest House Management
- Room calendar, housekeeping and invoices with city tax from one dashboard
- Room calendar with housekeeping status
- Reservations with deposit and city tax
- Invoices with city tax handling

Questions the page must answer:

- How do I book a room?
- What is the city tax percentage?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Room calendar: month view with room labels, status colours (available/cleaned/occupied/inspected), housekeeping status badge, reservation overlay
- Room detail: label, type, capacity, price per night, current status, housekeeping status, last cleaned, associated reservation
- Reservation creation: select room, enter client name and phone, check-in/check-out dates, set deposit % and amount, set total (nightCount × price), set status (confirmed/cancelled/noShow), set city tax status (paid/pending/unpaid)
- Housekeeping board: list of rooms with task (checkout/clean/inspect), assigned to, completed at, notes. Drag to reassign,
- Invoice editor: select reservation, compute subtotal (nightCount × price), city tax (percent of subtotal), total, set status (pending/paid/cancelled), issue, add notes
- Reservation list: all reservations with room, client, dates, status, deposit, city tax status

## 9. Pricing tier notes

- - Starter: 300 EGP / month, 1 branch, up to 20 rooms
- - Professional: 650 EGP / month, unlimited rooms, housekeeping module
- - Enterprise: custom for hotel chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| HotelPro | from 800 EGP/mo | no housekeeping board | full housekeeping board with task assignment and completion tracking |
| StayWell | from 750 EGP/mo | no city tax handling in invoices | city tax auto-compute (percent of subtotal) in every invoice |
| GuestHouseMart | from 820 EGP/mo | no room calendar with status | room calendar with status lifecycle (available/cleaned/occupied/inspected) |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-hotel-guest-house-tasks.md`:

1. Add room calendar with housekeeping status (M1)
2. Add reservation creation with deposit and city tax (M1)
3. Add housekeeping board with task assignment (M1)
4. Add invoice editor with city tax auto-compute (M1)
5. Add occupancy rate report (M1)
6. Add revenue per period report (M1)
7. Add average daily rate (ADR) report (M1)
8. Add housekeeping efficiency report (M1)
9. Add reservation status report (M1)
10. Add onboarding flow for initial hotel setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes room and reservation records unrecoverable
- WhatsApp template rejection if not approved by Meta
- City tax without proper legal basis can violate local taxation law
- Housekeeping task assignment without audit trail can lead to disputes over room status

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-hotel-guest-house-tasks.md`
