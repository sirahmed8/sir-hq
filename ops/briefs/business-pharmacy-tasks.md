# First 10 tasks: SIR Business sector Pharmacy (صيدلية)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/pharmacy.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the pharmacy pack in the sector registry (M1)

**Brief:** Add the manifest for pharmacy in packages/core/src/sectors/registry.ts with the base template pharmacy, the modules (pos, batches, fefo, patients, prescriptions, controlled log, alerts, suppliers), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/pharmacy/ and packages/core/src/sectors/pharmacy/__tests__/

**Done when:** getSector('pharmacy') returns the manifest and the registry test asserts the modules and the pharmacist role.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the pharmacy data model with batches, patients and prescriptions (M1)

**Brief:** Type the entities in packages/core/src/sectors/pharmacy/schema.ts: products with the active ingredient and the controlled flag, batches with the expiry and the cost, patients with the conditions and the allergies, prescriptions, interaction alerts and the controlled entry. Health fields are marked as encrypted and never enter analytics.

**Files:** packages/core/src/sectors/pharmacy/ and packages/core/src/sectors/pharmacy/__tests__/

**Done when:** The schema compiles with no any, the encrypted fields are marked in the type, and the validation rejects a sale of an expired batch.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the pharmacy seed with the forms and the units (M1)

**Brief:** Write packages/core/src/sectors/pharmacy/seed.ts with the Arabic forms and strengths, the unit set per form, the role templates where only the pharmacist dispenses, and the receipt layout. The patient list, the prescription list and the controlled substance list stay empty and marked as the pharmacist own documents.

**Files:** packages/core/src/sectors/pharmacy/seed.ts and packages/core/src/sectors/pharmacy/schema.ts

**Done when:** The seed loads, the test asserts the forms and units, and it asserts that no patient, prescription or substance was invented.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the pharmacy terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/pharmacy/glossary.ts with the pharmacy words: صيدلي, روشتة, جرعة, تركيز, صنف, منتهي الصلاحية, بديل, and the counter words, in Arabic and English.

**Files:** packages/ui/src/sector/pharmacy/

**Done when:** The glossary covers every screen of the sector with no generic retail wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the expiry radar with the batch actions (M2)

**Brief:** Build the expiry screen: the 7, 30 and 90 day bands, the batch with the quantity, the cost and the supplier, and the actions to return to the supplier or to discount, each written to the audit log with the user and the time.

**Files:** apps/web/src/app/(sector)/pharmacy/

**Done when:** The batches appear in the right order, the return records the batch as returned, the discount writes the audit entry, and an expired batch cannot be sold.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the prescription intake flow (M2)

**Brief:** Build the intake: attach the prescription image, read the doctor, the clinic and the date, turn the items into the cart lines with the strength, and print the label. The image is stored in the secure store, not in the browser cache.

**Files:** apps/web/src/app/(sector)/pharmacy/

**Done when:** A prescription with two items creates a sale with two lines, the label prints with the doctor and the date, and the image is served through a signed URL that expires.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the patient profile with encryption and the export and delete (M2)

**Brief:** Build the encrypted patient profile: the name, the phone, the chronic conditions and the allergies stored with the per tenant key, with the purchase history, and the export and delete actions that remove the record on request.

**Files:** packages/core/src/sectors/pharmacy/ and packages/core/src/sectors/pharmacy/__tests__/

**Done when:** The conditions and the allergies are encrypted at rest, the values never appear in a report or in an AI prompt, and the delete removes the record and the audit trail keeps the fact of the delete without the content.

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Build the interaction alert flow with a real source (M2)

**Brief:** Build the alert flow: when the medicines for a patient are known, the alert service is asked, and the result is shown with its source and its severity, and the pharmacist acknowledges it with the action taken. With no licensed source configured, the screen says that clearly and produces no alert.

**Files:** apps/web/src/app/(sector)/pharmacy/

**Done when:** With a source configured the alert appears with the source and the acknowledgement is stored, and with no source the screen shows the honest state and invents nothing.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the append only controlled log (M2)

**Brief:** Build the controlled substance log: an append only collection where no role can edit or delete a row, with the substance, the batch, the quantity, the reason, the patient, the doctor, the witness and the timestamp, plus the daily count report.

**Files:** packages/core/src/sectors/pharmacy/ and packages/core/src/sectors/pharmacy/__tests__/

**Done when:** An edit or a delete attempt is refused by the rules and by the code, the count report matches the rows, and the audit log records every attempt.

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Build the pharmacy report pack and the substitution screen (M2)

**Brief:** Add the reports of this sector: expiry loss by batch and supplier, the controlled entries by substance and day, the top medicines by quantity and by real margin, the prescriptions by doctor and the substitution rate, each with the CSV export, and build the substitution screen that offers the in stock generics with the same ingredient and strength.

**Files:** apps/web/src/app/(sector)/pharmacy/

**Done when:** The reports compute their own numbers, the test matches a manual calculation, and the substitution list only shows products that are really in stock.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
