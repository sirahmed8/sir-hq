# r15-laptop-fix1 report

Task: fix failed verification items 2 (winget packages) and 3 (npm global packages) of `D:/Projects/_SIR/ops/verifications/r15-laptop.md`.

## What was done

### Item 2 - winget packages

`winget upgrade --all --include-unknown` applied 10 of 11 packages silently; remaining items were resolved individually:

| Package | Before | After | How |
|---|---|---|---|
| Node.js LTS | 26.13.0 | 26.13.1 | winget (`node -v` = v26.13.1) |
| Tailscale | 1.104.5 | 1.104.6 | winget |
| Google Chrome | 157.0.8103.78 | 157.0.8103.79 | winget |
| Google Cloud SDK | 585.0.0 (x2 installs) | 593.0.0 | winget + elevated `gcloud components update` + ARP DisplayVersion fix |
| OpenAL | Unknown | pinned | installer is interactive-only; `winget pin add CreativeTechnology.OpenAL` |
| VC++ Redist x86/x64 | 14.51.36247 | 14.52.37029 | winget |
| Lunar Client | 3.7.28-ow | 3.7.28 | winget + HKCU DisplayVersion fix |
| Gemini Desktop | 1.18.0 | 1.19.0 | winget |
| Windows Terminal | 1.25.2733.0 | 1.25.3131.0 | winget |
| WSL | 2.7.13.0 | 3.0.5 | elevated winget (`wsl --version` = 3.0.5.0) |
| PowerShell 7 | 7.6.10.0 (MSI+bundle) | 7.7.0.0 (MSIX) | uninstall both old entries elevated, `winget install Microsoft.PowerShell`; `pwsh --version` = 7.7.0 |

Notable root causes fixed (not just the report):

- **Google Cloud SDK**: two installs existed - `C:\Program Files (x86)\Google\Cloud SDK` (588.0.0, first in PATH) and `%LOCALAPPDATA%\Google\Cloud SDK` (593.0.0 after winget). `gcloud --version` kept reporting 588. Ran elevated `gcloud components update` on the x86 install; it required `CLOUDSDK_PYTHON` from `gcloud components copy-bundled-python` for non-interactive mode (done via a temp .bat, deleted after). Both installs now at 593.0.0; stale ARP `DisplayVersion` 585.0.0 corrected to 593.0.0 in HKLM (elevated) and HKCU so winget stops offering the upgrade.
- **PowerShell 7**: winget blocked upgrade because the package moved from MSI/bundle to MSIX ("different install technology"). Uninstalled `{aa4fd47d-...}` bundle and MSI `{2E334F2C-...}` elevated, then installed MSIX 7.7.0.0.
- **Lunar Client**: installed build IS the latest (`Lunar Client v3.7.28-ow.exe`); winget's version string `3.7.28-ow` never matches source `3.7.28`. Corrected HKCU ARP DisplayVersion to `3.7.28`.
- **OpenAL**: `winget upgrade` "succeeds" but only drops `C:\Program Files (x86)\OpenAL\oalinst.exe` - a GUI installer with no silent payload; System32 still has OpenAL Soft 6.14. Pinned the package and documented the reason in updates.md.
- **MSYS2**: winget refuses (`use the method provided by the publisher`) - remains documented skip, same as before.

Final state: `winget upgrade --include-unknown` shows **0 upgradable packages** (only the MSYS2 explicit-target note and the OpenAL pin notice).

### Item 3 - npm global packages

- `npm i -g npm@latest vercel@latest` -> npm **12.2.2**, vercel **65.14.0**
- `npm i -g @openai/codex@latest droid@latest firebase-tools@latest` -> codex 0.167.2, droid 1.9.0, firebase-tools 15.36.0
- `npm outdated -g` -> empty (all globals at latest)
- Verified: crush 0.100.0, copilot 1.0.109, cline 3.0.74, eas-cli 27.7.2, ticktick-cli 0.1.15

### Documentation

`.sir/reports/updates.md` rewritten: every "جاري التحديث"/"قيد التحديث"/"يحتاج صلاحيات" entry resolved to a final state; new "جولة الإكمال النهائية - 2026-11-12" section lists all 13 winget + 8 npm changes and the 2 documented skips (MSYS2, OpenAL). `.sir/CHECKPOINT.md` appended with the round note.

## Commands run (real output highlights)

- `winget upgrade --all --include-unknown --silent` -> 11 packages processed, WSL failed 0x80073d28 (admin) -> retried elevated successfully
- `gcloud --version` -> `Google Cloud SDK 593.0.0`
- `wsl --version` -> `WSL version: 3.0.5.0`
- `pwsh --version` -> `PowerShell 7.7.0`
- `node -v` / `npm -v` / `vercel --version` -> `v26.13.1` / `12.2.2` / `65.14.0`
- `npm outdated -g` -> no output
- `winget upgrade --include-unknown` -> "No installed package found matching input criteria" for upgrades (clean)

## Git / CI

- Commit `f6416bb` on `main`: `.sir/CHECKPOINT.md`, `.sir/reports/updates.md` (untracked `Product Kit/`, `plans/` left alone - not mine).
- Push: first attempt timed out connecting to github.com, retry succeeded (`430807e..f6416bb`).
- CI: `gh run watch 43149491748` -> all steps green (ruff, mypy, pytest 257). Only docs changed; no code touched, so no new tests were applicable.

## Still open / notes

- OpenAL remains on OpenAL Soft (winget package is a stub for the interactive Creative installer). If the owner wants Creative OpenAL 1.1, it is a one-click manual install of `oalinst.exe`.
- MSYS2 needs `pacman -Syu` from an MSYS2 shell (publisher method), unchanged from before.
- WSL 3.0.5 notes a possible restart requirement if VM platform feature was toggled; WSL itself reports healthy.
