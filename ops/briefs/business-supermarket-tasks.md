# First 10 tasks: SIR Business sector Supermarket (سوبر ماركت)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/supermarket.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the supermarket pack in the sector registry (M1)

**Brief:** Add the pack manifest for supermarket in packages/core/src/sectors/registry.ts with id, nameAr, nameEn, group, base template market, the modules it turns on, the feature flags, the role templates and the terminology map. The registry lists real module names only, nothing that is not implemented.

**Files:** packages/core/src/sectors/supermarket/ and packages/core/src/sectors/supermarket/__tests__/

**Done when:** The manifest loads, getSector('supermarket') returns it, and a unit test asserts the id, the module list and the role list.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the supermarket data model and its validation (M1)

**Brief:** Type the entities of this sector in packages/core/src/sectors/supermarket/schema.ts with the fields listed in the sector plan, add Zod validation at the boundaries, and add the money fields as integer piasters only.

**Files:** packages/core/src/sectors/supermarket/ and packages/core/src/sectors/supermarket/__tests__/

**Done when:** TypeScript compiles with no any, the validation rejects a sale without a branch, and the schema tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the supermarket catalog seed with units and shelf lives (M1)

**Brief:** Write packages/core/src/sectors/supermarket/seed.ts with the Arabic category tree, the unit set with weight conversions, the per category shelf life, the receipt layout and the empty reorder points. Every seed record carries the seed flag so the app can label it as a starting point.

**Files:** packages/core/src/sectors/supermarket/seed.ts and packages/core/src/sectors/supermarket/schema.ts

**Done when:** The seed loads without a database, the test asserts the category count and that no reorder point was invented.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the supermarket terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/supermarket/glossary.ts with every word the sector needs: the aisle names, the till words, the stock words, the expiry words and the receipt words in Arabic and English. No generic wording is allowed, so a supermarket cashier reads supermarket words.

**Files:** packages/ui/src/sector/supermarket/

**Done when:** The glossary has no entry from the generic retail set, the screen test asserts the label appears in the rendered till, and Arabic and English are both present.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the weigh and label screen for the produce wall (M2)

**Brief:** Add the weighed item flow to the till: the cashier presses the weight button, the scale value lands in the cart line, the label prints with product, weight and price, and the flow works with a simulated scale driver when no hardware is present.

**Files:** apps/web/src/app/(sector)/supermarket/

**Done when:** A sale of a weighed item stores the weight in grams, the printed label matches the cart line, and the simulated driver test passes.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the expiry and shelf screen for the stock controller (M2)

**Brief:** Build the expiry radar for this sector: 7, 30 and 90 day bands, the earliest batch first inside each category, the quantity left, the cost and the shelf, with the discount and the waste actions that write to the audit log.

**Files:** apps/web/src/app/(sector)/supermarket/

**Done when:** The screen lists the batches in the right order, the discount writes an audit entry with the user and the time, and the waste entry reduces the stock.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the goods receipt screen with the difference (M2)

**Brief:** Build the receiving flow: open the purchase order, scan the barcode, count, see the difference between the ordered and the arrived quantity and the money, then close the purchase order and update the batch cost and the expiry.

**Files:** apps/web/src/app/(sector)/supermarket/

**Done when:** A receipt with a missing item shows the difference, closes the order as partial and creates the batch with the real expiry and cost.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Write the supermarket receipt layout and the golden file (M2)

**Brief:** Build the 80 mm and 58 mm receipt templates for this sector with the store header, the weighed line format, the tax line, the loyalty line and the QR for the receipt lookup, and store one golden file per width.

**Files:** packages/core/src/sectors/supermarket/ and packages/core/src/sectors/supermarket/__tests__/

**Done when:** The golden file test passes for both widths, the printed line never wraps, and the tax line equals the cart total.

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Build the supermarket report pack and the dashboard cards (M2)

**Brief:** Add the report pack of this sector: sales by hour, sales by category, expiry loss in pounds, low stock with the reorder suggestion, shrink per item, and the cash reconciliation per shift, with the CSV export for each.

**Files:** apps/web/src/app/(sector)/supermarket/

**Done when:** Each report returns its own data from the business own documents, the numbers match a manual calculation in the test, and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the supermarket landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline in the sector plan: the Arabic first headline, the three benefits, the questions answered, and the proof blocks that are screenshots of the real till, the expiry screen and the goods receipt. English mirrors it.

**Files:** apps/web/src/app/(sector)/supermarket/

**Done when:** The page passes the layout rules at 320, 390, 768, 1280 and 1920 px in both languages and both themes, the copy matches the sector plan, and no price or claim without a source appears on it.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
