# PLAN: SIR ModPack (Wave 6, public product, not started)
Audited 2026-11-10. Replaces `SIR ModPack (v1)` (in `legacy/`, kept until M6). Free product; optional supporter tier in EGP.

## 1. Purpose (plain words)
A Windows launcher that installs a curated Minecraft modpack and manages a private server, plus a website with the download and a guide in Arabic. A player gets the pack running in one click.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR ModPack` |
| GitHub (private) | `sirahmed8/sir-modpack-source` (legacy public repo `sirahmed8/SIR-ModPack`: review and decide at M6 whether to archive) |
| Stack (planned) | Windows launcher on Tauri v2 (Rust + React/TypeScript) or the existing Python/pywebview, decided by a 2 hour spike in an ADR; manifest with SHA-256 per file; web hub on Cloudflare Pages |
| Domain | candidate `sirmodpack.com` (owner checks and buys; price "(unsourced, verify)"); `pages.dev` until then |
| Platforms | Windows launcher (first), web hub. macOS and Linux launcher: skipped for v1 (the pack targets the Windows players asked for). Android (Pojav-style) and consoles: skipped, out of scope |
| Money | Free download. Optional supporter tier in EGP (perks: name on the supporters page, early builds). No pay-to-win, no paywalled mods. "Launching soon" + email capture until keys exist |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30); 9 commits, setup and plan only. PORTFOLIO.md: 2 of 18 tasks.
Legacy facts (`ops/inventory/SIR-ModPack-and-GTA-V-mods.md`, 2026-10-29, nothing run): the old repo is 16.9 GB on disk; ships `SIR_Apps_Suite.zip` (120 MB); claims such as "100% PASS, zero bugs", "144+ FPS" and "Verified & Signed" had no reproducible evidence; the EULA text described bytecode transforms of the Minecraft game file on the player's machine; two account files were once tracked and the history was rewritten on 2026-10-29 (a backup bundle exists); the website folder was untracked; a copy of PrismLauncher (GPL-3) sits in `development/`.

## 4. Rules (each needs a test or command)
1. Mojang rules decide what can ship. Source: Minecraft Usage Guidelines, section on commercial use (`https://www.minecraft.net/en-us/usage-guidelines`; excerpt read 2026-11-10 via search, full text must be read at M0). The excerpt says money may be made from server access under conditions and that Mojang decides whether monetization fits its brand. Default: no paywall on any gameplay item; supporter perks are cosmetic and off-game; no Minecraft assets redistributed.
2. Never redistribute the Minecraft game files. The launcher downloads from the official sources on the player's machine. No byte-code rewriting of the game; if the pack needs a loader (Fabric, NeoForge), install the official loader.
3. Every mod in the pack has a licence entry (`docs/MOD_LICENSES.csv`: name, author, licence, source URL, redistribution allowed yes/no). The manifest generator refuses a mod without an entry or with redistribution "no" (then the launcher downloads it from the original host).
4. GPL/AGPL: do not copy PrismLauncher code into the proprietary launcher; use it only as a separate, unmodified tool or not at all. A licence audit task runs in CI.
5. No unprovable claims: no "zero bugs", no FPS number without a benchmark script and hardware named, no "signed" without a signature check output.
6. Downloads: SHA-256 verified before install; the launcher refuses a mismatch. Test: corrupted file is rejected.
7. Account data: the launcher never stores a Microsoft/Mojang password; sign-in uses the official device-code flow; tokens in Credential Manager. Test: grep finds no `accounts.json` tracking; `.gitignore` covers it.
8. Server manager binds to localhost unless the player enables LAN; shows a warning before opening a port.

## 5. Shared pieces
Platform `ui/styles/hooks`, `i18n`, `legal-pack`, `billing-fallback`, Telegram sender. The signed manifest/update channel idea is shared with Business and Content Studio (Electron updaters); write it once in Platform `sir-kit` only if two products reach it.

## 6. Screens and entities
Launcher: Home (play, update), Profiles (versions, RAM), Mods list (with licences), Server manager (start, stop, logs, backup), Settings and Profile, Help. Web: Landing, Download, Guide (Arabic first), Supporters, Legal. Entities: Pack, Mod, Manifest, Profile, Server, Backup, Supporter.
Five states, Arabic RTL first and English, themes, 320 px to 4K web, WCAG 2.2 AA, own logo.

## 7. AI and support
Support assistant (web and launcher) grounded in the guide and the known-issues file: "why does the game crash" reads the crash log locally and explains it in plain words; log text is not sent anywhere unless the user clicks Send. Chain via `ai-proxy`; free quota 5 per day; evals with 20 real-looking crash logs (Arabic and English). No AI in the install path.

## 8. Operations
Release checklist (build, sign, upload, manifest hash check), weekly Telegram line (downloads from analytics that need no cookies, error reports with consent), mod update watcher (new versions of listed mods, with test install), status JSON on the site.

## 9. Launch, legal and visibility
Owner buys the domain and a code-signing certificate (unsigned installers trigger SmartScreen warnings: "(unsourced, verify)" how severe). Legal: privacy, terms, "not affiliated with Mojang or Microsoft" notice, mod credits page, DMCA/takedown contact. Visibility: Arabic Minecraft queries ("مود باك ماينكرافت عربي"), YouTube install tutorials with transcripts, guide pages, `llms.txt`, facts page; game-community posts made honestly in the brand's name, no fake engagement.

## 10. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Deep scan, licence matrix, setup, CI | `docs/MOD_LICENSES.csv` complete for legacy pack; Minecraft guidelines read and summarized; green Actions URL |
| M1 | Core slice | launcher installs the pack into a temp folder from a manifest and verifies every hash |
| M2 | Parity | server manager, backups, profiles; checklist against legacy features |
| M3 | Security and legal | corrupted download test, token storage test, legal pages |
| M4 | Support assistant | crash-log eval recorded |
| M5 | Quality | clean-VM install test, screenshots, a11y, RTL |
| M6 | Release | signed installer (owner), site live, legacy repo archived or privatized |

## 11. Next 10 tasks (each under 2 hours)
1. Read the Minecraft Usage Guidelines in full and write `docs/MOJANG_RULES.md` with quoted section titles and the decisions it forces. Check: file has the URL and read date.
2. Licence matrix for the current pack from the legacy manifest. Files: `docs/MOD_LICENSES.csv`. Check: every mod has a row; unknown ones are marked "do not ship".
3. Launcher spike: Tauri v2 vs pywebview, 2 hour limit, ADR. Files: `docs/adr/001-launcher.md`. Check: ADR with a measured installer size and start time for each.
4. Manifest schema (zod or pydantic) and generator that refuses a missing licence. Check: tests green.
5. Downloader with SHA-256 check and resume. Check: corrupted-file test fails the install.
6. Device-code sign-in prototype (official flow) with token in Credential Manager. Check: no password prompt exists in the UI (grep test).
7. Server manager start/stop with log tail and localhost-only default. Check: test starts a fake server process and reads logs.
8. Website scaffold: Landing + Download + Arabic guide, with honest claims lint (bans "zero bugs", "100%"). Check: lint fails on a banned phrase.
9. CI: tests, gitleaks, licence audit. Check: green Actions URL.
10. Backup of world folders with restore test. Check: restore compares hashes.

## 12. Risks and open questions (defaults)
- Mojang monetization rules and brand check: default is free product with cosmetic supporter perks, no gameplay sales.
- Mod authors' permissions: default is link-to-source download instead of rehosting.
- Repo and disk size (16.9 GB): default is the new repo holds source only; builds and packs live in releases/storage, never in git.
- Competitor claims (CurseForge, Modrinth, Prism): see `plans/competitors/sir-modpack.md`; links required or "(unsourced, verify)".

## 13. Only the owner can do
Buy domain and code-signing certificate; sign in to GitHub releases, Cloudflare; contact mod authors if a licence says ask-first; accept any platform terms; lawyer review of terms.
