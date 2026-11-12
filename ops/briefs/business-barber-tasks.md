# First 10 tasks: SIR Business sector Barber (حلاقة رجالي)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/barber.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the barber pack in the sector registry (M1)

**Brief:** Add the manifest for barber in packages/core/src/sectors/registry.ts with the base template service and the modules (pos, queue, tickets, staff, retail, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/barber/ and packages/core/src/sectors/barber/__tests__/

**Done when:** getSector('barber') returns the manifest and the registry test asserts the modules and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the barber data model with the queue and the tickets (M1)

**Brief:** Type the entities in packages/core/src/sectors/barber/schema.ts: barbers with the commission, chairs, services with the duration, the walk in with the arrival and the call, the ticket with the number and the states, and the sale that closes a served ticket.

**Files:** packages/core/src/sectors/barber/ and packages/core/src/sectors/barber/__tests__/

**Done when:** The schema compiles with no any, the ticket number is unique per branch and per day, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the barber seed with the Arabic service categories (M1)

**Brief:** Write packages/core/src/sectors/barber/seed.ts with the Arabic service categories, the chair labels, the ticket display layout, the role templates and the receipt layout. No price and no client is invented.

**Files:** packages/core/src/sectors/barber/seed.ts and packages/core/src/sectors/barber/schema.ts

**Done when:** The seed loads, the test asserts the categories, and it asserts that no client, price or commission was seeded.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the barber terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/barber/glossary.ts with the trade words: تذكرة, رقم, طابور, قص, حلاقة, عمولة, and the counter words, in Arabic and English.

**Files:** packages/ui/src/sector/barber/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the queue screen with the call button (M2)

**Brief:** Build the queue: the waiting clients with their name, their arrival time and the waiting minutes, the call button that moves the person to the chair, and the ticket number that the display shows.

**Files:** apps/web/src/app/(sector)/barber/

**Done when:** A walk in appears in the queue with the waiting time, the call moves him to the chair, and the number on the display matches the ticket.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the ticket display for the wall (M2)

**Brief:** Build the full screen ticket display for the tablet on the wall: the current number in a large type, the last called numbers, the shop name and the time, with a quiet mode that dims the screen after a minute.

**Files:** apps/web/src/app/(sector)/barber/

**Done when:** The display shows the called number in a readable size at 1920 px, it updates when a client is called, and the quiet mode dims it without hiding it.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the fast sell with the service and the payment (M2)

**Brief:** Build the fast sell: the service, the barber, the price and the payment in two taps, the receipt that names the service and the wait, and the client link when the phone number is given.

**Files:** apps/web/src/app/(sector)/barber/

**Done when:** A sale closes the served ticket, the total matches the price and the wait time, and the receipt prints with the service and the barber.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the retail shelf with the opening date (M2)

**Brief:** Build the small retail shelf of this sector: the products, the price, the quantity and the opening date, with the days left, and the sale of a product next to the cut.

**Files:** apps/web/src/app/(sector)/barber/

**Done when:** The shelf lists the days left for every opened product, the sale reduces the quantity, and the stock never goes below zero without an audit entry.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the barber report pack (M2)

**Brief:** Add the reports of this sector: clients served per barber with the average wait, the revenue per service and per barber with the commission, the empty slots by hour, the walk in share and the cash reconciliation, each with the CSV export.

**Files:** apps/web/src/app/(sector)/barber/

**Done when:** Every report computes its own numbers, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the barber landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the queue and the ticket display as the proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/barber/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and every claim matches a screen that exists.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
