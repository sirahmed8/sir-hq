# SIR Business sector: Repair shop (صيانة أجهزة وموبايلات)

> Round r56 (2026-11-12). Sector 33 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `service + ticket`, group `service-and-ticket`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The repair shop owner manages ticket intake, spare parts and turnaround. Their day is new tickets, parts availability and customer approvals for quotes.

Why this sector is in the catalogue: Repair shops handle ticket-based intake (device, complaint, quote before work, customer approval via SMS/link), spare parts stock and turnaround tracking. The key is the ticket lifecycle and customer approval.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Shop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Ticket (id, shopId, deviceType (phone/appliance), imeiOrSerial, complaint, quotePiasters, status (draft/approved/customer-approved/in-progress/completed), approvedBy, approvedAt, completedAt, notes)
- SparePart (id, shopId, name, model, pricePiasters, costPiasters, taxRate, stockQty, reorderPoint, status, locationShelf)
- Customer (id, shopId, name, phone, optInWhatsApp, purchaseHistoryCount, totalSpentPiasters)
- PartReplacement (id, ticketId, sparePartId, quantity, pricePiasters, installedAt, notes)
- Staff (id, shopId, name, phone, role, hourlyRatePiasters, status)

Units in use: ticket, spare part, replacement

Batches: No : repair shop carries no stock or expiry (spare parts have reorder point not expiry)

Expiry and shelf life: Not applicable. Spare parts have reorder point; tickets have status and dates

Sector specific structures: The core structures are the ticket with its lifecycle (draft→approved→customer-approved→in-progress→completed), the spare part with reorder point and the part replacement record. Customer approval via SMS/link is the key differentiator.

## 3. Screens and workflows that belong to this sector

- Ticket intake screen: enter device type (phone/appliance), imei/serial, complaint, generate quote (quotePiasters), set status (draft). Done when the ticket is saved with draft status and quote amount.
- Customer approval screen: via SMS link or web, view ticket quote, approve/reject, update status to customer-approved. Done when the approval updates the ticket status and saves the approval method.
- Ticket list: all tickets with device type, imei/serial, complaint, quote amount, status, approval status, completed status
- Ticket detail: full info, complaint, quote, approval status, parts needed, completion notes
- Spare part catalogue: grid of spare parts with name, model, price, stock qty, reorder point, reorder badge
- Part replacement screen: select spare part, enter quantity, install, record installedAt, update ticket status to completed
- Cash register: scan ticket reference or device IMEI, record payment, print receipt with ticket details

## 4. Roles and permissions

- Owner: everything : tickets, spare parts, replacements, reports, billing
- Technician: view tickets, mark in-progress/completed, update part replacements, view part stock
- Sales rep: create tickets, generate quotes, handle customer approvals
- Cashier: scan ticket reference, tender payment, print receipt

## 5. Reports and KPIs

- Ticket pipeline: draft/approved/customer-approved/in-progress/completed counts per period, average duration per status
- Spare part stock: total stock, reorder point, items below reorder point, reorder frequency
- Part replacement volume: per ticket how many parts replaced, per period
- Customer repeat rate: visit count per customer, total spent per customer, re-book rate
- Quote conversion rate: how many quotes get customer-approved vs remain draft/approved per period

## 6. Integrations that matter

- SMS gateway for customer quote approval link (optional, provider integration)
- Esc/POS thermal printer for receipts and part replacement records
- WhatsApp deep link for customer quote approval and ready-notice
- Email for completion notice (opt-in)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Shop basics: name, branch, address, phone, currency, working hours
- Initial spare part list: the starting spare parts with name, model, price, stock qty and reorder point
- Ticket types: the device types (phone/appliance) and complaint categories
- Staff: add the initial team with their role templates
- First week plan: create first ticket, add first spare part, first customer approval

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

- صيانة أجهزة وموبايلات
- تذاكر، قطع غيار ومواعيد من لوحة واحدة
- مسار التذاكر من الاستلام حتى التسليم
- مخزون قطع الغيار
- موافقة العميل على القطعة عبر رابط

Questions the page must answer:

- كيف أرفع تذكرة صيانة؟
- هل يمكنني الموافقة على القطعة عبر رابط؟

### English

- Repair Shop Management
- Tickets, spare parts and turnaround from one dashboard
- Ticket lifecycle (draft→approved→customer-approved→in-progress→completed)
- Spare part stock with reorder point
- Customer approval via SMS/link

Questions the page must answer:

- How do I create a new ticket?
- Can I approve the quote via a link?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Ticket intake screen: enter device type (phone/appliance), imei/serial, complaint, generate quote (quotePiasters), set status (draft). Done when the ticket is saved with draft status and quote amount.
- Customer approval screen: via SMS link or web, view ticket quote, approve/reject, update status to customer-approved. Done when the approval updates the ticket status and saves the approval method.
- Ticket list: all tickets with device type, imei/serial, complaint, quote amount, status, approval status, completed status
- Ticket detail: full info, complaint, quote, approval status, parts needed, completion notes
- Spare part catalogue: grid of spare parts with name, model, price, stock qty, reorder point, reorder badge
- Part replacement screen: select spare part, enter quantity, install, record installedAt, update ticket status to completed

## 9. Pricing tier notes

- - Starter: 120 EGP / month, 1 branch, up to 30 tickets
- - Professional: 250 EGP / month, unlimited tickets, spare part module
- - Enterprise: custom for repair shop chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| FixIt | from 300 EGP/mo | no customer approval via link | full customer approval via SMS link or web with status update |
| RepairPro | from 280 EGP/mo | no spare part reorder point | spare part with reorder point and low-stock alert |
| TechCare | from 320 EGP/mo | no ticket pipeline by status | full ticket pipeline by status (draft/approved/customer-approved/in-progress/completed) |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-repair-shop-tasks.md`:

1. Add ticket intake screen with quote generation (M1)
2. Add customer approval via SMS/link (M1)
3. Add ticket list with status filters (M1)
4. Add spare part catalogue with reorder point (M1)
5. Add part replacement screen (M1)
6. Add cash register with ticket scanning (M1)
7. Add ticket pipeline report (M2)
8. Add spare part stock report (M2)
9. Add part replacement volume report (M2)
10. Add customer repeat rate report (M2)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes ticket and spare part records unrecoverable
- WhatsApp template rejection if not approved by Meta
- SMS gateway for quote approval without proper provider integration can fail silently
- Customer approval via link without audit trail can lead to disputes

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-repair-shop-tasks.md`
