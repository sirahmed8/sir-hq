# SIR Business sector: Spa and wellness (سبا وعناية)

> Round r56 (2026-11-12). Sector 25 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `service`, group `service`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The spa manager oversees package sales, room scheduling and client preference records. Their day is package sales, expiry tracking and room assignments.

Why this sector is in the catalogue: Spa and wellness centres sell package sessions (e.g. 10-session bundles) with expiry, private room scheduling and client preference tracking. The key is package sales, expiry tracking and client consent.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Spa (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Package (id, spaId, nameAr, nameEn, sessionCount, pricePiasters, expiryDays, isActive, features)
- Client (id, spaId, name, phone, preferencesAr, preferencesEn, consentPhotos, visitCount, totalSpentPiasters, lastVisit)
- Room (id, spaId, label, capacity, status, bookedBy, bookedAt, expiresAt)
- Appointment (id, roomId, clientId, dateTime, duration, serviceType, status, notes)
- PackageRedemption (id, packageId, clientId, sessionsUsed, sessionsRemaining, expiryDate, status, redeemedAt)

Units in use: session, package, room, appointment

Batches: No : spa carries no stock or expiry (package expiry is tracked via expiryDays and expiryDate)

Expiry and shelf life: Packages have expiry days from purchase and an expiry date; sessions must be used before expiry

Sector specific structures: The core structures are the package with session count and expiry, the client with preference tracking and photo consent, the room scheduling and the redemption tracker. Package expiry is the key differentiator from other service sectors.

## 3. Screens and workflows that belong to this sector

- Package catalogue: list of packages with session count, price, expiry days, features (fast lane, private room, etc.), activate/deactivate
- Client profile: name, phone, preferences, consent flag for photos, visit count, total spent, last visit, active redemptions
- Room scheduler: available rooms per time slot, book room, assign client, mark status (available/booked/free)
- Package redemption: select package, view sessions used/remaining, expiry date, update status (active/used/expired)
- Appointment scheduler: select room, date/time, service type, client, status (scheduled/in-progress/completed)
- Redemption history: all redemptions per client, sessions used, remaining, expiry events
- Staff shift: clock in/out, client load per hour, notes

## 4. Roles and permissions

- Owner: everything : packages, clients, rooms, appointments, redemptions, reports, billing
- Therapist: view appointments, mark in-progress/completed, view client preferences
- Front desk: package sales, client check-in, room booking, redemption processing
- Manager: package creation, pricing, therapist scheduling, reports

## 5. Reports and KPIs

- Package sales revenue: total per period, per package, sessions used vs total per package
- Package expiry rate: how many packages expired per period, how many sessions lost
- Client retention: visit count per client, total spent per client, re-book rate
- Room utilisation: booked hours vs available per period, peak times
- Therapist workload: appointments per period, utilisation rate per therapist

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and package redemptions
- WhatsApp deep link for package renewal notices and appointment reminders
- Email for invoice and package expiry notices (opt-in)
- Calendar sync for room bookings (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Spa basics: name, branch, address, phone, currency, working hours
- Initial packages: the starting packages (5-session, 10-session, 20-session) with price, expiry days and features
- Client intake: the fields collected (name, phone, preferences, photo consent)
- Staff: add the initial team with their role templates
- First week plan: create first package, first client, first room booking

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
- p
- a
- c
- k
- a
- g
- e
-  
- w
- i
- t
- h
-  
- e
- x
- p
- i
- r
- y
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

- سبا وعناية
- حزم جلسات، انتهاء وحجز غرف من لوحة واحدة
- حزم جلسات بفترات صلاحية
- حجز غرف خاصة
- تفضيلات العميل وتخزين consent

Questions the page must answer:

- كيف أشتري حزمة جلسات؟
- متى تنتهي صلاحية الحزمة؟

### English

- Spa & Wellness Management
- Package sessions, expiry and room booking from one dashboard
- Package sessions with expiry tracking
- Private room booking and scheduling
- Client preference and consent tracking

Questions the page must answer:

- How do I purchase a package?
- When does the package expire?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Package catalogue: list of packages with session count, price, expiry days, features (fast lane, private room, etc.), activate/deactivate
- Client profile: name, phone, preferences, consent flag for photos, visit count, total spent, last visit, active redemptions
- Room scheduler: available rooms per time slot, book room, assign client, mark status (available/booked/free)
- Package redemption: select package, view sessions used/remaining, expiry date, update status (active/used/expired)
- Appointment scheduler: select room, date/time, service type, client, status (scheduled/in-progress/completed)
- Redemption history: all redemptions per client, sessions used, remaining, expiry events

## 9. Pricing tier notes

- - Basic: 200 EGP / month, up to 3 packages, 10 sessions each
- - Professional: 400 EGP / month, unlimited packages, expiry tracking
- - Enterprise: custom for spa chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| SpaPro | from 500 EGP/mo | no package expiry tracking | full package expiry from purchase date with sessions-used and remaining |
| WellnessClub | from 480 EGP/mo | no room scheduler | room scheduler with available slots per time and booking management |
| BodyCare | from 520 EGP/mo | no client preference photo consent | client preferences with photo consent flag and storage |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-spa-wellness-tasks.md`:

1. Add package catalogue with expiry days and features (M1)
2. Add client profile with preferences and photo consent (M1)
3. Add room scheduler with available slots per time (M1)
4. Add package redemption screen (M1)
5. Add appointment scheduler with room and client (M1)
6. Add redemption history per client (M2)
7. Add package expiry rate report (M2)
8. Add room utilisation report (M2)
9. Add therapist workload report (M2)
10. Add onboarding flow for initial spa wellness setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes client and package records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Package expiry without clear purchase-date linkage can violate consumer protection law
- Photo consent storage without proper legal basis can violate PDPL

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-spa-wellness-tasks.md`
