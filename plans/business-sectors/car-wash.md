# SIR Business sector: Car wash (غسيل سيارات)

> Round r56 (2026-11-12). Sector 24 of 41 in `plans/business-sectors/_INDEX.md`, wave 3.
> Base template `service`, group `service`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The car wash owner manages membership tiers, fast ticket sales and queue management. Their day is member check-ins, subscription renewals and cash reconciliation.

Why this sector is in the catalogue: Car washes are membership-based with fast tickets, subscription tiers and quick turnaround. The key is the fast lane, membership management and cash-flow predictability.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- CarWash (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- MembershipTier (id, washId, nameAr, nameEn, pricePiasters, durationDays, washCount, isActive, features)
- Member (id, washId, name, phone, membershipTierId, status, joinDate, expiryDate, visitsThisPeriod, washesThisPeriod)
- Ticket (id, washId, memberId, phone, type (membership/ticket/pay-per-wash), amountPiasters, status, generatedAt, usedAt)
- Queue (id, washId, ticketId, position, status (waiting/being-served/done), updatedAt)
- CashRecord (id, date, openingPiasters, countedPiasters, variancePiasters, notes)

Units in use: wash, membership, ticket, slot

Batches: No : car wash carries no stock or expiry

Expiry and shelf life: Not applicable. Memberships have duration and wash count, tickets have status

Sector specific structures: The core structures are the membership tier with wash count and duration, the ticket (membership/ticket/pay-per-wash) and the queue position. Fast turnaround and cash-flow predictability are the key metrics.

## 3. Screens and workflows that belong to this sector

- Member check-in: scan member phone or ticket, view membership status, increment washesThisPeriod, position in queue
- Membership management: add tier, set price, duration, wash count, features (fast lane, free vacuum, etc.), activate/deactivate
- Ticket generation: create ticket (membership/ticket/pay-per-wash), record amount, set status (active/used)
- Queue management: view waiting tickets, position, move to being-served, mark done
- Cash reconciliation: daily opening vs counted, variance, notes, print Z-report
- Membership overview: all members, active tiers, renewal upcoming, visits per period
- Staff shift: clock in/out, customer load per hour, notes

## 4. Roles and permissions

- Owner: everything : memberships, tickets, queue, cash, reports, billing
- Attendant: member check-in, ticket generation, queue management, cash recording
- Manager: membership tiers, pricing, attendant scheduling, reports

## 5. Reports and KPIs

- Daily revenue: total washes, membership revenue, ticket sales, cash variance
- Membership growth: new members per period, renewals, churn per period
- Wash frequency per member: visits per period, average visits per member
- Queue efficiency: average wait time, tickets per hour, peak hours
- Membership tier performance: which tiers sell best, wash count per tier

## 6. Integrations that matter

- Esc/POS thermal printer for tickets and Z-report
- WhatsApp deep link for membership renewal notices and membership reactivation
- SMS for appointment reminders (optional)
- Payment gateway for membership top-up (optional)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Wash basics: name, branch, address, phone, currency, working hours
- Membership tiers: the initial tiers (basic, premium, premium-plus) with price, duration and wash count
- Initial members: the first member records with tier assignment
- Staff: add the initial team with their role templates
- First week plan: set up first membership tier, first member, first ticket

Template data that is ready on day one (seeded and marked "review before going live", never shown as if it were the shop's own data):

- N
- o
-  
- s
- e
- c
- t
- o
- r
- -
- s
- p
- e
- c
- i
- f
- i
- c
-  
- s
- e
- e
- d
-  
- d
- a
- t
- a
- .
-  
- T
- h
- e
-  
- e
- n
- g
- i
- n
- e
-  
- p
- r
- o
- v
- i
- d
- e
- s
-  
- t
- h
- e
-  
- m
- e
- m
- b
- e
- r
- s
- h
- i
- p
-  
- t
- i
- e
- r
-  
- a
- n
- d
-  
- r
- o
- l
- e
-  
- t
- e
- m
- p
- l
- a
- t
- e
- s
- .

## 8. The landing page outline

The sector gets its own page, its own words and its own proof. No shared generic copy.

### Arabic (ar-EG, written first)

- غسيل سيارات
- اشتراكات، تذاكرLane سريعة من لوحة واحدة
- اشتراكات بأدوار مختلفة
- مسار سريع للسيارات
- تتبع الزيارات والمبيعات

Questions the page must answer:

- كيف أصبح عضواً في الغسيل؟
- ما هي التierces المتوفرة؟

### English

- Car Wash Management
- Memberships, tickets and fast lane from one dashboard
- Membership tiers with wash count and duration
- Ticket generation (membership/ticket/pay-per-wash)
- Queue management and efficiency tracking

Questions the page must answer:

- How do I become a member?
- What tiers are available?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Member check-in: scan member phone or ticket, view membership status, increment washesThisPeriod, position in queue
- Membership management: add tier, set price, duration, wash count, features (fast lane, free vacuum, etc.), activate/deactivate
- Ticket generation: create ticket (membership/ticket/pay-per-wash), record amount, set status (active/used)
- Queue management: view waiting tickets, position, move to being-served, mark done
- Cash reconciliation: daily opening vs counted, variance, notes, print Z-report
- Membership overview: all members, active tiers, renewal upcoming, visits per period

## 9. Pricing tier notes

- - Basic: 120 EGP / month, 5 washes/month, standard lane
- - Premium: 220 EGP / month, 15 washes/month, fast lane + free vacuum
- - PremiumPlus: 350 EGP / month, 30 washes/month, fast lane, free vacuum, priority booking

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| SpeedWash | from 250 EGP/mo | no membership tiers | full membership tiers with wash count and duration |
| AutoSpa | from 280 EGP/mo | no fast lane ticket generator | fast lane ticket with status and queue management |
| CarFresh | from 300 EGP/mo | no cash reconciliation Z-report | daily cash reconciliation with variance and Z-report |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-car-wash-tasks.md`:

1. Add membership tier manager (M1)
2. Add member check-in with queue position (M1)
3. Add ticket generation (membership/ticket/pay-per-wash) (M1)
4. Add queue management (waiting/being-served/done) (M1)
5. Add daily cash reconciliation Z-report (M1)
6. Add membership growth report (M2)
7. Add wash frequency per member report (M2)
8. Add queue efficiency report (M2)
9. Add membership tier performance report (M2)
10. Add onboarding flow for initial car wash setup (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes member and cash records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Membership subscriptions without clear duration and wash count can violate consumer protection law
- Cash variance without audit trail can lead to disputes

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-car-wash-tasks.md`
