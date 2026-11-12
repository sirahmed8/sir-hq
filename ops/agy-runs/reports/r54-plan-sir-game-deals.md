# Report: r54-plan-sir-game-deals

Round r54 (HQ, 2026-11-12). Worker: OpenCode. Output scope: `D:/Projects/_SIR` only (plans and ops folders). Result: ok.

---

## 1. What this round was asked to do

The brief (`D:/Projects/_SIR/ops/briefs/r54-plan-sir-game-deals.md`) asked for one thing: turn the owner's "game deals" idea into its own small independent product with the same premium standard as every other product, by writing a deeper plan than the old note, after reading every existing note about the idea and researching the market on the web.

Required outputs, all delivered:

| Output | Path | State |
|---|---|---|
| The plan | `D:/Projects/_SIR/plans/sir-game-deals.md` | written, 481 lines |
| The competitor study | `D:/Projects/_SIR/ops/competitors/sir-game-deals.md` | written, 88 lines |
| The first ten build tasks | `D:/Projects/_SIR/ops/briefs/sir-game-deals-tasks.md` | written, 34 lines |
| One line on the HQ bus | `D:/Projects/_SIR/ops/bus/sir-hq.md` | appended |
| Round checklist | `D:/Projects/_SIR/.sir/r54-plan-sir-game-deals_CHECKLIST.md` | all 15 lines ticked |
| Project checkpoint | `D:/Projects/_SIR/.sir/CHECKPOINT.md` | worker note appended |

Explicitly forbidden and not done: no project folder `D:/Projects/SIR Game Deals`, no GitHub repo `sirahmed8/sir-game-deals`, no Firebase project, no code, no keys, no deployment. M0 of the plan and T1 of the task file do that in the next round.

---

## 2. The rescan (rule 20)

Read before writing:

- `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`, `D:/Projects/_SIR/standard/OWNER_DEFAULTS.md` (items 1 to 22, including item 19 the Desktop folder kit and item 22 the rescan rule).
- `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md` sections 6 and 8 (binding): section 8 names SIR Game Deals as its own small independent project and orders the split of `plans/sir-deals.md` into SIR Price Finder and SIR Game Deals.
- `D:/Projects/_SIR/ops/briefs/r52-product-premium-plan.md` (the exact structure to write).
- `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md` (the twenty sections every GLOBAL product adopts).
- `D:/Projects/_SIR/ops/SKILLS_INDEX.md` (385 skills) and the digests under `ops/encyclopedia/`.
- Every existing note about the idea: `plans/sir-deals.md` (r51, the games half plus the price finder half), `plans/PRODUCT_DIRECTION_2026-11-12.md` sections 5 and 8, `ops/TICKTICK_MAP.md` row 28 ("| 15, 16 | price and game-deal finder | concept (needs lawful data sources) |"), `ops/IDEAS_INBOX.md` (empty), `ops/briefs/r51-backlog-projects.md`, `ops/briefs/r52-product-premium-plan.md`, `ops/briefs/r54-plan-sir-game-deals.md` and `ops/briefs/r54-plan-sir-game-deals.prompt.txt`.
- Sibling rounds of the same day for consistency: `plans/sir-cars.md`, `plans/sir-life.md`, `plans/sir-movies.md`, `ops/competitors/sir-cars.md`, `ops/competitors/sir-life.md` and `ops/briefs/sir-cars-tasks.md`. The plan follows the structure of the sibling r54 rounds (cars, movies) so the family reads as one set.

Searched for any other mention of the idea:

```
$ grep -ril "game deal" plans/ ops/ --include="*.md"
plans/PRODUCT_DIRECTION_2026-11-12.md
plans/PROJECT_MERGE_RECORD.md
plans/sir-deals.md
plans/sir-laptop-manager.md
ops/briefs/r51-backlog-projects.md
ops/briefs/r54-plan-sir-game-deals.md
ops/HQ_CHECKPOINT.md
```

`plans/sir-laptop-manager.md` is an unrelated match (the word "game" in a gaming-laptop context), `plans/PROJECT_MERGE_RECORD.md` and `ops/HQ_CHECKPOINT.md` carry the backlog row only. No hidden note, no TickTick task with more detail, and `ops/IDEAS_INBOX.md` is empty.

---

## 3. The market research, with the real commands

The built-in web search tool answered `{"error":"Web search cancelled"}` for both queries, exactly as the worker manual warns. Research was therefore done with direct page fetches and with curl probes against public endpoints. Every page below was opened on 2026-11-12; every probe output is pasted verbatim.

### 3.1 The measurement the plan stands on

Steam's public store endpoint honours the country code. Same title, same moment, five country codes:

```
$ curl -s "https://store.steampowered.com/api/appdetails?appids=1245620&cc=$cc&l=english"
cc=EG : $39.99 USD
cc=SA : 249.00 SR
cc=AE : 249.00 AED
cc=US : $59.99
cc=TR : $39.99 USD
```

and a second title:

```
$ curl -s "https://store.steampowered.com/api/appdetails?appids=413150&cc=EG&l=english"
Stardew Valley $5.99 USD
```

**Finding: Steam has no Egyptian pound price.** It prices Saudi Arabia in riyals and the UAE in dirhams, and it leaves Egypt on a US dollar tier (the same tier as Turkey for these two titles). So an Egyptian player's real cost moves with the dollar rate, every price needs a rate and a date, and "the price in pounds" is the product rather than a formatting detail. This is now the opening fact of the plan, of the competitor study and of the free tier.

### 3.2 Other probes

```
$ curl -s "https://api.steampowered.com/ISteamApps/GetAppList/v2/?format=json"
v2 404
<html><head><title>Not Found</title></head><body><h1>Not Found</h1>Method 'GetAppList' not found in interface 'ISteamApps'</body></html>

$ curl -s -o /dev/null -w "%{http_code}" -A "Mozilla/5.0 ..." "https://steamdb.info/app/1245620/"
403

$ curl -s "https://www.cheapshark.com/api/2.0/deals?dealCount=1"
<!DOCTYPE html> ... <title>Not Found | CheapShark</title>

$ curl -s "https://www.freetogame.com/api/games?platform=pc"
[{"id":540,"title":"Overwatch","thumbnail":"https://www.freetogame.com/g/540/thumbnail.jpg", ...

$ curl -s -o /dev/null -w "%{http_code}" "https://store.epicgames.com/en-US/free-games"
403
$ curl -s -X POST "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?..." 
<HTML><HEAD><TITLE>Bad Request</TITLE>...</HEAD></HTML>
```

Reading: the old free Steam catalogue route is gone, so a keyed route is needed; SteamDB and GG.deals block automated access with a bot challenge (HTTP 403), which means a community price database is not a lawful feed for us to copy; the CheapShark API is documented but its route must be re-checked; the FreeToGame giveaway API answers a clean JSON list and is a candidate source; the Epic free games route is refused by the edge and needs the published terms and a working route before we depend on it.

### 3.3 The ten competitors

Egypt and the Arab market first, then global. Every row in `ops/competitors/sir-game-deals.md` carries its market, its strengths, its flaws, our edge, the idea to steal and a dated source.

| # | Competitor | Market | How it was read on 2026-11-12 |
|---|---|---|---|
| 1 | HalfLoot | Egypt | full page read at https://halfloot.com/ |
| 2 | PSprices | global, Arabic interface, no Egypt region | full page read at https://psprices.com/?lang=ar and https://psprices.com/pro/ |
| 3 | Games2Egypt | Egypt | full page read at https://www.games2egypt.com/offers |
| 4 | NileShopper | Egypt | full page read at https://nileshopper.com/ar/category/games |
| 5 | Games4Egypt | Egypt | search index only, tagged "(unsourced, verify)" |
| 6 | IsThereAnyDeal | global, has an EG region | full page read at https://isthereanydeal.com/ |
| 7 | GG.deals | global | bot challenge (403), described only from its own indexed URLs, tagged "(unsourced, verify)" |
| 8 | CheapShark | global | home and /api read, the API route itself answered 404 on 2026-11-12 |
| 9 | GamerPower | global | full page read at https://www.gamerpower.com/ |
| 10 | SteamDB | global | bot challenge (403), described only from its own indexed URLs, tagged "(unsourced, verify)" |

Second ring kept for the record: Kanbkam (Egypt), TechBites Store (Egypt), eogstore (Egypt), Microsoft Store Egypt, G2A / Kinguin / Eneba / CDKeys / K4G, GameBillet / Green Man Gaming / Fanatical / Zapagames / WinGameStore / Playsum / AllYouPlay / GamesPlanet / Fortuna Digital, Epic Games Store, FreeToGame, Humble Bundle, Game Pass, PS Plus, EA Play, Dealabs, Slickdeals and the Steam store itself.

Facts worth keeping from the pages that answered, all quoted in the competitor file with their dates:

- HalfLoot: 426 games tracked, 107 with a live discount, the strongest discount first, prices tracked through the day, payment by InstaPay or Telda or any mobile wallet with no card, PS Plus from 709 EGP, EA Play from 549 EGP, Ubisoft+ Classics from 599 EGP, a real human on WhatsApp, and it says it is a new brand with no track record.
- PSprices: 50,000+ games, 76 regions, hourly refresh, price history, a lowest-price collection, a free games collection, Telegram, email and browser alerts, PSN sync, Pro at $5 per month, $9 per quarter, $24 per year and $65 once, 400K+ active users, 11+ years online, and it shows the EGP reference price. Its region list has Bahrain, Kuwait, Qatar, Oman, Iraq and Lebanon, and **no Egypt**.
- Games2Egypt: 152 deals, 4.8 "Excellent" on Trustpilot from 245 reviews, instant digital codes, instalments, and a gift-card catalogue covering Steam, PlayStation, Xbox and Nintendo regions for USA, Europe, UAE, KSA, Bahrain, India, Indonesia, Kuwait, Oman, Qatar, Turkey and Lebanon, plus top-ups for PUBG, Fortnite, Roblox, Free Fire, Valorant, FIFA Points, Apex, League of Legends, Razer Gold, OBucks and Blizzard.
- NileShopper: 200+ products across Egyptian stores from 450 EGP, a price history and availability record per product, the explicit rule that any price not seen in the last two days is dropped, and the clear line that it compares and never sells.
- IsThereAnyDeal: "Country: EG Currency: USD" in its own footer, an EG selector in the header, waitlists, heat and collected counters, collections, subscription tracking for Game Pass and EA Play Pro, and the key shop list.
- GamerPower: 130.1K+ members, 2.7K+ giveaways, $28.7K saved, Steam, Epic, itch.io, GOG, Xbox, PlayStation, Nintendo, Android, iOS and DRM-free, an expires-soon list, an API, RSS and discount codes.

---

## 4. What the plan contains

`plans/sir-game-deals.md`, following the r52 structure and the sibling r54 rounds:

1. Vision and truth rule, with the statement that the product has never been built and that this round created no folder, repo, code or key.
2. Who it is for and the promise: "See every discount and every free game for the games you play, in pounds, before the offer ends."
3. The ten competitors and where we win, as a table plus the category truth.
4. Features: 20 parity rows with their source, the owner's own ideas with where each came from, what is explicitly out of scope, and section 3.4 on lawful data in four tiers (public endpoints we may call, partner and affiliate feeds, our own observations and user-owned data, and the never list).
5. Platform matrix: web, PWA, Windows, macOS, Linux, Android, iOS required; Wear OS, watchOS, TV, car and the browser extension skipped with a written reason; Telegram bot required at M3.
6. Architecture on the shared kit: the shape, `owner-auth`, the owner-only analytics page, AI with the fallback chain, the data model, data and money, hosting and delivery, and the security baseline.
7. Premium quality bar: spring motion, RTL first, five states, WCAG 2.2 AA, the teal token set, native app feel and the evidence list.
8. Free tier and fair pricing in EGP and USD.
9. M0 to M6 with exit checks that can be run or clicked.
10. The first ten tasks, the skills from the library, the risks with their defaults, the owner-only steps and the sources.

**Data model** (section 5.5, 19 collections with their key fields): `games`, `stores`, `offers`, `pricePoints`, `priceHistory`, `giveaways`, `giveawayClaims`, `watchlists`, `alerts`, `wishlistImports`, `notifications`, `storesEgypt`, `users`, `preferences`, `subscriptions`, `leads`, `ingestionRuns`, `fxRates`. Every price is an integer in the smallest currency unit, every converted number carries the rate and the observation time, `pricePoints` is append only, `priceHistory` is derived, and the lowest-ever flag is computed only from points we observed ourselves.

**Owner-only analytics page** (section 5.3): `/owner` behind a server-verified owner token, real metrics from aggregates only (signups, weekly active users, watchlist size, alerts created, delivered and failed, giveaway reminders sent and clicked, games tracked, price points stored, ingestion freshness per source, cheapest-known coverage, free to Pro conversion, MRR in EGP and in the visitor currency, AI cost, error rate, notification failure rate), a source health panel with a red badge when a source goes stale, a dash with a reason instead of a fake zero, and a subscription that grants the owner every Pro permission.

**Pricing** (section 7, test prices, not published prices): Free 0 (the whole feed, every history, the lowest-ever flag, the free game tracker, up to 5 watchlist items, up to 10 alerts, email alerts). Pro monthly 39 EGP (about 0.80 USD). Pro yearly 349 EGP (about 7.30 USD). The closest global comparable lists $5 per month and $24 per year on its own page, so our price sits below the category. Six fairness rules: browsing, history and free games are never behind a plan, the free tier keeps working, the original currency and the rate are always next to the price, no ads in any tier, no fake urgency, and the owner pays nothing.

**M0 to M6** (section 8): M0 the kit, the repo, the Firebase project, the Desktop folder kit, the verify script and the source ledger. M1 the price data core with the ingestion pipeline, the history engine and the lowest-ever calculation. M2 the browse experience with the five states. M3 the watchlist, the wishlist import, the alert engine and the Telegram bot link. M4 the free game tracker and the two mobile apps. M5 the owner console, the pricing page, the legal pack, the two hosts and the desktop shells. M6 the release, the AI layer and the store listings. M0 creates `D:\Projects\SIR Game Deals` with the `.sir` set, `AGENTS.md`, `folder.ico`, the repo `sirahmed8/sir-game-deals`, the Firebase project `sir-game-deals` and the Desktop folder kit with `Versions.txt` at 1.0.0, exactly as `OWNER_DEFAULTS.md` item 19 asks.

---

## 5. The ten tasks

`ops/briefs/sir-game-deals-tasks.md`, one title plus one paragraph each, with the queue order, the dependencies and the file ownership so two agents never fight over one file:

1. The M0 kit: project folder, `.sir` set, `AGENTS.md`, `folder.ico`, repo, Firebase project, Desktop folder kit, verify script.
2. The data source ledger and the source probes, with the terms status of every source.
3. The monorepo scaffold, the design tokens, the RTL shell and CI.
4. The product's own Firebase project and `owner-auth` with the three negative tests.
5. The data model, the Firestore rules and the emulator tests.
6. The scheduled ingestion pipeline, the price history engine and the lowest-ever calculation.
7. The deals feed, the game detail page with the history curve and the five states.
8. The watchlist, the Steam wishlist import, the alert engine and the Telegram bot link.
9. The free game tracker, the countdown and the claim reminder.
10. The owner analytics page with the source health panel, the pricing page, the legal pack and the two hosts.

The file also states what is deliberately not in these ten: the mobile apps, the desktop shells, the AI digest, the store partnerships, the launch package, the watch surfaces and any paid plan going live.

---

## 6. Quality checks and CI

Content rules checked on the three new files:

```
$ python -c "... count em dashes, en dashes and emoji ..."
== plans/sir-game-deals.md          lines 481 chars 49899 em-dash 0 en-dash 0 emoji 0
== ops/competitors/sir-game-deals.md lines 88 chars 22389 em-dash 0 en-dash 0 emoji 0
== ops/briefs/sir-game-deals-tasks.md lines 34 chars 15468 em-dash 0 en-dash 0 emoji 0
== .sir/r54-plan-sir-game-deals_CHECKLIST.md lines 20 chars 3016 em-dash 0 en-dash 0 emoji 0
```

No emoji, no em dash in copy, version stated as 1.0.0, no invented price, game, discount, countdown or user anywhere.

Commit and push (explicit paths only; the working tree carries other agents' unrelated edits, which were left untouched):

```
$ git add plans/sir-game-deals.md ops/competitors/sir-game-deals.md ops/briefs/sir-game-deals-tasks.md \
        .sir/r54-plan-sir-game-deals_CHECKLIST.md .sir/CHECKPOINT.md ops/bus/sir-hq.md
$ git commit -m "r54: SIR Game Deals premium plan (small independent GLOBAL product)"
b1c0274 r54: SIR Game Deals premium plan (small independent GLOBAL product)
$ git push origin main
To https://github.com/sirahmed8/sir-hq.git
   0ea0809..b1c0274  main -> main
```

CI on `main` for that commit, read from the run list and the run view:

```
$ gh run list --limit 4
completed	success	r54: SIR Game Deals premium plan (small independent GLOBAL product)	verify	main	push	43260621906	14s	2026-11-12T16:37:04Z
completed	success	r54: SIR Game Deals premium plan (small independent GLOBAL product)	test	main	push	43260621009	11s	2026-11-12T16:37:03Z

$ gh run view 43260621906
✓ secrets in 11s (ID 131330581448)
✓ python-verify in 7s (ID 131330582015)
```

Both runs are green and were seen green. Note for HQ: the flag file `ops/ci-quota-exhausted.flag` exists on disk, but the Actions minutes are working again (the runs executed every step and passed), so that flag is stale and can be deleted. The same thing happened once before on 2026-11-12 and the file was deleted then.

---

## 7. What is unsure, and what is open

1. **Games4Egypt, Kanbkam, TechBites Store and eogstore were seen only through the DuckDuckGo index** (their pages were not opened), so every claim about them in the competitor file is tagged "(unsourced, verify)". Task 2 opens them properly.
2. **GG.deals and SteamDB could not be read** (bot challenge, HTTP 403), so their rows describe only their own indexed URLs and titles, tagged "(unsourced, verify)". They are not used as a data source anywhere.
3. **The CheapShark API route answered a 404 page today** even though its API page exists. The route must be re-checked before we depend on it; task 2 does that.
4. **The Epic free games route was refused twice** (403 on the storefront page, a bad request at the Akamai edge). The documented public route and its terms must be found before we use it.
5. **Every price in this report is a proposal.** The EGP to USD rate of 48 is "(unsourced, verify)", the Pro prices are test prices, and the paid plan cannot go live before the Paymob and Fawry fee schedules, the tax treatment, the refund wording and the lawyer review are done.
6. **The Steam country probe covers two titles only.** Before the plan is quoted as fact, someone should confirm the pattern on a wider sample and record the date. Task 2 adds the repeatable probe script.
7. **The plan is a plan, not a product.** Nothing exists yet: no folder, no repo, no Firebase project, no code, no key, no deployment, and no screen was seen.

---

## 8. What I recommend next

1. Queue T1 to T10 from `ops/briefs/sir-game-deals-tasks.md`, T1 first and T2 beside T3. T1 creates the folder, the repo, the Firebase project and the Desktop kit, so nothing else can start before it.
2. Let T2 settle the lawful data question before any UI work starts on prices. If the Steam and Epic routes do not clear their terms, the plan's Tier C (our own observations plus user-reported Egyptian prices with moderation) becomes the main engine and the schedule has to grow by a milestone.
3. Split the TickTick row "| 15, 16 | price and game-deal finder | concept (needs lawful data sources) |" into two rows, SIR Price Finder and SIR Game Deals, and give the Game Deals row a parent task, because it is now its own project with its own folder, kit and plan.
4. Delete the stale `ops/ci-quota-exhausted.flag` so the owner page stops showing a false quota banner and the verifier judges CI normally again.

---

## 9. Files changed in this round

```
plans/sir-game-deals.md                      (new, 481 lines)
ops/competitors/sir-game-deals.md            (new, 88 lines)
ops/briefs/sir-game-deals-tasks.md           (new, 34 lines)
.sir/r54-plan-sir-game-deals_CHECKLIST.md    (new, 20 lines)
.sir/CHECKPOINT.md                           (worker note appended)
ops/bus/sir-hq.md                            (one line appended)
```

Commit `b1c0274`, pushed to `sirahmed8/sir-hq` `main`. CI runs `43260621906` (verify) and `43260621009` (test) are green.
