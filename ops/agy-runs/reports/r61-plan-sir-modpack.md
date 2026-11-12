# Report: r61-plan-sir-modpack (planning-only refresh, rule 20)

Date: 2026-11-12. Worker: devin (Devin CLI). Scope honoured: wrote only under `D:/Projects/_SIR` (`plans/`, `ops/briefs/`, `ops/competitors/`, `ops/bus/`). Nothing written inside `D:/Projects/SIR ModPack`, no repos or Firebase projects created.

## What was done

1. Read the required context: `ops/WORKER_PREAMBLE.md`, `.sir/CHECKPOINT.md`, the brief `ops/briefs/r61-plan-sir-modpack.prompt.txt`, `git status` / `git log` / `git diff --stat`, `plans/sir-modpack.md` (457 lines), `plans/sir-modpack-DEEP.md`, `ops/briefs/sir-modpack-tasks.md` (was 10 tasks), `ops/competitors/sir-modpack.md`, the product folder read-only (`.sir/PLAN_REFRESH.md`, `CHECKPOINT.md`, `legacy/` listing), `ops/TICKTICK_MAP.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md`, `ops/SKILLS_INDEX.md`.
2. Appended START and DONE lines to `ops/bus/team.md`; appended the HQ inbox line to `ops/bus/sir-hq.md`.
3. Fresh web research (real searches, sources recorded in the competitor addendum):
   - Minecraft Java Edition moved to `YY.N` versioning in 2026: 26.1 "Tiny Takeover" (2026-03-24), 26.1.1, 26.1.2, 26.2 "Chaos Cubed" (2026-06-16), 26.3 "Wilderness Bound" (2026-09-15); last `1.x` was 1.21.11 (Dec 2025). Java 25+ required from 26.1. Sources: minecraft.net versioning article, minecraft.wiki, mcreference.com, serverskings/gameserverkings KB.
   - PojavLauncher archived 2025-09-23, successor Amethyst (AngelAuraMC, LGPL-3.0, ~2.4k stars, supports 26.3 snapshots); fake APK mirror sites documented. Sources: GitHub repo pages, folly.io guide.
   - New competitors: Dawn (dawn.gg), Millida Launcher (millida.net), Modgrade (modgrade.com), Fastly Optimised (mcreference.com). Sources fetched/checked 2026-11-12.
   - Microsoft device-code auth still works but the Azure client ID needs Mojang approval via `aka.ms/mce-reviewappid`; XSTS errors 2148916233 (no Java Edition) and 2148916238 (Xbox Live region) mapped. Sources: Horizon launcher docs, minecraft-auth, LightyLauncher docs.
   - Modrinth API v2 is official (PAT/OAuth2); April 2025 read-only outage broke Prism Launcher (modrinth/code issue #3496) -> one-adapter-with-cache rule.
4. Plan changes:
   - `plans/sir-modpack.md`: added section 14 "Plan refresh r61 (2026-11-12)" with the six findings, the `YY.N` version-support rule (v1 = 26.3 + 26.2 + 1.21.11 legacy line; Java 8/17/21/25 probing; Mojang runtime auto-download), five new risks with defaults, seven open questions with recommended answers, and the task summary.
   - `ops/briefs/sir-modpack-tasks.md`: expanded 10 -> 50 tasks. T1-T10 unchanged (T1 already done per `.sir/PLAN_REFRESH.md`); T11-T50 added, each with files/steps/acceptance test/skills and a full rewritten dependency map.
   - `ops/competitors/sir-modpack.md`: appended the r61 addendum (new competitors, version change, auth gate, Modrinth outage, still-unsourced items kept flagged).
   - `plans/sir-modpack-REFRESH-LOG.md`: created with the rescan record.
5. Committed explicit paths only and pushed. First push was rejected (remote moved by parallel workers); `git pull --rebase` then push succeeded. Verified: commit `0774a40` is on `main`, remote `main` at `4a181dd` contains it (`git ls-remote` checked).

## Commands run (real output, abbreviated)

- `git status` at start: only unrelated modified files (`ops/READ_LOG.md`, `ops/bus/sir-hq.md`, `plans/sir-access-map.md`) belonging to the parallel sir-access-map task — left untouched.
- `git commit` -> `6 files changed, 265 insertions(+), 4 deletions(-), create mode 100644 plans/sir-modpack-REFRESH-LOG.md`.
- `git push origin main` -> first attempt `remote rejected ... cannot lock ref`; after `git pull --rebase` (`Already up to date`) and re-push, `git ls-remote origin main` = `4a181dd...` and `git log` shows `0774a40 r61: expand SIR ModPack planning...` under it.
- CI: `ops/ci-quota-exhausted.flag` exists (GitHub Actions quota exhausted until ~2026-12-01), so per WORKER_PREAMBLE rule 18 local verification replaces CI-watching; this round is docs/plans only, no code to build or test. No `gh run` needed.

## State notes for the next worker

- The product folder `D:/Projects/SIR ModPack` has uncommitted r60 build work (`package.json`, `packages/`, `tsconfig*`, modified `assets/brand/icon.png`) — deliberately untouched (planning-only brief). The first build task must `git status` there and continue, never revert.
- Heavy parallel r61 activity in `_SIR`: many unrelated modified files remain uncommitted in the shared tree; only the six explicit paths above were committed.
- Owner steps now documented in the plan (section 12/14): Azure app registration + Mojang client-ID approval submission, domain, code-signing cert, Paymob/Fawry, store accounts, lawyer review, legacy key rotation (TickTick "Rotate secrets, Day 1" row names this product).

## Still open / unsure

- Lunar+ and Badlion prices, BisectHosting per-GB prices, CurseForge/Modrinth author redistribution terms, and five public crash-experience complaints remain **(unsourced, verify)** on the competitor file's open-sourcing list.
- Whether the r60 uncommitted build work in the product folder is coherent was not verified (out of scope, read-only rule); flagged for the next build task.

## Recommendation

Queue T2, T3, T4 next (parallel-safe per the dependency map); T1 is already done. The owner should submit the Azure app registration for Mojang approval early — it is the longest external lead time in M0.
