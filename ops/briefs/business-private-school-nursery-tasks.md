# First 10 tasks: SIR Business sector Private school and nursery (مدرسة خاصة وحضانة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/private-school-nursery.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add guardian consent flag for student records (M1)

**Brief:** Build the student screen: name, class, guardian name and phone, consent flag for under-18, wallet balance. Done when the student is saved with consent flag and minimal child data fields.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When student record stores data with guardian consent flag

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add term subscription screen (M1)

**Brief:** Build the subscription screen: select student, select type (full/half/quarter), set amount and dates, record payment, track status (active/pending/expired). Done when the subscription is saved and the status updates correctly.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When term subscription screen works end-to-end with status tracking

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add attendance taking screen (M1)

**Brief:** Build the attendance screen: select student, select date, mark present/absent/late, add notes, save attendance. Done when the attendance is saved and propagates to student profile.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When attendance taking works end-to-end and updates student data

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add fee record screen with due date and payment (M1)

**Brief:** Build the fee record screen: enter amount, due date, mark paid, record receipt, compute outstanding. Done when the fee record saves and the outstanding balance updates correctly.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When fee record screen works end-to-end with balance computation

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add fee summary per class report (M2)

**Brief:** Build the report showing total fees collected vs outstanding per class per period. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When fee summary per class report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add attendance rate per period report (M2)

**Brief:** Build the report showing present vs absent vs late per period, per class, overall rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When attendance rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add term subscription volume report (M2)

**Brief:** Build the report showing active vs pending vs expired subscriptions per period, total subscriptions, total amount collected. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When term subscription volume report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add fee collection rate report (M2)

**Brief:** Build the report showing collected vs outstanding per period, aging of outstanding per class. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When fee collection rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add student retention report (M2)

**Brief:** Build the report showing new students per period, re-enrollment rate, withdrawal rate. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When student retention report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial school nursery setup (M1)

**Brief:** Build the onboarding flow: school basics, initial student list, term subscription types, staff addition. Done when the flow completes and the school appears with all defaults.

**Files:** packages/core/src/sectors/private-school-nursery/ and packages/core/src/sectors/private-school-nursery/__tests__/

**Done when:** When onboarding flow works end-to-end and school is created

**Check:** `npm test -- sectors/{slug}` prints passed
