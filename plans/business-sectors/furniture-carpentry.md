# SIR Business sector: Furniture and carpentry (أثاث ونجارة)

> Round r56 (2026-11-12). Sector 29 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `retail + production`, group `retail-and-commerce`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The furniture carpenter sells custom pieces, manages client deposits and coordinates delivery. Their day is client specs, deposit tracking and delivery slot scheduling.

Why this sector is in the catalogue: Furniture shops sell custom-sized items, require deposits for big-ticket orders and offer delivery slots. Distinct from fast retail: long production cycles, custom specs and deposits.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- DesignSpec (id, shopId, clientName, clientPhone, drawingsAr, drawingsEn, dimensions (l,w,h), material, finish, status, createdAt)
- Order (id, shopId, designSpecId, clientName, clientPhone, depositPiasters, totalPiasters, balancePiasters, status, deliverySlot, deliveryDate, notes)
- DeliverySlot (id, shopId, date, startTime, endTime, assigned, status)
- Payment (id, orderId, amountPiasters, method, status, paidAt, receiptPrinted)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: piece, meter, set, room

Batches: No : furniture shop carries no stock or expiry

Expiry and shelf life: Not applicable. Orders have delivery dates not expiry dates

Sector specific structures: The core structures are the design specification per client, the order with deposit and balance, and the delivery slot scheduling. Deposits are a fixed percentage of the total and are tracked separately.

## 3. Screens and workflows that belong to this sector

- Design spec editor: enter client name and phone, upload or draw sketches (Ar/En), set dimensions (l,w,h), select material and finish, save spec
- Order creation: select design spec, set deposit percentage and amount, set total price, compute balance, set delivery slot and date, set status (draft/confirmed/in-progress/completed)
- Delivery slot scheduler: available slots per day, assign slot, mark assigned, update status
- Order list: all orders with status, client, deposit, balance, delivery slot and date
- Payment screen: record payment against order balance, update status, print receipt
- Design gallery: view saved design specs with client name and dimensions
- Cash register: scan order reference, record payment, print receipt

## 4. Roles and permissions

- Owner: everything : designs, orders, deposits, delivery, reports, billing
- Carpenter: create design specs, update orders, mark payments received
- Sales rep: create design specs, client quotes, order creation
- Cashier: record payments against orders, print receipts

## 5. Reports and KPIs

- Order book: all orders by status (draft/confirmed/in-progress/completed), total revenue, total deposits, total outstanding balance
- Deposit tracking: total deposits received vs total orders, outstanding deposits per order
- Delivery slot utilisation: slots booked vs available per period, on-time delivery rate
- Revenue per period: total sales, deposits collected, balance collected
- Popular materials and finishes: which combinations are most requested

## 6. Integrations that matter

- WhatsApp deep link for client communication (spec updates, delivery notifications)
- Esc/POS thermal printer for receipts and payment records
- Google Calendar for delivery slot scheduling (optional)
- SMS for delivery ETA alerts (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial design specs: the starting catalogue of sample designs with dimensions and materials
- Deposit policy: the percentage and terms for deposits on orders
- Staff: add the initial team with their role templates
- First week plan: create first design spec, first order, first deposit received

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
- d
- e
- s
- i
- g
- n
-  
- s
- p
- e
- c
-  
- f
- l
- a
- g
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

- أثاث ونجارة
- مقاسات مخصصة، تقسيط وSlots التسليم من لوحة واحدة
- تصاميم مقاس مخصص
- نظام التقسيط مع الوديعة
- Slots التسليم المتاحة

Questions the page must answer:

- هل يمكن تصميم قطعة بأبعاد محددة؟
- ما نسبة الوديعة المطلوبة؟

### English

- Furniture & Carpentry Management
- Custom designs, deposits and delivery slots from one dashboard
- Custom design specifications per client
- Deposit tracking with percentage of total
- Delivery slot scheduling and tracking

Questions the page must answer:

- Can I design a piece with specific dimensions?
- What deposit percentage is required?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Design spec editor: enter client name and phone, upload or draw sketches (Ar/En), set dimensions (l,w,h), select material and finish, save spec
- Order creation: select design spec, set deposit percentage and amount, set total price, compute balance, set delivery slot and date, set status (draft/confirmed/in-progress/completed)
- Delivery slot scheduler: available slots per day, assign slot, mark assigned, update status
- Order list: all orders with status, client, deposit, balance, delivery slot and date
- Payment screen: record payment against order balance, update status, print receipt
- Design gallery: view saved design specs with client name and dimensions

## 9. Pricing tier notes

- - Starter: 200 EGP / month, 1 branch, up to 20 design specs
- - Professional: 450 EGP / month, unlimited specs, deposit module
- - Enterprise: custom for furniture chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| FurniturePro | from 600 EGP/mo | no deposit tracking | full deposit tracking with percentage of total and balance computation |
| CarpentryMart | from 550 EGP/mo | no delivery slot scheduler | delivery slot scheduling with available slots and on-time rate |
| DesignHub | from 620 EGP/mo | no order book with status tracking | full order book with status (draft/confirmed/in-progress/completed) |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-furniture-carpentry-tasks.md`:

1. Add design spec editor with Ar/En sketches and dimensions (M1)
2. Add order creation with deposit and delivery slot (M1)
3. Add delivery slot scheduler with available slots (M1)
4. Add payment screen against order balance (M1)
5. Add order book report with status breakdown (M2)
6. Add deposit tracking report (M2)
7. Add delivery slot utilisation report (M2)
8. Add revenue per period report (M2)
9. Add popular materials and finishes report (M3)
10. Add onboarding flow for initial furniture shop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes design specs and order records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Deposits without clear percentage and terms can violate consumer protection law
- Delivery slots without clear confirmation can lead to no-show disputes

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-furniture-carpentry-tasks.md`
