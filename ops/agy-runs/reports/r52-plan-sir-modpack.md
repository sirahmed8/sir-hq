# Report: r52-plan-sir-modpack

Round r52, 2026-11-12. Task: rewrite `plans/sir-modpack.md` as a premium complete plan, create `ops/competitors/sir-modpack.md` (10 competitors with sources), create `ops/briefs/sir-modpack-tasks.md` (first 10 queue-ready tasks), commit explicit paths to `main`, and append one line to `ops/bus/sir-hq.md`.

---

## 1. What I read (and what I did not)

**Read in full:**
- `D:/Projects/AGENTS.md` (workspace laws), `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/standard/OWNER_DEFAULTS.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`, `D:/Projects/_SIR/ops/LESSONS.md` (380 lines, all 51 lessons plus the r43 competitor-research rule), `D:/Projects/_SIR/plans/MAIN_PLAN.md`, `D:/Projects/_SIR/plans/PROJECT_MERGE_RECORD.md`, `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md` (all 20 sections + adoption rules), `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md`, `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`, `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, `D:/Projects/_SIR/ops/SKILLS_INDEX.md` (the rows for the 47 skills I reference), `D:/Projects/_SIR/ops/TICKTICK_MAP.md`, `D:/Projects/_SIR/ops/IDEAS_INBOX.md`, `D:/Projects/_SIR/ops/inventory/SIR-ModPack-and-GTA-V-mods.md`.
- Product folder `D:/Projects/SIR ModPack`: `AGENTS.md`, `.sir/PLAN.md`, `.sir/MASTER_PLAN.md`, `.sir/CHECKPOINT.md`, `.sir/PLATFORMS.md`, `legacy/README.md`, and the legacy source `legacy/SIR ModPack (v1)`: `PROJECT.md`, `README.md`, `development/launcher_core/` (37 services), `development/installer_core/installer_bridge.py`, `development/launcher_ui/js/` (26 modules), `development/server_ui/`, `development/installer_ui/`, `website-next/` (32 routes, `package.json`, `lib/`, `components/`), `mods/` (185 jars), `instances/` (10 folders), `shaderpacks/`, `resourcepacks/`.
- Previous plan `plans/sir-modpack.md` (88 lines, r44-era) and the old competitor file `plans/competitors/sir-modpack.md` (38 lines, carrying a 2026-11-10 audit banner saying every claim in it was unsourced).
- `ops/bus/sir-hq.md` (tail), `ops/agy-runs/reports/r52-plan-sir-content-creation-studio.md` (format reference), `ops/briefs/sir-hagoozat-tasks.md` (format reference), `plans/sir-hagoozat.md` (format reference for the 13-section plan).

**Never opened:** `D:/Projects/AHome` (rule, and the brief says so explicitly). No private data was read or written anywhere.

---

## 2. Findings about the product

**State: nothing has been built.** `D:/Projects/SIR ModPack` holds the kit files (`.sir/` with 18 files), the Desktop folder kit and one legacy project, and nothing that runs. The `.sir/CHECKPOINT.md` is still the HQ setup note from 2026-10-30 saying "Ready for the first project chat".

**Repos, verified today with `gh`:**
- `sirahmed8/sir-modpack-source`: PRIVATE, default branch `main`, last update 2026-11-09 18:37 UTC. This is the only remote of the product folder (`git remote -v`).
- `sirahmed8/SIR-ModPack`: **still PUBLIC**, last update 2026-10-30. This is the legacy public repo. It goes private or archived at M6 in the plan, with that as an M6 exit check.

**Firebase:** the Firebase CLI is **not on the PATH** on this machine (`where.exe firebase` found nothing, `firebase --version` returned "command not found"). So the product's own Firebase project `sir-modpack` does not exist and cannot be created by this round. It is M0 work for the agents (T3 in the task file), and creating it needs the CLI installed.

**Legacy facts counted today (not taken from the legacy's own claims):**
- `development/launcher_core/*.py` excluding `__init__.py`: **37 service modules**.
- `website-next/app`: **32 `page.tsx` files** and 32 route folders. The legacy `PROJECT.md` claims "38 static routes" and "Next.js 16.3 App Router (38 static routes)" - that claim is **wrong by six**, and the plan and the T1 brief now say 32 and instruct the parity matrix to record the gap.
- `mods/*.jar`: **185** jars. Present and confirmed on disk: `sodium-fabric-0.9.1-mc26.2.jar`, `lithium-fabric-0.25.3+mc26.2.jar`, `ferritecore-9.0.0-fabric.jar`, `iris-fabric-1.11.2+mc26.2.jar`, `modernfix-5.27.19-build.1.jar`, `entityculling-fabric-1.10.5-mc26.2.jar`.
- `instances/`: 10 folders, of which **6 are real tiers** (`26.2-ultra`, `26.2-balanced`, `26.2-performance`, `1.8.9-ultra`, `1.8.9-balanced`, `1.8.9-performance`) plus a base `26.2` folder and three working folders (`logs`, `skins`, `state`).
- `development/launcher_ui/js/`: 26 modules including `crash` diagnostics in `diagnostics.js`, `hardware.js`, `gallery.js`, `skins.js`, `worlds.js`, `shaders.js`, `command_palette.js`, `i18n.js`, `theme.js`, `downloads_manager.js`, `onboarding.js`.

**Legacy code I read and used as source for the plan (not guessed):**
- `crash_analyzer_service.py` docstring: diagnoses "Mixin conflicts, Java version mismatches, OutOfMemory spectrum (Heap, Direct, Metaspace, GC Overhead, Native Thread), native crash logs (hs_err_pid*.log), mod dependency conflicts, corrupted region files, and shader compilation failures". The plan's feature table and the T7 brief list exactly these.
- `java_service.py`: `get_pe_binary_arch(exe_path)` reads the Windows PE header for the architecture, probes HKLM and HKCU, scans the filesystem and parses semver. T6 ports this.
- `controls_service.py`: holds `GLFW_TO_LWJGL2`, the bidirectional GLFW-token to LWJGL2-scancode table, and states it supports "Modern GLFW Token Strings (Minecraft 1.21+ / 26.2) and Legacy LWJGL 2 Scancodes (1.8.9)". T6 ports this as the keycode invariant.
- `native_runner.py` `_sanitize_launch_environment`: forces `fullscreen:false`, `exclusiveFullscreen:false` and `overrideWidth:0` to "eliminate DWM/GPU stalls, exclusive fullscreen lockouts, and black screen freezes on launch and exit". T6 ports this as the second invariant.
- `video_preset_service.py`: exactly **three layers** (vanilla `options.txt`; Sodium/Embeddium `sodium-options.json`; Iris/Oculus/OptiFine `iris.properties` and `optionsshaders.txt`) and **five tiers**: Ultra, Balanced, Performance, Competitive, Potato, for Modern (26.2 / 1.21.x) and Legacy (1.8.9). The plan row was corrected to say three named layers and five tiers (my first draft said "the third layer", which was sloppy).
- `installer_bridge.py` uses `creationflags=0x08000000` (CREATE_NO_WINDOW) for the Java probe. The plan cites the file rather than only the old `.sir/MASTER_PLAN.md` line.
- `auth_service.py` and `loopback_service.py` state the rule the plan now formalises: "SIR stores only display metadata. Prism owns Microsoft OAuth/Xbox/Minecraft tokens in its own local account file" and the bridge "is intentionally loopback-only". The plan's two-identity rule (SIR email account vs Microsoft device-code account) comes from here.
- `auto_remapper_service.py`: "5-Pass ASM & Namespace Auto-Remapping Engine ... Performs header rewriting, nested jar-in-jar patching, **Mojang signature stripping**, and class remapping." This is **dropped for good**, with the reason written into the plan and into the T1 brief so a later agent does not "restore" it.
- `repair_service.py`: parallel SHA-256 hashing, ZIP CRC validation and quarantine. T5 ports the quarantine behaviour.
- `syncer_service.py` (differential repair), `clone_service.py` (isolated instances), `worlds_service.py` (world saves, thumbnails, backups), `rcon_service.py`, `satellite_service.py` (TCP latency), `controlify_compat.py`, `discord_service.py`, `gallery_service.py`, `screenshot_tools_service.py`, `skin_studio_service.py`, `telemetry_governor_service.py` (Windows memory and commit-charge governor), `hardware_monitor_service.py`, `native_runner.py` (resolves JVM arguments and classpaths from the Mojang, Fabric and Prism manifests, evaluates the Mojang OS rules, extracts LWJGL 2 and 3 natives with file-lock recovery).

**The old plan (88 lines) and what I kept.** It was already legally careful and I kept its hard rules: never redistribute the game files, never rewrite the game JAR, SHA-256 on every download, the device-code flow with the token in the Credential Manager, the server bound to localhost unless the player opens a port, the owner-only analytics page, dual hosting, the `(unsourced, verify)` discipline and the "no paywall on any gameplay item" money rule. What it lacked: the 13-section structure, the platform matrix in the new all-platform form, the EGP/USD pricing table, M0 to M6 with acceptance tests, the competitor matrix with real sources, and the ten ready-to-queue tasks. It also still said "web hub on Cloudflare Pages" in one place while the standing rule is Firebase Hosting plus Vercel; the new plan uses Firebase Hosting plus Vercel and keeps Cloudflare out.

---

## 3. Competitor research (sources opened today, 2026-11-12)

Method: official pages fetched directly with `curl` and `webfetch`; where a Cloudflare challenge blocked the plain fetch (CurseForge, Badlion) I read the page through the text proxy, which returned the page content itself, so the numbers below are from the page, not from a snippet. Licence and star counts came from the **GitHub REST API**, never from an aggregator blog.

| Source fetched | What it gave |
|---|---|
| `curseforge.com/minecraft` | 344,660 Minecraft projects; 10,000+ modpacks; the top packs with their download counts (ATM10 23.0M, RLCraft 30.5M, Better MC 19.0M, Fabulously Optimized 8.1M) |
| `curseforge.com/minecraft/modpacks` | The 26.2 / 26.3 / 1.21.x loader filter and the "10,000+ Projects" figure for the modpack category |
| `curseforge.com/premium` | Premium $2.99/month monthly, or $2.50/month billed annually at $30.00/year (16% off); 70% of a subscription goes to mod authors; over $18 million paid to creators since 2020 |
| `modrinth.com` | "over 100,000 creations"; the "NOT AN OFFICIAL MINECRAFT SERVICE" notice; the open-source statement and the link to `github.com/modrinth/code` |
| `modrinth.com/plus` | Modrinth Plus $4.99/month, 16% off annual; ad-free; 50% of the subscription to creators |
| `modrinth.com/hosting` | Small $10/month billed quarterly (4 GB RAM, 32 GB storage, 2 shared CPUs, bursts to 4); Medium $15/month (6 GB, 48 GB, 3 CPUs, bursts to 6); Large $20/month (8 GB, 64 GB, 4 CPUs, bursts to 8); customised from $5/month; 15 off-site backups; AMD Ryzen 7950X/9950X with DDR5; DDoS up to 17 Tbps; **prices are USD only** |
| `modrinth.com/app` | The App is open source; **the Linux build is officially "known to have issues"** and the site points those users to Prism Launcher; Windows and Linux downloads, beta |
| `prismlauncher.org` | "an open-source Minecraft launcher with the ability to manage multiple instances, accounts and mods. Focused on user freedom and free redistributability"; "Not affiliated with Mojang or Microsoft" |
| `atlauncher.com` | The pack catalogue and the server browser; Algolia-backed pack search over `prod_packs` |
| `gdlauncher.com` | "Install Minecraft mods and modpacks with one click from CurseForge and Modrinth"; "manages Java, dependencies, and updates automatically"; "Free, with no overlay or premium tier"; instance sharing with a friend through a code; parallel downloads; all major loaders |
| `feed-the-beast.com` and `/ftb-app` | The curated-house model; the FTB App installs FTB packs **and** CurseForge packs; supports NeoForge, Fabric and Forge; FTB Worlds for playing with friends in minutes; BisectHosting as the server partner |
| `aternos.org` | "Free. Forever." with "no possibility to pay for anything"; hosting since 2013; the site's own counters: 142,800,357 users, 1 million players every day, 219,013 GB RAM, 79,705 players online |
| `lunarclient.com` and `/features` | "over 65 customizable mods and hundreds of settings"; the frame-rate claim "often doubling your frame rate"; single install and auto-updates; 263,200 online on the homepage; Lunar+ store for cosmetics |
| `bisecthosting.com/minecraft-hosting` | Hosting sold per GB with monthly, quarterly, semi-annual and annual billing; 21 locations; one-click install from over 2,300 modpacks; a 3-slot instance manager; free DDoS protection; NVMe; "based on 25,000+ reviews" |
| `minecraft.net/en-us/usage-guidelines` | Read in full for the commercial-use section (published 2025-10-15). Money may be made by charging for access to a server **when** the cost is the same for everyone, everyone who pays gets access to all the mods the server owner enabled, the owner owns and controls the server the whole time they charge, and the entitlements do not ruin other players' experience or give a competitive advantage; donations are fine if the donor gets nothing only they can use, with server-wide rewards allowed when a goal is met; cosmetics may be sold **except** anything acting like a player cape; virtual currencies must have no real-world value; events limited to roughly 150 participants; commercial companies may not use Minecraft gameplay to market unrelated products without written approval |

GitHub API (2026-11-12): `PrismLauncher/PrismLauncher` GPL-3.0, 11,107 stars, C++ · `HMCL-dev/HMCL` GPL-3.0, 10,960 stars, Java · `PojavLauncherTeam/PojavLauncher` LGPL-3.0, 9,517 stars, Java, **archived** · `CaffeineMC/sodium` NOASSERTION, 5,851 stars · `GeyserMC/Geyser` MIT, 5,964 stars · `MultiMC/Launcher` NOASSERTION, 4,697 stars, C++ · `IrisShaders/Iris` LGPL-3.0, 3,894 stars · `modrinth/code` NOASSERTION, 2,524 stars, Rust · `CaffeineMC/lithium` LGPL-3.0, 2,194 stars · `malte0811/FerriteCore` MIT, 416 stars · `Fabulously-Optimized/fabulously-optimized` BSD-3-Clause, 1,188 stars · `ATLauncher/ATLauncher` GPL-3.0, 862 stars, Java · `MinecraftForge/ForgeGradle` LGPL-2.1, 573 stars.

**Honest gaps in the research, marked in the file as (unsourced, verify):** the Lunar+ subscription price and the Badlion price (Badlion sits behind a Cloudflare challenge and returned 403 through the proxy); the exact BisectHosting per-GB prices (the pricing table renders client-side and did not come through the text fetch); the Modrinth API terms of use; the CurseForge and Modrinth modpack-author redistribution terms; five public player complaints about crash-log experiences, with links, so the old file's unsourced quotes cannot come back.

**Currency rate used:** 53.55 EGP per 1 USD, read from `open.er-api.com/v6/latest/USD` on 2026-11-12, and the plan says the pricing page recomputes it from the live rate. The 49 EGP / 490 EGP supporter prices and the 149 / 1,490 team prices are **test prices** pending the official gateway fee schedule and the lawyer review, and the plan says so.

---

## 4. Files written

1. **`D:/Projects/_SIR/plans/sir-modpack.md`** (458 lines, new) - full rewrite into the 13-section house structure: who it is for and the promise; the ten competitors and where we win; features split into parity (18 rows), the owner's own ideas carried from legacy and TickTick (21 rows, each with its source file) and four explicitly dropped legacy items with reasons; the platform matrix for web, PWA, Windows, macOS, Linux, Android, iOS, Wear OS, watchOS, TV, car, widgets, browser extension and Docker, with Wear/watch/TV/car skipped with written reasons; the architecture on the shared kit (shape, `owner-auth` with the two-identity rule, owner-only analytics page, AI with the fallback chain, data and money, hosting and delivery, security baseline); the premium quality bar; free tier and pricing in EGP and USD with the Mojang rule that decides the shape; M0 to M6 with runnable exit checks; the ten task titles; the skills from the library with real digest paths; risks and defaults; owner-only actions; sources.

2. **`D:/Projects/_SIR/ops/competitors/sir-modpack.md`** (130 lines, new) - the ten competitors with what it is, licence, pricing with the source and date, three strengths, three flaws and our edge, then the second ring (Aternos, BisectHosting, Fabulously Optimized, Badlion/Comet, and the Mojang rules themselves as the rule-setter), a copy table, and seven open sourcing tasks with a time box each. The file states its own sourcing method.

3. **`D:/Projects/_SIR/ops/briefs/sir-modpack-tasks.md`** (58 lines, new) - T1 to T10, each with a title, a one-paragraph brief, an exit check that can be run, a report line, the queue order with dependencies, and the file each task owns so two agents never fight over one file.

---

## 5. Decisions worth the manager's attention

- **The supporter tier is cosmetic and the server is not rented in v1.** The Mojang rules read today allow charging for server access under four conditions, but they forbid commercial use that exploits the brand and they do not clearly cover a launcher that rents someone else's server. So v1 sells a supporter tier (49 EGP/month or 490 EGP/year) with a name on the supporters page, an early build channel, a badge and a higher AI quota, and no gameplay perk at all. The local server manager on the player's own machine is free. This keeps the product on the safe side of the brand rules and keeps the Mojang rule about competitive advantage impossible to break.
- **The ASM remapper is dropped for good.** The legacy `auto_remapper_service.py` rewrites third-party mod JARs and strips the Mojang signature. That is a legal and malware risk, so it is dropped in the plan and the T1 brief tells the parity agent to write the reason down, so a later agent cannot restore it as "a missing feature".
- **One Rust core for the three desktop platforms, not Electron and not Python.** The legacy was Python and pywebview with PyInstaller; the plan calls for Tauri v2 with the engine work in Rust, confirmed by a two-hour spike with an ADR at M0 that must measure the installer size and the start time. The reason: the product needs a native file watcher, a real memory governor and a small idle footprint, and one core keeps the fix count down.
- **The phone app is a remote, not a pretend laptop.** PojavLauncher proved phones matter to this audience, but running Java Minecraft on a phone is a different job from controlling and monitoring your PC. The Android and iOS companion does the remote, the server status and the crash assistant. Running the game on the phone is explicitly out of scope and would be its own project with its own licence review.
- **The performance promise must be a benchmark, never a number.** The legacy README says "144+ FPS" and "Verified & Signed" with no evidence; the plan forbids any FPS number in a user-facing path unless a benchmark script produced it on named hardware, and the benchmark output is stored next to the claim.
- **The two-identity rule is written down.** The SIR account (email, on our server) and the Minecraft account (Microsoft device code, token in the OS store) are separate in the plan, in `docs/AUTH.md` in T3, and in the security baseline. The legacy `auth_service.py` already worked this way in practice; the plan makes it a rule with a test.
- **The pricing anchors are competitor prices, not invented.** 49 EGP/month sits under CurseForge Premium at $2.99 and Modrinth Plus at $4.99, and the plan says the prices are test prices until the gateway fee schedule and the lawyer have read them.

---

## 6. Verification actually performed

- `git status` and `git log -5` in `D:/Projects/_SIR` at the start: the tree had many modified files from other agents (skill digests, dashboards, other products' plans). **None of them are mine.** I touched only my three files plus the bus line, and I staged only explicit paths, never `git add -A`.
- Every file counted with a real command (37 launcher services, 32 web routes, 185 jars, 10 instance folders, 6 real tiers) and cross-checked against the legacy's own claims, which turned out to be wrong on the route count.
- Every legacy code reference in the plan and the briefs was read in the source file before it was written down, not recalled from the README.
- Every one of the 47 skill digests I named was checked to exist under `D:/Projects/_SIR/ops/encyclopedia/deep/` with a loop that printed MISS for anything absent (three candidates were missing: `content-security-policy`, `binary-analysis`, `prompt-injection-defense` - **none of them are referenced**).
- Table syntax of all three files checked with a script: 0 malformed rows.
- `gh repo view` used to confirm both repos' visibility, branch and update time.

**Not done and honestly open:**
- The Firebase project `sir-modpack` was **not** created: the Firebase CLI is not installed on this machine.
- The Vercel project was not checked or created (M0 work).
- CI: `ops/ci-quota-exhausted.flag` exists, so GitHub Actions minutes are exhausted. This change is **markdown only** with no code to verify, so the local-verification substitute in WORKER_PREAMBLE rule 18 is not applicable; what I did instead is the file existence, table-syntax, source-count and skill-path checks listed above, all of which passed. I did not run `gh run list` because there is no workflow change to watch.

---

## 7. Git

- `git add plans/sir-modpack.md ops/competitors/sir-modpack.md ops/briefs/sir-modpack-tasks.md` then commit `r52: premium plan rewrite for SIR ModPack + sourced competitor matrix + 10 queued tasks`, pushed to `main`.
- The bus line appended to `ops/bus/sir-hq.md` in a second commit, pushed.

---

## 8. Recommended next

1. Queue `ops/briefs/sir-modpack-tasks.md` T1 to T10 to the free agents. T1, T2, T3 and T4 can run side by side; T1 (read-only deep scan) unblocks the rest.
2. Install the Firebase CLI before T3 runs, otherwise T3 blocks on a missing tool.
3. Decide the launcher-shell question early: the M0 ADR (Tauri v2 against the legacy Python) is the largest open technical decision and it gates the desktop build.
4. Check the legacy public repo `sirahmed8/SIR-ModPack` and decide whether it goes private now or at M6. It is public today and carries the "144+ FPS" and "Verified & Signed" claims that the new plan forbids.
5. When the plan is next reviewed, replace the "(unsourced, verify)" marks in section 7 of the plan with the real Paymob and Fawry fee schedules, and take the server-retail question to the lawyer, because the Mojang rules read today do not clearly cover a launcher that rents a server it does not own.
6. The seven open sourcing tasks in the competitor file are small (under two hours each) and would let the next revision of the plan quote the Lunar+ price, the BisectHosting per-GB prices and five linked player complaints.
