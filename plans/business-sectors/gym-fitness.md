# SIR Business sector: Gym and fitness (جيم ولياقة)

> Round r56 (2026-11-12). Sector 10 of 41 in `plans/business-sectors/_INDEX.md`, wave 2.
> Base template `service`, group `health-and-beauty`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The owner runs a hall with a floor, a class room and a coach on shift. The business is renewals: a member who came three times in the month and will not come back, a membership that was frozen in July and forgot to restart, and a coach who counts the class attendance by hand. The pain is the member list in a notebook and the argument about a month that was paid but not used.

Why this sector is in the catalogue: It sells months at a time: the membership, the class seat and the coach share, and the owner lives from renewals that nobody tracks.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Gym (id, name, branchId, address, phone, currency, openingHours, taxRegistration)
- Plan (id, nameAr, nameEn, periodDays, pricePiasters, sessionsIncluded, classAccess, isActive)
- Membership (id, memberId, planId, startsAt, expiresAt, status, freezeUntil, notes)
- Member (id, name, phone, whatsappOptIn, birthYear, emergencyContact, consentGivenAt, createdAt)
- Freeze (id, membershipId, fromDate, toDate, reason, loggedBy)
- Class (id, branchId, titleAr, coachId, roomId, startsAt, endsAt, capacity, bookedCount)
- ClassBooking (id, classId, memberId, bookedAt, attended, checkedInAt)
- CheckIn (id, memberId, membershipId, at, method)
- Coach (id, name, phone, role, commissionPercent, hourlyRatePiasters, status)
- BodyMetric (id, memberId, recordedAt, weightKg, heightCm, bodyFatPercent, note)
- Sale (id, branchId, memberId, lines, totalsPiasters, payments, createdAt, idempotencyKey)
- SaleLine (id, saleId, planId, quantity, unitPricePiasters, coachId)
- Shift (id, branchId, openedBy, openedAt, closedAt, floatPiasters, countedPiasters)

Units in use: month, session, class seat, day and the plan period in days

Batches: None. Nothing in a gym is sold per batch, and the pack does not carry the expiry machinery

Expiry and shelf life: The membership has an expiry date and a freeze window, and the screen shows who is about to lapse so the owner can call before the month ends

Sector specific structures: The structures specific to this sector are the membership with its plan, its freeze and its expiry, the class with a capacity and a booking list, the check in at the door, and the coach share of the membership revenue

## 3. Screens and workflows that belong to this sector

- Front desk: the member comes, the check in happens with the phone number or the card, and the screen says if the membership is active, frozen or expired
- Members: the list with the plan, the last visit, the visits this month and the days to the expiry
- Membership: the new member, the plan, the start, the payment, and the card with the number that opens the door
- Class book: the classes of the week with the coach, the room, the capacity and the booked names
- Freeze and pause: a member asks to freeze for a month, the membership shows the new dates and the reason is stored
- Coach sheet: the classes of each coach, the attendance per class and the money the coach share gives
- End of day: the check ins, the new memberships, the renewals and the money counted

## 4. Roles and permissions

- Owner: everything, including the plans, the coaches and the reports
- Manager: everything except billing, approves the freeze, the refund and the discount
- Receptionist: the check in, the membership, the class booking and the payment
- Coach: his classes, his attendance list and his clients, no money
- Cleaner and maintenance: the tasks and the stock of the cleaning materials, no member data

## 5. Reports and KPIs

- Active members, new this month, lapsed and frozen
- Renewals due in the next fourteen days with the last visit of each
- Visits per member per month: who is coming and who is fading
- Class fill rate per class and per coach
- Coach share per period
- Revenue per plan and the churn by plan
- Cash reconciliation per shift

## 6. Integrations that matter

- A door reader or a QR code on the phone for the check in, with the manual check in as a fallback
- Thermal printer through ESC/POS for the receipt and the membership card
- WhatsApp for the expiry reminder and the class reminder through the gym own account
- Card terminal through Paymob and the mobile wallets at the front desk

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Business basics: name, branch, address, phone, currency, opening hours
- Plans: the monthly, the quarterly and the annual plans with the price and what they include
- Coaches: the team with the commission or the hourly rate
- Classes: the class types, the rooms and the capacity
- Members: the first members with the plan and the start date
- Check in method: the reader, the QR code or the manual list
- First week plan: check a member in, book a class, sell a membership, run the end of day
- Review and finish

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- Plan templates in Arabic with the period, the price and the sessions included
- Class type list in Arabic: كلاس, تمارين, تدريب فردي, and the rooms
- Role templates for the receptionist, the coach and the manager
- A membership card layout with the member number, the plan and the expiry
- An empty member list, never seeded with fake names

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- جيم بيعرف مين جاي ومين داخلش، والتجديد بيتابع قبل ما يوقف
- تسجيل دخول بالباب، حصص بالسعة، وعضويات ليها تجميد وتاريخ انتهاء
- شاشة الباب: العضوية نشطة ولا مجمدة ولا منتهية في ثانية
- قائمة المتجددين خلال أسبوعين مع آخر زيارة لكل واحد
- نسبة الحضور للحصص والمدرّب بيتحسب من الحضور الحقيقي

Questions the page must answer:

- العضو تجمد شهر؟ التجميد بيتسجل بسببه وبيتعدل تاريخ الانتهاء، والموضوع واضح في السجل
- بيشتغل من غير نت؟ أيوه: تسجيل الدخول والبيع بيفضلوا شغالين

### English

- A gym that knows who comes and who stops coming, and tracks the renewal before it lapses
- Check in at the door, classes with a real capacity, and memberships with a freeze and an expiry date
- The door screen says in one second whether the membership is active, frozen or expired
- The list of the renewals due in two weeks with the last visit of each member
- The class fill rate and the coach share are computed from the real attendance

Questions the page must answer:

- What if a member freezes for a month? The freeze is recorded with its reason, the expiry moves, and it stays visible in the member record
- Does it work with no connection? Yes: the check in and the sale keep working

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Front desk: the member comes, the check in happens with the phone number or the card, and the screen says if the membership is active, frozen or expired
- Members: the list with the plan, the last visit, the visits this month and the days to the expiry
- Membership: the new member, the plan, the start, the payment, and the card with the number that opens the door
- Class book: the classes of the week with the coach, the room, the capacity and the booked names
- Freeze and pause: a member asks to freeze for a month, the membership shows the new dates and the reason is stored
- Coach sheet: the classes of each coach, the attendance per class and the money the coach share gives

## 9. Pricing tier notes

- The free tier fits a small hall with one desk: one business, one branch, two seats, the check in and the membership list
- Starter adds the class book, the expiry reminders and a year of history
- The Business tier adds the coach share, the fill rate report, the freezes and the multi branch transfer
- The door hardware is the shop own device: we support the reader and the QR code, and we never force a bundle

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| Daftra (دفترة) | Free start, published rates not readable on the page opened (daftra.com, opened 2026-11-12) | An ERP where a gym needs a door, a class and a renewal list | The check in, the class capacity and the renewals are the product |
| Loyverse | Free POS, add-ons from US$5 per store per month (loyverse.com/pricing, opened 2026-11-12) | A retail till with no membership and no class book | The membership, the freeze and the class attendance in one pack |
| Square | Free with processing fees, Plus US$49 per month per location (squareup.com, opened 2026-11-12) | No membership engine and no Arabic, and it is not offered in Egypt | The membership life cycle and the Arabic front desk |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-gym-fitness-tasks.md`:

1. Register the gym pack in the sector registry (M1)
2. Write the gym data model with the memberships and the classes (M1)
3. Build the gym seed with the plan templates (M1)
4. Write the gym terminology map in Arabic and English (M1)
5. Build the front desk check in screen (M2)
6. Build the class book with the capacity and the attendance (M2)
7. Build the membership screen with the freeze and the expiry (M2)
8. Build the coach sheet and the share (M2)
9. Build the gym report pack (M2)
10. Publish the gym landing page in Arabic and English (M3)

## 12. Risks, unknowns and what we refuse to fake

- The member data (body metrics, emergency contact) is personal data of the gym: it never enters our analytics and can be exported and deleted
- Body metrics are optional and never required for a membership
- The coach share is the gym own agreement, and the product never changes the percentage
- Nothing in this pack gives health or nutrition advice, and the app never claims that it does

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-gym-fitness-tasks.md`
