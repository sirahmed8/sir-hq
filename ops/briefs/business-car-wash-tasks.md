# First 10 tasks: SIR Business sector Car wash (غسيل سيارات)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/car-wash.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add membership tier manager (M1)

**Brief:** Build the tier screen: add tier, set price, duration, wash count, features, activate/deactivate. Done when the tier is saved and appears in the member check-in screen.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When membership tier manager works and tiers appear in check-in

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add member check-in with queue position (M1)

**Brief:** Build the check-in screen: scan member phone or ticket, view membership status, increment washesThisPeriod, position in queue. Done when check-in saves and queue position updates correctly.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When member check-in works end-to-end with queue position

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add ticket generation (membership/ticket/pay-per-wash) (M1)

**Brief:** Build the ticket screen: create ticket type, record amount, set status (active/used). Done when the ticket is saved and status updates correctly.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When ticket generation works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add queue management (waiting/being-served/done) (M1)

**Brief:** Build the queue screen: view waiting tickets, position, move to being-served, mark done. Done when the queue updates positions and status correctly.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When queue management works end-to-end with position and status updates

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add daily cash reconciliation Z-report (M1)

**Brief:** Build the Z-report screen: opening vs counted, variance, notes, print. Done when the report computes from the day's cash record and prints correctly.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When Z-report works end-to-end and prints correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add membership growth report (M2)

**Brief:** Build the report showing new members per period, renewals, churn. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When membership growth report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add wash frequency per member report (M2)

**Brief:** Build the report showing visits per period per member and average visits per member. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When wash frequency report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add queue efficiency report (M2)

**Brief:** Build the report showing average wait time, tickets per hour, peak hours. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When queue efficiency report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add membership tier performance report (M2)

**Brief:** Build the report showing which tiers sell best, wash count per tier. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When membership tier performance report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial car wash setup (M1)

**Brief:** Build the onboarding flow: wash basics, initial membership tiers, first members, staff addition. Done when the flow completes and the wash appears with all defaults.

**Files:** packages/core/src/sectors/car-wash/ and packages/core/src/sectors/car-wash/__tests__/

**Done when:** When onboarding flow works end-to-end and wash is created

**Check:** `npm test -- sectors/{slug}` prints passed
