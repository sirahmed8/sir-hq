# Competitors: SIR ModPack

Research round r52, 2026-11-12. Every price, number and feature claim carries a source link and the date it was read, or is marked **(unsourced, verify)**. Nothing flagged here may be copied into public copy, store listings, legal pages or comparison pages until it is sourced.

Product: a curated Minecraft modpack plus the desktop launcher that installs and runs it, plus a small server manager, plus the website. Category: modpack distribution, Minecraft launchers, modded server hosting.

**Sourcing method used today.** Official product and pricing pages were fetched directly (`curseforge.com/minecraft`, `curseforge.com/premium`, `curseforge.com/minecraft/modpacks`, `modrinth.com`, `modrinth.com/plus`, `modrinth.com/hosting`, `modrinth.com/app`, `prismlauncher.org`, `atlauncher.com`, `gdlauncher.com`, `feed-the-beast.com`, `feed-the-beast.com/ftb-app`, `aternos.org`, `lunarclient.com`, `lunarclient.com/features`, `bisecthosting.com/minecraft-hosting`, `minecraft.net/en-us/usage-guidelines`). Licence and star counts come from the GitHub REST API, not from aggregator blogs. CurseForge and Badlion sit behind a Cloudflare challenge and were read through the text proxy; the numbers below were read on the page itself.

---

## 1. CurseForge (Overwolf) - the catalogue everyone uses

- **What it is:** the largest mod and modpack catalogue for Minecraft, with a desktop client. 344,660 Minecraft projects and 10,000+ modpacks listed (curseforge.com/minecraft, checked 2026-11-12).
- **Licence:** proprietary platform. Mods on it carry their own licences.
- **Pricing (sourced, curseforge.com/premium, checked 2026-11-12):** Premium $2.99/month monthly, or $2.50/month billed annually at $30.00/year (16% off). Premium gives ad-free browsing, instant downloads, custom themes and new app layouts. 70% of a subscription goes to mod authors.
- **Strengths:** the library everyone already knows; the desktop app exists and updates itself; version and dependency metadata is deep; author revenue share is real and published.
- **Flaws:** ads on the free tier and the Overwolf client is a second process that users complain about; no curated pack for a specific laptop; no server manager; a first-time user faces a wall of 344,660 projects with no guidance; no Arabic-first experience.
- **Our edge:** one curated pack that runs on a specific laptop class, installed in one click with every file hash checked, plus the plain-language crash explanation in Arabic and English that no catalogue provides.

## 2. Modrinth - the open-source benchmark

- **What it is:** an open-source Minecraft content platform and the Modrinth App launcher. The site advertises "over 100,000 creations" (modrinth.com, checked 2026-11-12). Backend `labrinth` is AGPL-3.0, the frontend `knossos` and `omorphia` are AGPL-3.0, the monorepo `modrinth/code` is 2,524 stars with licence NOASSERTION (GitHub API, 2026-11-12).
- **Pricing (sourced, modrinth.com/plus and modrinth.com/hosting, checked 2026-11-12):** Modrinth Plus $4.99/month or 16% off annual. Hosting: Small $10/month billed quarterly (4 GB RAM, 32 GB storage, 2 shared CPUs, bursts to 4), Medium $15/month quarterly (6 GB, 48 GB, 3 CPUs, bursts to 6), Large $20/month quarterly (8 GB, 64 GB, 4 CPUs, bursts to 8), customised plans "starting at $5/month". Prices are in USD only.
- **Strengths:** open source, no ads on the platform for supporters, a real API that other launchers build on, a launcher that stays current with the platform, server hosting bundled with one-click modpack install, 15 off-site backups per server.
- **Flaws:** the Linux build of the App is officially "known to have issues" on some systems and the site points those users to Prism Launcher (modrinth.com/app, checked 2026-11-12); no curated performance pack for a specific laptop; the crash problem is not solved in words a normal player understands; USD-only pricing for an Egyptian player; no Arabic-first experience.
- **Our edge:** we are not a catalogue, we are one pack with the laptop tuning done once and the crash answer written in the player's own language.

## 3. Prism Launcher - the reference desktop launcher

- **What it is:** a fork of MultiMC, C++ and Qt, GPL-3.0, 11,107 stars (GitHub API, 2026-11-12). prismlauncher.org describes itself as "an open-source Minecraft launcher with the ability to manage multiple instances, accounts and mods. Focused on user freedom and free redistributability."
- **Pricing:** free, no paid tier. All money comes from donations (prismlauncher.org, checked 2026-11-12).
- **Strengths:** reliable multi-instance management, free and redistributable, real account handling, widely recommended; Modrinth points users here when its own Linux App is unstable.
- **Flaws:** the interface assumes you already know what a loader, a profile and a JVM argument are; there is no curated pack; there is no crash explanation; no server manager; no Arabic-first experience.
- **Our edge:** we keep Prism's correctness (isolated instances, clean account handling) and add the curated pack, the tuning, the Arabic guide and the crash answer. **Prism is GPL-3.0: its code must not be copied into a proprietary launcher.** Use it as a separate unmodified tool or not at all.

## 4. ATLauncher - the old catalogue launcher

- **What it is:** a Java launcher for Minecraft that integrates many modpacks, GPL-3.0, 862 stars (GitHub API, 2026-11-12). atlauncher.com confirms the pack catalogue and the server browser on its own pages (checked 2026-11-12).
- **Pricing:** free, donation-supported (atlauncher.com, checked 2026-11-12).
- **Strengths:** a long-lived catalogue of packs, one-click install of an existing pack, a built-in server list.
- **Flaws:** the interface looks like a 2012 Java Swing app; file hash verification is slow; no modern motion or layout discipline; no plain-language crash help; the pack catalogue is a firehose with no curation.
- **Our edge:** the same one-click install without the dated look, plus the tuning and the crash answer.

## 5. MultiMC - the upstream that forked into Prism

- **What it is:** C++, 4,697 stars, licence reported as NOASSERTION by the GitHub API (checked 2026-11-12). Its own README states it "focuses on predictability, long term stability and simplicity".
- **Pricing:** free.
- **Strengths:** the instance model that the whole launcher category copies; predictable and stable.
- **Flaws:** the original project is not the one people install today, so its advantages are inherited through Prism rather than developed; no curation, no crash help, no Arabic.
- **Our edge:** we build the curation, the guide and the crash answer, and we take the instance model as a known-good design rather than reinventing it.

## 6. HMCL (Hello Minecraft! Launcher) - the feature-heavy Java one

- **What it is:** a Java launcher, GPL-3.0, 10,960 stars (GitHub API, 2026-11-12). Its README lists mod management, game customising, auto-installing Forge, LiteLoader and OptiFine, modpack creating and UI customising.
- **Pricing:** free.
- **Strengths:** very broad feature coverage, deep auto-install, a large community, a genuine modpack creator.
- **Flaws:** the breadth makes the interface dense for a first-time player; it asks the user to know the loader ecosystem; no curated performance pack for a laptop; no Arabic-first experience; a Java app starts slower than a native one.
- **Our edge:** the same coverage without the density: one pack, one decision screen, and the rest explained when it matters.

## 7. PojavLauncher - the Android route to Java Minecraft

- **What it is:** a Java launcher for running Minecraft Java Edition on Android, LGPL-3.0, 9,517 stars, **archived by its owners** (GitHub API, 2026-11-12).
- **Pricing:** free.
- **Strengths:** proved that Java Minecraft can be run on a phone; solved the touch-control problem.
- **Flaws:** archived, so no security or version support; touch controls are a compromise; no curated pack for a desktop-class laptop; no crash help.
- **Our edge:** an Android companion that **remotely controls and monitors the PC launcher**, which is a different job from running the game on the phone. Our phone never pretends to be a laptop.

## 8. GDLauncher - the Android catalogue app

- **What it is:** an Android launcher that installs CurseForge and Modrinth content, manages Java and dependencies automatically, offers parallel downloads and shares an instance with a friend through a code (gdlauncher.com, checked 2026-11-12).
- **Pricing:** "Free, with no overlay or premium tier" (its own words on gdlauncher.com, checked 2026-11-12).
- **Strengths:** one-click install from both catalogues, automatic dependency handling, cloud instance sharing by code, free with no premium upsell.
- **Flaws:** phone-only, so no server manager and no laptop tuning; the shared-instance code is a sharing feature, not a tuned pack; no Arabic-first experience; it depends on the two catalogues staying up.
- **Our edge:** the instance-sharing idea is worth copying (a friend can join your exact setup with one code), and our phone app adds the remote control of the PC and the server, which no phone launcher has.

## 9. Feed The Beast (FTB) - the curated-pack brand that proved the model

- **What it is:** a curated modpack house with its own desktop app (feed-the-beast.com/ftb-app, checked 2026-11-12). The app installs and manages FTB packs and can also install CurseForge packs, and it supports NeoForge, Fabric and Forge. It also runs FTB Worlds for playing with friends in minutes and points to BisectHosting for server offers.
- **Pricing:** the packs and the app are presented as free to install (feed-the-beast.com, checked 2026-11-12); the money is in hosting partnerships and the store (feed-the-beast.com, checked 2026-11-12).
- **Strengths:** curation is the whole product, so the brand carries trust; the app is real and works; the hosting partner is already wired in; FTB packs are popular.
- **Flaws:** the curation is content-led, so there is no engineering story about frame time or memory; the tuning for a specific laptop class is not the point; the crash experience is not a feature; the site is English-first.
- **Our edge:** **this is the closest business model to ours and the most useful one to copy**: one house, one curated experience, the app as the delivery mechanism. We add what FTB leaves out: measurable performance engineering, a server manager that runs on the player's own machine, and Arabic-first support.

## 10. Lunar Client - the performance-first client that sets the FPS bar

- **What it is:** a free client that installs and updates its own mods. Its features page claims "over 65 customizable mods and hundreds of settings" and performance work that "often doubling your frame rate" on low-end PCs (lunarclient.com/features, checked 2026-11-12). The site showed 263,200 players online (lunarclient.com, checked 2026-11-12).
- **Pricing:** the client is free; the Lunar+ store sells cosmetics, emotes and a subscription (store.lunarclient.com, checked 2026-11-12). Exact subscription prices were not readable from the store page in this round: **(unsourced, verify)**.
- **Strengths:** the frame-rate promise is the headline and the community believes it; single install, no mod hunting; free client with paid cosmetics; updates with each Minecraft release.
- **Flaws:** it is a fixed client, not a configurable pack: the user cannot choose the loader, the mods or the server; no server manager; the FPS claim is marketing, not a benchmark you can reproduce; English-first; it does not support a server the player owns.
- **Our edge:** **our FPS promise must be a reproducible benchmark on named hardware, never a marketing number** (the legacy README's "144+ FPS" is exactly the failure mode to avoid). And we do the opposite of Lunar: the pack is open, the mods are listed with licences, the player can change them, and the server is theirs.

---

## Second ring, read for context, not for the top ten

- **Aternos (free hosting).** "Free. Forever." with no possibility to pay for anything, hosting since 2013, and it shows 142,800,357 users, 1 million players every day, 219,013 GB of RAM and 79,705 players online (aternos.org, checked 2026-11-12). Strength: free servers with mods and plugins. Flaw: no performance tuning, no Arabic-first experience, and the free queue is the product. Our edge: a **local** server manager (the player's own machine, no queue, no waiting) is the honest answer for the same need.
- **BisectHosting.** Minecraft hosting sold per GB with monthly, quarterly, semi-annual and annual billing, 21 locations, one-click install from over 2,300 modpacks, a 3-slot instance manager and free DDoS protection (bisecthosting.com/minecraft-hosting, checked 2026-11-12). Exact per-GB prices did not render in the text fetch: **(unsourced, verify)**. Strength: proven hosting with backups and a plugin library. Flaw: it rents someone else's machine, so the player never owns the server; English-only support pages.
- **Fabulously Optimized.** A community performance modpack, BSD-3-Clause, 1,188 stars (GitHub API, 2026-11-12), with 8.1M downloads on CurseForge and a 26.2 Fabric build (curseforge.com/minecraft/modpacks, checked 2026-11-12). Strength: free, open, popular, well-tuned. Flaw: it is a pack with no launcher, no server manager, no crash help and no Arabic guide. Our edge: we are compatible with it and can recommend it, we do not fight it.
- **Badlion, Comet, and other PvP clients.** Not read in this round beyond confirming Badlion is behind a Cloudflare challenge. Treated as **(unsourced, verify)**.
- **The Mojang and Microsoft rules themselves.** These are not a competitor but they decide what may be sold. Read today from minecraft.net/en-us/usage-guidelines (published 2025-10-15). Money may be made by charging for access to a server when the cost is the same for everyone, everyone who pays gets access to all the mods the server owner enabled, the owner owns and controls the server for the whole time they charge, and the entitlements do not ruin other players' experience or give a competitive advantage. Cosmetics may be sold except anything that acts like a player cape. Events are limited to roughly 150 participants. Commercial companies may not use Minecraft gameplay to market unrelated products without written approval from Mojang or Microsoft. **Every price in our plan is written against these rules.**

---

## What we copy, what we do better

| Competitor | What we copy | What we do better |
|---|---|---|
| CurseForge | The one-click install and the deep version metadata | No ads, no second background process, a curated pack instead of a 344,660-item wall, Arabic-first |
| Modrinth | The open API mindset and the "everything is updatable" promise | A pack tuned for a named laptop class, a crash answer in plain Arabic and English, EGP pricing for an Egyptian player |
| Prism Launcher | The isolated instance model and free-redistributable discipline | Plain-language setup, one decision screen, no JVM jargon, no loader knowledge required |
| ATLauncher | One-click install of a named pack | A modern interface, fast hash verification, a server manager |
| MultiMC | Predictable multi-instance behaviour | The same stability with the curation on top |
| HMCL | Depth of auto-install and mod management | Density removed: one path for a first-time player |
| PojavLauncher | The proof that phones matter to this audience | The phone controls the PC instead of imitating it |
| GDLauncher | Instance sharing by code, no premium upsell | The shared code carries a tuned pack and a server, and the phone becomes a remote |
| Feed The Beast | The curated-house business model | Engineering proof of the performance claim, a server that runs on the player's own machine, Arabic-first |
| Lunar Client | Making frame rate the headline promise | A reproducible benchmark on named hardware instead of a marketing number, an open and configurable pack, the player owns the server |

---

## Open sourcing tasks (each under 2 hours, none blocking the plan)

1. Read the whole Minecraft Usage Guidelines page and record the section titles and the decisions they force into `docs/MOJANG_RULES.md` with the URL and the read date. Partially done today (the commercial-use section was read on 2026-11-12); the events and promotions sections are still unread.
2. Read the CurseForge and Modrinth modpack-author terms and record what each platform allows a pack author to redistribute, with links.
3. Read the Modrinth API terms of use and record what a third-party launcher may and may not cache.
4. Find the current Lunar+ subscription price and the current Badlion price with links.
5. Get the BisectHosting per-GB prices for a Minecraft server in the nearest region, with a link and a date.
6. Find five public player complaints about the crash-log experience in modded launchers, with links (the previous file had unsourced quotes; they must not return).
7. Read the Prism Launcher and MultiMC licences in full and write down, in one paragraph, exactly why no line of their code may be copied into a proprietary launcher.
