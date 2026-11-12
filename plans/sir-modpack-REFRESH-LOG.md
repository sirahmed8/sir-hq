# SIR ModPack plan refresh log (rule 20 rescan)

## 2026-11-12 (round r61, planning-only refresh)

**Re-read in full (read-only):** `D:/Projects/SIR ModPack/.sir/` (`PLAN_REFRESH.md`, `CHECKPOINT.md`, kit files), the product `AGENTS.md`/`README.md`, `plans/sir-modpack.md`, `plans/sir-modpack-DEEP.md`, `ops/briefs/sir-modpack-tasks.md`, `ops/competitors/sir-modpack.md`, `ops/inventory/SIR-ModPack-and-GTA-V-mods.md`, `ops/TICKTICK_MAP.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md`, `ops/WORKER_PREAMBLE.md`, `standard/23-premium-code-bar.md` (via the brief).

**Fresh web research (sources in `ops/competitors/sir-modpack.md` addendum):**

1. Minecraft Java Edition moved to `YY.N` versioning in 2026 (26.1 Tiny Takeover 2026-03-24, 26.2 Chaos Cubed 2026-06-16, 26.3 Wilderness Bound 2026-09-15; last 1.x was 1.21.11 in Dec 2025). Java 25+ required from 26.1.
2. PojavLauncher archived 2025-09-23; successor Amethyst (LGPL-3.0) is alive and supports 26.3 snapshots; fake APK mirrors proliferate.
3. New competitors: Dawn (free ad-supported multi-loader launcher), Millida Launcher (nickname sign-in, low-end focus), Modgrade (per-mod security grading), Fastly Optimised (ARR-licensed low-end pack on 26.4 snapshots).
4. Microsoft device-code auth still works but the Azure client ID must be approved by Mojang (`aka.ms/mce-reviewappid`); XSTS errors 2148916233/2148916238 mapped to user-facing states.
5. Modrinth API v2 official; April 2025 read-only outage broke Prism — one-adapter-with-cache rule added.
6. `.mrpack` + CurseForge manifest import planned as verified read-only import (T12, T13).

**Plan changes made:**

- `plans/sir-modpack.md`: new section 14 with the six research findings, the `YY.N` version-support rule (26.3 + 26.2 + 1.21.11 legacy line, Java 8/17/21/25 probing, Mojang runtime auto-download), five new risks with defaults, seven open questions with recommended answers, and the 50-task summary.
- `ops/briefs/sir-modpack-tasks.md`: expanded from 10 to 50 tasks (T11 to T50 added), each with files, steps, an acceptance test and the skills from `ops/SKILLS_INDEX.md`; full dependency map rewritten; footer updated.
- `ops/competitors/sir-modpack.md`: r61 addendum with the new competitors, the version-numbering change, the auth gate and the Modrinth outage lesson; unsourced items kept flagged.

**State notes:** the product folder has uncommitted build work from the r60 round (`package.json`, `packages/`, `tsconfig*`, modified `assets/brand/icon.png`) — left untouched per the planning-only brief; the next build task's worker must read `git status` there first and continue, never revert. This refresh wrote nothing inside `D:/Projects/SIR ModPack`.
