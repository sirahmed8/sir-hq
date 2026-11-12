# SIR Business sector: Veterinary clinic (عيادة بيطرية)

> Round r56 (2026-11-12). Sector 26 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `clinic + shop`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The vet sees animals across shifts. Their day is appointments, vaccination records, pet food/drug sales and controlled-substance tracking. Client consent is required for photos of pets.

Why this sector is in the catalogue: Veterinary clinics need appointment scheduling, pet records (vaccinations), pet food/drug sales with FEFO and reminders. Some controlled vet drugs are tracked like a pharmacy log.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Clinic (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Pet (id, clinicId, name, species, breed, ownerName, ownerPhone, vaccinationRecord (array with vaccine type, date, nextDue), status, notes)
- Appointment (id, clinicId, petId, dateTime, duration, type (consultation/vaccination/surgery), status, notes)
- DrugSale (id, clinicId, productName, activeIngredient, quantityPiasters, costPiasters, taxRate, fe4oFlag, supplierId, expiryDate, status, prescriptionRequired)
- ControlledDrugLog (id, clinicId, drugName, batchId, quantityPiasters, dateIn, dateOut, authorisedBy, reason, status (administered/sold/wasted))
- Staff (id, clinicId, name, phone, role, hourlyRatePiasters, status)

Units in use: visit, appointment, drug sale, controlled dose

Batches: Yes for drugs and food: batches with supplier, received date, expiry date and cost, so the clinic can sell by batch and claim credit

Expiry and shelf life: Drugs and food have expiry dates tracked per batch; the clinic sees alerts for items expiring in 30/60/90 days

Sector specific structures: The core structures are the pet record with vaccination history, the drug sale with FEFO batch tracking, the controlled drug append-only log and the appointment system. Patient (pet) data has lower sensitivity than pharmacy but still requires consent for photos.

## 3. Screens and workflows that belong to this sector

- Appointment calendar: day/week view with animal names, status colours and duration slots
- Patient record: name, species, breed, owner name and phone, vaccination history (type, date, next due), notes, photo consent flag
- Drug catalogue: list of drugs with active ingredient, price, FEFO flag, expiry date, supplier, reorder point
- Controlled drug log: append-only list of administered/sold/wasted drugs with date, batch, quantity and authorised user
- Drug sale screen: select drug, enter quantity, check FEFO expiry, record sale, compute price with tax
- Vaccination reminder: list of pets due for vaccination, send notice
- Staff shift: clock in/out, patient load per hour, notes

## 4. Roles and permissions

- Owner: everything : appointments, drugs, controlled log, reports, billing
- Vet: create appointments, prescribe drugs, view controlled log, approve administration
- Veterinary assistant: enter drug sales, update controlled log, record vaccinations
- Cashier: record drug sales, print receipt, shift close

## 5. Reports and KPIs

- Vaccination compliance: pets due per period, by vaccine type, send-overdue notices
- Drug sales by type and period: which drugs sell most, revenue per drug per month
- Controlled drug log: administered vs sold vs wasted counts per period, audit trail
- Appointment no-show rate: per period, by vet, with overdue notice rates
- Drug expiry radar: items expiring in 30/60/90 days, value at risk

## 6. Integrations that matter

- Esc/POS thermal printer for prescriptions and receipts
- WhatsApp deep link for vaccination reminders and drug pick-up notifications
- Email for vaccination records and prescription copies (opt-in)
- SMS for drug expiry alerts (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Clinic basics: name, branch, address, phone, currency, working hours
- Initial drug catalogue: the starting list of common veterinary drugs with active ingredient, price and FEFO flag
- Vaccination schedule: the standard vaccine types and dates for dogs/cats
- Staff: add the initial team with their role templates
- First week plan: set up first appointment type, first drug catalogue entry, first vaccination reminder

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
- e
- t
-  
- r
- e
- c
- o
- r
- d
- /
- d
- r
- u
- g
-  
- s
- a
- l
- e
- /
- c
- o
- n
- t
- r
- o
- l
- l
- e
- d
-  
- l
- o
- g
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

- العيادة البيطرية
- مواعيد، لقاحات ومبيعات أدوية من لوحة واحدة
- تتبع اللقاحات وتذكيرات
- حزمة الأدوية بتracking FEFO
- سجل controlled drug append-only

Questions the page must answer:

- كيف أسجل لقاحاً جديداً؟
- ما هي الأدوية المسيطر عليها؟

### English

- Veterinary Clinic Management
- Appointments, vaccinations and drug sales from one dashboard
- Vaccination compliance tracking and overdue notices
- FEFO drug batch tracking with expiry radar
- Controlled drug append-only log with audit trail

Questions the page must answer:

- How do I register a new vaccination?
- What are controlled drugs?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Appointment calendar: day/week view with animal names, status colours and duration slots
- Patient record: name, species, breed, owner name and phone, vaccination history (type, date, next due), notes, photo consent flag
- Drug catalogue: list of drugs with active ingredient, price, FEFO flag, expiry date, supplier, reorder point
- Controlled drug log: append-only list of administered/sold/wasted drugs with date, batch, quantity and authorised user
- Drug sale screen: select drug, enter quantity, check FEFO expiry, record sale, compute price with tax
- Vaccination reminder: list of pets due for vaccination, send notice

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 5 staff
- - Professional: 300 EGP / month, unlimited staff, drug module
- - Enterprise: custom for veterinary chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| VetPro | from 400 EGP/mo | no FEFO batch tracking | full FEFO batch tracking with expiry radar and 30/60/90 day alerts |
| AnimalCare | from 380 EGP/mo | no controlled drug log | append-only controlled drug log with authorisation and reason per entry |
| PetClinic | from 420 EGP/mo | no vaccination reminder | vaccination reminder with notice sending (WhatsApp/SMS) |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-veterinary-clinic-tasks.md`:

1. Add patient record with vaccination history (M1)
2. Add drug catalogue with FEFO flag and expiry (M1)
3. Add controlled drug append-only log (M1)
4. Add drug sale screen with FEFO check (M1)
5. Add vaccination reminder screen (M1)
6. Add controlled drug log audit report (M2)
7. Add drug expiry radar report (30/60/90 days) (M2)
8. Add vaccination compliance report (due per period) (M2)
9. Add appointment no-show rate report (M2)
10. Add onboarding flow for initial veterinary clinic setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes patient and drug records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Controlled drug log without append-only enforcement and audit can violate legal requirements
- Drug sales without proper prescription recording can violate veterinary regulations

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-veterinary-clinic-tasks.md`
