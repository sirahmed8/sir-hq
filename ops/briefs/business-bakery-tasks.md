# First 10 tasks: SIR Business sector Bakery (مخبز وحلواني)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/bakery.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the bakery pack in the sector registry (M1)

**Brief:** Add the manifest for bakery in packages/core/src/sectors/registry.ts with the base template restaurant and the mix of retail modules (pos, weights, production, expiry, purchasing, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/bakery/ and packages/core/src/sectors/bakery/__tests__/

**Done when:** getSector('bakery') returns the manifest and the registry test asserts the modules and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the bakery data model with the production batches (M1)

**Brief:** Type the entities in packages/core/src/sectors/bakery/schema.ts: products with the weighed flag and the shelf life, production batches with the date, the quantity and the cost, daily prices with a reason, the waste log and the sale lines with the weight in grams.

**Files:** packages/core/src/sectors/bakery/ and packages/core/src/sectors/bakery/__tests__/

**Done when:** The schema compiles with no any, the validation rejects a sale of a product without a production batch when the category requires one, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the bakery seed with the Arabic categories and the shelf lives (M1)

**Brief:** Write packages/core/src/sectors/bakery/seed.ts with the Arabic categories, the weight and piece units, the shelf life per category marked as a starting point to confirm, the receipt layout with the weight line and the production date, and the role templates.

**Files:** packages/core/src/sectors/bakery/seed.ts and packages/core/src/sectors/bakery/schema.ts

**Done when:** The seed loads, the test asserts the categories and the shelf lives, and it asserts that no price was invented.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the bakery terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/bakery/glossary.ts with the trade words: عيش, معجنات, دفعة, اليوم التاني, خصم, وزن, and the counter words, in Arabic and English.

**Files:** packages/ui/src/sector/bakery/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the weighed till and the scale driver (M2)

**Brief:** Build the weight based sale: the cashier presses the weight button, the scale value lands in the line in grams, the price per kilogram multiplies it, and the manual entry stays available when the scale does not answer.

**Files:** apps/web/src/app/(sector)/bakery/

**Done when:** A weighed sale stores the grams and the price matches the scale value, the simulated driver test passes, and a manual weight is accepted and marked as manual.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the production plan and the night batches (M2)

**Brief:** Build the screen where the night shift records what it baked: the product, the quantity, the ingredients cost and the expiry, and the comparison with what was sold during the day.

**Files:** apps/web/src/app/(sector)/bakery/

**Done when:** A batch records the production date and the expiry, the plan against the sale comparison matches a manual count in the test, and the batch label prints with the date.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the day old screen with the discount rule (M2)

**Brief:** Build the day old screen: the batches that expire today with the quantity, the rule for the discount day, one tap to apply the discount and one tap to write off with a reason, each written to the audit log.

**Files:** apps/web/src/app/(sector)/bakery/

**Done when:** The batches due today are listed with their quantities, the discount rule applies the right percentage, the write off reduces the stock and both actions are audited.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the raw material stock and the purchasing (M2)

**Brief:** Build the stock of the flour, the sugar, the butter, the fillings and the packaging with the last count and the reorder point, and the order to the supplier with the last price.

**Files:** apps/web/src/app/(sector)/bakery/

**Done when:** The low stock list names the items below their reorder point with the last purchase price, and the order prints with the quantity and the price.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the bakery report pack (M2)

**Brief:** Add the reports of this sector: sales by product and by hour, the day old waste in money, the margin per product after the real batch cost, the production against the plan, the raw material stock and the cash reconciliation, each with the CSV export.

**Files:** apps/web/src/app/(sector)/bakery/

**Done when:** Every report computes its own numbers, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the bakery landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the weighed till and the day old screen as the proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/bakery/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and every claim matches a screen that exists.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
