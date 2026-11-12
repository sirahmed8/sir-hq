# First 10 tasks: SIR Business sector Gym and fitness (جيم ولياقة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/gym-fitness.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Register the gym pack in the sector registry (M1)

**Brief:** Add the manifest for gym-fitness in packages/core/src/sectors/registry.ts with the base template service and the modules (pos, memberships, check in, classes, attendance, coaches, shifts), the feature flags, the role templates and the terminology map.

**Files:** packages/core/src/sectors/gym-fitness/ and packages/core/src/sectors/gym-fitness/__tests__/

**Done when:** getSector('gym-fitness') returns the manifest and the registry test asserts the modules and the flags.

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Write the gym data model with the memberships and the classes (M1)

**Brief:** Type the entities in packages/core/src/sectors/gym/schema.ts: plans, memberships with the start, the expiry and the status, the freeze, the member, the class with the capacity, the class booking with the attendance, the check in and the coach share.

**Files:** packages/core/src/sectors/gym-fitness/ and packages/core/src/sectors/gym-fitness/__tests__/

**Done when:** The schema compiles with no any, the validation rejects a booking over the class capacity, and the tests pass.

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Build the gym seed with the plan templates (M1)

**Brief:** Write packages/core/src/sectors/gym/seed.ts with the Arabic plan templates, the class types and rooms, the role templates, the membership card layout and the empty member list. No price, member or coach is invented.

**Files:** packages/core/src/sectors/gym-fitness/seed.ts and packages/core/src/sectors/gym-fitness/schema.ts

**Done when:** The seed loads, the test asserts the plans and the class types, and it asserts that no member was seeded.

**Check:** `npm test -- sectors` prints passed and the seed count for this sector is asserted

## 4. Write the gym terminology map in Arabic and English (M1)

**Brief:** Create packages/ui/src/sector/gym/glossary.ts with the trade words: عضوية, تجديد, تجميد, حصة, كلاس, تسجيل دخول, مدرّب, and the front desk words, in Arabic and English.

**Files:** packages/ui/src/sector/gym-fitness/

**Done when:** The glossary covers every screen of the sector with no generic shop wording and the label test passes.

**Check:** the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark

## 5. Build the front desk check in screen (M2)

**Brief:** Build the check in: find the member by the phone number or the card, show the membership state in one line (active, frozen, expired), record the visit, and let the desk sell a renewal or a freeze on the spot.

**Files:** apps/web/src/app/(sector)/gym-fitness/

**Done when:** The check in records the visit with the method, an expired membership is refused with a clear message and a renewal action, and the whole flow works on a tablet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 6. Build the class book with the capacity and the attendance (M2)

**Brief:** Build the weekly class book: the classes with the coach, the room, the time and the capacity, the booked names, the wait list when it is full, and the attendance the coach marks.

**Files:** apps/web/src/app/(sector)/gym-fitness/

**Done when:** A booking over the capacity is refused and offered the wait list, the coach marks the attendance, and the fill rate is computed from it.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 7. Build the membership screen with the freeze and the expiry (M2)

**Brief:** Build the membership: the plan, the start, the expiry, the freeze with a reason and a period, the renewal, and the list of the members who lapse in the next fourteen days.

**Files:** apps/web/src/app/(sector)/gym-fitness/

**Done when:** A freeze moves the expiry and keeps the reason, a renewal extends the period, and the lapsing list names each member with the last visit.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 8. Build the coach sheet and the share (M2)

**Brief:** Build the coach view: the classes, the attendance per class and the share of the money, with the period sheet and the payout mark.

**Files:** apps/web/src/app/(sector)/gym-fitness/

**Done when:** The sheet matches a manual calculation in the test, it uses only the classes that really happened, and the payout mark is stored.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 9. Build the gym report pack (M2)

**Brief:** Add the reports of this sector: the active, the new, the lapsed and the frozen, the renewals due, the visits per member, the class fill rate, the coach share, the revenue and the churn by plan, each with the CSV export.

**Files:** apps/web/src/app/(sector)/gym-fitness/

**Done when:** Every report computes its own numbers, the test matches a manual calculation and the export opens in a spreadsheet.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px

## 10. Publish the gym landing page in Arabic and English (M3)

**Brief:** Build the sector page from the outline: the Arabic headline first, the front desk and the class book as the proof blocks with real screenshots, the two questions answered, and the English mirror.

**Files:** apps/web/src/app/(sector)/gym-fitness/

**Done when:** The page passes the layout rules at 320 to 1920 px in both languages and both themes, and every claim matches a screen that exists.

**Check:** `npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px
