# SIR Business sector: Factory workshop (مصنع وورشة إنتاج)

> Round r56 (2026-11-12). Sector 32 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `production`, group `production`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The workshop owner manages bills of materials, work orders and output. Their day is job orders, material consumption and output verification against spec.

Why this sector is in the catalogue: Small production workshops need bill of materials, work orders and output tracking with scrap. Distinct from retail: bill of materials, output tracking and scrap tracking.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Workshop (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- BillOfMaterials (id, workshopId, productName, productSku, lines with componentName and quantity, totalComponents, status)
- WorkOrder (id, workshopId, billOfMaterialsId, customerName, customerPhone, quantityOrdered, quantityCompleted, status (pending/in-progress/completed), scrappedQty, notes, dueDate)
- Component (id, billOfMaterialsId, name, quantityPerUnit, consumedQty, remainingQty, status)
- OutputRecord (id, workOrderId, actualOutputQty, expectedOutputQty, scrapQty, notes, recordedAt)
- Supplier (id, workshopId, name, phone, paymentTerms, visitDays, leadTimeDays)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Staff (id, workshopId, name, phone, role, hourlyRatePiasters, status)

Units in use: unit, component, work order, output

Batches: No : workshop carries no stock or expiry

Expiry and shelf life: Not applicable. Work orders have due dates, components are consumed per build

Sector specific structures: The core structures are the bill of materials per product, the work order with consumed components and the output record with scrap tracking. Bill of materials is the key differentiator from retail.

## 3. Screens and workflows that belong to this sector

- Bill of materials editor: enter product name/SKU, add component lines (name, quantity per unit), save BOM, set status (active/inactive)
- Work order creation: select BOM, enter customer name and phone, enter quantity ordered, set status (pending/in-progress/completed), set due date, compute total components needed
- Component consumption tracker: per work order, view components, mark consumed, update remaining qty per component
- Output record: enter actual output qty, compare to expected, enter scrap qty, add notes, save
- Work order list: all orders with status, customer, quantity ordered, completed, scrapped, due date
- Component consumption report: per BOM, which components are low or consumed per period
- Output summary: actual vs expected per period, scrap total per period
- Cash register: scan work order reference, record payment, print receipt

## 4. Roles and permissions

- Owner: everything : BOMs, work orders, output, reports, billing
- Master craftsman: create BOMs, update work orders, mark output received
- Workshop assistant: consume components per work order, record output
- Sales rep: create work orders, client quotes, order management

## 5. Reports and KPIs

- Work order pipeline: pending/in-progress/completed per period, average duration, scrapped qty per period
- BOM component consumption: per BOM which components are low or consumed per period, reorder suggestions
- Output summary: actual vs expected per period, scrap total per period and reason
- Revenue per product per period: total completed work orders, revenue per product type per month
- Supplier performance: lead time actual vs expected per supplier per period

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and output records
- WhatsApp deep link for client order status updates and delivery notifications
- Email for order updates and completion notices (opt-in)
- SMS for component low-stock alerts (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Workshop basics: name, branch, address, phone, currency, working hours
- Initial bill of materials: the starting BOM for the workshop's main product with component lines
- Work order types: the work order categories the workshop handles
- Staff: add the initial team with their role templates
- First week plan: create first BOM, first work order, first output record

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
- b
- i
- l
- l
-  
- o
- f
-  
- m
- a
- t
- e
- r
- i
- a
- l
- s
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

- مصنع وورشة إنتاج
- بills of materials، أوامر عمل ومخرجات من لوحة واحدة
- Bills of materials per product
- Work orders with component consumption
- Output record with scrap tracking

Questions the page must answer:

- كيف أنشئ Bill of Materials جديد؟
- كيف أحصي المكونات المستهلكة؟

### English

- Factory Workshop Management
- Bills of materials, work orders and output tracking from one dashboard
- Bill of materials per product
- Work orders with component consumption tracking
- Output record with scrap tracking

Questions the page must answer:

- How do I create a new Bill of Materials?
- How do I track consumed components?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Bill of materials editor: enter product name/SKU, add component lines (name, quantity per unit), save BOM, set status (active/inactive)
- Work order creation: select BOM, enter customer name and phone, enter quantity ordered, set status (pending/in-progress/completed), set due date, compute total components needed
- Component consumption tracker: per work order, view components, mark consumed, update remaining qty per component
- Output record: enter actual output qty, compare to expected, enter scrap qty, add notes, save
- Work order list: all orders with status, customer, quantity ordered, completed, scrapped, due date
- Component consumption report: per BOM, which components are low or consumed per period

## 9. Pricing tier notes

- - Starter: 200 EGP / month, 1 branch, up to 5 BOMs
- - Professional: 450 EGP / month, unlimited BOMs, work order module
- - Enterprise: custom for workshop chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| FactoryPro | from 600 EGP/mo | no bill of materials | full BOM with component lines and quantity per unit |
| WorkshopMart | from 550 EGP/mo | no work order output tracking | full work order from creation to output with scrap tracking |
| BuildCo | from 620 EGP/mo | no supplier performance report | supplier performance with lead time actual vs expected |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-factory-workshop-tasks.md`:

1. Add bill of materials editor (M1)
2. Add work order creation and component consumption (M1)
3. Add component consumption tracker (M1)
4. Add output record screen (M1)
5. Add work order list with status and due date (M1)
6. Add BOM component consumption report (M2)
7. Add output summary report (M2)
8. Add revenue per product report (M2)
9. Add supplier performance report (M2)
10. Add onboarding flow for initial workshop setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes BOM and work order records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Component consumption without tracking can lead to material shortages mid-production
- Scrap tracking without reason can violate consumer protection law on waste reporting

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-factory-workshop-tasks.md`
