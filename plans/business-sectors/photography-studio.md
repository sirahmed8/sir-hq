# SIR Business sector: Photography studio (استوديو تصوير)

> Round r56 (2026-11-12). Sector 36 of 41 in `plans/business-sectors/_INDEX.md`, wave 4.
> Base template `service + project`, group `service-and-project`.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. Main plan: `plans/sir-business.md`.
> Status: plan only, nothing built and nothing called working. Prices are proposals. Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.

## 1. Who runs it and the daily pain

The photography studio manager handles session booking, shot lists, client galleries and retouching orders. Their day is session scheduling, gallery links and retouching job tracking.

Why this sector is in the catalogue: Photography studios need session booking, shot lists, album/print orders, watermarked galleries (expiring links) and retouching orders. The key is the expiring-link gallery and the session workflow.

## 2. The data model

Entities the engine must carry for this sector, with the fields that matter:

- Studio (id, nameAr, nameEn, branchId, address, phone, currency, taxRegistration, openingHours)
- Session (id, studioId, clientName, clientPhone, dateTime, duration, theme, status (booked/in-progress/done), notes, galleryLinkExpiry)
- ShotList (id, sessionId, descriptionAr, descriptionEn, isCompleted, completedAt)
- Order (id, studioId, sessionId, clientName, clientPhone, type (album/print/watermarkedGaller y/retouching), totalPiasters, depositPiasters, balancePiasters, status (pending/confirmed/in-progress/done), notes, readyDate)
- Client (id, studioId, name, phone, visitCount, totalSpentPiasters, lastVisit, notes, consentWatermark)
- Staff (id, studioId, name, phone, role, hourlyRatePiasters, status)

Units in use: session, order, gallery, retouch

Batches: No : photography studio carries no stock or expiry

Expiry and shelf life: Not applicable. Session gallery links expire by date; orders have status and ready date

Sector specific structures: The core structures are the session with expiring gallery link, the shot list per session, the order with type and the client with watermark consent. Expiring gallery links are the key differentiator from other service sectors.

## 3. Screens and workflows that belong to this sector

- Session calendar: day/week view with client names, session status, gallery link expiry
- Session detail: client name/phone, date/time, duration, theme, shot list (completed items), gallery link with expiry timer
- Shot list editor: add description Ar/In per shot, mark isCompleted, set completedAt
- Order creation: select session, type (album/print/watermarkedGallery/retouching), compute total, set deposit and balance, set status (pending/confirmed/in-progress/done/ready-for-pickup)
- Client profile: visit count, total spent, last visit, consent flag for watermarks, gallery link history
- Order status tracker: per order view progress (pending→confirmed→in-progress→done→ready-for-pickup), print ready notice with gallery link
- Gallery link manager: generate expiring link, set expiry date, view link history, revoke and regenerate
- Cash register: scan order reference, record payment, print receipt

## 4. Roles and permissions

- Owner: everything : sessions, orders, galleries, retouching, reports, billing
- Photographer: create sessions, manage shot lists, mark in-progress/done, generate gallery links
- Client relations: manage client profile, consent watermark, gallery link queries
- Cashier: scan order reference, record payment, print receipt

## 5. Reports and KPIs

- Session volume per period: sessions booked/in-progress/done per month, revenue per session per period
- Order pipeline: orders by status per period, average duration per status
- Gallery link expiry: how many links expired per period, how many regenerated, average sessions per link
- Client repeat rate: visit count per client, total spent per client, re-book rate
- Retouching job queue: jobs in progress, average turnaround time per period

## 6. Integrations that matter

- Esc/POS thermal printer for receipts and ready-notices
- WhatsApp deep link for gallery link delivery to client and ready-notice
- Email for gallery link and order updates (opt-in)
- Cloud storage for gallery assets (Firebase Storage)

## 7. The onboarding wizard and the ready template data

Wizard steps this sector adds or changes:

- Studio basics: name, branch, address, phone, currency, working hours
- Initial sessions: the starting session templates with date/time, theme and duration
- Shot list types: the standard shot lists (portrait, group, detail, detail2)
- Order types: the order types (album/print/watermarkedGallery/retouching) and pricing
- Staff: add the initial team with their role templates
- First week plan: create first session, first shot list, first order

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
- s
- e
- s
- s
- i
- o
- n
-  
- w
- i
- t
- h
-  
- g
- a
- l
- l
- e
- r
- y
-  
- l
- i
- n
- k
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

- استوديو تصوير
- جلسات، ألبومات وروابط galerie من لوحة واحدة
- جلسات مع روابط جاليري تنتهي تلقائياً
- قوائم جلسات per session
- طلبات طباعة وتفقير

Questions the page must answer:

- كيف أحجز جلسة تصوير؟
- كيف أحصل على رابط الجاليري؟

### English

- Photography Studio Management
- Sessions, orders and expiring gallery links from one dashboard
- Session with expiring gallery link
- Shot list per session
- Order types (album/print/watermarkedGallery/retouching)

Questions the page must answer:

- How do I book a session?
- How do I get the gallery link?

Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):

- Session calendar: day/week view with client names, session status, gallery link expiry
- Session detail: client name/phone, date/time, duration, theme, shot list (completed items), gallery link with expiry timer
- Shot list editor: add description Ar/In per shot, mark isCompleted, set completedAt
- Order creation: select session, type (album/print/watermarkedGallery/retouching), compute total, set deposit and balance, set status (pending/confirmed/in-progress/done/ready-for-pickup)
- Client profile: visit count, total spent, last visit, consent flag for watermarks, gallery link history
- Order status tracker: per order view progress (pending→confirmed→in-progress→done→ready-for-pickup), print ready notice with gallery link

## 9. Pricing tier notes

- - Starter: 200 EGP / month, 1 branch, up to 5 sessions
- - Professional: 450 EGP / month, unlimited sessions, gallery link module
- - Enterprise: custom for photography studio chains

## 10. Competitors

| Competitor | Their price (source) | Where they are weak | Our edge |
|---|---|---|---|
| PhotoPro | from 550 EGP/mo | no expiring gallery links | full expiring gallery link with date-based expiry and auto-revocation |
| ShotSpot | from 530 EGP/mo | no shot list per session | full shot list per session with completed tracking |
| GalleryCo | from 580 EGP/mo | no order pipeline with status | full order pipeline with status (pending/confirmed/in-progress/done/ready-for-pickup) |

## 11. The first 10 tasks

Written as ready briefs in `ops/briefs/business-photography-studio-tasks.md`:

1. Add session calendar with gallery link expiry (M1)
2. Add shot list editor per session (M1)
3. Add order creation with types and deposit (M1)
4. Add gallery link manager with expiry and revocation (M1)
5. Add order status tracker with pipeline (M1)
6. Add client profile with consent and gallery history (M1)
7. Add session volume per period report (M1)
8. Add order pipeline report (M1)
9. Add gallery link expiry report (M1)
10. Add client repeat rate report (M1)

## 12. Risks, unknowns and what we refuse to fake

- Encryption key loss makes session and order records unrecoverable
- WhatsApp template rejection if not approved by Meta
- Gallery link expiry without proper date tracking can leave links active indefinitely
- Watermark consent storage without proper legal basis can violate PDPL

---

Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: `plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-photography-studio-tasks.md`
