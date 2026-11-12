# First 10 tasks: SIR Business sector Car service and garage (صيانة سيارات)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/car-service-garage.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the garage pack in the sector registry (M1)

**Brief:** Add the manifest for car-service-garage in packages/core/src/sectors/registry.ts with the base template garage and the modules (pos, job cards, estimates, labour, parts, warranties, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/car-service-garage/ and packages/core/src/sectors/car-service-garage/__tests__/

**Done when:** getSector('car-service-garage') returns the manifest and the registry test asserts the modules and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the garage data model with the vehicles and the job cards (M1)

**Brief:** Type the entities in packages/core/src/sectors/garage/schema.ts: vehicles with the plate and the history, the service order with the complaint, the estimate with its approval state, the service lines with the kind (part or labour), the labour time, the checklist and the warranty.

**Files:** packages/core/src/sectors/car-service-garage/ and packages/core/src/sectors/car-service-garage/__tests__/

**Done when:** The schema compiles with no any, the validation refuses a job without a vehicle and an estimate cannot be approved twice, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the garage seed with the Arabic job types (M1)

**Brief:** Write packages/core/src/sectors/garage/seed.ts with the Arabic job types, the part categories, the role templates, the job card layout with the plate and the mileage, and the empty vehicle list. No price, plate or customer is invented.

**Files:** packages/core/src/sectors/car-service-garage/seed.ts and packages/core/src/sectors/car-service-garage/schema.ts

**Done when:** The seed loads, the test asserts the job types, and it asserts that no vehicle was seeded.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the garage terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/garage/glossary.ts with the trade words: كارت صيانة, عرض سعر, قطعة, ميكانيكي, ضمان, صيانة دورية, and the reception words, in Arabic and English.

**Files:** packages/ui/src/sector/car-service-garage/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the job card screen (M2)

**Brief:** Build the job card: the vehicle, the complaint, the inspection checklist, the photos, the estimate total, the state of the work and the promised day, all in one screen that works on a tablet in the bay.

**Files:** apps/web/src/app/(sector)/car-service-garage/

**Done when:** The job card shows the car, the complaint and the checklist, a photo attaches, the state changes are audited, and the layout holds at 320 to 1920 px.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the estimate and the customer approval (M2)

**Brief:** Build the estimate: the parts and the labour lines, the total, the send on WhatsApp through the garage account, the approval or the refusal from the customer, and the extra work that needs a new approval.

**Files:** apps/web/src/app/(sector)/car-service-garage/

**Done when:** The estimate sends with the lines and the total, the approval is recorded with the time and the channel, and a job cannot start over the approved total without a new approval.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the parts stock and the order desk (M2)

**Brief:** Build the parts stock with the barcode, the cost, the price, the reorder point and the movement out with the job, and the order desk that lists the parts to order for the waiting jobs with the supplier and the expected day.

**Files:** apps/web/src/app/(sector)/car-service-garage/

**Done when:** A part used on a job leaves the stock, the low stock list names the items below the reorder point, and the order to the supplier prints with the quantity and the price.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the handover with the warranty and the next service (M2)

**Brief:** Build the handover: the finished work, the before and after photos, the invoice, the warranty with its months and its end date, and the next service date computed from the mileage and the interval.

**Files:** apps/web/src/app/(sector)/car-service-garage/

**Done when:** The handover shows the photos, the invoice and the warranty, and the next service date appears on the vehicle record and in the reminder list.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the garage report pack (M2)

**Brief:** Add the reports of this sector: jobs per bay and per mechanic, the estimate to the approved ratio, the turnaround against the promised day, the fast moving parts, the labour time and the commission, the warranty returns and the cash reconciliation, each with the CSV export.

**Files:** apps/web/src/app/(sector)/car-service-garage/

**Done when:** Every report computes its own numbers, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the garage landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the job card and the estimate approval as the proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/car-service-garage/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and every claim matches a screen that exists.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
