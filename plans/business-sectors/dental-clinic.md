# SIR Business sector: Dental clinic (عيادة أسنان)

> Round r56 (2026-11-12). Sector 15 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `clinic + dental`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The dentist sees patients across shifts. Their day is treatment plans, staged payments, tooth charting and follow-up reminders. Each treatment has a cost, a deposit and a schedule for the remaining installments.

Why this sector is in the catalogue: Dental clinics need treatment plans, staged payments (deposit + installments) and a tooth chart, distinct from general clinic appointments.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- DentalClinic (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Patient (id, clinicId, name, phone, encryptedHealthData, consentWhatsApp, guardianPhone, visitsCount)
- TreatmentPlan (id, patientId, nameAr, nameEn, surfaces, chartNumber, depositPiasters, totalPiasters, installmentCount, status, notes)
- ToothChart (id, patientId, chart with tooth numbers, surfaces marked, treatment notes per tooth)
- Installment (id, treatmentPlanId, amountPiasters, dueDate, status, paidAt)
- Appointment (id, clinicId, patientId, dateTime, duration, type, status, notes)

Units in use: visit, treatment, installment, tooth

Batches: No : dental clinic carries no stock or expiry

Expiry and shelf life: Not applicable. Treatment plans are not product-based

Sector specific structures: The core structures are the treatment plan with staged payments, the tooth chart per patient, the installment tracker and the appointment system. Patient data is special-category: encrypted, exportable on request, deletable on request.

## 3. Screens and workflows that belong to this sector

- Appointment calendar: day/week view with patient names, status colours
- Patient record: name, phone, guardian, visit history, consent flag, encrypted health summary
- Treatment plan editor: add plan, select tooth chart, set deposit and total, choose installment count
- Tooth chart: interactive chart with tooth numbers, mark surfaces treated, add notes per tooth
- Installment tracker: list of installments per treatment, amounts due, paid status, receipt print
- Payment screen: accept deposit or installment, record payment, print receipt
- Shift summary: patient load, treatments completed, outstanding installments

## 4. Roles and permissions

- Owner: everything : treatment plans, staff, reports, billing
- Dentist: create treatment plans, edit tooth chart, approve installments
- Dental assistant: enter treatment plans, chart teeth, mark installments paid
- Cashier: accept payments, print receipts, shift close

## 5. Reports and KPIs

- Treatment plan volume per dentist per period
- Installment collection rate: collected vs outstanding, aging report
- Tooth chart completion: which plans have full charting vs partial
- Patient treatment history: all plans per patient, completion rate
- Shift summary: hours worked, treatments completed, outstanding deposits

## 6. Integrations that matter

- Esc/POS thermal printer for payment receipts and treatment plans
- WhatsApp deep link for appointment reminders and follow-up prompts
- Email for treatment plan copies (opt-in)
- Google Calendar sync for appointment reminders

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Clinic basics: name, branch, address, phone, currency, working hours
- Specialities: the dental services offered (cleaning, filling, root canal, ortho, etc.)
- Treatment plan types: the plan templates the clinic uses (single treatment, multi-tooth, full mouth)
- Staff: add the initial team with their role templates
- First week plan: set up first treatment plan template, first patient, first payment flow

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
- t
- r
- e
- a
- t
- m
- e
- n
- t
-  
- p
- l
- a
- n
- /
- i
- n
- s
- t
- a
- l
- l
- m
- e
- n
- t
- /
- t
- o
- o
- t
- h
-  
- c
- h
- a
- r
- t
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

- عيادة الأسنان
- خطط علاجية، تقسيط وخرائط أسنان من لوحة واحدة
- خطة علاجية بتقسيط مراحل
- خرائط أسنان تفاعلية
- تذكيرات المتابعة

Questions the page must answer:

- كيف أنشئ خطة علاجية جديدة؟
- كيف أدفع التقسيط؟

### English

- Dental Clinic Management
- Treatment plans, staged payments and tooth charting from one dashboard
- Staged payment plans with deposit and installments
- Interactive tooth chart per patient
- Follow-up reminders and tracking

Questions the page must answer:

- How do I create a new treatment plan?
- How do I pay an installment?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Appointment calendar: day/week view with patient names, status colours
- Patient record: name, phone, guardian, visit history, consent flag, encrypted health summary
- Treatment plan editor: add plan, select tooth chart, set deposit and total, choose installment count
- Tooth chart: interactive chart with tooth numbers, mark surfaces treated, add notes per tooth
- Installment tracker: list of installments per treatment, amounts due, paid status, receipt print
- Payment screen: accept deposit or installment, record payment, print receipt

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 3 staff
- - Professional: 300 EGP / month, unlimited staff, treatment plans
- - Enterprise: custom for multi-branch dental groups

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Denta | from 350 EGP/mo | no tooth chart or installment tracking | full tooth chart with installment tracking and printable charts |
| OralCare | from 320 EGP/mo | no WhatsApp reminders | WhatsApp deep links for appointment and follow-up reminders |
| Smile | from 330 EGP/mo | no staged payment plans | full staged payment (deposit + installments) per treatment plan |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-dental-clinic-tasks.md`:

1. Add treatment plan editor with tooth chart (M1)
2. Add installment tracker per treatment plan (M1)
3. Add interactive tooth chart (M1)
4. Add payment screen for deposits and installments (M2)
5. Add WhatsApp deep link for appointment reminder (M2)
6. Add treatment plan completion report (M3)
7. Add outstanding installments aging report (M3)
8. Add patient treatment history screen (M3)
9. Add onboarding flow for initial dental setup (M1)
10. Add payment summary report (M2)

## 12. Risks, unknowns and what we refuse to fake

- Patient health data is special-category: mishandling violates PDPL
- Encryption key loss makes patient records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Staged payments can create disputes if installment terms are unclear

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-dental-clinic-tasks.md`
