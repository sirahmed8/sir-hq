# First 10 tasks: SIR Business sector Butcher and fresh grocery (ملحمة وخضار)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/butcher-fresh-grocery.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the butcher pack in the sector registry (M1)

**Brief:** Add the manifest for butcher-fresh-grocery in packages/core/src/sectors/registry.ts with the base template market and the modules (pos, weights, cuts, batches, expiry, daily price, purchasing, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/butcher-fresh-grocery/ and packages/core/src/sectors/butcher-fresh-grocery/__tests__/

**Done when:** getSector('butcher-fresh-grocery') returns the manifest and the registry test asserts the modules and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the butcher data model with the cuts and the cold chain (M1)

**Brief:** Type the entities in packages/core/src/sectors/butcher/schema.ts: products with the cut reference, cuts with the yield and the price per kilo, batches with the expiry and the temperature at receiving, daily prices with a reason and the sale line with the weight and the cut.

**Files:** packages/core/src/sectors/butcher-fresh-grocery/ and packages/core/src/sectors/butcher-fresh-grocery/__tests__/

**Done when:** The schema compiles with no any, the validation rejects a received batch without a temperature when the category needs the cold chain, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the butcher seed with the Arabic categories (M1)

**Brief:** Write packages/core/src/sectors/butcher/seed.ts with the Arabic categories, the common cuts with an empty yield, the weight units, the receipt layout and the role templates. No price is invented and no customer is seeded.

**Files:** packages/core/src/sectors/butcher-fresh-grocery/seed.ts and packages/core/src/sectors/butcher-fresh-grocery/schema.ts

**Done when:** The seed loads, the test asserts the categories and the units, and it asserts that the yields and the prices are empty.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the butcher terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/butcher/glossary.ts with the trade words: لحمة, قطع, دفعة, وزن, سعر الكيلو, تالف, and the counter words, in Arabic and English.

**Files:** packages/ui/src/sector/butcher-fresh-grocery/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the weighed cut sale with the cut choice (M2)

**Brief:** Build the sale where the cashier chooses the product, the customer chooses the cut, the scale value lands in the line in grams, and the price per kilogram multiplies it, with the manual weight fallback.

**Files:** apps/web/src/app/(sector)/butcher-fresh-grocery/

**Done when:** The sale stores the grams, the cut and the batch, the total matches the scale value, and a manual weight is accepted and marked as manual.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the cold chain receiving screen (M2)

**Brief:** Build the receiving: the delivery, the temperature at arrival typed or read, the expiry of every tray, the difference against the order, and the batch created with the real cost.

**Files:** apps/web/src/app/(sector)/butcher-fresh-grocery/

**Done when:** A batch is created with the temperature, the expiry and the cost, the difference against the order is shown, and a missing temperature is blocked for the cold chain categories.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the expiry radar and the write off with a reason (M2)

**Brief:** Build the expiry screen with the 7, 30 and 90 day bands, the quantity, the cost and the write off with a reason, all audited with the user and the time.

**Files:** apps/web/src/app/(sector)/butcher-fresh-grocery/

**Done when:** The batches appear in the right order, the write off reduces the stock and the reason is stored, and the audit log shows who did it.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the daily price board (M2)

**Brief:** Build the screen where the owner changes the price per kilogram for today with a reason, keeps the history, and prints a board for the shop window and sends it to the regulars on WhatsApp.

**Files:** apps/web/src/app/(sector)/butcher-fresh-grocery/

**Done when:** The price applies to the new sales of today only, the old price stays in the history, and the printed board shows the new price and the date.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the butcher report pack (M2)

**Brief:** Add the reports of this sector: the weight sold per category per day, the expiry loss per batch, the margin per cut after the real cost, the price change history, the cold chain record and the cash reconciliation, each with the CSV export.

**Files:** apps/web/src/app/(sector)/butcher-fresh-grocery/

**Done when:** Every report computes its own numbers, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the butcher landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the weighed sale and the cold chain receiving as the proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/butcher-fresh-grocery/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and every claim matches a screen that exists.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
