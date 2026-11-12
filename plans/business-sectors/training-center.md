# SIR Business sector: Training center (مركز تدريبي)

> Round r56 (2026-11-12). Sector 40 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `education`, group `education-and-community`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The training centre manager oversees cohorts of adult learners, attendance, fee collection and teacher commissions. Their day is attendance checks, fee reminders and commission calculations per teacher per cohort.

Why this sector is in the catalogue: Training centres (language, technical, academic) need cohort management, attendance tracking, fee collection and teacher payout sharing. Distinct from school: adult learners, no child data, focus on course completion and payouts.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- TrainingCenter (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Cohort (id, centerId, nameAr, nameEn, startDate, endDate, subject, capacity, enrolledCount, status)
- Attendance (id, cohortId, learnerId, date, status (present/absent/late), notes)
- Learner (id, centerId, name, phone, email, totalSessions, attendedSessions, feePiasters, status)
- Teacher (id, centerId, name, phone, commissionRatePiasters, status, assignedCohortId)
- FeeRecord (id, learnerId, amountPiasters, dueDate, paidAt, status)
- Payout (id, teacherId, amountPiasters, cohortId, period, status, paidAt)

Units in use: session, cohort, learner, teacher, payout

Batches: No : training centre carries no stock or expiry

Expiry and shelf life: Not applicable. Sessions and cohorts have date ranges not expiry dates

Sector specific structures: The core structures are the cohort with enrolled learners, the attendance tracker per session, the fee record per learner and the teacher payout per cohort. No child data is collected (adult learners only).

## 3. Screens and workflows that belong to this sector

- Cohort list: all cohorts with name, subject, start/end dates, enrolled count, capacity, status
- Cohort detail: enrolled learners, attendance per session, fee status per learner, assigned teacher
- Attendance taking: select cohort, mark present/absent/late for each learner, save attendance for the session
- Learner profile: total sessions, attended sessions, fee status, outstanding balance, payment history
- Fee record: enter amount, due date, mark paid, record receipt, compute outstanding per learner
- Teacher payout: select cohort, compute commission per teacher based on attended sessions, generate payout doc
- Staff shift: clock in/out, cohort load per hour, notes

## 4. Roles and permissions

- Owner: everything : cohorts, learners, fees, payouts, reports, billing
- Manager: cohorts, learners, fees, payout approval
- Instructor: mark attendance per session, view learner fee status
- Administrator: fee records, payout generation, cohort management

## 5. Reports and KPIs

- Cohort attendance rate: present vs absent vs late per cohort per period
- Learner completion rate: sessions attended vs total per learner per cohort
- Fee collection rate: collected vs outstanding per period, aging of outstanding
- Teacher payout summary: total per teacher per period, commission computation verification
- Revenue per cohort: total fees collected vs total feasible per cohort per period

## 6. Integrations that matter

- WhatsApp deep link for attendance alerts and fee reminders to learners
- Email for fee invoices and payout summaries (opt-in)
- Paymob or Fawry for fee collection (optional)
- CSV import for bulk learner enrollment

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Center basics: name, branch, address, phone, currency, working hours
- Initial cohorts: the subject areas, start/end dates, capacity per cohort
- Fee structure: the fee per session or per cohort, payment terms
- Teachers: add the initial team with their commission rates and assigned cohorts
- First week plan: create first cohort, enroll first learners, first attendance session

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
- c
- o
- h
- o
- r
- t
- /
- l
- e
- a
- r
- n
- e
- r
- /
- f
- e
- e
- /
- p
- a
- y
- o
- u
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

- مركز تدريبي
- قرورات، حضور وأجور من لوحة واحدة
- إدارة القرورات
- تتبع الحضور
- حساب أجور المعلمين

Questions the page must answer:

- كيف أنشئ كورسًا جديدًا؟
- كيف أحصي حضور المتعلمين؟

### English

- Training Center Management
- Cohorts, attendance and teacher payouts from one dashboard
- Cohort management with start/end dates and capacity
- Attendance tracking per session
- Teacher commission payouts per cohort

Questions the page must answer:

- How do I create a new cohort?
- How do I mark learner attendance?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Cohort list: all cohorts with name, subject, start/end dates, enrolled count, capacity, status
- Cohort detail: enrolled learners, attendance per session, fee status per learner, assigned teacher
- Attendance taking: select cohort, mark present/absent/late for each learner, save attendance for the session
- Learner profile: total sessions, attended sessions, fee status, outstanding balance, payment history
- Fee record: enter amount, due date, mark paid, record receipt, compute outstanding per learner
- Teacher payout: select cohort, compute commission per teacher based on attended sessions, generate payout doc

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 3 cohorts
- - Professional: 300 EGP / month, unlimited cohorts, reports
- - Enterprise: custom for training center chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Learnify | from 350 EGP/mo | no attendance tracking per session | full session-level attendance with present/absent/late |
| SkillBuild | from 330 EGP/mo | no fee per-learner tracking | fee records per learner with outstanding balance and payment history |
| TrainCo | from 380 EGP/mo | no teacher payout auto-compute | automatic commission computation per attended session per cohort |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-training-center-tasks.md`:

1. Add cohort list and detail screen (M1)
2. Add attendance taking screen (M1)
3. Add learner profile with fee status (M1)
4. Add fee record screen with due date and payment (M1)
5. Add teacher payout computation screen (M2)
6. Add cohort attendance rate report (M2)
7. Add learner completion rate report (M2)
8. Add fee collection rate report (M3)
9. Add teacher payout summary report (M3)
10. Add onboarding flow for initial training center setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- No child data collected (adult learners only), but encryption still required for all personal data per PDPL
- Encryption key loss makes all records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Fee collection without clear due dates and outstanding caps can violate consumer protection law

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-training-center-tasks.md`
