# First 10 tasks: SIR Business sector School shop (مقصف ومكتبة مدرسة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/school-shop.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add guardian consent flag for student records (M1)

**Brief:** Build the student screen: name, class, guardian phone, consent flag for under-18. Done when the member is saved with consent flag and minimal child data fields.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When student record stores data with guardian consent flag

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add term subscription screen (M1)

**Brief:** Build the subscription screen: select type, set amount and dates, record payment, track status (active/pending/expired). Done when the subscription is saved and the status updates correctly.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When term subscription screen works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add wallet top-up screen with InstaPay (M1)

**Brief:** Build the top-up screen: enter amount, select payment method (cash, card, InstaPay), record top-up, print receipt. Done when the top-up is saved and receipt prints correctly.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When wallet top-up works with InstaPay and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add campus catalog grid with sizes and prices (M1)

**Brief:** Build the product catalogue: grid of campus items with name, price, size options, availability. Done when the catalogue loads and displays items with correct size options and price badges.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When campus catalog displays live data with size options and prices

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add cash register with student name and class print (M2)

**Brief:** Build the cash register: scan SKU, apply discount, tender payment, print receipt with student name and class. Done when the sale records all fields and receipt prints correctly with student info.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When cash register works end-to-end and receipt prints with student name and class

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add term subscription volume report (M2)

**Brief:** Build the report showing active vs pending vs expired subscriptions per period. Done when the report pulls live data and displays correct figures.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When term subscription volume report pulls live data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add wallet top-up frequency report (M3)

**Brief:** Build the report showing top-ups per student per period and total amount collected. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When wallet top-up frequency report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add campus item stock report (M3)

**Brief:** Build the report showing how many uniform/supply items in stock and low-stock alerts. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When campus item stock report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add parent purchase history report (M3)

**Brief:** Build the report showing total spent per student, visit frequency per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When parent purchase history report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial school shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial catalog, term subscription types, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/school-shop/ and packages/core/src/sectors/school-shop/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
