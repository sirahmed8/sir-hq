# First 10 tasks: SIR Business sector Cafe (كافيه)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/cafe.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the cafe pack in the sector registry (M1)

**Brief:** Add the manifest for cafe in packages/core/src/sectors/registry.ts with the base template restaurant, the modules (pos, modifiers, dayparts, prep, stock, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/cafe/ and packages/core/src/sectors/cafe/__tests__/

**Done when:** getSector('cafe') returns the manifest and the registry test asserts the modules and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the cafe data model with modifiers and day parts (M1)

**Brief:** Type the entities in packages/core/src/sectors/cafe/schema.ts: menu items, modifier groups with a required flag and a maximum number of choices, modifiers with a price delta and a stock flag, recipes with the milk and the ice, day parts and the preparation list.

**Files:** packages/core/src/sectors/cafe/ and packages/core/src/sectors/cafe/__tests__/

**Done when:** The schema compiles with no any, the validation rejects a drink without its required modifier, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the cafe seed with the modifier groups (M1)

**Brief:** Write packages/core/src/sectors/cafe/seed.ts with the Arabic menu sections, the modifier groups (size, ice, milk type, extra shot, syrup, no sugar), the day part preset, the receipt layout that prints the modifiers on separate lines, and the role templates.

**Files:** packages/core/src/sectors/cafe/seed.ts and packages/core/src/sectors/cafe/schema.ts

**Done when:** The seed loads, the test asserts the modifier groups, and no drink price is invented.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the cafe terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/cafe/glossary.ts with the cafe words: the drink names, the modifier words, the preparation words, the till words and the receipt words, in Arabic and English.

**Files:** packages/ui/src/sector/cafe/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the quick order grid and the drink builder (M2)

**Brief:** Build the grid of the top items with large touch targets and the drink builder that opens the modifiers of the chosen item, updating the price live and refusing to continue when a required modifier is missing.

**Files:** apps/web/src/app/(sector)/cafe/

**Done when:** A drink is built in three taps, the price always matches the modifiers, and the missing required modifier blocks the cart.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the availability switch and the day parts (M2)

**Brief:** Build the screen where the barista marks a drink as sold out with one tap, which removes it from the grid, the QR menu and the delivery view, and build the day part prices with the sales of each part.

**Files:** apps/web/src/app/(sector)/cafe/

**Done when:** A sold out drink disappears everywhere within the branch, the audit log records who did it, and the day part report shows the sales of each part.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the morning preparation list (M2)

**Brief:** Build the preparation list: what to prepare before opening and what to restock during the day, with the quantity needed, the quantity done and the timestamps, and the waste of what was prepared and not sold.

**Files:** apps/web/src/app/(sector)/cafe/

**Done when:** The list shows the real counts, the waste report values the difference in money, and the list is linked to the real sales of the previous days.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Write the cafe receipt layout and the golden file (M2)

**Brief:** Build the receipt templates for 80 mm and 58 mm with the drink written exactly as it was built, the modifiers on their own lines, the tax line and the QR for the receipt lookup, and store a golden file per width.

**Files:** packages/core/src/sectors/cafe/ and packages/core/src/sectors/cafe/__tests__/

**Done when:** The golden file test passes for both widths, the modifiers never wrap and the tax line equals the cart total.

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Build the cafe report pack (M2)

**Brief:** Add the reports of this sector: sales and cups per hour, margin per drink and per food, the average ticket by day part, the discounts given with the user who gave them, the preparation waste, and the bar stock with the days left, each with the CSV export.

**Files:** apps/web/src/app/(sector)/cafe/

**Done when:** Every report computes its own numbers, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the cafe landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the drink builder and the preparation list as the proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/cafe/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and every claim on it matches a screen that exists.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
