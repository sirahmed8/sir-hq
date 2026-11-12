# First 10 tasks: SIR Business sector Restaurant (مطعم)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/restaurant.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the restaurant pack in the sector registry (M1)

**Brief:** Add the manifest for restaurant in packages/core/src/sectors/registry.ts with the base template restaurant, the modules (pos, tables, kds, inventory, recipes, orders, shifts, deliveries), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/restaurant/ and packages/core/src/sectors/restaurant/__tests__/

**Done when:** getSector('restaurant') returns the manifest and the registry test asserts the module list and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the restaurant data model with tables, zones and recipes (M1)

**Brief:** Type the entities of this sector in packages/core/src/sectors/restaurant/schema.ts: tables with a position and a state, zones, menu sections and items with variants and allergens, recipes with yield and lines, orders with a service type, kitchen tickets, and the delivery order. Money stays in integer piasters.

**Files:** packages/core/src/sectors/restaurant/ and packages/core/src/sectors/restaurant/__tests__/

**Done when:** The schema compiles with no any, the validation rejects an order without a table for a dine in service, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the restaurant seed with the Arabic menu sections and the floor tables (M1)

**Brief:** Write packages/core/src/sectors/restaurant/seed.ts with the Arabic menu sections, the station list, the table shapes for two, four and six seats, the role templates and the receipt layout with the table and ticket numbers. The menu items, the stock and the recipes stay empty.

**Files:** packages/core/src/sectors/restaurant/seed.ts and packages/core/src/sectors/restaurant/schema.ts

**Done when:** The seed loads, the test asserts the sections and the tables, and it asserts that no dish and no recipe was invented.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the restaurant terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/restaurant/glossary.ts with the words the floor and the kitchen use: ترابيزة, تيكيت, إرسال, مشروب, صنف, تقسيط, and the kitchen stations, in Arabic and English.

**Files:** packages/ui/src/sector/restaurant/

**Done when:** The glossary covers the floor, the kitchen and the receipt with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the interactive floor plan (M2)

**Brief:** Build the floor map with drag to place the tables, the state of each table (free, seated, ordered, ready, bill asked), the minutes since seated and the order total, and the actions to seat, open the order and close the table.

**Files:** apps/web/src/app/(sector)/restaurant/

**Done when:** A table can be moved and the position persists, the state changes with the order, and the screen passes the layout rules at 320 to 1920 px.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the kitchen display and the ticket routing (M2)

**Brief:** Build the kitchen view: tickets by station, the time on each one with the colour bands, the ready and served buttons, and the routing from the order line to the right station. The view must run on a tablet in a bright kitchen with large touch targets.

**Files:** apps/web/src/app/(sector)/restaurant/

**Done when:** An order line lands on the right station, the timer starts when it is fired, and the ready button updates the table state on the floor.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the waiter order flow with modifiers and notes (M2)

**Brief:** Build the waiter flow: open a table, add items with the variants and the note, send to the kitchen in one tap, see the sent state and the running total, and split the bill by guest or by item.

**Files:** apps/web/src/app/(sector)/restaurant/

**Done when:** A waiter can open, order, send and split a table without touching the till, and the split produces separate receipts that add up to the table total.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the food cost and the recipe cost screen (M2)

**Brief:** Build the recipe cost: each dish with its lines, the yield, the cost of one portion from the batch that was used, the waste percentage and the margin against the menu price.

**Files:** apps/web/src/app/(sector)/restaurant/

**Done when:** The cost of a portion equals the sum of its lines divided by the yield, the margin matches a manual calculation in the test, and a dish with a missing cost is flagged instead of counted as zero.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the delivery order screen with the manual link (M2)

**Brief:** Build the delivery screen: orders from each channel with the driver, the promise time, the status buttons and the handover, and a clearly labelled manual entry for a channel whose interface is not confirmed. No fake integration status is ever shown.

**Files:** apps/web/src/app/(sector)/restaurant/

**Done when:** A manually entered delivery order reaches the till and prints, and the screen states which channel is connected and which is manual.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Build the restaurant report pack and the shift summary (M2)

**Brief:** Add the reports of this sector: sales and covers per hour, food cost and margin per dish, kitchen time per station, table turn time, delivery counts and late orders, waste with the reason, and the shift summary with cash variance, each with the CSV export.

**Files:** apps/web/src/app/(sector)/restaurant/

**Done when:** Every report computes its own numbers from the business documents, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
