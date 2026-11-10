# PLAN: SIR Controller (Wave 8, optional and last, not started)
Audited 2026-11-10. Replaces `SIR Controller (v1)` and `SIR Optimizer` (both in `legacy/`, kept until M6). The controller part is derived from the open-source x360ce project, so it is not Ahmed's own work; the optimizer part is his. Whether to sell any of it is decided at M0 by the licence audit.

## 1. Purpose (plain words)
Two Windows tools for PC gamers: a controller mapper that makes a PlayStation, Switch or wheel controller work as an Xbox controller in any game, and a PC optimizer that scans a Windows laptop and explains in plain words what slows it down. A small website offers the downloads.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Controller` |
| GitHub (private) | `sirahmed8/sir-controller` (legacy repos `sirahmed8/SIR-Controller`, `sirahmed8/sir-optimizer`) |
| Stack (planned) | Mapper: keep the existing .NET core (Engine, tests) and decide the UI after a 2 hour spike: WinUI 3 or Tauri v2 in an ADR; Optimizer: .NET 8 or PowerShell engine with a Tauri UI; web portal: Next.js on Cloudflare Pages |
| Domain | the old plan used `sircontroller.app` and `siroptimizer.com`: neither resolved when last checked (2026-10-29 inventory); owner checks and buys a name; price "(unsourced, verify)" |
| Platforms | Windows only (first). Web portal. macOS, Linux, Android, iOS, TV, watch: skipped, the tools use Windows drivers |
| Money | Free controller mapping. Pro in EGP for profile sync and the optimizer suite; older strings in the optimizer used 249 EGP/month and 1,999 EGP/year: test prices only, "(unsourced, verify)". "Launching soon" + email capture until keys |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30); 9 commits, setup and plan only. PORTFOLIO.md: 2 of 20 tasks.
Legacy facts (inventories 2026-10-29, nothing run): Controller is a WinForms app on .NET Framework 4.6.2 with about 410 vendored engine files and a commit claiming "298/298 MSTest pass" (unverified); about 20 binaries tracked in git; LGPL-3.0 text sits beside a proprietary EULA that names "SIR Systems LLC" (no evidence this company exists: remove the name unless the owner confirms a real registered entity); three identical generic agent files; download button pointed at a private repo; unsigned webhook and client-side owner gate with a hard-coded email (stopgaps merged separately). Optimizer: any user could flip an owner flag in the client, AI keys in the web bundle, open CORS chat route with no auth, simulated owner transactions, a nested `public_repo/.git`, tracked .exe and .zip files.

## 4. Rules (each needs a test or command)
1. Licence audit first (M0): list every vendored component with licence (`docs/THIRD_PARTY.csv`). LGPL-3.0 parts stay replaceable (dynamic link or source offered) and the EULA must not contradict the licence. Selling is allowed only if the audit says so; otherwise the controller stays free and open and only the optimizer is Pro. Legal reading is the lawyer step; "(unsourced, verify)".
2. Driver-level changes are risky: ship a read-only scan first. Any change to Windows settings is a dry run with an undo (restore point or saved registry export), tested on a VM.
3. No binaries in git; releases hold installers; a CI check fails on files over 5 MB.
4. Server-side owner and Pro checks only (verified ID token, allow-list). Test: client flag flip changes nothing.
5. No AI key in any bundle; chat route authenticated, rate-limited, CORS locked.
6. Webhooks signed with timestamp inside the payload; idempotent.
7. No fake transactions or numbers in the owner dashboard; empty states are honest.
8. The "OP mode" idea (owner bypass) exists only server-verified for the owner account.
9. No performance claim without a reproducible benchmark script on named hardware; no "boosts FPS by X percent".

## 5. Shared pieces
Platform `owner-auth`, `signed-webhook`, `billing-fallback`, `ai-proxy`, `legal-pack`, `i18n`, `ui`. The scan/dry-run/undo pattern and quarantine bucket come from SIR Laptop Manager (same author, same ideas): reuse its tested design instead of a third implementation; if Laptop Manager's core is extracted, depend on it.

## 6. Screens and entities
Mapper: Devices, Mapping editor, Profiles per game, Test pad, Settings and Profile. Optimizer: Scan report (plain-language findings), Fix with preview and undo, History. Web: Landing, Downloads, Pricing, Privacy/Terms/Refunds/Cookies, Owner. Entities: Device, Profile, Preset, ScanFinding, FixAction, UndoPoint, Subscription.
Five states, Arabic RTL first and English, themes, 320 px to 4K web, WCAG 2.2 AA, own logo.

## 7. AI and support
Support assistant grounded in the guide and the known-issues list; "why is my game stuttering" explains the scan result in plain words and never changes anything itself. Chain via `ai-proxy`, free 5 per day, owner unmetered, kill switch, evals with 30 scan-result fixtures (explanation must name only findings present in the fixture).

## 8. Operations
Release checklist with signature check, crash reports with consent, weekly Telegram line, status JSON, update channel; support triage by assistant.

## 9. Launch, legal and visibility
Owner buys domain, code-signing certificate (needed for driver-adjacent installers), payment accounts. Legal pack: privacy, terms, refunds, cookies, third-party licence notices, DMCA contact, "not affiliated" notice for console brands; lawyer review before paid launch. Visibility: Arabic and Gulf queries ("برنامج تشغيل يد بلايستيشن على الكمبيوتر"), setup guides per controller, YouTube demos, `llms.txt`, facts page. Honest limit: giants exist; target niche queries.

## 10. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Licence audit and decision | `docs/THIRD_PARTY.csv`; written go/no-go on selling; green CI |
| M1 | Core slice | engine tests run in CI on `windows-latest` with real counts; a pad is read in a test harness |
| M2 | Parity | mapping editor and profiles; optimizer scan (read-only) |
| M3 | Security, legal, billing | owner flag test, key grep, webhook tests, legal pages |
| M4 | AI | scan explanation eval |
| M5 | Quality | clean-VM install, screenshots, a11y, RTL |
| M6 | Release | signed installer (owner), site live, legacy repos archived |

## 11. Next 10 tasks (each under 2 hours)
1. Inventory vendored components and binaries with licence column. Files: `docs/THIRD_PARTY.csv`. Check: every vendored folder has a row.
2. Write `docs/LICENSE_DECISION.md`: what may be sold, what stays free. Check: file cites each licence file path.
3. Run the existing .NET tests on `windows-latest` in CI and record counts. Files: `.github/workflows/build.yml`. Check: Actions URL with passed count.
4. Remove binaries from the new repo layout; add a size check script. Files: `scripts/check-size.mjs`. Check: fails on a 6 MB test file.
5. UI spike ADR (WinUI 3 vs Tauri), 2 hours, measured size and start time. Files: `docs/adr/001-ui.md`. Check: numbers present.
6. Optimizer read-only scan v0 (startup items, disk free, power plan) as JSON. Files: `apps/optimizer/engine/scan.ps1` or `.cs`. Check: output validated by a JSON schema test.
7. Plain-words explanation mapper for findings (rules, no AI). Check: unit tests for 10 findings in Arabic and English.
8. Portal scaffold with owner check server-side. Check: client flag flip test returns 403.
9. Signed webhook package copy with 10 negative tests. Check: tests green.
10. Honest-claims lint for site and README. Check: fails on "boost", "100%" without a linked benchmark.

## 12. Risks and open questions (defaults)
- Third-party and AGPL/LGPL obligations: default is keep the mapper free and open if the audit is unclear.
- Console-brand trademarks (PlayStation, Xbox): default is nominative use only with a "not affiliated" notice.
- Driver and registry changes can brick a setup: default is read-only until undo is proven on a VM.
- Competitor claims (x360ce itself, DS4Windows, Steam Input, vendor tools): `plans/competitors/sir-controller.md` must carry links or "(unsourced, verify)".

## 13. Only the owner can do
Decide to sell or not after the licence note; buy domain and certificate; create payment accounts; test with real controllers (he must plug them in); lawyer review.
