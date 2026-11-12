# First 10 tasks: SIR Business sector Laundry (مغسلة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/laundry.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the laundry pack in the sector registry (M1)

**Brief:** Add the manifest for laundry in packages/core/src/sectors/registry.ts with the base template service and the modules (pos, tickets, tags, workshop, express tiers, deliveries, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/laundry/ and packages/core/src/sectors/laundry/__tests__/

**Done when:** getSector('laundry') returns the manifest and the registry test asserts the modules and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the laundry data model with the tickets and the tags (M1)

**Brief:** Type the entities in packages/core/src/sectors/laundry/schema.ts: tickets with the promised and the due date, the items with the tag number, the condition and the stains, the tags with the barcode, the services with the price per kilogram or per piece, the express tiers and the lost item record.

**Files:** packages/core/src/sectors/laundry/ and packages/core/src/sectors/laundry/__tests__/

**Done when:** The schema compiles with no any, the tag number is unique inside a ticket, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the laundry seed with the Arabic categories and the services (M1)

**Brief:** Write packages/core/src/sectors/laundry/seed.ts with the Arabic clothing categories, the service templates, the express tier presets, the ticket layout and the tag layout, and the role templates. No price and no customer is invented.

**Files:** packages/core/src/sectors/laundry/seed.ts and packages/core/src/sectors/laundry/schema.ts

**Done when:** The seed loads, the test asserts the categories and the services, and it asserts that no price was seeded.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the laundry terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/laundry/glossary.ts with the trade words: تاج, تذكرة, كيس, بقعة, سريع, كجم, and the counter words, in Arabic and English.

**Files:** packages/ui/src/sector/laundry/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the intake screen with the tags and the photos (M2)

**Brief:** Build the intake: the customer, the bag count, each piece described and tagged with a barcode, the stain photos taken with the phone camera, the weight and the price by the rule, and the ticket that prints with the promised day.

**Files:** apps/web/src/app/(sector)/laundry/

**Done when:** Each piece gets a unique tag, the total matches the weights and the services, the photos attach to the item, and the ticket prints with the promised date.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the workshop board with the states (M2)

**Brief:** Build the board where the workshop moves the tickets between the states (received, washing, ready, delivered), with the late tickets highlighted and the promised date visible.

**Files:** apps/web/src/app/(sector)/laundry/

**Done when:** A ticket moves between the states with the user and the time, a ticket past its promised date is flagged, and the counter sees the same board.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the pickup reminder and the unclaimed list (M2)

**Brief:** Build the ready for pickup screen: the tickets that are ready, the customer phone, one tap to call or to send the WhatsApp message, and the unclaimed list after fourteen days with the value of the pieces.

**Files:** apps/web/src/app/(sector)/laundry/

**Done when:** The message goes out through the shop own account, the sent state is stored, and the unclaimed list shows the value and the days waiting.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the collection and delivery on the bag (M2)

**Brief:** Build the pickup service: the bag collected from the customer, the rider and the time, the ticket created without a counter visit, and the handover back with the same tags.

**Files:** apps/web/src/app/(sector)/laundry/

**Done when:** A collected bag creates a ticket with the tag numbers, the rider sees only his own pickups, and the returned bag matches the tags of the intake.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the laundry report pack (M2)

**Brief:** Add the reports of this sector: tickets received, ready and delivered per day, the revenue per service and per kilogram, the late tickets, the unclaimed pieces with their value, the lost items and the cash reconciliation, each with the CSV export.

**Files:** apps/web/src/app/(sector)/laundry/

**Done when:** Every report computes its own numbers, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the laundry landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the tagged intake and the workshop board as the proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/laundry/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and every claim matches a screen that exists.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
