# First 10 tasks: SIR Business sector Pet shop (محل حيوانات أليفة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/pet-shop.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add FEFO-tracked pet food catalogue (M1)

**Brief:** Build the product catalogue: grid of pet products with name, type, price, weight (for food), FEFO badge, expiry date badge, stock. Done when the catalogue loads and displays products with FEFO badges and expiry dates correctly.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When product catalogue displays live data with FEFO tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add grooming appointment scheduler (M1)

**Brief:** Build the grooming appointment screen: select service (bath/trim/full groom), date/time, pet name and type, set price, status (booked/in-progress/done). Done when the appointment is saved and status updates propagate.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When grooming appointment scheduler works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add FEFO food radar with expiry alerts (M1)

**Brief:** Build the FEFO radar screen: items expiring in 30/60/90 days, value at risk, one-tap discount tag. Done when the radar pulls live data and the discount tag can be applied.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When FEFO radar works end-to-end with discount tag

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add customer profile with grooming history (M1)

**Brief:** Build the customer profile: name, phone, purchase history, opt-in WhatsApp, grooming history. Done when the profile saves and displays correct data.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When customer profile works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add vet referral hand-off screen (M1)

**Brief:** Build the referral screen: enter issue, referred clinic, referral status (pending/accepted/rejected), date. Done when the referral is saved and status updates propagate.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When vet referral hand-off works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cash register with FEFO discount (M1)

**Brief:** Build the cash register: scan SKU or product, apply FEFO discount if urgent, tender payment, print receipt with FEFO note. Done when the sale applies the discount and receipt prints correctly.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When cash register works end-to-end with FEFO discount and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add grooming appointment pipeline report (M2)

**Brief:** Build the report showing grooming appointments by status (booked/in-progress/done) and average duration per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When grooming pipeline report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add customer retention report (M2)

**Brief:** Build the report showing visit count per customer, total spent per customer, re-book rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When customer retention report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add vet referral status report (M2)

**Brief:** Build the report showing referral status (pending/accepted/rejected) counts per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When vet referral status report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial pet shop setup (M1)

**Brief:** Build the onboarding flow: shop basics, initial product list with FEFO flag, grooming services, staff addition. Done when the flow completes and the shop appears with all defaults.

**Files:** packages/core/src/sectors/pet-shop/ and packages/core/src/sectors/pet-shop/__tests__/

**Done when:** When onboarding flow works end-to-end and shop is created

**Check:** `npm test -- sectors/{slug}` prints passed
