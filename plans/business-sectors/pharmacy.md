# SIR Business sector: Pharmacy (صيدلية)

> Round r56 (2026-11-12). Sector 5 of 41 in `plans/business-sectors/_INDEX.md`, wave 1.
> Base template `pharmacy`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The pharmacist of record runs the counter, checks prescriptions, and answers the same questions about the same medicine every day. Their day is pressure from two sides: a queue of people who need the medicine now, and a stock that expires in the back room because nobody could read the batch dates. The one thing that can end a career is a mistake, so they need the expiry and the interaction data to be right and to come from a real source.

Why this sector is in the catalogue: It is the most regulated shop in the catalogue and the one where a wrong number is a patient safety problem, so the pack has to earn trust before it earns money.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Pharmacy (id, name, branchId, address, phone, currency, licenseNumber, pharmacistOfRecord, taxRegistration)
- Pharmacist (id, name, licenseNumber, licenseExpiry, phone)
- Product (id, sku, barcode, nameAr, nameEn, genericName, activeIngredient, form, strength, unit, pricePiasters, taxRate, supplierId, reorderPoint, isControlled, isPrescriptionOnly)
- Batch (id, productId, supplierId, quantity, receivedAt, expiryAt, costPiasters, purchaseOrderId)
- Prescription (id, patientId, doctorName, clinicName, issuedAt, imageUrl, items, notes)
- Patient (id, name, phone, nationalIdLast4, birthYear, chronicConditions, allergies, whatsappOptIn, consentGivenAt)
- Sale (id, branchId, cashierId, patientId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- SaleLine (id, saleId, productId, batchId, quantity, unitPricePiasters, isSubstitution)
- Substitution (id, requestedProductId, offeredProductId, reason, acceptedBy, acceptedAt)
- InteractionAlert (id, patientId, productIds, severity, source, acknowledgedBy, acknowledgedAt, actionTaken)
- ControlledEntry (id, productId, batchId, quantity, reason, patientId, doctorName, loggedBy, createdAt, witnessName)
- Supplier (id, nameAr, phone, paymentTerms, licenseNumber, lastOrderAt)
- PurchaseOrder (id, supplierId, status, lines, expectedAt, totalPiasters)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)
- Employee (id, name, phone, role, licenseNumber, status)

Units in use: tablet, capsule, bottle, tube, box, strip, vial, sachet, millilitre, gram and the pack multiples the wholesalers use

Batches: Every medicine is a batch with a received date, an expiry date and a purchase cost, because the expiry is the life of the shop and the cost per batch is what makes the margin true

Expiry and shelf life: The radar is the main screen of the sector: 7 days critical, 30 days watch, 90 days plan, with the batch, the quantity, the cost and the action (return to the supplier, discount, or keep). No medicine is sold from an expired batch

Sector specific structures: The structures specific to this sector are the patient profile with the chronic conditions and the allergies, the prescription with the doctor and the image, the drug interaction alert that a pharmacist acknowledges, the controlled drug log that is append only, and the substitution offer when a medicine is missing

## 3. Screens and workflows that belong to this sector

- Pharmacy till: scan the barcode, see the batch that will be used, the patient name if the customer is a regular, and the price with the tax
- Expiry radar: the batches that expire first with the quantity, the cost and one tap to return them to the supplier or to discount them
- Prescription intake: photograph or scan the prescription, read the doctor, the date and the items, and turn it into a sale in one flow
- Interaction check: when a medicine is added for a patient with a chronic condition, the alert appears with the source and the pharmacist decides
- Controlled log: an append only list that never deletes a row, with the reason, the patient, the doctor and a second name as witness
- Patient profile: the name, the phone, the conditions and the allergies, encrypted, with the purchase history and the export and delete buttons
- Substitution: when a medicine is out of stock, the in stock generics with the same active ingredient and the same strength, and the price difference
- Stock and suppliers: the items to reorder, the last purchase price and the supplier, and the returns to make
- Shift close: the money, the controlled entries of the day and the sales count

## 4. Roles and permissions

- Owner (pharmacist of record): everything, including the staff, the prices and the reports, and the only role that can change the controlled log settings
- Pharmacist: checks the prescription, acknowledges the interaction alerts, sells, and is the only role allowed to approve a substitution
- Assistant (technician): sells an over the counter medicine, counts the stock, receives deliveries, cannot dispense a prescription only medicine
- Cashier: takes the payment, closes the shift, no medicine advice

## 5. Reports and KPIs

- Expiry loss in money, per batch and per supplier, with what was returned
- Controlled entries for the day and the month, with the counts by substance
- Top medicines by quantity and by margin, with the margin after the real batch cost
- Prescription intake: how many, from which doctors, and the days of the month they arrive
- Substitution rate: how often a missing medicine became a generic
- Stock value at cost and at retail, and the reorder list
- Shift summary with the cash variance and the sales count

## 6. Integrations that matter

- Thermal printer through ESC/POS for the receipt and for the prescription label
- Barcode scanner in keyboard mode, the standard for the medicine boxes
- A real drug data source for the interaction rules: licensed and paid, or the feature stays off with an honest label (the legacy pharmacy shipped eight hand typed rules with no source, and that is banned)
- WhatsApp for the prescription photo and the order confirmation through the pharmacy own account
- ETA e receipt behind the server side signer, off until the specification is read
- A secure store for the patient data with a per tenant key, never in the browser cache

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency
- Licence: the pharmacy licence number and the pharmacist of record with the licence expiry
- Catalog: import the medicines from a spreadsheet with the barcode, the generic name and the supplier
- Batches: the first batches with their expiry dates, so the radar has something to show
- Team: the pharmacist and the assistant with their permissions, and the pharmacist licence numbers
- Suppliers: the main suppliers with their payment terms
- First week plan: sell one item, receive one delivery with batches, print a receipt, acknowledge one alert in the test, set the reorder point
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Form and strength lists in Arabic (tablet, capsule, syrup, cream, injection) with the unit set for each
- Role templates where the pharmacist alone can dispense and acknowledge
- An empty patient list and an empty prescription list, never seeded with fake names
- A receipt layout with the pharmacy header, the tax line and the medicine line with the strength
- A controlled substance list left empty and marked as the pharmacist own list, because the real list is a legal document

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- صيدلية تشوف التالف قبل ما يبقى خسارة، ومعلومات الأدوية من مصدر مرخّص
- تشتغل بالدفعات وتواريخ الصلاحية، وسجل الأدوية المراقَبة يُضاف إليه ولا يُمسح
- شاشة التالف بأيامه الأولى: كل صنف بتاريخه وكميته
- سجل الأدوية المراقَبة يُضاف إليه فقط: كل سطر فيه السبب والشاهد
- بديل متاح لنفس المادة الفعالة لنفس التركيز، بالسعر

Questions the page must answer:

- تفاعلات الأدوية بتجيب منين؟ من مصدر مرخّص، ولو المصدر مش متاح الشاشة بتقول كده بصراحة وما بتخترعش
- بيانات المرضى بتتخزن فين؟ مشفّرة بمفتاح لكل صيدلية، ومش بتيجي في أي تقرير ولا في أي سؤال للذكاء الاصطناعي

### English

- A pharmacy that sees the expiry before it becomes a loss, and drug data from a licensed source
- It runs on batches with their dates, and the controlled log can only be added to, never edited
- The expiry screen shows the batches that go first with the quantity and the cost
- The controlled log is append only: every row has the reason, the patient and a witness
- An in stock generic with the same active ingredient and strength, with the price difference

Questions the page must answer:

- Where does the drug interaction data come from? From a licensed source, and when the source is not available the screen says so plainly instead of inventing an answer
- Where is the patient data stored? Encrypted with a key per pharmacy, and it never enters a report or an AI question

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Pharmacy till: scan the barcode, see the batch that will be used, the patient name if the customer is a regular, and the price with the tax
- Expiry radar: the batches that expire first with the quantity, the cost and one tap to return them to the supplier or to discount them
- Prescription intake: photograph or scan the prescription, read the doctor, the date and the items, and turn it into a sale in one flow
- Interaction check: when a medicine is added for a patient with a chronic condition, the alert appears with the source and the pharmacist decides
- Controlled log: an append only list that never deletes a row, with the reason, the patient, the doctor and a second name as witness
- Patient profile: the name, the phone, the conditions and the allergies, encrypted, with the purchase history and the export and delete buttons

## 9. Pricing tier notes

- The free tier covers the counter of a small pharmacy: one business, one branch, two seats, the till and the batch list
- Starter adds a year of history and the expiry radar as a standing screen
- The Business tier adds the patient profiles, the prescriptions, the substitution and the controlled log, because those are the parts that need more seats and more care
- The licensed drug data source is priced separately and never bundled as if it were free

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | A wide ERP where the pharmacy needs the expiry and the interaction to be exact | The expiry radar, the append only controlled log and the encrypted patient profile as first class features |
| Qoyod (قيود) | Free 14 day trial, published rates not readable; Saudi first, Egypt listed as coming soon (qoyod.com, opened 2026-11-12) | Saudi tax compliance and an accounting first product, with no Egypt pharmacy flow yet | An Egypt first pharmacy with the Egyptian receipt pipeline and the Egyptian pharmacy flow |
| Odoo | One App Free at US$0, Standard US$8.95 per user per month on annual billing (odoo.com/pricing, opened 2026-11-12) | No pharmacy specifics: no batch expiry radar, no controlled log, no patient profile | Those three exist here from the first release, with the pharmacist only role |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-pharmacy-tasks.md`:

1. Register the pharmacy pack in the sector registry (M1)
2. Write the pharmacy data model with batches, patients and prescriptions (M1)
3. Build the pharmacy seed with the forms and the units (M1)
4. Write the pharmacy terminology map in Arabic and English (M1)
5. Build the expiry radar with the batch actions (M2)
6. Build the prescription intake flow (M2)
7. Build the patient profile with encryption and the export and delete (M2)
8. Build the interaction alert flow with a real source (M2)
9. Build the append only controlled log (M2)
10. Build the pharmacy report pack and the substitution screen (M2)

## 12. Risks, unknowns and what we refuse to fake

- The drug interaction and substitution data must come from a licensed source or be clearly marked as unverified: inventing a clinical answer is a patient safety risk and it is banned
- Patient data is special category: encrypted per tenant, never in analytics, never in an AI prompt, exported and deleted on request
- The controlled log is append only, and the pharmacist of record is the only role that can change its settings
- The pharmacy licence and the pharmacist licence numbers are stored as the shop wrote them and are never checked by us with any claim of validation

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-pharmacy-tasks.md`
