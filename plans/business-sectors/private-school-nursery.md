# SIR Business sector: Private school and nursery (مدرسة خاصة وحضانة)

> Round r56 (2026-11-12). Sector 39 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `education`, group `education-and-community`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The school owner manages student attendance, fee collection and term subscriptions. Their day is attendance checks, fee reminders and term deposit tracking.

Why this sector is in the catalogue: Private schools and nurseries need attendance tracking, fee collection, term subscriptions and parent consent for child data (PDPL). The key is the student with guardian consent, term subscriptions and fee tracking.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- School (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours, termStartDate, termEndDate)
- Student (id, schoolId, name, class, guardianName, guardianPhone, guardianConsent, walletPiasters, enrollmentYear, status, notes)
- TermSubscription (id, studentId, type (full/half/quarter), amountPiasters, startDate, endDate, status (active/pending/expired), paidAt)
- Attendance (id, studentId, date, status (present/absent/late), notes)
- FeeRecord (id, studentId, amountPiasters, dueDate, paidAt, status)
- Staff (id, schoolId, name, phone, role, hourlyRatePiasters, status)

Units in use: student, term, attendance, fee

Batches: No : school carries no stock or expiry

Expiry and shelf life: Not applicable. Term subscriptions have start/end dates, attendance is date-based

Sector specific structures: The core structures are the student with guardian consent flag, the term subscription with start/end dates, the attendance tracker per date and the fee record per student. Guardian consent and minimal child data per PDPL is the key differentiator.

## 3. Screens and workflows that belong to this sector

- Student list: all students with name, class, guardian phone, consent flag, wallet balance, active subscriptions
- Student detail: name, class, guardian name and phone, consent flag, wallet balance, active subscriptions, attendance history
- Attendance taking: select student, select date, mark present/absent/late, add notes, save attendance
- Term subscription: select student, select type (full/half/quarter), set amount and dates, record payment, track status (active/pending/expired)
- Fee record: enter amount, due date, mark paid, record receipt, compute outstanding per student
- Fee summary per class: total fees collected vs outstanding per class per period
- Staff shift: clock in/out, student load per hour, notes

## 4. Roles and permissions

- Owner: everything : students, term subscriptions, attendance, fees, reports, billing
- Manager: students, term subscriptions, attendance oversight, fee approval
- Teacher: take attendance per session, view student profiles
- Cashier: record fee payments, print receipts, shift close

## 5. Reports and KPIs

- Attendance rate per period: present vs absent vs late per period, per class, overall rate
- Term subscription volume: active vs pending vs expired per period, total subscriptions, total amount collected
- Fee collection rate: collected vs outstanding per period, aging of outstanding per class
- Student retention: new students per period, re-enrollment rate, withdrawal rate
- Staff attendance: clock in/out hours per staff per period, student load per hour per staff

## 6. Integrations that matter

- WhatsApp deep link for fee reminders and attendance alerts to guardians
- Email for fee invoices and term subscription renewals (opt-in)
- SMS for attendance alerts (optional, guardian phone)
- Paymob or Fawry for fee collection (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- School basics: name, branch, address, phone, currency, working hours, term start/end dates
- Initial student list: the starting student records with name, class, guardian name/phone and consent flag
- Term subscription types: the types (full/half/quarter) and amounts and date ranges
- Staff: add the initial team with their role templates
- First week plan: create first student record, first term subscription, first attendance session

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
- s
- t
- u
- d
- e
- n
- t
- /
- g
- u
- a
- r
- d
- i
- a
- n
-  
- c
- o
- n
- s
- e
- n
- t
- /
- t
- e
- r
- m
-  
- s
- u
- b
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

- مدرسة خاصة وحضانة
- طلاب، اشتراكات واجور من لوحة واحدة
- طلاب مع ضمان ولي الأمر
- اشتراكات بالفصل
- متابعة الأجور

Questions the page must answer:

- كيف أسجل طالبًا جديدًا؟
- كيف أحمل رصيد محفظة الولي؟

### English

- Private School & Nursery Management
- Students, term subscriptions and fee tracking from one dashboard
- Student with guardian consent flag and minimal child data
- Term subscriptions with start/end dates
- Attendance tracker per date

Questions the page must answer:

- How do I register a new student?
- How do I top up the guardian wallet?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Student list: all students with name, class, guardian phone, consent flag, wallet balance, active subscriptions
- Student detail: name, class, guardian name and phone, consent flag, wallet balance, active subscriptions, attendance history
- Attendance taking: select student, select date, mark present/absent/late, add notes, save attendance
- Term subscription: select student, select type (full/half/quarter), set amount and dates, record payment, track status (active/pending/expired)
- Fee record: enter amount, due date, mark paid, record receipt, compute outstanding per student
- Fee summary per class: total fees collected vs outstanding per class per period

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 50 students
- - Professional: 350 EGP / month, unlimited students, reports
- - Enterprise: custom for school chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| SchoolMan | from 400 EGP/mo | no guardian consent flag | parent consent and minimal child data with PDPL deletion on request |
| EduCare | from 380 EGP/mo | no term subscription tracking | full term subscriptions with start/end dates and aging reports |
| BrightStart | from 420 EGP/mo | no attendance rate report | attendance rate per period by class and overall rate |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-private-school-nursery-tasks.md`:

1. Add guardian consent flag for student records (M1)
2. Add term subscription screen (M1)
3. Add attendance taking screen (M1)
4. Add fee record screen with due date and payment (M1)
5. Add fee summary per class report (M2)
6. Add attendance rate per period report (M2)
7. Add term subscription volume report (M2)
8. Add fee collection rate report (M2)
9. Add student retention report (M2)
10. Add onboarding flow for initial school nursery setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Member data with children (under 18) requires parent consent and minimal fields per PDPL
- Encryption key loss makes student records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Term subscriptions without clear start/end dates and outstanding caps can violate consumer protection law

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-private-school-nursery-tasks.md`
