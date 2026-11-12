# SIR Controller: Task Queue (sir-controller-tasks.md)

> REFRESH 2026-11-12 (r61, rule 20): expanded from 10 to 46 tasks, each with an acceptance test and the skills from ops/SKILLS_INDEX.md that fit. **PLANNING ONLY: the owner has not authorized build.** Do not start any task until HQ clears it. First 10 (section A) stay ready to hand to the agents unchanged in order. All tasks work in `D:\Projects\SIR Controller` (app code) and write reports/evidence only inside that project or `D:\Projects\_SIR\ops\`. Never open `D:\Projects\AHome`. Version stays 1.0.0. No placeholders, no invented data, five states, Arabic RTL and English, 44 px targets, bidi-isolated mixed text. After finishing any build task: run the gates, update the project checkpoint, commit to main, push the SIR Controller repo (NOT D:\Projects\_SIR).

Skills referenced (exact names from ops/SKILLS_INDEX.md): modern-app-engineering, pulse-engineering, nextjs, react-best-practices, shadcn, modern-ui-ux-design-system, anti-vibecoded-design-system, taste-design-engine, emil-motion-impeccable, a11y-debugging, chrome-devtools, mobile-ergonomics-polish, vibe-auth-hardening, zero-trust-security-hardening, owasp-vulnerability-shield, legal-compliance-shield, auth, webhook-testing, firebase_firestore, firebase_auth_basics, firebase_basics, database-reliability-transactions, production-engineering-standards, test-driven-development, review-agent, binary-reverse-engineer, memory-leak-debugging, performance-testing, open-seo-auditor, commercial-app-blueprint, high-conversion-copywriting, system-design-architect, ponytail-yagni-optimizer, karpathy-skills, direct-action-shield, verification, env-vars, deployments-cicd, vercel-cli, vercel-functions, firebase_hosting_basics, cookie-debugging.

---

## A. First 10 (ready to hand, in order, each under 2 hours)

**A1. Inventory vendored components and binaries with licence column**
Files: `docs/THIRD_PARTY.csv`, legacy engine folder inventory, `.sir/reports/vendored-inventory.md`. Acceptance: every vendored folder/file has a row with licence; `node -e` check exits non-zero listing any component missing licence; report lists ~410 engine files grouped by folder. Skills: binary-reverse-engineer, production-engineering-standards, karpathy-skills.

**A2. Write LICENSE_DECISION.md from the audit**
Files: `docs/LICENSE_DECISION.md` (extend the one drafted 2026-10-30). Acceptance: file cites each licence file path; states what may be sold, what stays free, what must be replaced; exits non-zero if any audited component is unresolved; unsigned by anyone except owner. Skills: legal-compliance-shield, production-engineering-standards.

**A3. Remove binaries from new repo layout; add size check script**
Files: new repo layout, `scripts/check-size.mjs`. Acceptance: size check fails on a planted 6 MB test file, passes after removal; CI step wired; no `.exe`/`.dll`/`.zip` tracked (`git ls-files` clean). Skills: production-engineering-standards, zero-trust-security-hardening.

**A4. UI spike ADR: WinUI 3 vs Tauri (2 hours, measured)**
Files: `docs/adr/001-ui.md`, spike code under `spikes/ui-winui` and `spikes/ui-tauri` (throwaway, deleted after). Acceptance: ADR records measured installer size, cold start ms, idle RAM for both options on the owner's PC; decision stated with trade-offs; exits 0. Skills: modern-app-engineering, pulse-engineering, system-design-architect.

**A5. Optimizer read-only scan v0 as JSON**
Files: `apps/optimizer/engine/scan.ps1` (or `.cs`), `apps/optimizer/engine/scan.schema.json`, test. Acceptance: scan outputs JSON validating against the schema (startup items, disk free, power plan, network adapter, services); schema mismatch exits non-zero; nothing is modified (dry-run proof: registry snapshot identical before/after). Skills: test-driven-development, production-engineering-standards, zero-trust-security-hardening.

**A6. Plain-words explanation for mapper findings (rules, no AI)**
Files: `packages/explainer/` with unit tests for 10 findings in Arabic and English. Acceptance: 10/10 unit tests pass both languages; explainer is pure (no side effects, imports nothing that writes); bidi-safe Arabic strings reviewed. Skills: test-driven-development, modern-ui-ux-design-system.

**A7. Portal scaffold with server-side owner check**
Files: Next.js portal (`apps/portal`), landing/downloads/pricing pages, `/owner` route with middleware gate. Acceptance: client flag flip returns 403 for `/owner`; owner route renders real aggregates (zeros when empty, never estimates) only with a verified owner token; `npm test` green. Skills: nextjs, vibe-auth-hardening, auth, shadcn, vercel-functions.

**A8. Signed webhook package with 10 negative tests**
Files: `packages/signed-webhook/` + tests. Acceptance: 10 negative tests pass (tampered body, replayed timestamp, unsigned, wrong secret, expired timestamp, future timestamp beyond skew, duplicate event id idempotent, bad content-type, missing signature header, downgraded algorithm). Skills: webhook-testing, zero-trust-security-hardening, test-driven-development.

**A9. Honest-claims lint for site copy and README**
Files: `scripts/honest-claims-lint.mjs`, wired into CI. Acceptance: lint fails on "boost", "FPS +", "100%" without a linked benchmark URL; passes with benchmark link present; README and site copy pass. Skills: production-engineering-standards, open-seo-auditor.

**A10. README claims pass + gentle nudge for unsupported claims (EN/AR)**
Files: README.md update, one small dismissible notice component in portal docs. Acceptance: README passes the A9 lint; with an unsupported claim planted, the notice renders (320 px safe, Arabic and English, light/dark), dismisses, and disappears once the claim is fixed. Skills: anti-vibecoded-design-system, a11y-debugging, high-conversion-copywriting.

---

## B. Licence, legal, governance (M0)

**B11. Read x360ce licence file directly; record terms + redistribution rights**
Files: `docs/licenses/x360ce-LICENSE.txt`, audit row. Acceptance: licence text archived with source URL + date; redistribution rights stated in LICENSE_DECISION.md; if missing/incompatible, mapper stays free (R1). Skills: legal-compliance-shield, binary-reverse-engineer.

**B12. ViGEmBus dependency ADR (pin 1.22.0, hash-verified, never vendored)**
Files: `docs/adr/002-vigembus.md`. Acceptance: ADR states version, SHA-256, official URL, install/uninstall chain, failure UX, migration trigger (Windows update breakage); links retired-driver notice. Skills: system-design-architect, zero-trust-security-hardening.

**B13. Remove "SIR Systems LLC" from EULA/assets unless owner confirms entity**
Files: legacy-derived EULA draft, `docs/legal/EULA.md`. Acceptance: zero occurrences of the entity name unless an owner-confirmed registration exists in writing; copyright line reads "Ahmed Alaa" otherwise. Skills: legal-compliance-shield.

**B14. EULA + Privacy + Terms + Refund drafted from actual data practices; marked for Egyptian attorney review**
Files: `docs/legal/` (4 files), disclaimer banner "AI-drafted ... review by a qualified Egyptian attorney before commercial launch". Acceptance: privacy policy lists only what the product really collects (opt-in telemetry counts, email capture); no AHome/Habiba reference anywhere; review checklist attached. Skills: legal-compliance-shield.

**B15. Delete-my-data flow spec + implementation note**
Files: spec in `docs/specs/delete-my-data.md`, Firestore rules draft. Acceptance: spec enumerates `users`, `profiles`, `scanRuns`, `aiUsage`, `devices` deletion for a uid; 30-day soft-delete + purge job defined; rules deny cross-user reads (test). Skills: firebase_firestore, database-reliability-transactions, legal-compliance-shield.

**B16. Signed-installer decision ADR (code-signing cert vs unsigned beta)**
Files: `docs/adr/003-signing.md`. Acceptance: ADR states cert options + prices "(unsourced, verify)", owner action listed; unsigned builds labelled beta with SmartScreen guidance; no unsigned stable release ships. Skills: system-design-architect, legal-compliance-shield.

---

## C. Driver and engine (M1-M2)

**C17. ViGEmBus detection + guided install flow (hash-verified chain)**
Files: `apps/desktop/src/driver/` (detect, download, verify, install, rollback), onboarding screen. Acceptance: on a clean Win11 VM, flow installs 1.22.0 with SHA-256 check; wrong hash aborts with honest error; uninstall removes only our additions; detection reports driver state in Arabic/English. Skills: modern-app-engineering, zero-trust-security-hardening, test-driven-development.

**C18. HidHide optional install + double-input prevention**
Files: `apps/desktop/src/driver/hidhide.*`. Acceptance: with HidHide on, physical pad hidden from games (verified via GameControllers API in test game); off = unhidden; clean VM evidence. Skills: modern-app-engineering, test-driven-development.

**C19. Live controller input reader (Windows Raw Input / DirectInput) with tests**
Files: `apps/desktop/src/engine/input/`. Acceptance: unit tests with recorded HID reports pass; live read on owner's pad shows buttons/sticks/triggers at >= 250 Hz; zero allocations in hot loop (benchmark note). Skills: test-driven-development, performance-testing, memory-leak-debugging.

**C20. ViGEmBus virtual Xbox 360 bridge; button report mapping**
Files: `apps/desktop/src/driver/vigem_bridge.*`. Acceptance: Windows GameControllers API lists "Xbox 360 Controller for Windows"; mapping applied from profile JSON; zero driver signature warnings on clean VM. Skills: modern-app-engineering, test-driven-development.

**C21. Radial deadzone + anti-deadzone calibrator (math module + lab screen)**
Files: `packages/calibration/deadzone.ts`, lab screen. Acceptance: unit tests for radial normalization (inner/outer bounds, axial vs radial); live canvas plots raw vs calibrated; stick-drift test shows < 1% output inside inner deadzone. Skills: test-driven-development, modern-ui-ux-design-system, emil-motion-impeccable.

**C22. Sensitivity curves (linear, exponential, S-curve) with live graph**
Files: `packages/calibration/curves.ts`, curve picker screen. Acceptance: curve math unit tests (endpoints exact, monotonic); switching curve updates graph live; profile persists curve choice. Skills: test-driven-development, taste-design-engine.

**C23. Trigger lab: hair trigger + actuation point**
Files: `packages/calibration/triggers.ts`, trigger lab screen. Acceptance: hair-trigger test: 10% physical pull -> 100% virtual trigger; actuation point slider honored; settings persist per profile. Skills: test-driven-development, modern-ui-ux-design-system.

**C24. Live test pad screen (all inputs, real-time)**
Files: test pad screen component. Acceptance: every button/axis/trigger/gyro renders live at >= 30 fps; five states; Arabic/English; 320 px safe; screenshot at 5 viewports attached. Skills: modern-ui-ux-design-system, chrome-devtools, a11y-debugging.

**C25. Profile store + save/load + export/import (file)**
Files: `packages/profiles/` (schema, migration, export/import). Acceptance: round-trip export->import identical (JSON canonical compare); schema versioned; corrupt file shows honest error with retry; unit tests. Skills: test-driven-development, production-engineering-standards.

**C26. Process watcher: foreground window -> profile switch < 50 ms**
Files: `apps/desktop/src/profiles/process_watcher.*`, auto-switch rules UI. Acceptance: switching to a configured game exe activates its profile in < 50 ms (measured); toast shown; rule list editable; no profile => default; race-safe on rapid window switches. Skills: modern-app-engineering, performance-testing.

**C27. Multi-controller player slot assignment (up to 4)**
Files: slot assignment screen + engine routing. Acceptance: 4 pads assigned to P1-P4; visual slot indicator; per-slot profile; disconnect/replug keeps assignment. Skills: modern-app-engineering, modern-ui-ux-design-system.

**C28. Hotplug/disconnect resilience (WM_DEVICECHANGE)**
Files: `apps/desktop/src/driver/hotplug.*`. Acceptance: unplug/replug mid-game: virtual controller restored < 2 s, no crash, no orphan virtual devices (Device Manager count stable); soak test 30 cycles. Skills: modern-app-engineering, memory-leak-debugging, performance-testing.

**C29. DualSense/DualShock battery + lightbar + rumble (M2)**
Files: `apps/desktop/src/driver/sony_extras.*`. Acceptance: battery % read and displayed; lightbar color settable live; rumble test fires both motors; graceful no-extras fallback for generic pads. Skills: modern-app-engineering, test-driven-development.

**C30. DirectInput generic pad auto-mapper templates (M2)**
Files: `apps/desktop/src/driver/dinput_templates/`, template picker UI. Acceptance: 3 generic pads detected and mapped from templates with working D-pad; unknown pad -> guided manual template creation; tests with recorded reports. Skills: modern-app-engineering, binary-reverse-engineer.

---

## D. Optimizer (M2)

**D31. Read-only scan full v1: startup, disk, power plan, network, services, RAM**
Files: scan engine + findings catalog (`docs/findings/` with Arabic+English text). Acceptance: scan < 3 s; output schema-validated; findings carry risk labels (safe/caution/avoid) and a cited source each; nothing modified; VM evidence. Skills: test-driven-development, production-engineering-standards, zero-trust-security-hardening.

**D32. Timer-resolution diagnostics (honest wording, rule 12)**
Files: `apps/optimizer/engine/timer.*`, diagnostics section. Acceptance: reports resolution of our process (timeGetDevCaps + measured) and of the foreground game process; wording never claims game-wide 0.5 ms; unit test blocks banned phrases. Skills: test-driven-development, legal-compliance-shield.

**D33. Fix engine with preview + undo (.reg delta backups)**
Files: `apps/optimizer/engine/fixes/`, fix preview screen, undo history screen. Acceptance: every fix writes `.reg` delta first; undo restores byte-identical prior state (VM test); preview shows exact keys+values before apply; avoid-class findings cannot auto-apply. Skills: zero-trust-security-hardening, test-driven-development, modern-ui-ux-design-system.

**D34. restore_all_defaults.ps1 (standalone revert)**
Files: `scripts/restore_all_defaults.ps1`. Acceptance: on VM with all fixes applied, script returns registry/power-plan/services to clean pre-fix snapshot (compare exports); idempotent; signed note; Arabic/English output. Skills: zero-trust-security-hardening, production-engineering-standards.

**D35. Anti-cheat safe mode (competitive process detection)**
Files: `apps/optimizer/engine/safemode.*`, safe-mode UI badge. Acceptance: Valorant/CS2/Apex/Fortnite detection from exe list; in safe mode only certified-safe actions enabled (read-only scan + timer info); all tweak buttons disabled with explanation; whitelist editable. Skills: zero-trust-security-hardening, vibe-auth-hardening, modern-ui-ux-design-system.

**D36. Optional Nagle toggle labelled "TCP games only" with undo**
Files: fix module + UI label + undo. Acceptance: toggle writes TcpAckFrequency/TCPNoDelay for the active adapter with backup; label states TCP-only truth; undo restores; no marketing claim derived from it anywhere (lint A9 passes). Skills: test-driven-development, legal-compliance-shield.

**D37. Daemon watchdog: < 25 MB RAM, < 0.1% CPU, 24 h soak**
Files: `apps/desktop/src/diagnostics/watchdog.*`, tray status. Acceptance: 24 h soak on owner's PC: RAM stays < 25 MB, CPU < 0.1% average, zero leaks (handle count stable); report attached; `CREATE_NO_WINDOW` verified (no console flash at login). Skills: memory-leak-debugging, performance-testing, pulse-engineering.

**D38. Scheduled-task silent autostart installer (user-consent)**
Files: `scripts/install-autostart.ps1`, settings toggle. Acceptance: task `SIR_Controller_Daemon` registers on user login, runs windowless; uninstall removes task; opt-in only; works after reboot; honest off switch. Skills: production-engineering-standards, zero-trust-security-hardening.

---

## E. Portal, billing, owner analytics (M3)

**E39. Portal landing + downloads with SHA-256 manifest**
Files: `apps/portal/` landing, downloads page, `manifest.json` generator. Acceptance: downloads page shows latest version + hashes from a generated manifest; hash mismatch = honest error; both Firebase Hosting and Vercel deploy the same build; 200 on both. Skills: nextjs, firebase_hosting_basics, vercel-cli, vercel-functions, deployments-cicd.

**E40. Pricing page: Launching Soon + email capture (EGP/USD/SAR/AED toggle)**
Files: pricing page, `POST /api/leads`, locale detection. Acceptance: capture dedupes and rate-limits; toggle auto-detects locale/IP with manual override; "Subscriptions launching soon" shows until Paymob keys exist; honest copy (no invented prices; test prices flagged). Skills: nextjs, high-conversion-copywriting, commercial-app-blueprint, env-vars.

**E41. Paymob + Fawry webhook activation (test mode) with idempotency**
Files: webhook routes, license activation, tests. Acceptance: A8 suite green against both payload shapes; duplicate event no-ops; license flips server-side only; test-mode end-to-end documented (no live keys without owner). Skills: webhook-testing, vibe-auth-hardening, firebase_firestore.

**E42. Owner analytics `/owner` with real metrics only**
Files: `/owner` route + middleware, `analyticsDaily` aggregates. Acceptance: non-owner -> 403; owner sees downloads/installs/scanRuns/errors/activations from real data; empty state renders honest zeros with "no data yet" action; no user-level PII; middleware test. Skills: vibe-auth-hardening, nextjs, a11y-debugging.

**E43. Firestore security rules + per-user isolation tests**
Files: `firestore.rules`, rules unit tests (emulator). Acceptance: user A cannot read user B's profiles/scans/devices (denied); owner role reads aggregates only; rules deploy clean; CI job runs emulator tests. Skills: firebase_firestore, zero-trust-security-hardening, test-driven-development.

---

## F. AI, help center, quality (M4-M5)

**F44. "Why is my game stuttering?" assistant grounded in known-issues catalog**
Files: `docs/help/stuttering.md`, known-issues catalog `docs/help/catalog.json` (cited), assistant component, `POST /api/ai/chat`. Acceptance: catalog has >= 15 cited issues; assistant refuses out-of-catalog system fixes (test); Arabic+English; free 5/day enforced server-side; eval set green. Skills: ai-sdk, gemini-api-dev, modern-ui-ux-design-system.

**F45. AI explainer for scan findings (rephrase only, rules decide)**
Files: explainer v2 with ai-proxy; findings catalog. Acceptance: AI never upgrades an "avoid" to "safe" (test); safety label always from rules engine; outputs cached; evals Arabic+English green; kill switch `AI_ENABLED` honored. Skills: ai-sdk, test-driven-development, owasp-vulnerability-shield.

**F46. Full quality sweep: five states, 4 themes, a11y, Lighthouse 90+, screenshots, e2e**
Files: all screens audited; `tests/e2e/` (Playwright); screenshot set 320/390/768/1280/1920 px LTR+RTL light+dark. Acceptance: axe 0 violations; Lighthouse mobile >= 90 P/90 A; zero horizontal overflow; every screen shows all five states in evidence folder; Arabic copy reviewed by native reader checklist. Skills: a11y-debugging, chrome-devtools, react-best-practices, shadcn, verification, review-agent, emil-motion-impeccable.

**F47. Honest-claims sweep across repo (README, site, help, store copy)**
Files: full copy audit; lint A9 enforced. Acceptance: zero unsupported performance claims; every claim links benchmark or is removed; grep for banned phrases ("boost", "guaranteed", "best") returns only quoted competitor complaints. Skills: open-seo-auditor, legal-compliance-shield, karpathy-skills.

**F48. Release: signed installer, checksums, dual-host portal deploy, legacy retirement**
Files: release pipeline, `CHANGELOG.md` (1.0.0), GitHub release with SHA-256 manifest; Firebase Hosting + Vercel deploys. Acceptance: fresh VM install-to-mapped < 5 min; both hosts 200 with same build; legacy folders moved to `old projects/` only at M6 after owner confirms; retro report with real numbers. Skills: deployments-cicd, vercel-cli, firebase_hosting_basics, review-agent, direct-action-shield.

---

## Sequencing notes

- Milestones: A (M0-M1 entry) -> B (M0) -> C (M1-M2) -> D (M2) -> E (M3) -> F (M4-M6). Items cross-reference the plan's M0-M6 gates (plans/sir-controller.md section 17).
- Nothing here starts before the owner authorizes build (PLANNING ONLY, 2026-11-12).
- Each task updates `.sir/CHECKPOINT.md` and the ticks in `.sir/TASKS.md` when executed; reports go to `D:\Projects\_SIR\ops\agy-runs\reports\<task>.md`.
