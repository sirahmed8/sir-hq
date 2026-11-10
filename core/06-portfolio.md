# A4. Portfolio map (a proposal from 2026-10-29; the validated list is in `D:\Projects\AGENTS.md` "Portfolio map" and `ops/PORTFOLIO.md`)

> **Status 2026-11-10.** Names below that no longer exist as folders were merged into their SIR product (Laptop Manager, Jobs, Optimizer, Obour Academic Hub). SIR Odysseus was removed (not Ahmed's project). SIR Negm Furniture is plans only (friend's project). Product lines such as SIR Health, SIR Deen, SIR Learn, SIR Deals, SIR Fix, SIR Cars and SIR Sight are ideas, not projects; only the 16 folders in `plans/WAVE_STUDY.md` are active.

## Existing projects

| Project | Likely role (verify in the inventory) | Platform set |
|---|---|---|
| Hagoozat Elite | Pitch / venue booking (TickTick #6: turn the booking site into an app) | Full |
| Merged sites (working name) | Football platform. Ahmed already merged 11Players and EGFootball5 into it: player cards (TickTick #8), plus the Pitch IQ module (#30). Hagoozat Elite may join (3.5) | Full |
| 11Players, EGFootball5 | Merged into Merged sites; the originals move to `old projects` once parity is verified | — |
| Obour Academic Hub | Institute portal (TickTick #7: site → app); can reuse the SIR Learn engine | Full |
| SIR Restaurant | POS and ordering; a SIR Business vertical | Full, plus tablet POS mode |
| SIR Market | Retail; a SIR Business vertical | Full |
| SIR Pharmacy | Pharmacy management (batches, expiry, regulated data); a vertical | Full |
| SIR Library | Library management; a vertical | Full |
| Negm Furniture | Furniture business (check whether it's a client project); a vertical | Full |
| SIR AI | To confirm; candidate home for the shared AI layer or an assistant product | Per inventory |
| SIR Controller, SIR Optimizer, Odysseus | To confirm | Per inventory |
| SIR Content Creation Studio | Media and social engine (Phase 8) | Web + desktop, plus a mobile companion |
| SIR ModPack, SIR Mods for GTA V | Game mods | Web + Windows (proposed exception) |
| Laptop Manager | Local Windows utility | Exception |
| sirahmed8 | GitHub profile and portfolio | Exception |
| Antigravity Agent Suite | Agent tooling | Exception |
| AHome | Private app for Ahmed and Habiba; local AI; no subscriptions, ads or paywalls | Full, private |
| Jobs | CV, applications, freelance profiles (Phase 8.3) | Workspace |
| Obour Institute Second Year 1st term | Course materials and study kits (Phase 8.6) | Workspace |
| Learning | Ahmed's learning tracks (Phase 8.7) | Workspace |
| AI_Models_Hub | Local model files (Phase 8.7) | Workspace |
| SIR Media (new) | Exports for social content (Phase 8.2) | Workspace |

**AI at the core applies to existing products too:** each gets its flagship AI feature in its wave, written into its PRODUCT.md (module 10). Examples: an ordering assistant and demand forecasts for the SIR Business verticals, AI captions and clip-cutting in SIR Content Creation Studio, a local-AI PC assistant in Laptop Manager, a study assistant in Obour Academic Hub, a room visualizer for Negm Furniture if its owner wants one.

Workspaces aren't apps. They get a light SIR file set (`AGENTS.md`, `.sir/CHECKPOINT.md`, a README, clear folder structure), no platform matrix.

## TickTick ideas → product lines (merge proposal)

| Product line | Absorbs TickTick ideas | AI at the core (module 10) | Notes |
|---|---|---|---|
| **SIR Life**: daily life OS | 9 full daily routine around prayer times · 10 daily-life management & personal development · 22 reminders for things you always forget · 18 expense tracker | An AI planner that builds each day around prayer times, tasks and energy; capture in plain words or voice ("remind me to call Mom after Asr"); receipts read into expenses | Shares the prayer-time engine with SIR Deen |
| **SIR Health**: body and mind | 1 calm, meditation, yoga, problem-solving · 2 medication reminders · 3 water reminders · 4 diet tracking & tips · 5 gym plan & weight tracking · 17 food calorie counter · 21 face analysis, reframed as a skin & grooming coach | Meal photo to calories with a confidence level; an AI coach for training and diet plans that adapts to progress; a guided-calm voice companion; reminders set from a photo of a prescription, confirmed by the user | Not medical advice; crisis resources in the mind section; no attractiveness scores; face images are biometric data (explicit consent, minimal retention) |
| **SIR Deen**: Muslim companion | 13 Sunnah, task list by prayer times, Quran memorization, daily wird, all adhkar | A memorization coach that listens to recitation and marks mistakes against the verified text; questions answered only with cited verified sources; a personal wird planner | Quran, tafsir and hadith only from verified sources (Tarteel, UmmahAPI or equivalent); never AI-generated religious text; religious-practice data is sensitive |
| **SIR Learn**: learning platform | 11 skill-building plans · 24 study-problem solver · 25 language learning · 27 teaching platform | An adaptive tutor that explains step by step and checks understanding; a conversation partner with pronunciation feedback; course and quiz generation for teachers | Engine reused by Obour Academic Hub; teaches, never does graded work for students |
| **SIR Business**: SME suite | 12 employees (check-in/out, payroll, location, performance) · 19 inventory with automatic reorder · 20 customer ordering app for a company | Demand forecasts and automatic reorder suggestions; reports asked in plain words ("sales this week against last week"); invoices and receipts read by AI; an ordering assistant for customers | One core shared by the Restaurant, Market, Pharmacy, Library and Negm verticals; employee location needs explicit consent and must follow labor and privacy law. POS essentials: barcode scanning (camera and USB scanners), receipt printers (ESC/POS over USB, Bluetooth or network), cash drawers, a kitchen or order display on the TV app, offline-first sales with sync, and Egypt's e-invoice and e-receipt rules (verify the Tax Authority's current requirements and POS certification) |
| **SIR Deals**: best price for anything | 15 best price across online stores, with sources · 16 game deals · 29 movies & series (where to watch, rent or buy) | Price comparison with sources and a deal-quality score; price-drop predictions; review summaries; a "what should I watch tonight" assistant | Official APIs and affiliate feeds first; respect site terms; never link to pirated content |
| **SIR Fix**: home services | 28 request a maintenance technician | Describe the problem by photo or voice; AI classifies it, estimates a price range and matches a technician | Two-sided marketplace; trust & safety, ratings, disputes |
| **SIR Cars** | 23 specs, pros and cons, spare-parts locations, owner opinions | Compare cars in plain words; summaries of owner opinions; find a spare part from a photo | Data licensing |
| **SIR Sight**: accessibility | 26 voice-first AI assistant for blind users (e.g., interactive Pyramids map) | Scene description, reading text aloud, finding objects, guidance through places; on-device first for privacy and speed | Software first; hardware sensors are a later R&D phase |
| Football (existing) | 6 → Hagoozat Elite · 8 → the merged football platform · 30 → Pitch IQ (AI position coach) inside it | Pitch IQ: a position coach that explains what to do in each situation; a booking assistant that fills empty slots; player-card insights | |
| Concept (parked) | 14 citizen-services platform | | Needs a government partner and a legal basis for national-ID data; keep it as a concept doc |

## Platform matrix

- **Default for every product** (all except the exceptions above): web, Windows, macOS, Android, iOS and iPadOS. Windows apps ship through the Microsoft Store (an MSIX package that Microsoft signs for free) and as a direct installer. Android apps also go to free alternative stores, including Huawei AppGallery for phones without Google services (module 07).
- **Watch apps (Wear OS + watchOS):** Ahmed wants them everywhere. Build them first where there's a real wrist use case: SIR Health, SIR Life, SIR Deen, AHome, Hagoozat Elite (booking reminders), SIR Business (staff check-in). For the rest, ship a minimal companion (notifications plus one glanceable tile or complication) after the phone app is store-ready. Watch work never delays phone or web releases.
- Any exclusion is written down as an ADR, and Ahmed can override it.
- **Also core for every product:** Linux (AppImage and `.deb` from the same Electron app); Chromebooks (the Android app plus the PWA); compatibility mode on Apple Vision Pro and Android XR (iPad and large-screen Android apps run there).
- **Widgets and Live Activities** for products with glanceable data. Small iOS widgets and Live Activities also appear in CarPlay automatically, which gives most products a car presence.
- **TV apps** (Android TV / Google TV and Apple TV) are core: every product gets one from the same Expo codebase through the TV profile (module 20), built around a real TV use: SIR Deen (recitations), SIR Health (yoga and meditation sessions), SIR Learn (lessons), SIR Deals (what to watch), the football projects (highlights and stats), AHome (photos and memories); for business products, a big-screen dashboard or a customer-facing display (an order-status board, promotions, queue numbers).
- **Car apps** are core wherever Android Auto and CarPlay allow them (categories in module 20): SIR Deen, SIR Health and SIR Learn as audio apps; SIR Restaurant for quick food ordering in CarPlay; SIR AI if it's a voice assistant (CarPlay voice-based conversational apps); navigation, parking or charging features where a product has them. The platforms reject other categories, so every other product gets its car presence through widgets and Live Activities, which CarPlay shows automatically.
- **Browser extensions** where they add real value (a price checker for SIR Deals).
- Ahmed wants maximum coverage: build every platform a product can legitimately have. Skip only what is technically impossible or forbidden by platform policy, with the reason in an ADR.

## Languages and search (every public product)

- **Locales: Arabic, English, Mandarin Chinese (Simplified) and Hindi.** Ahmed asked for Arabic, English and the two most-spoken languages besides them. Ethnologue's 2026 figures by total speakers: English ~1.53B, Mandarin ~1.18B, Hindi ~611M, Spanish ~561M, Modern Standard Arabic ~335M, French ~334M.
  - Spanish is a close fourth, and its markets often spend more per user. The locale list is one line in `.sir/project.yml`, so a product can switch when its market says so (ADR).
  - A Chinese UI alone doesn't open mainland China: Google Play isn't available there, and China's App Store requires a government app registration.
  - AHome stays Arabic and English (private).
- **Search:** every public product aims to be the best answer for its category in search engines, app stores and AI assistants (module 16). Nobody can guarantee rank #1; doing everything in our control is the standard. AHome is excluded: no indexing, no listings.
