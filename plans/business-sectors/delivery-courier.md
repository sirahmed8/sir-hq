# SIR Business sector: Delivery and courier (توصيل وشحن)

> Round r56 (2026-11-12). Sector 13 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `delivery`, group `delivery`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The courier owner manages a fleet of riders and vehicles. Their day is job assignments, route changes, cash reconciliation and proving each delivery arrived on time.

Why this sector is in the catalogue: Egypt's delivery market is growing fast. Riders, zones, cash-on-delivery and proof of delivery are the core ops every courier needs.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- CourierCompany (id, nameAr, nameEn, branchId, phone, email, taxRegistration)
- Rider (id, name, phone, vehicleId, status, commissionRate, earningsPiasters)
- Vehicle (id, plate, type, status, lastSeen)
- Zone (id, nameAr, nameEn, areas, minRadius, maxRadius)
- DeliveryOrder (id, companyId, customerPhone, customerName, pickupName, pickupAddr, deliveryAddr, status, zoneId, assignedRider, codAmountPiasters, deliveredAt, proofType, proofRef)
- Route (id, companyId, orderIds, waypoints, estimatedDuration, actualDuration)
- Customer (id, phone, name, notes, optInWhatsApp)

Units in use: piece, kilogram, litre, box, envelope, parcel

Batches: No : delivery orders carry no stock or expiry

Expiry and shelf life: Not applicable. Orders are time-sensitive not product-sensitive

Sector specific structures: The core structures are the delivery order with its status lifecycle, the zone geometry for route planning, the COD reconciliation and the proof-of-delivery (photo or signature) artefact

## 3. Screens and workflows that belong to this sector

- Dashboard: today's assignments, unassigned orders, rider status and zone heat map
- Order intake: create a new delivery order with pickup, delivery address, COD amount and service type
- Route map: assigned orders on a map with rider location and ETA
- COD reconciliation: counted cash vs expected per shift, variance and audit log
- Proof of delivery: photo upload, signature capture, customer confirmation
- Rider panel: assigned orders, route, earnings, pause/resume
- Customer status: live order tracking with ETA and delivery completed notice

## 4. Roles and permissions

- Owner: everything : fleet, pricing, payouts, reports
- Manager: riders, zones, order assignments, payout approval
- Cashier: COD counting, shift close, variance reporting
- Rider: assigned orders only, status updates, pause/resume

## 5. Reports and KPIs

- Daily dispatch report: orders dispatched, dispatched per zone, on-time rate
- COD summary: counted vs expected, variance, trends
- Rider performance: completed orders, earnings, on-time rate
- Zone analytics: orders per zone, peak times, unassigned rate
- Customer repeat rate: opt-in WhatsApp and return orders

## 6. Integrations that matter

- Web GPS tracker for rider location
- WhatsApp Business for customer delivery updates
- Paymob or Fawry for COD card collection (optional)
- SMS gateway for delivery notifications
- Google Maps routing

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Company basics: name, branch, address, phone, currency, working hours
- Zones: define the geographic zones riders operate in
- Riders: add riders with contact and commission terms
- Service types: define the delivery categories (same-day, scheduled, COD)
- First week plan: assign first rider, first order, first route, first COD close

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
- o
- r
- d
- e
- r
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

- خدمة التوصيل والشحن
- ادِر riders، الركازات وأوامر التوصيل من لوحة تحكم واحدة
- تتبع الطلبات لحظياً
- إدارة الكود Cash on Delivery
- تقارير أداء riders

Questions the page must answer:

- كيف أضيف rider جديد؟
- ما هي رسوم العمولة؟

### English

- Delivery & Courier Management
- Manage riders, zones and delivery orders from one dashboard
- Real-time order tracking
- COD management
- Rider performance reports

Questions the page must answer:

- How do I add a new rider?
- What is the commission rate?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Dashboard: today's assignments, unassigned orders, rider status and zone heat map
- Order intake: create a new delivery order with pickup, delivery address, COD amount and service type
- Route map: assigned orders on a map with rider location and ETA
- COD reconciliation: counted cash vs expected per shift, variance and audit log
- Proof of delivery: photo upload, signature capture, customer confirmation
- Rider panel: assigned orders, route, earnings, pause/resume

## 9. Pricing tier notes

- - Basic plan: 150 EGP / month per rider
- - Pro plan: 300 EGP / month, includes zone analytics and COD reconciliation
- - Enterprise: custom pricing for 10+ riders

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Sapaad | from 200 EGP/mo | no built-in rider GPS | native rider tracking and COD reconciliation |
| Kashat | from 250 EGP/mo | limited zone geometry | flexible zone rules and per-region pricing |
| Dukan | from 180 EGP/mo | no COD reconciliation | full COD counting and variance reporting |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-delivery-courier-tasks.md`:

1. Add delivery order creation screen with COD field (M1)
2. Implement rider assignment and zone picker (M2)
3. Add COD shift reconciliation screen (M2)
4. Add rider dashboard with order list and status update (M3)
5. Add WhatsApp deep link for customer order status (M3)
6. Add route map with rider location (M4)
7. Add electronic proof of delivery (photo/signature) (M4)
8. Add daily dispatch report (M5)
9. Add rider earnings calculator (M5)
10. Add rider onboarding flow (first ride) (M1)

## 12. Risks, unknowns and what we refuse to fake

- Riders may deliver to wrong address without photo proof
- COD variance can grow if counting is inconsistent
- GPS tracking accuracy depends on phone and network
- WhatsApp template rejection if not approved by Meta

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-delivery-courier-tasks.md`
