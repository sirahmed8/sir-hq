# SIR Business sector: Library (مكتبة)

> Round r56 (2026-11-12). Sector 22 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `library`, group `education-and-community`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The library manager oversees book circulation, membership fees, study-desker bookings and overdue fines. Their day is member check-in, book returns and fine collection.

Why this sector is in the catalogue: Egyptian public and private libraries need circulation tracking, deposit management, study-desker booking and a public OPAC page. Lending deposits and child-data privacy rules apply.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Library (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Member (id, libraryId, name, phone, encryptedChildData, parentConsent, class, membershipType, joinDate, expiryDate, depositsPiasters)
- Book (id, libraryId, isbn, titleAr, titleEn, authorAr, authorEn, category, unitPricePiasters, costPiasters, status, locationShelf)
- Borrowing (id, memberId, bookId, borrowedAt, dueDate, returnedAt, finePiasters, status)
- StudyDesk (id, libraryId, label, capacity, status, bookedBy, bookedAt, expiresAt)
- Staff (id, libraryId, name, phone, role, hourlyRatePiasters, status)

Units in use: book, member, desk, borrowing

Batches: No : library carries no stock or expiry

Expiry and shelf life: Not applicable. Borrowing is time-based not product-based

Sector specific structures: The core structures are the membership with deposits, the borrowing lifecycle, the study-desk booking and the child-data privacy flag. Member data with children (under 18) requires parent consent and minimal fields.

## 3. Screens and workflows that belong to this sector

- OPAC public page: search books by ISBN, title or author, view availability
- Member check-in: scan member card, view active borrowings, due dates
- Book checkout: scan book barcode, decrement stock, record borrowing with due date
- Study desk booking: available desks, book slot, confirm booking, cancel booking
- Return book: scan borrowing record, mark returned, compute fine if overdue
- Fine management: unpaid fines per member, receipt print, write-off reason
- Staff shift: clock in/out, member load per hour, notes

## 4. Roles and permissions

- Owner: everything : book inventory, membership, reports, billing
- Librarian: member check-in/out, book check-in/out, fine assessment
- Assistant: member registration, study desk booking, fine collection
- Cashier: fine receipts, shift close

## 5. Reports and KPIs

- Active borrowings per day: how many books out, by category
- Overdue fines revenue: total unpaid, collected, written off per period
- Study desk utilisation: booked hours vs available per day
- Member retention: new members, renewals, lapsed members per month
- Book circulation by category: which genres are most borrowed

## 6. Integrations that matter

- Barcode scanner for book and member check-in
- Esc/POS thermal printer for fine receipts and overdue notices
- WhatsApp deep link for overdue notices and membership renewals
- Email for membership renewal notices (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Library basics: name, branch, address, phone, currency, working hours
- Collection: the initial book inventory with ISBN, titles and categories
- Membership types: the categories (student, adult, child, family) and deposit amounts
- Study desks: the desks available and their capacity
- First week plan: register first member, check out first book, book first desk

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
- m
- e
- m
- b
- e
- r
- s
- h
- i
- p
- /
- b
- o
- r
- r
- o
- w
- i
- n
- g
- /
- d
- e
- s
- k
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

- المكتبة
- حصر، إرجاع ودور من لوحة واحدة
- حجز مقاعد للدراسة
- تعقّب الاستعارات
- إدارة الغرامات

Questions the page must answer:

- كيف أصبح عضواً في المكتبة؟
- ما غرامة التأخر في الإرجاع؟

### English

- Library Management
- Circulation, deposits and study-desk booking from one dashboard
- Membership with deposit tracking
- Borrowing lifecycle with due dates
- Study-desk booking and utilisation

Questions the page must answer:

- How do I become a library member?
- What is the late-return fine?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- OPAC public page: search books by ISBN, title or author, view availability
- Member check-in: scan member card, view active borrowings, due dates
- Book checkout: scan book barcode, decrement stock, record borrowing with due date
- Study desk booking: available desks, book slot, confirm booking, cancel booking
- Return book: scan borrowing record, mark returned, compute fine if overdue
- Fine management: unpaid fines per member, receipt print, write-off reason

## 9. Pricing tier notes

- - Starter: 80 EGP / month, 1 branch, up to 20 members
- - Professional: 180 EGP / month, unlimited members, reports
- - Enterprise: custom for multi-branch library networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Kitab | from 200 EGP/mo | no child-data consent flag | parent consent and minimal child fields with deletion on request |
| Maktaba | from 180 EGP/mo | no study-desk booking | full study-desk booking with utilisation reports |
| Dar | from 220 EGP/mo | no OPAC public page | online OPAC search by ISBN, title, author |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-library-tasks.md`:

1. Add OPAC public search page (M1)
2. Add member check-in with scan (M1)
3. Add book checkout and check-in screen (M1)
4. Add study desk booking screen (M2)
5. Add fine management screen (M2)
6. Add member registration with parent consent for children (M2)
7. Add overdue fines revenue report (M3)
8. Add study desk utilisation report (M3)
9. Add book circulation by category report (M4)
10. Add onboarding flow for initial library setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Member data with children (under 18) requires parent consent and minimal fields per PDPL
- Encryption key loss makes member records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Overdue fines that accumulate without a cap can violate consumer protection law

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-library-tasks.md`
