# First 10 tasks: SIR Business sector Spa and wellness (سبا وعناية)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/spa-wellness.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add package catalogue with expiry days and features (M1)

**Brief:** Build the package catalogue: list of packages with session count, price, expiry days, features, activate/deactivate. Done when the catalogue loads and displays packages with correct expiry and features.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When package catalogue displays live data with expiry and features

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add client profile with preferences and photo consent (M1)

**Brief:** Build the client profile: name, phone, preferences Ar/En, consent flag for photos, visit count, total spent, last visit. Done when the profile saves and displays correct data.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When client profile works and displays live data with consent flag

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add room scheduler with available slots per time (M1)

**Brief:** Build the room scheduler: available rooms per time slot, book room, assign client, mark status. Done when the scheduler saves the booking and displays availability correctly.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When room scheduler works end-to-end with availability display

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add package redemption screen (M1)

**Brief:** Build the redemption screen: select package, view sessions used/remaining, expiry date, update status (active/used/expired). Done when the redemption saves and the status updates correctly.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When package redemption works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add appointment scheduler with room and client (M1)

**Brief:** Build the appointment screen: select room, date/time, service type, client, status (scheduled/in-progress/completed). Done when the appointment saves and the room status updates correctly.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When appointment scheduler works end-to-end with room status update

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add redemption history per client (M2)

**Brief:** Build the history screen: all redemptions per client, sessions used, remaining, expiry events. Done when the history pulls and displays client's full redemption trail.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When redemption history works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add package expiry rate report (M2)

**Brief:** Build the report showing how many packages expired per period and how many sessions lost. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When package expiry rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add room utilisation report (M2)

**Brief:** Build the report showing booked hours vs available per period, peak times. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When room utilisation report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add therapist workload report (M2)

**Brief:** Build the report showing appointments per period, utilisation rate per therapist. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When therapist workload report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial spa wellness setup (M1)

**Brief:** Build the onboarding flow: spa basics, initial packages, client intake fields, staff addition. Done when the flow completes and the spa appears with all defaults.

**Files:** packages/core/src/sectors/spa-wellness/ and packages/core/src/sectors/spa-wellness/__tests__/

**Done when:** When onboarding flow works end-to-end and spa is created

**Check:** `npm test -- sectors/{slug}` prints passed
