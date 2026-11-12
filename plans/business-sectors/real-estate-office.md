# SIR Business sector: Real estate office (مكتب عقاري)

> Round r56 (2026-11-12). Sector 38 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `realestate`, group `hospitality-and-real-estate`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The real estate agent manages property listings, leads and contracts. Their day is new listings, lead follow-ups and contract generation with commission calculation.

Why this sector is in the catalogue: Real estate offices need property listings (photos, price, status), lead pipeline, appointment calendar, contracts + commission calc and document vault per deal. The key is the lead pipeline and contract management.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Office (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- PropertyListing (id, officeId, titleAr, titleEn, photos (array), pricePiasters, status (active/pending/sold), areaSqm, locationAr, locationEn, commissionPercent, notes)
- Lead (id, officeId, name, phone, source (web/referral/walk-in), status (new/contacted/qualified/offerSent/closedLost), notes, expectedDealSizePiasters, followUpDate)
- Appointment (id, officeId, leadId, dateTime, duration, type (viewing/consultation), status (scheduled/completed/cancelled), notes)
- Contract (id, listingId, buyerId, sellerId, commissionPiasters, signedDate, expiryDate, status (draft/signed/expired), notes, depositPiasters)
- Client (id, officeId, name, phone, visitCount, totalSpentPiasters, notes, consentPhotos)

Units in use: listing, lead, appointment, contract

Batches: No : real estate office carries no stock or expiry

Expiry and shelf life: Not applicable. Contracts have expiry dates, leads have follow-up dates

Sector specific structures: The core structures are the property listing with photos and commission, the lead pipeline with status flow, the appointment system and the contract with commission and signed date. Lead status flow (new→contacted→qualified→offerSent→closedLost) is the key differentiator.

## 3. Screens and workflows that belong to this sector

- Property list: grid of listings with title, price, status badge, area, location preview, commission %
- Property detail: full info, photos array, price, commission, notes, associated leads and contracts
- Lead pipeline: kanban board with columns new/contacted/qualified/offerSent/closedLost, drag lead between columns, view lead details
- Lead detail: name, phone, source, status, expected deal size, follow-up date, notes, associated listings and contracts
- Appointment scheduler: select lead, date/time, type (viewing/consultation), set status (scheduled/completed/cancelled), add notes
- Contract editor: select listing, enter buyer/seller, commission % and amount, signed date, expiry date, set status (draft/signed/expired), add notes, compute deposit
- Client list: all clients with visit count, total spent, consent photos flag
- Cash register: scan listing reference or lead ID, record payment of commission, print receipt

## 4. Roles and permissions

- Owner: everything : listings, leads, appointments, contracts, reports, billing
- Agent: create listings, manage leads through pipeline, create appointments, create contracts, view commission
- Manager: oversee all agents, approve commissions, view full pipeline
- Cashier: record commission payments, print receipts

## 5. Reports and KPIs

- Lead pipeline: leads per status per period (new/contacted/qualified/offerSent/closedLost), conversion rates per stage
- Property sales: listings created, sold per period, revenue per period, average time to sell
- Commission collected: total commission per period, per agent, collection rate
- Agent productivity: deals closed per agent per period, average deal size, commission per agent
- Client repeat rate: visit count per client, total spent per client, re-book rate for repeat consultations

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and contract copies
- WhatsApp deep link for lead follow-ups and appointment reminders
- Email for property listings and contract delivery (opt-in)
- GIS map integration for property location (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Office basics: name, branch, address, phone, currency, working hours
- Initial property list: the starting property listings with photos, price, area and commission %
- Lead source types: the sources (web/referral/walk-in) and the lead status flow (new→contacted→qualified→offerSent→closedLost)
- Staff: add the initial team with their role templates
- First week plan: create first listing, first lead, first appointment

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
- r
- o
- p
- e
- r
- t
- y
-  
- l
- i
- s
- t
- i
- n
- g
- /
- l
- e
- a
- d
-  
- p
- i
- p
- e
- l
- i
- n
- e
- /
- c
- o
- n
- t
- r
- a
- c
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

- مكتب عقاري
- إدراجات، عملاء محتملين، وحسابات العمولة من لوحة واحدة
- إدارة الإدراجات مع الصور
- مسار العملاء المحتملين مع حالات
- عقود والعمولة التلقائية

Questions the page must answer:

- كيف أضيف إدراج جديد؟
- كيف أسير عميلاً محتملاً عبر المسار؟

### English

- Real Estate Office Management
- Property listings, lead pipeline and commission management from one dashboard
- Property listings with photos and commission
- Lead pipeline with status flow and conversion rates
- Commission management and collection

Questions the page must answer:

- How do I add a new listing?
- How do I move a lead through the pipeline?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Property list: grid of listings with title, price, status badge, area, location preview, commission %
- Property detail: full info, photos array, price, commission, notes, associated leads and contracts
- Lead pipeline: kanban board with columns new/contacted/qualified/offerSent/closedLost, drag lead between columns, view lead details
- Lead detail: name, phone, source, status, expected deal size, follow-up date, notes, associated listings and contracts
- Appointment scheduler: select lead, date/time, type (viewing/consultation), set status (scheduled/completed/cancelled), add notes
- Contract editor: select listing, enter buyer/seller, commission % and amount, signed date, expiry date, set status (draft/signed/expired), add notes, compute deposit

## 9. Pricing tier notes

- - Starter: 200 EGP / month, 1 branch, up to 30 listings
- - Professional: 450 EGP / month, unlimited listings, lead pipeline module
- - Enterprise: custom for real estate chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| EstatePro | from 600 EGP/mo | no lead pipeline status flow | full lead pipeline with status flow (new→contacted→qualified→offerSent→closedLost) and conversion rates |
| PropertyMart | from 550 EGP/mo | no commission auto-compute | commission auto-compute (percent of sale price) per contract |
| RealEstate | from 620 EGP/mo | no agent productivity report | agent productivity: deals closed, average deal size, commission per agent per period |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-real-estate-office-tasks.md`:

1. Add property list grid with status badge (M1)
2. Add lead pipeline kanban board (M1)
3. Add lead detail screen (M1)
4. Add appointment scheduler (M1)
5. Add contract editor with commission compute (M1)
6. Add client list with visit count and total spent (M1)
7. Add cash register with listing/lead scanning (M1)
8. Add lead pipeline report (M1)
9. Add property sales report (M1)
10. Add commission collected report (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes listing and contract records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Commission calculation without clear percent and sale price can violate legal agreements
- Lead data without proper consent can raise privacy concerns per PDPL

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-real-estate-office-tasks.md`
