# SIR Business sector: Optical shop (محل نظارات)

> Round r56 (2026-11-12). Sector 28 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `service + retail`, group `service-and-retail`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The optical shop owner manages a frame inventory, lens types and client prescriptions. Their day is eye tests (recorded), frame selection, lens ordering and fitting notes.

Why this sector is in the catalogue: Optical shops sell glasses with lens types, prescriptions and fitting. Each pair is tracked by prescription and lens specification. The key is lens catalog, prescription linking and fitting notes.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Frame (id, shopId, nameAr, nameEn, brand, pricePiasters, costPiasters, taxRate, size, color, status, locationShelf)
- LensType (id, shopId, nameAr, nameEn, index, coating (antiReflective,UV,photochromic), pricePiasters, costPiasters)
- Prescription (id, clientName, clientPhone, sphere, cylinder, axis, add, pupillaryDistance, notes, validUntil, hasAstigmatism)
- Order (id, shopId, frameId, lensTypeId, clientPrescriptionId, totalPiasters, depositPiasters, balancePiasters, status, readyDate, notes)
- Client (id, shopId, name, phone, visitCount, totalSpentPiasters, lastVisit, notes)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: pair, frame, lens, prescription

Batches: No : optical shop carries no stock or expiry

Expiry and shelf life: Not applicable. Prescriptions have validUntil dates, frames have no expiry

Sector specific structures: The core structures are the frame inventory, lens type catalog, prescription per client and the order with deposit and balance. Prescription validity and lens fitting are the key differentiators.

## 3. Screens and workflows that belong to this sector

- Frame catalogue: grid of frames with name, brand, price, size, color, availability badge
- Frame detail: full info, supplier, reorder point, try-virtual (optional)
- Lens type catalogue: list of lens types with index, coating, price, cost
- Prescription editor: enter sphere, cylinder, axis, add, pupillary distance, validUntil, astigmatism flag, save per client
- Order creation: select frame, select lens type, select prescription, compute total (frame + lenses), set deposit and balance, set status (draft/confirmed/in-progress/ready/ready-for-pickup)
- Client profile: visit count, total spent, last visit, prescription history
- Order status tracker: per order view progress (draft→confirmed→in-progress→ready→ready-for-pickup), print ready notice
- Cash register: scan frame or order reference, record payment, print receipt

## 4. Roles and permissions

- Owner: everything : frames, lenses, prescriptions, orders, reports, billing
- Optician: create prescriptions, select lens types, approve orders, fit frames
- Sales rep: manage frames, create orders, client quotes
- Cashier: scan frames/orders, tender payment, print receipt

## 5. Reports and KPIs

- Frame sales by model and period: count per model/brand per month, revenue per model
- Lens type performance: which lens types sell most, revenue per lens type per period
- Prescription volume per optician: how many prescriptions per optician per period
- Order pipeline: orders by status (draft/confirmed/in-progress/ready/ready-for-pickup) per period
- Client repeat rate: visit count per client, total spent per client, re-book rate

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and order ready notices
- WhatsApp deep link for ready-notice to client and prescription copy (opt-in)
- Email for prescription copy and order updates (opt-in)
- Visual measurement tool integration (optional, hardware)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial frame inventory: the starting list of frames with SKU, brand, price and size
- Lens type scheme: the lens types the shop carries with index, coating and pricing
- Staff: add the initial team with their role templates
- First week plan: receive first frame stock, first lens type, first prescription, first order

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
- f
- r
- a
- m
- e
- /
- l
- e
- n
- s
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

- محل نظارات
- إطارات، تركيبات وأوصاف من لوحة واحدة
- كتالوج إطارات مع المقاسات والألوان
- توليف تركيباتصرية
- تتبع الأوصاف وحالة الطلب

Questions the page must answer:

- هل يمكن تركيب عدسات على إطار имеем؟
- ما أنواع العدسات المتوفرة؟

### English

- Optical Shop Management
- Frames, lens types and prescriptions from one dashboard
- Frame inventory with sizes and colors
- Lens type catalog with index and coating
- Prescription per client with validity tracking

Questions the page must answer:

- Can I fit new lenses into an existing frame?
- What lens types are available?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Frame catalogue: grid of frames with name, brand, price, size, color, availability badge
- Frame detail: full info, supplier, reorder point, try-virtual (optional)
- Lens type catalogue: list of lens types with index, coating, price, cost
- Prescription editor: enter sphere, cylinder, axis, add, pupillary distance, validUntil, astigmatism flag, save per client
- Order creation: select frame, select lens type, select prescription, compute total (frame + lenses), set deposit and balance, set status (draft/confirmed/in-progress/ready/ready-for-pickup)
- Client profile: visit count, total spent, last visit, prescription history

## 9. Pricing tier notes

- - Starter: 150 EGP / month, 1 branch, up to 30 frames
- - Professional: 350 EGP / month, unlimited frames, lens module
- - Enterprise: custom for optical chain networks

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| VisionPro | from 450 EGP/mo | no prescription tracking | full prescription per client with sphere/cylinder/axis/add and validUntil tracking |
| EyeWear | from 430 EGP/mo | no lens type catalog | full lens type catalog with index, coating and pricing |
| OptiCare | from 480 EGP/mo | no order pipeline with status | full order pipeline with status (draft/confirmed/in-progress/ready/ready-for-pickup) |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-optical-shop-tasks.md`:

1. Add frame catalogue with availability badge (M1)
2. Add lens type catalogue (M1)
3. Add prescription editor per client (M1)
4. Add order creation with deposit and balance (M1)
5. Add client profile with prescription history (M1)
6. Add order status tracker with pipeline (M1)
7. Add cash register with frame/Order scanning (M1)
8. Add frame sales by model report (M2)
9. Add lens type performance report (M2)
10. Add prescription volume per optician report (M2)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes frame and prescription records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Prescription validity without clear validUntil can violate consumer protection law
- Fitting claims without proper optician certification can raise liability issues

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-optical-shop-tasks.md`
