# SIR Business sector: Pet shop (محل حيوانات أليفة)

> Round r56 (2026-11-12). Sector 27 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `retail`, group `retail`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The pet shop owner manages pet food stock, accessories and grooming appointments. Their day is food stock checks, grooming slot scheduling and vet referral hand-offs.

Why this sector is in the catalogue: Pet shops sell pet food, accessories and grooming services. They need FEFO food tracking, grooming slot scheduling and vet link hand-off. The key is FEFO pet food and grooming appointments.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Product (id, shopId, sku, nameAr, nameEn, type (food/toy/accessory), brand, weightKg (for food), pricePiasters, costPiasters, taxRate, fe4oFlag, expiryDate, stockQty, status, locationShelf)
- GroomingAppointment (id, shopId, petName, petType, dateTime, duration, service (bath/trim/ full groom), pricePiasters, status, notes)
- Customer (id, shopId, name, phone, optInWhatsApp, purchaseHistoryCount, totalSpentPiasters)
- VetReferral (id, shopId, petName, petType, issue, referredTo, referredAt, status)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: piece, pack, kilogram, liter, appointment

Batches: Yes for pet food: FEFO batches with supplier, received date, expiry date and cost, so the shop can sell by batch and claim credit

Expiry and shelf life: Pet food has expiry dates tracked per batch; the shop sees alerts for items expiring in 30/60/90 days

Sector specific structures: The core structures are the FEFO-tracked pet food, the grooming appointment with service type and duration, and the vet referral hand-off. FEFO food expiry is the key differentiator from regular retail.

## 3. Screens and workflows that belong to this sector

- Product catalogue: grid of pet products with name, type, price, weight (for food), FEFO badge, expiry date badge, stock
- Product detail: full info, batch details, supplier, reorder point, FEFO expiry alert
- Grooming appointment scheduler: select service (bath/trim/full groom), date/time, pet name and type, set price, status (booked/in-progress/done)
- Customer profile: name, phone, purchase history, opt-in WhatsApp, grooming history
- FEFO food radar: items expiring in 30/60/90 days, value at risk, one-tap discount tag
- Vet referral hand-off: enter issue, referred clinic, referral status (pending/accepted/rejected), date
- Cash register: scan SKU or product, apply FEFO discount if urgent, tender payment, print receipt with FEFO note
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : inventory, grooming, vet referrals, reports, billing
- Groomer: create grooming appointments, mark in-progress/done, update pet notes
- Sales rep: manage product stock, create grooming appointments, handle vet referrals
- Cashier: scan products, tender payment, print receipt

## 5. Reports and KPIs

- Product sales by type: food vs toys vs accessories, revenue per type per period
- FEFO food radar: items expiring in 30/60/90 days, value at risk, discounts applied
- Grooming appointment pipeline: booked/in-progress/done counts per period, average duration
- Customer retention: visit count per customer, total spent per customer, re-book rate
- Vet referral status: pending/accepted/rejected counts per period

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and grooming completion notes
- WhatsApp deep link for grooming ready notifications and vet referral follow-ups
- Email for vaccination record requests (opt-in)
- SMS for food expiry alerts (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial product list: the starting pet food and accessories with SKU, prices and FEFO flag
- Grooming services: the service types (bath, trim, full groom) and pricing
- Staff: add the initial team with their role templates
- First week plan: receive first stock, create first grooming appointment, first vet referral

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
- F
- E
- F
- O
-  
- p
- e
- t
-  
- f
- o
- o
- d
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

- محل حيوانات أليفة
- طعام، إكسسوارات وحجوزات من لوحة واحدة
- تتبع FEFO للطعام
- حجوزات الحلاقة
- حيل الإحالة للطبيب البيطري

Questions the page must answer:

- كيف أحجز موعد حلاقة؟
- ما نوع الطعام الموجود؟

### English

- Pet Shop Management
- Pet food, accessories and grooming from one dashboard
- FEFO-tracked pet food with expiry
- Grooming appointment scheduling
- Vet referral hand-off

Questions the page must answer:

- How do I book a grooming appointment?
- What food is available?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Product catalogue: grid of pet products with name, type, price, weight (for food), FEFO badge, expiry date badge, stock
- Product detail: full info, batch details, supplier, reorder point, FEFO expiry alert
- Grooming appointment scheduler: select service (bath/trim/full groom), date/time, pet name and type, set price, status (booked/in-progress/done)
- Customer profile: name, phone, purchase history, opt-in WhatsApp, grooming history
- FEFO food radar: items expiring in 30/60/90 days, value at risk, one-tap discount tag
- Vet referral hand-off: enter issue, referred clinic, referral status (pending/accepted/rejected), date

## 9. Pricing tier notes

- - Starter: 120 EGP / month, 1 branch, up to 50 products
- - Professional: 250 EGP / month, unlimited products, grooming module
- - Enterprise: custom for pet shop chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| PetCare | from 300 EGP/mo | no FEFO food tracking | full FEFO pet food tracking with expiry radar and 30/60/90 day alerts |
| CocoPet | from 280 EGP/mo | no grooming appointment scheduler | full grooming appointment from booking to completion with status |
| PawShop | from 320 EGP/mo | no vet referral hand-off | full vet referral from issue to accepted/rejected with status |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-pet-shop-tasks.md`:

1. Add FEFO-tracked pet food catalogue (M1)
2. Add grooming appointment scheduler (M1)
3. Add FEFO food radar with expiry alerts (M1)
4. Add customer profile with grooming history (M1)
5. Add vet referral hand-off screen (M1)
6. Add cash register with FEFO discount (M1)
7. Add grooming appointment pipeline report (M2)
8. Add customer retention report (M2)
9. Add vet referral status report (M2)
10. Add onboarding flow for initial pet shop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes product and appointment records unrecoverable
- WhatsApp template rejection if not approved by Meta
- FEFO expiry without proper batch tracking can safety-compromise pets
- Vet referral without documented hand-off can lead to lost follow-up

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-pet-shop-tasks.md`
