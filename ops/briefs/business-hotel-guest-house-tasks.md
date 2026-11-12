# First 10 tasks: SIR Business sector Hotel and guest house (فندق وغرفة مفروشة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/hotel-guest-house.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add room calendar with housekeeping status (M1)

**Brief:** Build the room calendar: month view with room labels, status colours, housekeeping status badge, reservation overlay. Done when the calendar loads and displays rooms with correct status and housekeeping badges.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When room calendar works and displays status and housekeeping badges correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add reservation creation with deposit and city tax (M1)

**Brief:** Build the reservation screen: select room, client name/phone, check-in/out dates, deposit % and amount, total (nightCount × price), status, city tax status. Done when the reservation saves all fields and city tax computes correctly.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When reservation creation works end-to-end with city tax computation

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add housekeeping board with task assignment (M1)

**Brief:** Build the housekeeping board: list of rooms with task (checkout/clean/inspect), assigned to, completed at, notes. Done when the board loads and task assignment works correctly.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When housekeeping board works and task assignment saves correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add invoice editor with city tax auto-compute (M1)

**Brief:** Build the invoice screen: select reservation, compute subtotal (nightCount × price), city tax (percent of subtotal), total, set status, issue, add notes. Done when the invoice saves and city tax auto-computes correctly.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When invoice editor works and city tax auto-computes correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add occupancy rate report (M1)

**Brief:** Build the report showing occupied rooms vs available rooms per day/week/month and occupancy %. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When occupancy rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add revenue per period report (M1)

**Brief:** Build the report showing total night revenue, total city tax collected, total revenue (nights + tax) per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When revenue per period report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add average daily rate (ADR) report (M1)

**Brief:** Build the report showing ADR: total night revenue / occupied rooms per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When ADR report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add housekeeping efficiency report (M1)

**Brief:** Build the report showing rooms cleaned per day, average time in status, tasks completed per staff. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When housekeeping efficiency report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add reservation status report (M1)

**Brief:** Build the report showing confirmed vs cancelled vs noShow counts per period and city tax collected vs pending. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When reservation status report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial hotel setup (M1)

**Brief:** Build the onboarding flow: hotel basics, initial room types, housekeeping tasks, staff addition. Done when the flow completes and the hotel appears with all defaults.

**Files:** packages/core/src/sectors/hotel-guest-house/ and packages/core/src/sectors/hotel-guest-house/__tests__/

**Done when:** When onboarding flow works end-to-end and hotel is created

**Check:** `npm test -- sectors/{slug}` prints passed
