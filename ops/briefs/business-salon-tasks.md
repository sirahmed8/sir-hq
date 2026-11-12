# First 10 tasks: SIR Business sector Salon (صالون)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/salon.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the salon pack in the sector registry (M1)

**Brief:** Add the manifest for salon in packages/core/src/sectors/registry.ts with the base template service and the modules (pos, appointments, staff schedule, packages, commissions, retail, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/salon/ and packages/core/src/sectors/salon/__tests__/

**Done when:** getSector('salon') returns the manifest and the registry test asserts the modules and the commission role.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the salon data model with appointments, packages and commissions (M1)

**Brief:** Type the entities in packages/core/src/sectors/salon/schema.ts: stylists with the commission percentage and the working hours, chairs, services with the duration, appointments with the status and the deposit, packages with the sessions used, sales with the commission per line and the commission sheet.

**Files:** packages/core/src/sectors/salon/ and packages/core/src/sectors/salon/__tests__/

**Done when:** The schema compiles with no any, the validation rejects an overlapping booking for the same stylist, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the salon seed with the Arabic service categories (M1)

**Brief:** Write packages/core/src/sectors/salon/seed.ts with the Arabic service categories, the chair labels, the role templates, the receipt layout and the empty duration and commission fields. No price, no client and no stylist is invented.

**Files:** packages/core/src/sectors/salon/seed.ts and packages/core/src/sectors/salon/schema.ts

**Done when:** The seed loads, the test asserts the categories and the chairs, and it asserts that no client or commission was seeded.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the salon terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/salon/glossary.ts with the trade words: موعد, stylist, chair, عمولة, جلسة, باقة, no show, and the reception words, in Arabic and English.

**Files:** packages/ui/src/sector/salon/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the booking book grid (M2)

**Brief:** Build the day book: the stylists as columns, the slots as rows, the booked, the free and the blocked cells, with the client name and phone on the cell, and the drag to move a booking within the stylist working hours.

**Files:** apps/web/src/app/(sector)/salon/

**Done when:** A booking appears in the right column and slot, a double booking for the same stylist is refused, and the layout holds at 320 to 1920 px.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the new booking flow with the deposit and the reminder (M2)

**Brief:** Build the booking: the client, the services, the stylist, the time, the deposit and the price, with the WhatsApp confirmation and the reminder, and the option to block a slot without a name.

**Files:** apps/web/src/app/(sector)/salon/

**Done when:** A booking sends the confirmation and the reminder through the salon account, the deposit is recorded, and the slot appears on the book.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the wait list and the no show flow (M2)

**Brief:** Build the wait list: the clients who want a slot and accept a cancellation, offered in order when a slot frees, plus the no show record with the minutes and the penalty with the manager approval.

**Files:** apps/web/src/app/(sector)/salon/

**Done when:** A freed slot offers the first client on the list, the accepted booking is created, and the no show is recorded with the penalty and the audit entry.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the packages with the expiry and the sessions used (M2)

**Brief:** Build the packages: buying a number of sessions at a price, the sessions used and left per client, the expiry date, and the use of a session at the till reducing the count.

**Files:** apps/web/src/app/(sector)/salon/

**Done when:** Buying a package creates it with the sessions total and the expiry, a sale reduces the sessions used, and an expired package cannot be used and is flagged.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the commission sheet (M2)

**Brief:** Build the commission period: the money per stylist from the services really sold and the retail share, the total and the payout mark, with the CSV export for the payroll.

**Files:** apps/web/src/app/(sector)/salon/

**Done when:** The sheet matches a manual calculation in the test, the payout mark is stored, and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Build the salon report pack and the public booking page (M3)

**Brief:** Add the reports of this sector: booked hours per stylist, the empty slots by hour, the revenue per service and per stylist, the no show rate, the retail sales and the package usage, each with the CSV export, and build the public booking page for the salon with the services, the free slots and the request form.

**Files:** apps/web/src/app/(sector)/salon/

**Done when:** Every report computes its own numbers, a booking request from the public page lands on the book, and the layout rules pass at 320 to 1920 px in both languages.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
