# SIR Business sector: General clinic (عيادة)

> Round r56 (2026-11-12). Sector 14 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `clinic`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The clinic owner sees patients across morning and evening shifts. Their day is appointments, patient histories, lab requests and printing prescriptions for patients to take to a pharmacy.

Why this sector is in the catalogue: Egyptian clinics need appointment scheduling, patient record keeping and prescription printing without crossing into medical-device claims.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Clinic (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Patient (id, clinicId, name, phone, encryptedHealthData, consentWhatsApp, guardianPhone, visitsCount, lastVisit)
- Appointment (id, clinicId, patientId, dateTime, duration, type, status, notes, followUpRequired)
- LabOrder (id, clinicId, patientId, testType, status, resultStatus, requestedAt, collectedAt, reportedAt)
- Prescription (id, clinicId, patientId, issuedAt, lines with medicineRef, dosage, notes, validUntil)
- Staff (id, clinicId, name, phone, role, hourlyRatePiasters, status)

Units in use: visit, appointment, test, prescription

Batches: No : clinic carries no stock or expiry

Expiry and shelf life: Not applicable. Patient data is not product-based

Sector specific structures: The core structures are the appointment lifecycle, the encrypted patient record, the lab order tracking and the printable prescription. Patient data is special-category: encrypted, exportable on request, deletable on request.

## 3. Screens and workflows that belong to this sector

- Appointment calendar: day/week view with patient names, status colours and duration slots
- Patient record: name, phone, guardian phone, visit history, consent flag, encrypted health data summary
- Lab order: test type, status (pending/collected/reported), result status, dates
- Prescription editor: medicine list, dosage, instructions, printable layout with doctor signature
- Visit summary: recap of symptoms, recommendations, follow-up dates, printable PDF
- Staff shift: clock in/out, patient load per hour, notes

## 4. Roles and permissions

- Owner: everything : menu, staff, reports, billing
- Manager: everything except billing and export; approves leaves and overrides
- Nurse: patient vitals entry, lab order entry, prescription countersign
- Cashier: appointment billing, receipt printing, shift close

## 5. Reports and KPIs

- Appointments by day and hour: utilisation and no-show rate
- Patient visit frequency: returning patients, new patients per month
- Lab order status: pending, collected, reported counts
- Prescription volume per doctor, per period
- Staff shift summary: hours worked, patient load, notes

## 6. Integrations that matter

- Esc/POS thermal printer for prescriptions
- WhatsApp deep link for appointment reminders and confirmations
- Email for lab result delivery (opt-in)
- Google Calendar sync for appointment reminders

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Clinic basics: name, branch, address, phone, currency, working hours
- Specialities: the clinic's medical specialities and the staff assigned
- Appointment types: the visit types the clinic offers (consultation, follow-up, check-up)
- Staff: add the initial team with their role templates
- First week plan: set up first appointment type, first patient record, first prescription format

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
- a
- p
- p
- o
- i
- n
- t
- m
- e
- n
- t
- /
- p
- a
- t
- i
- e
- n
- t
- /
- p
- r
- e
- s
- c
- r
- i
- p
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

- العيادات العامة
- مواعيد، سجلات مرضى ووصفات طباعة من لوحة واحدة
- حجز المواعيد وحظر التداخل
- سجلات مرضى مشفرة وخابلة للحذف
- وصفات طباعة فورية

Questions the page must answer:

- كيف أسجل مريض جديد؟
- هل يمكنني حذف سجل patient؟

### English

- General Clinic Management
- Appointments, patient records and prescription printing from one dashboard
- Appointment scheduling with conflict prevention
- Encrypted patient records with export/delete on request
- Printable prescriptions instantly

Questions the page must answer:

- How do I register a new patient?
- Can I delete a patient record?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Appointment calendar: day/week view with patient names, status colours and duration slots
- Patient record: name, phone, guardian phone, visit history, consent flag, encrypted health data summary
- Lab order: test type, status (pending/collected/reported), result status, dates
- Prescription editor: medicine list, dosage, instructions, printable layout with doctor signature
- Visit summary: recap of symptoms, recommendations, follow-up dates, printable PDF
- Staff shift: clock in/out, patient load per hour, notes

## 9. Pricing tier notes

- - Starter: 120 EGP / month, 1 branch, up to 3 staff
- - Professional: 250 EGP / month, unlimited staff, reports
- - Enterprise: custom for multi-branch clinics

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Dafne | from 300 EGP/mo | no encrypted patient data export | field-level AES-256-GCM encryption and deletion on request |
| Tiba | from 250 EGP/mo | no WhatsApp appointment reminders | WhatsApp deep links for reminders and confirmations |
| Sehaty | from 280 EGP/mo | no prescription print layout customisation | fully customisable prescription templates |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-clinic-tasks.md`:

1. Add appointment calendar screen with conflict detection (M1)
2. Add encrypted patient record screen (M1)
3. Add lab order screen with status tracking (M2)
4. Add printable prescription editor (M2)
5. Add WhatsApp deep link for appointment reminder (M2)
6. Add visit summary screen with printable PDF (M3)
7. Add staff shift clock in/out screen (M3)
8. Add appointment no-show report (M4)
9. Add patient visit frequency report (M4)
10. Add onboarding flow for initial clinic setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Patient health data is special-category: mishandling violates PDPL
- Encryption key loss makes patient records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Over-prescription risk if the system does not flag duplicate medicines

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-clinic-tasks.md`
