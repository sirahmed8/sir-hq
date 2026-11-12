# SIR Business sector: Print shop (مطبعة)

> Round r56 (2026-11-12). Sector 31 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `production`, group `production`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The print shop manager handles job tickets, paper stock and client proofs. Their day is job intake, paper tracking and proof approval.

Why this sector is in the catalogue: Print shops handle job tickets, paper stock and unit pricing (per page, per poster, per banner). The key is job tracking, paper inventory and proofing.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- JobTicket (id, shopId, clientName, clientPhone, jobType (poster/banner/flyer/invitation), dimensions (w,h), unitPricePiasters, copies, totalPiasters, depositPiasters, balancePiasters, status (pending/proofing/printing/done), notes, readyDate)
- PaperStock (id, shopId, name, sizeAr, sizeEn, weightPiasters per sheet, sheetQty, minThreshold, status, locationShelf)
- Proof (id, jobTicketId, clientName, clientProofPDFUrl, status (pending/approved/rejected), approvedBy, approvedAt, notes)
- Supplier (id, nameAr, phone, paymentTerms, visitDays, leadTimeDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: job, sheet, copy, banner

Batches: No : print shop carries no stock or expiry

Expiry and shelf life: Not applicable. Job tickets have status and ready date, paper has threshold not expiry

Sector specific structures: The core structures are the job ticket with its lifecycle (pending→proofing→printing→done), the paper stock with threshold tracking and the proof approval loop. Unit pricing per page/poster/banner is the key differentiator.

## 3. Screens and workflows that belong to this sector

- Job ticket list: all tickets with type, client, dimensions, copies, total, deposit, balance, status, ready date
- Job ticket detail: full info, dimensions, proof status, paper requirements, notes, ready date
- Paper stock level: sheets in stock, minimum threshold, low-stock alert, reorder suggestion
- Proof manager: upload client proof PDF, status (pending/approved/rejected), approve/reject, add notes
- Proof gallery: view all proofs per job, approve/reject per proof
- Purchase order: receive from supplier, update paper stock, record cost
- Cash register: scan job ticket reference, record payment, print receipt with job details
- Staff shift: clock in/out, job load per hour, notes

## 4. Roles and permissions

- Owner: everything : job tickets, paper stock, proofs, reports, billing
- Print operator: create job tickets, upload proofs, mark status (pending/proofing/printing/done)
- Proof approver: review client proofs, approve/reject, add notes
- Stock clerk: receive paper shipments, update stock levels, reorder

## 5. Reports and KPIs

- Job ticket volume per period: tickets created, proofing, printing, done per month
- Proof approval rate: approved vs rejected per period, reasons for rejection
- Paper stock turnover: sheets per period, low-stock alerts per period, reorder frequency
- Revenue per job type: posters vs banners vs flyers vs invitations, revenue per type per period
- Job turnaround time: from creation to done, average days per job type

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and proofs
- WhatsApp deep link for client proof approval and ready-notice
- Email for proof delivery and updates (opt-in)
- File storage for proof PDFs (Firebase Cloud Storage)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial job types: the starting job types (poster/banner/flyer/invitation) with unit pricing per page/poster/banner
- Paper stock: the initial paper list with size, weight and minimum threshold
- Staff: add the initial team with their role templates
- First week plan: create first job ticket, receive first paper shipment, first proof upload

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
- j
- o
- b
-  
- t
- i
- c
- k
- e
- t
-  
- l
- i
- f
- e
- c
- y
- c
- l
- e
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

- مطبعة
- وظائف، أوراق ومواصفات من لوحة واحدة
- تعقّب الوظائف من الاستلام حتى التسليم
- متابعة مخزون الورق
- معاودات الموافقات (proofs)

Questions the page must answer:

- كيف أنشئ وظيفة طباعة جديدة؟
- ما هي أنواع الوظائف المتوفرة؟

### English

- Print Shop Management
- Job tickets, paper stock and proofing from one dashboard
- Job ticket lifecycle (pending→proofing→printing→done)
- Paper stock with threshold tracking
- Proof approval loop

Questions the page must answer:

- How do I create a new print job?
- What job types are available?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Job ticket list: all tickets with type, client, dimensions, copies, total, deposit, balance, status, ready date
- Job ticket detail: full info, dimensions, proof status, paper requirements, notes, ready date
- Paper stock level: sheets in stock, minimum threshold, low-stock alert, reorder suggestion
- Proof manager: upload client proof PDF, status (pending/approved/rejected), approve/reject, add notes
- Proof gallery: view all proofs per job, approve/reject per proof
- Purchase order: receive from supplier, update paper stock, record cost

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 20 job types
- - Professional: 350 EGP / month, unlimited job types, paper module
- - Enterprise: custom for print shop chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| PrintPro | from 500 EGP/mo | no job ticket lifecycle | full job ticket from creation to done with status tracking |
| PrintMart | from 480 EGP/mo | no proof approval loop | full proof manager with upload, approve/reject and notes |
| CopyHouse | from 520 EGP/mo | no paper stock threshold tracking | paper stock with minimum threshold and low-stock alerts |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-print-shop-tasks.md`:

1. Add job ticket list and detail screen (M1)
2. Add paper stock level screen (M1)
3. Add proof manager with upload and status (M1)
4. Add proof gallery per job (M1)
5. Add purchase order and paper stock update (M1)
6. Add cash register with job ticket scanning (M1)
7. Add job ticket volume per period report (M2)
8. Add proof approval rate report (M2)
9. Add paper stock turnover report (M2)
10. Add revenue per job type report (M2)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes job ticket and paper records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Proof approval without clear criteria can lead to client disputes
- Paper threshold without regular reorder can halt production

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-print-shop-tasks.md`
