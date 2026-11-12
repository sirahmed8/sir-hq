# First 10 tasks: SIR Business sector Dental clinic (عيادة أسنان)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/dental-clinic.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add treatment plan editor with tooth chart (M1)

**Brief:** Build the UI for creating a treatment plan: select tooth chart, set deposit and total price, choose installment count. Done when the plan saves to Firestore and the tooth chart is selectable.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When treatment plan editor works and saves plan with tooth chart

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add installment tracker per treatment plan (M1)

**Brief:** Build the installment screen: list of installments, amounts due, paid status, receipt print. Done when each installment is recorded and the total matches the plan.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When installment tracker records payments and computes outstanding correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add interactive tooth chart (M1)

**Brief:** Build the tooth chart UI: tooth numbers, mark surfaces treated, add notes per tooth. Done when the chart saves and displays correctly per patient.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When tooth chart saves patient data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add payment screen for deposits and installments (M2)

**Brief:** Build the payment screen: accept deposit or installment payment, record payment, print receipt. Done when payment saves to the installment doc and receipt prints correctly.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When payment screen works end-to-end and receipt prints

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add WhatsApp deep link for appointment reminder (M2)

**Brief:** Build the WhatsApp deep link that sends an appointment reminder to the patient. Done when the link opens WhatsApp with pre-filled appointment details.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When WhatsApp link opens chat with pre-filled appointment info

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add treatment plan completion report (M3)

**Brief:** Build the report showing treatment plans by completion status. Done when the report pulls live data and displays completion rates per dentist.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When treatment completion report pulls live data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add outstanding installments aging report (M3)

**Brief:** Build the aging report: installments by due date, how many overdue, total outstanding. Done when the report computes from Firestore and displays correct aging buckets.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When aging report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add patient treatment history screen (M3)

**Brief:** Build the screen showing all treatment plans per patient, their status and completion. Done when the screen pulls and displays patient's full treatment history.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When patient treatment history screen works and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add onboarding flow for initial dental setup (M1)

**Brief:** Build the onboarding flow: clinic basics, dental specialities, treatment plan templates, staff addition. Done when the flow completes and the clinic appears with all defaults.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When onboarding flow works end-to-end and clinic is created

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add payment summary report (M2)

**Brief:** Build the report showing total payments collected per period, per dentist, outstanding per patient. Done when the report computes from Firestore and displays correct figures.

**Files:** packages/core/src/sectors/dental-clinic/ and packages/core/src/sectors/dental-clinic/__tests__/

**Done when:** When payment summary report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed
