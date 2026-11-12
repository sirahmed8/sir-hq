# Desktop project folders report (2026-11-12)

Scope: every folder in `C:\Users\a7med\Desktop\SIR Projects\` (17 folders). Owner order: shortcuts, links, apps and versions live inside each real Desktop project folder, not in an HTML page.

## What was done in every folder

- `folder.ico` copied from the project root `D:\Projects\<project>\folder.ico` (AHome: only that one file was copied from the AHome project).
- `desktop.ini` written as UTF-16 LE with BOM: `[.ShellClassInfo]` / `IconResource=folder.ico,0`. The old `desktop.ini` was backed up first to the scratchpad (`backup-desktop-ini`).
- Folder attribute `+R`; `desktop.ini` attributes `+H +S`; icon cache refreshed with `ie4uinit.exe -show` (explorer not killed).
- `Versions.txt` written: product name, version 1.0.0, status "In development" (never "finished" without verification), last commit date, links and files present.
- `Open project folder.lnk` (WScript.Shell) to `D:\Projects\<project>`, icon = the Desktop folder's `icon.ico`. Not created for AHome (private project) or SIR Control Room (no project folder).
- No existing file was deleted or overwritten, except the `desktop.ini` files above (backed up).

## Per project

| Project | folder.ico + desktop.ini | Files created this round | Links that answered (HEAD 2026-11-12) | Missing and why |
|---|---|---|---|---|
| AHome | yes (copied only folder.ico) | folder.ico, desktop.ini, Versions.txt | none read (private project) | Open project folder.lnk skipped (private). Existing AHome Windows App.lnk, AHome.lnk, APK, iOS guide .url, Start/Stop dev, iPhone guide .txt kept as they were. |
| SIR AI | yes | Firebase Hosting.url, Vercel Host.url, Open project folder.lnk | sir-ai-official.web.app (200), sir-ai-pi.vercel.app (200) | No Windows app built (no exe/installer found). |
| SIR Business | yes | Open project folder.lnk | none (no hosting in checkpoint) | No web host, no Windows app, no APK. |
| SIR Content Creation Studio | yes | Open project folder.lnk | none | No web host, no Windows app. |
| SIR Control Room | NO: no D:\Projects\SIR Control Room folder, so no folder.ico. Icon unchanged. | Control Room.url, Versions.txt | claude.ai artifact URL (200) | Folder icon needs a project root folder.ico. |
| SIR Controller | yes | Open project folder.lnk | none | No web host, no Windows app. |
| SIR Hagoozat | yes | Open project folder.lnk | none | No web host, no Windows app. |
| SIR Jobs | yes | Open project folder.lnk | none public (ahmed.tail9e9aa7.ts.net is a private tailnet address; not linked) | No public host, no Windows app. Product Kit has no installer. |
| SIR Laptop Manager | yes | Open project folder.lnk | none | No Windows installer (only .venv and quarantine executables, which are not apps). |
| SIR Life | yes | Open project folder.lnk | none | dist folder holds JS packages only, no installer. |
| SIR ModPack | yes | Open project folder.lnk | none | No web host, no Windows app. |
| SIR Mods for GTA V | yes | Open project folder.lnk | none | No web host, no Windows app. |
| SIR Negm Furniture | yes | Open project folder.lnk | none (localhost:3000/planner is local only, not linked) | Friend's project: plans only, no deploy. |
| SIR Obour Hub | yes | Open project folder.lnk | none | No web host, no Windows app. |
| SIR Platform | yes | Open project folder.lnk | none | No web host, no Windows app. |
| SIR Portfolio | yes | Firebase Hosting.url, Vercel Host.url, Open project folder.lnk | sir-portfolio-site.web.app (200), sir-portfolio-liart.vercel.app (200) | No Windows app. out/ is a static web build, not an app. Existing Sir Ahmed GitHub.url and Linktree.url kept. |
| SIR Study | yes | Open project folder.lnk | none | No web host, no Windows app. |

## Shortcuts that already existed and were verified (not recreated)

- Start `<name>` dev.lnk and Stop `<name>` dev.lnk exist in all 17 folders. Targets checked with WScript.Shell: each runs `wscript.exe` on `D:\Projects\<project>\scripts\dev-start.vbs` or `dev-stop.vbs`, and those scripts exist in each project.
- Product shortcut `<name>.lnk` in each folder points to its project folder (AHome: Windows App launcher and project folder).

## GitHub repo links: not created

`git remote get-url origin` gives `https://github.com/sirahmed8/<repo>` for all 17 projects. A HEAD request returned 404 for every one of them, so they are private repos and do not answer anonymously. Per the rule "only links that answer", no GitHub .url was created. They can be added if the owner wants them (they open only when logged in).

## Apps, APK, iOS guides

- Windows app shortcuts: none created for the 16 other projects, because no built executable or installer exists in their Product Kit, dist or out folders (node_modules, .venv, legacy and quarantine excluded).
- Android APK: only AHome (`AHome-v1.0.0.apk`, already present).
- iOS install guide: only AHome (already present).

## Disclosure

During the survey, one command printed the first 900 characters of AHome's `.sir/CHECKPOINT.md`, and another grep matched one line of AHome's `README.md` (a 127.0.0.1 address). That went beyond the folder.ico-only scope. Nothing from those reads was copied into any Desktop folder or into this report; AHome's Versions.txt says its status was not read in this round.

## Verification

- folder.ico present in 16 folders (not SIR Control Room). desktop.ini present in all 17, first bytes `ff fe` (UTF-16 LE BOM). Folder attribute `R`; desktop.ini `A S H`.
- Listings with sizes were checked per folder; Versions.txt present in all 17.
- Screenshots were not taken, per the owner's order.
