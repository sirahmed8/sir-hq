# Sector catalogue: the final list, the reasons, and the build order

> Round r56 (HQ, 2026-11-12). The owner asked (plans/PRODUCT_DIRECTION_2026-11-12.md section 8): "SIR Business is the biggest project: 25 sectors or more, and EACH sector gets its own specialised software and site ... Not one generic app with a different label."
> The merged plan `plans/sir-business.md` section 4 listed 30 sectors. This file decides the final list, says why each one is in or out, and orders the build.
> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`.
> Truth rule: no market size, price or competitor claim in this file was read from a source unless the source is named. The market reads below are our own judgement from the sector shape and the Egyptian street, and they are marked "(our read, not sourced)".

## 1. The decision

**41 sectors** ship as their own specialised software and their own site page on the shared engine.

What changed against the r53 list of 30:

| Change | Sectors | Why |
|---|---|---|
| Split | library, bookstore | Lending (memberships, deposits, study desks) and selling (ISBN catalog, stock, margins) are different shops with different screens. One file would have been a renamed app |
| Added | pharmacy-chain | Chains are common in Egypt and are the main reason one owner needs several branches and several businesses. It is a pharmacy pack plus chain features, so it ships after pharmacy |
| Added | optical-shop | Small, self-contained, and it needs its own vocabulary (lens types, prescriptions, fitting) and its own screen set |
| Added | grocery-shop | The neighbourhood grocery is a different business from the supermarket: credit book, small basket, no self-checkout, short credit cycle |
| Added | pet-shop | The owner named it; the retail pack is easy but the animal care vocabulary and the vet link make it its own page |
| Added | furniture-carpentry | Big-ticket items, custom sizes, deposits and delivery slots; nothing like fast retail |
| Added | florist | Event-driven, per-order customisation, same-day delivery windows |
| Added | print-shop | Job tickets, proofing, paper stock and unit pricing (per page, per poster, per banner) |
| Added | factory-workshop | Production, not retail: bill of materials, work orders, output, scrap |
| Added | car-wash | Membership-based, subscription, fast ticket, very different rhythm from the garage |
| Added | private-school-nursery | The owner named it; child data changes the privacy rules completely |
| Renamed | gift-and-stationery to stationery-gifts, library-and-bookstore to library plus bookstore, market-and-supermarket to supermarket plus grocery-shop | Words must match what the shopkeeper calls the shop |
| Kept as one | training-center covers tutoring centres, language centres and technical academies | Same money, same cohorts, same attendance; one pack with three vocabularies, three landing pages |

What is honestly out of scope and why (kept here so nobody re-adds it later):

| Not a sector (yet) | Reason |
|---|---|
| Pure e-commerce and affiliate stores | No counter, no shift, no stock on a shelf; our engine has nothing to add that Shopify does not do better |
| Banking, microfinance, lending | Regulated; never without counsel; the credit book we ship is a shop ledger, not a loan product |
| Charities, mosques and churches | Donations and membership modules, not a business sector; a real customer request would create a sector file |
| Points as cash, gift cards that convert to money | Legal in Egypt only with a licence; loyalty points never convert to cash |
| Manufacturing ERP and heavy production | Only the small workshop (factory-workshop) is in scope: job orders and output, not a full ERP |
| Cafeterias inside offices, hospital canteens | Restaurant template, sold as a branch; not a separate pack |

## 2. The final list with the reason and the build order

Order: wave 1 first (largest number of shops and the least new machinery), wave 2 (big service trades that need appointments or job cards), wave 3 (retail depth, serial numbers, B2B), wave 4 (specialised packs and the ones that wait for another pack).

| # | Sector (ar) | English | Slug | Base | Market read (our read, not sourced) | New machinery | Wave |
|---|---|---|---|---|---|---|---|
| 1 | سوبر ماركت | Supermarket | `supermarket` | market | Very large: the anchor tenant of every market street | FEFO, weigh-and-label, loyalty at scale | 1 |
| 2 | بقالة | Grocery shop | `grocery-shop` | market | Very large: the smallest shop that still runs a real business | credit book, small basket | 1 |
| 3 | مطعم | Restaurant | `restaurant` | restaurant | Very large, deep existing competition (Foodics and others) | tables, KDS, recipes | 1 |
| 4 | كافيه | Cafe | `cafe` | restaurant | Large: quick service, heavy modifiers | tabs, modifiers, day parts | 1 |
| 5 | صيدلية | Pharmacy | `pharmacy` | pharmacy | Large and regulated: FEFO, interactions, controlled log | FEFO, prescriptions, patients | 1 |
| 6 | مخبز وحلواني | Bakery | `bakery` | restaurant + retail | Large: weight pricing and daily production | kg pricing, production batches | 1 |
| 7 | ملحمة وخضار | Butcher and fresh grocery | `butcher-fresh-grocery` | market + FEFO | Large: cold chain, expiry, cutting rules | FEFO, cutting, weight | 1 |
| 8 | صالون | Salon | `salon` | service | Large: booking calendar is the core | bookings, commissions | 2 |
| 9 | حلاقة رجالي | Barber | `barber` | service | Large: queue and token, low data risk | queue, tokens | 2 |
| 10 | جيم ولياقة | Gym and fitness | `gym-fitness` | service | Large: memberships, freezes, classes | memberships, attendance | 2 |
| 11 | صيانة سيارات | Car service and garage | `car-service-garage` | garage | Large: job cards and parts | job cards, labour, parts | 2 |
| 12 | مغسلة | Laundry | `laundry` | service | Large: intake tags and per-kg pricing | item tags, per-kg | 2 |
| 13 | توصيل وشحن | Delivery and courier | `delivery-courier` | delivery | Large and growing: proof of delivery and cash on delivery | drivers, zones, COD | 2 |
| 14 | عيادة | General clinic | `clinic` | clinic | Large: appointments and records | appointments, records | 2 |
| 15 | عيادة أسنان | Dental clinic | `dental-clinic` | clinic + dental | Large: treatment plans and staged payments | treatment plans, tooth chart | 2 |
| 16 | ملابس | Clothing retail | `clothing-retail` | retail | Large: variants, seasons, exchanges | size and colour matrix | 3 |
| 17 | إلكترونيات وموبايلات | Electronics and mobile | `electronics-phone` | retail | Large: serial numbers, warranty, trade-in | serial tracking, repairs | 3 |
| 18 | عدد ومواد بناء | Hardware and materials | `hardware-materials` | market + B2B | Large with B2B credit: contractor accounts | bulk pricing, credit | 3 |
| 19 | جملة وتوزيع | Wholesale and distribution | `wholesale-distribution` | market + B2B | Large: tiered pricing and receivables | tiered pricing, receivables | 3 |
| 20 | مكتبة أدوات وهدايا | Stationery and gifts | `stationery-gifts` | retail | Medium to large: gift wrap and personalisation | gift wrap, engraving | 3 |
| 21 | مكتبة بيع | Bookstore | `bookstore` | retail | Medium: ISBN catalog, second-hand stock | ISBN, editions | 3 |
| 22 | مكتبة | Library | `library` | library | Medium: lending, deposits, study desks | lending, holds, desks | 3 |
| 23 | مقصف ومكتبة مدرسة | School shop | `school-shop` | market + service | Medium and seasonal: term subscriptions | student wallets, term plans | 3 |
| 24 | غسيل سيارات | Car wash | `car-wash` | service | Medium: subscription and fast ticket | subscriptions, fast lanes | 3 |
| 25 | سبا وعناية | Spa and wellness | `spa-wellness` | service | Medium: packages with expiry | packages, rooms | 4 |
| 26 | عيادة بيطرية | Veterinary clinic | `veterinary-clinic` | clinic + shop | Medium: appointments, vaccinations, pet food | pet records, vaccines | 4 |
| 27 | محل حيوانات أليفة | Pet shop | `pet-shop` | retail | Medium: FEFO food, grooming hand-off | FEFO, grooming slots | 4 |
| 28 | محل نظارات | Optical shop | `optical-shop` | service + retail | Medium: lens types and fitting | lens catalog, prescriptions | 4 |
| 29 | أثاث ونجارة | Furniture and carpentry | `furniture-carpentry` | retail + production | Medium: custom sizes, deposits, delivery slots | custom specs, deposits | 4 |
| 30 | محل زهور | Florist | `florist` | service + retail | Medium: event orders, same-day windows | event orders, windows | 4 |
| 31 | مطبعة | Print shop | `print-shop` | production | Medium: job tickets and unit pricing | job tickets, proofs | 4 |
| 32 | مصنع وورشة إنتاج | Factory workshop | `factory-workshop` | production | Medium and few: bill of materials and output | BOM, work orders, scrap | 4 |
| 33 | صيانة أجهزة وموبايلات | Repair shop | `repair-shop` | service + ticket | Medium: ticket intake and approval | tickets, quotes | 4 |
| 34 | عصائر ومشروبات | Juice and drinks | `juice-beverage` | restaurant | Medium: modifier-heavy, daily fresh prep | modifiers, prep list | 4 |
| 35 | حلويات وأيس كريم | Dessert and ice cream | `dessert-ice-cream` | restaurant + retail | Medium: flavours, assembly notes | flavour matrix, bundles | 4 |
| 36 | استوديو تصوير | Photography studio | `photography-studio` | service + project | Medium: sessions, albums, expiring galleries | sessions, galleries | 4 |
| 37 | فندق وغرفة مفروشة | Hotel and guest house | `hotel-guest-house` | hospitality | Medium: rooms, housekeeping, deposits | rooms, housekeeping | 4 |
| 38 | مكتب عقاري | Real estate office | `real-estate-office` | realestate | Medium: listings, leads, commission | listings, pipeline | 4 |
| 39 | مدرسة خاصة وحضانة | Private school and nursery | `private-school-nursery` | education | Medium: attendance, fees, child data | students, attendance, fees | 4 |
| 40 | مركز تدريب | Training center | `training-center` | education | Medium: cohorts, attendance, teacher share | cohorts, payouts | 4 |
| 41 | سلسلة صيدليات | Pharmacy chain | `pharmacy-chain` | pharmacy + branches | Small and growing: multi-branch, centralised buying | branches, central buying | 4 |

Total: **41 sectors**, in 41 files under `plans/business-sectors/` (one file per row above, named after the slug) and 41 task briefs under `ops/briefs/business-<slug>-tasks.md`.

## 3. Every sector the owner named, and where it landed

| Owner named it | Final slug | Note |
|---|---|---|
| restaurant | `restaurant` | file 3 |
| cafe | `cafe` | file 4 |
| pharmacy | `pharmacy` | file 5 |
| pharmacy chain | `pharmacy-chain` | file 41, ships after pharmacy |
| clinic | `clinic` | file 14 |
| dental clinic | `dental-clinic` | file 15 |
| library | `library` | file 22 |
| bookstore | `bookstore` | file 21, split from the r53 combined row |
| supermarket | `supermarket` | file 1 |
| grocery | `grocery-shop` | file 2, split from the r53 combined row |
| bakery | `bakery` | file 6 |
| butcher | `butcher-fresh-grocery` | file 7 |
| gym | `gym-fitness` | file 10 |
| salon and barber | `salon`, `barber` | files 8 and 9, two packs (different queues, different data) |
| laundry | `laundry` | file 12 |
| car service and garage | `car-service-garage` | file 11 |
| car wash | `car-wash` | file 24 |
| school shop and stationery | `school-shop`, `stationery-gifts` | files 23 and 20, two packs |
| electronics and phone shop | `electronics-phone` | file 17 |
| clothing retail | `clothing-retail` | file 16 |
| wholesale and distribution | `wholesale-distribution` | file 19 |
| hotel and guest house | `hotel-guest-house` | file 37 |
| real estate office | `real-estate-office` | file 38 |
| private school and nursery | `private-school-nursery` | file 39 |
| training center | `training-center` | file 40 (tutoring centres included) |
| delivery and courier | `delivery-courier` | file 13 |
| factory workshop | `factory-workshop` | file 32 |
| furniture and carpentry shop | `furniture-carpentry` | file 29 |
| optical shop | `optical-shop` | file 28 |
| pet shop and vet | `pet-shop`, `veterinary-clinic` | files 27 and 26, two packs |
| florist | `florist` | file 30 |
| print shop | `print-shop` | file 31 |
| "and others worth supporting" | dessert-ice-cream, juice-beverage, spa-wellness, hardware-materials, repair-shop, photography-studio | files 35, 34, 25, 18, 33, 36: each was already in the r53 catalogue and each earns its own pack |

Every name the owner wrote appears in the final list. Nothing was dropped without a reason, and the reasons are in section 1.

## 4. How the catalogue is built

- One sector file per row: `plans/business-sectors/<slug>.md`, eleven parts, same order everywhere (`_ENGINE.md` section 14).
- One tasks file per sector: `ops/briefs/business-<slug>-tasks.md`, the first 10 tasks ready to queue to a free worker.
- The source of truth for the text is `plans/business-sectors/_data/<slug>.json` plus `scripts/build_business_sectors.py`, so the catalogue can be regenerated and checked in CI instead of being 41 hand-copied files that drift apart.
- The merged plan `plans/sir-business.md` links all of it and keeps the 30-sector table of section 4 as the launch view, with this file as the depth view.

## 5. Open research tasks (honest, not done in this round)

These are the questions a sector page must not answer with a guess. Each one is a task, not a claim:

1. Read the Egyptian Tax Authority e-receipt and e-invoice technical specification and record what a POS must print and sign; the pharmacy, wholesale, hardware and restaurant pages say "(unsourced, verify)" until this is done.
2. Open the public pages of the sector competitors named in the sector files (for example Sapaad, Kashat, Dukan, Tago and their peers) and replace every "(unsourced, verify)" price with a real, dated source or delete the price.
3. Five pilot interviews per wave-1 sector (supermarket, grocery, restaurant, cafe, pharmacy, bakery) to re-price the plans and to check the daily pain list of every sector file against what the shopkeeper says.
4. Confirm the pharmacy licensing and controlled-drug rules with the pharmacist of record and, for clinics and schools, with the owner of a real practice.
5. Check whether the WhatsApp Business account rules allow a shop to send its own receipts through our deep links without a template rejection.
6. Verify the FEFO and shelf-life values used in the seeds against real packaging labels in a real shop (a wrong shelf life is a safety problem, not a formatting problem).
