# Competitor Study: SIR Hagoozat (Sports Venue & Turf Reservation)

> AUDIT 2026-11-10 (plans audit): this file has no source links. Every price, market share, user count, feature claim, quoted review and complaint quote below is "(unsourced, verify)" until it has a link and a date. Do not copy anything from here into public copy, store listings, legal pages or comparison pages. Quoted reviews could not be traced to a real page: treat them as illustrative, not as evidence. Sourcing tasks are at the end of this file.
**Date of Research**: 2026-11-09  
**Category**: Sports Tech, Turf Reservation, Padel & Football Booking  
**Target Markets**: Egypt (Primary: Cairo, Giza, Alexandria), Gulf (Saudi Arabia, UAE)


## 0. Sourced findings (web search, 2026-11-10; excerpts only, open each page before relying on it)
| Competitor | What the page says | Link |
|---|---|---|
| Hareefa | Connects players with football courts in Egypt; players book matches, court owners manage bookings | https://hareefa.com/ |
| Yalla Hagz | App to book a pitch; site mentions live availability, instant confirmation, football, padel, padbol | https://www.yallahagz-eg.com/ and the App Store page https://apps.apple.com/eg/app/yalla-hagz-%D9%8A%D9%84%D8%A7-%D8%AD%D8%AC%D8%B2/id6451365492 |
| Playtomic | Has a manager pricing page and a player Premium plan with "zero booking fees"; a UK club post says the player booking fee is 3 percent with a minimum of 35p and a maximum of 99p per person | https://playtomic.com/pricing , https://playerhelp.playtomic.com/hc/en-gb/articles/19831696399633-Premium-Plan-Unlimited |
| Pitchbooking | Sports facility management software (booking, payments) | https://pitchbooking.com/ |
Corrections to the table below: the competitor "Bookafield" did not appear in a search for it and may not exist: removed from consideration until a link is found. The Playtomic price "5 to 10 EGP per booking, 80 EUR per month" is replaced by the sourced UK figures above (not Egypt). Real Egyptian competitors to study first: Hareefa and Yalla Hagz.

---

## 1. Top Competitors Overview

| Competitor | Market & Reach | Tech & Platforms | Pricing Model | Arabic / Local Fit |
|---|---|---|---|---|
| **Playtomic** | Global leader (Spain, Europe, expanding to GCC/Egypt) | React Native (iOS/Android), Web app | Player booking fee (~5–10 EGP / booking) + Venue subscription (~€80/mo) | English/Spanish first; clumsy Arabic translation; **No Vodafone Cash or Meeza support**. |
| **Malaeb** | GCC & Egypt (Bahrain-based) | Native iOS & Android, Web | Commission per reservation (10–15%) | Good Arabic, but focuses heavily on GCC tournaments; Egyptian venue listings frequently out of date. |
| **Grinta / Local WhatsApp Booking** | Informal Egyptian Market (80%+ market share) | Manual WhatsApp chats & paper notebooks | Zero software cost, high human overhead | 100% Egyptian dialect, but zero real-time calendar sync; frequent double-booking arguments and lost deposits. |
| **Bookafield** | Egyptian regional attempts | Hybrid mobile app | Flat monthly venue fee | Infrequent updates; users complain of UI freezing and abandoned customer support. |

---

## 2. Real User Complaints & Pain Points (Sourced from App Store, Google Play & Local Groups)
- **Complaint 1 (Double Booking Friction)**: *"حجزت الملعب عن طريق التطبيق ولما رحت لقيت في ناس تانية حاجزة بالتليفون وصاحب الملعب قال ما شافش الحجز!"* (Source: Google Play Review, Cairo; no link, unsourced, verify). Venues maintain paper notebooks alongside apps, causing race conditions.
- **Complaint 2 (Payment Exclusion)**: *"ليه كل البرامج لازم فيزا بنكية؟ إحنا شلة صحاب وعايزين ندفع بفودافون كاش ومحافظ الموبايل"* (Source: Reddit r/Egypt discussion on sports apps; no link, unsourced, verify). Lack of local Egyptian wallet integrations.
- **Complaint 3 (Split Payment Headache)**: One organizer pays the entire fee upfront (e.g. 600 EGP) and spends three days chasing 9 other players for 60 EGP each via InstaPay.
- **Complaint 4 (High Commissions for Venue Owners)**: Small pitch owners refuse 15% booking commissions because profit margins on electric lighting and turf maintenance are already slim.

---

## 3. "We Do Better" Advantage Map (SIR Hagoozat Superiority)

1. **Instant Multi-Player Split Payments**: The organizer selects a 600 EGP slot, taps "Split with 10 players", and the app generates individual Paymob payment links (60 EGP each via Vodafone Cash, InstaPay, or Meeza). The slot is held until fully funded.
2. **Real-Time Venue WhatsApp Synchronization**: When a booking occurs in SIR Hagoozat, our WhatsApp bot sends an instant audio-chime and calendar ticket to the pitch manager's WhatsApp, confirming slot reservation without requiring them to install complex software.
3. **Ultra-Fair Local Pricing**: Low flat transaction fee (2.5% + 3 EGP) instead of predatory 15% commissions, making Egyptian turf owners eager partners rather than reluctant hosts.
4. **Offline-Capable Venue Dashboard**: If venue internet drops, the local PWA caches the day's schedule offline and syncs immediately when connectivity returns.

## Sourcing tasks (open, each under 2 hours)
1. Done in part on 2026-11-10: see the sourced section above. Remaining: open Hareefa and Yalla Hagz pages and record features, payment methods and any prices with links.
2. Check Malaeb's Egypt coverage and fees on its official page (link, date).
3. Find the real fee schedules of Paymob and Fawry (official pages) before quoting any gateway fee.
