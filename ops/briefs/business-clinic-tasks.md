# First 10 tasks: SIR Business sector General clinic (عيادة)

> Written by round r56 (2026-11-12). Read `plans/business-sectors/clinic.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.
> Each task is under a day for one worker. Every task names the files it touches and the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` (private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder screens, no emoji, no em-dash.
## 1. Add appointment calendar screen with conflict detection (M1)

**Brief:** Build the UI for the appointment calendar: day/week view, patient names, status colours, duration slots, no-overlap validation. Done when the calendar prevents double-booking and saves appointments to Firestore.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When appointment creation blocks overlapping times and persists data

**Check:** `npm test -- sectors/{slug}` prints passed

## 2. Add encrypted patient record screen (M1)

**Brief:** Build the patient record screen: name, phone, guardian phone, visit history, consent flag. Done when the data is stored with encryption metadata and is viewable only to role-gated users.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When patient record stores data with encryption and role-based access

**Check:** `npm test -- sectors/{slug}` prints passed

## 3. Add lab order screen with status tracking (M2)

**Brief:** Build the lab order screen: test type, status flow (pending → collected → reported), dates, result entry. Done when the status updates propagate and the audit log records each change.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When lab order status tracking works end-to-end with audit logging

**Check:** `npm test -- sectors/{slug}` prints passed

## 4. Add printable prescription editor (M2)

**Brief:** Build the prescription editor: medicine list, dosage, instructions, doctor signature, printable layout. Done when the prescription prints to ESC/POS thermal printer and renders correctly in the browser.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When prescription prints correctly both thermally and as browser view

**Check:** `npm test -- sectors/{slug}` prints passed

## 5. Add WhatsApp deep link for appointment reminder (M2)

**Brief:** Build the WhatsApp deep link that sends an appointment reminder to the patient. Done when the link opens WhatsApp with pre-filled appointment details (date, time, clinic name).

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When WhatsApp link opens chat with pre-filled appointment info

**Check:** `npm test -- sectors/{slug}` prints passed

## 6. Add visit summary screen with printable PDF (M3)

**Brief:** Build the visit summary recapping symptoms, recommendations, follow-up dates. Done when the summary renders as a PDF that prints correctly from browser and thermal printer.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When visit summary PDF generates and prints correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 7. Add staff shift clock in/out screen (M3)

**Brief:** Build the shift screen: clock in/out, patient load per hour, notes. Done when clock in/out saves timestamps and the shift summary displays correct data.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When shift clock in/out works and summary displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 8. Add appointment no-show report (M4)

**Brief:** Build the report showing appointments by day/hour with no-show counts and rates. Done when the report pulls live data from Firestore and displays correct rates.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When no-show report pulls live data and displays correctly

**Check:** `npm test -- sectors/{slug}` prints passed

## 9. Add patient visit frequency report (M4)

**Brief:** Build the report showing returning vs new patients per month. Done when the report computes and displays the frequency breakdown from Firestore data.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When visit frequency report computes correctly from live data

**Check:** `npm test -- sectors/{slug}` prints passed

## 10. Add onboarding flow for initial clinic setup (M1)

**Brief:** Build the onboarding flow: clinic basics, specialities, staff addition, first appointment type. Done when the flow completes and the clinic appears in the system with all defaults.

**Files:** packages/core/src/sectors/clinic/ and packages/core/src/sectors/clinic/__tests__/

**Done when:** When onboarding flow works end-to-end and clinic is created

**Check:** `npm test -- sectors/{slug}` prints passed
