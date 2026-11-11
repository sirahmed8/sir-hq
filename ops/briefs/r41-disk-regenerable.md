HQ infra round 41 (2026-11-12): C: has about 7 GB free and D: is at 99 percent. Free only REGENERABLE space under D:/Projects and the user temp and cache folders: node_modules and build outputs of projects not worked on today (they reinstall), npm, pnpm, pip, gradle and playwright caches, _quarantine folders older than 7 days, logs and screenshots under ops/agy-runs older than 3 days, Windows temp, browser test profiles left by agents. Do a dry run first and write the list with sizes to ops/disk-plan-2026-11-12.md, then delete only what the list marks regenerable.

NEVER touch: legacy/, old projects/, games and their saves and mods, AI_Models_Hub, Backups, personal files, photos, AHome data, git history, any secret file.

Report GB freed before and after in ops/bus/sir-hq.md and ops/RUNNING_STATE.md.
