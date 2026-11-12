# First 10 tasks: SIR Business sector Training center (مركز تدريبي)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/training-center.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add cohort list and detail screen (M1)

**Brief:** Build the cohort screen: list all cohorts with name, subject, dates, enrolled count, capacity, status. Done when the cohort list loads and the detail screen shows enrolled learners and fee status.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When cohort list and detail screen works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add attendance taking screen (M1)

**Brief:** Build the attendance screen: select cohort, mark present/absent/late for each learner, save attendance for the session. Done when attendance is saved and propagates to learner profile.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When attendance taking works end-to-end and updates learner data

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add learner profile with fee status (M1)

**Brief:** Build the learner profile: total sessions, attended sessions, fee status, outstanding balance, payment history. Done when the profile saves and displays correct data.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When learner profile works and displays live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add fee record screen with due date and payment (M1)

**Brief:** Build the fee record screen: enter amount, due date, mark paid, record receipt, compute outstanding. Done when the fee record saves and the outstanding balance updates correctly.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When fee record screen works end-to-end with balance computation

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add teacher payout computation screen (M2)

**Brief:** Build the payout screen: select cohort, compute commission per teacher based on attended sessions, generate payout doc. Done when the payout computes correctly and the doc is saved to Firestore.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When teacher payout computation works end-to-end and saves doc

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add cohort attendance rate report (M2)

**Brief:** Build the report showing present vs absent vs late per cohort per period. Done when the report computes from Firestore and displays correct rates.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When attendance rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add learner completion rate report (M2)

**Brief:** Build the report showing sessions attended vs total per learner per cohort. Done when the report computes from Firestore and displays correct rates.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When completion rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add fee collection rate report (M3)

**Brief:** Build the report showing collected vs outstanding per period, aging of outstanding. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When fee collection rate report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add teacher payout summary report (M3)

**Brief:** Build the summary showing total payout per teacher per period and commission verification. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When payout summary report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial training center setup (M1)

**Brief:** Build the onboarding flow: center basics, initial cohorts, fee structure, teachers addition. Done when the flow completes and the center appears with all defaults.

**Files:** packages/core/src/sectors/training-center/ and packages/core/src/sectors/training-center/__tests__/

**Done when:** When onboarding flow works end-to-end and center is created

**Check:** `npm test -- sectors/{slug}` prints passed
