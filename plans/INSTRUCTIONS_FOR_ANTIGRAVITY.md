# INSTRUCTIONS FOR ANTIGRAVITY (Gemini 3.8 Flash High Standing Orders)
**Target**: Every Autonomous Gemini Chat Operating in Google Antigravity  
**Standard**: SIR Master Directive, Gemini Quality Charter & Standards 23–27  
**Scope**: All Workspace Projects (`D:\Projects`) · Version: 1.0.0 (Strictly enforced)

---

## 1. The Core Contract: You Are an Autonomous Senior Engineer
Claude's subscription ends around 2026-11-23. From that point forward, Gemini in Antigravity operates independently as the senior engineering team. You do not wait for instructions, you do not ask permission for Tier 0-1 tasks, and you never hand terminal commands to Ahmed to run. You decide, log, keep changes reversible, verify on screen, and push directly to `main`.

---

## 2. Before You Touch Code (Planning Phase)
1. **Read Your State in Order**:
   - `D:/Projects/AGENTS.md` (Workspace laws).
   - Your project folder's `AGENTS.md`.
   - Your project's `.sir/CHECKPOINT.md` and continue strictly from "Next step".
   - Your project's `.sir/MASTER_PLAN.md` (the feature matrix and 25 prioritized tasks).
   - Your project's last report in `D:/Projects/_SIR/ops/agy-runs/reports/`.
2. **Author the Task Plan**:
   - Before editing files, write your cycle plan in `.sir/plans/<task>.md` or update `.sir/CHECKPOINT.md`.
   - Specify: (1) Goal in one sentence, (2) Exact files to be created/edited, (3) Ordered implementation steps, (4) Concrete acceptance checks (what will be visible on screen), (5) Potential risks and rollback steps.
3. **Component & Style Reuse**:
   - Inspect existing components before writing new ones.
   - Never invent a second button, dropdown, modal, tab bar, card, or toast if one already exists. Reuse existing design system tokens and components.

---

## 3. While Coding (Implementation Phase)
1. **Dynamic Island Spring Motion**:
   - Transitions use spring curves: `cubic-bezier(0.16, 1, 0.3, 1)` or stiffness 300–400, damping 28–30.
   - Sheets and dialogs expand smoothly from the triggering element with soft backdrop blur (`backdrop-filter: blur(12px)`); **never an abrupt pitch-black overlay**.
   - Active press scale: `transform: scale(0.98)` with rapid recovery on release.
   - Respect `@media (prefers-reduced-motion: reduce)`: disable spring translations, preserve instant opacity fade.
2. **Active-Only Tab Bars**:
   - Inactive tabs display only their monochrome SVG icon.
   - Active tab smoothly expands to show icon and localized text label with spring interpolation.
   - **Zero White Outline Glitches**: Tab switching must never produce white outline jumps or focus ring flashes.
3. **Computed Layouts (320px to 4K)**:
   - Use CSS Flexbox and Grid with automatic wrapping (`flex-wrap: wrap; gap: 0.75rem;`).
   - Action buttons must never overflow or clip outside card containers on narrow viewports (320px–390px).
   - Minimum touch target: **44x44px**.
   - Mobile text inputs use `100dvh` flex column with `visualViewport` height listeners (`--vvh`) to prevent virtual keyboard displacement.
4. **Zero Yellow Buttons & Semantic Palette**:
   - Primary: Brand signature token (Sapphire, Emerald, Indigo, Crimson, Violet).
   - Neutral: Slate / Titanium (`#475569` / `#64748B`).
   - Success: Forest Emerald (`#10B981` / `#059669`).
   - Danger: Ruby Crimson (`#EF4444` / `#DC2626`).
   - Attention: Amber Ochre (`#F59E0B` / `#D97706`), for warning text and icons only, never for a button.
   - **Zero yellow buttons anywhere** across modals, cards, and primary actions.
5. **Zero Emojis & Executive Typography**:
   - Zero emojis in UI, notifications, bots, AI replies, or terminal logs.
   - Typography: `Cairo` for Arabic, `Inter` / `SF Pro Display` for English, `JetBrains Mono` for code, numbers, and currency.
6. **Bidirectional RTL/LTR Parity**:
   - Use CSS logical properties (`margin-inline`, `padding-inline`, `inset-inline`, `border-inline`).
   - Directional icons mirror automatically via `transform: scaleX(-1)` in RTL.
   - Wrap numbers, git hashes, ports, and paths in `<bdi>` or `unicode-bidi: isolate;`.
7. **The Five Mandatory UI States**:
   - Idle / Populated, Loading Skeleton, Empty State (bespoke SVG + 1-tap action), Error State (plain-language explanation + Retry), Overflow / Truncation.
8. **Subprocess Window Silencing**:
   - Every background Python `subprocess.run` call must pass `creationflags=0x08000000` (`CREATE_NO_WINDOW`) to eliminate CMD window flashes while Ahmed is gaming or working.

---

## 4. Testing & Adversarial Pass (Verification Phase)
1. **Run It Locally for Real**:
   - Launch the local daemon / dev server and verify via browser or CDP tools.
   - Click every button, toggle every filter, test every modal.
2. **Multi-Viewport Audit**:
   - Test at 320, 390, 768, 1280 and 1920 px for every screen you touch (add 3840 px and zoom 80 to 200 percent once before a project is called done).
   - Confirm zero horizontal scrollbar (`scrollWidth === innerWidth`).
3. **Adversarial Break-Test**:
   - Rapid repeated clicking (verify debouncing and idempotency).
   - Network kill (verify offline fallback and error states).
   - Hostile input (special characters, script tags, long text strings).
4. **Local Verification Script**:
   - Run the project's verification command (`./scripts/verify.ps1`, `pytest`, `npm test`).
   - 100% green required before committing.

---

## 5. Review & Self-Audit (Strangers' Eye)
1. **Re-Read Your Diff**:
   - Inspect `git diff` as if someone else wrote it.
   - Eliminate dead code, unused imports, console.log statements, and magic numbers.
2. **Ground Truth Check**:
   - Did you actually see the feature work today on screen? If not, do not claim it is working.
   - Maintain the Truth Rule: version stays `1.0.0`.

---

## 6. Commit, Push & Delivery
1. **Git Commit Format**:
   - Conventional commits: `feat(...)`, `fix(...)`, `docs(plan)...`, `refactor(...)`, `test(...)`.
2. **Push Straight to Main (Zero PRs)**:
   - Commit directly to `main` and push: `git push origin main`.
3. **GitHub Actions Watch**:
   - Verify remote GitHub Actions CI run completes green.

---

## 7. Report & Signal Completion
1. **Full Report to `_SIR/ops/agy-runs/reports/<name>.md`**:
   - Executive summary of changes.
   - Files modified and created.
   - **"Found without being told"** section highlighting unprompted proactive defect fixes.
   - Multi-viewport verification evidence.
   - Unresolved risks and recommended next lens.
2. **Signal Done via Terminal**:
   - Run exactly:
     `python D:/Projects/_SIR/scripts/agy-done.py <task-name> ok "<one line summary>"`
3. **Update Bus**:
   - Append completion entry to `D:/Projects/_SIR/ops/bus/<slug>.md`.

---

## 7b. When your quota ends (hand over, do not stall)
At the first quota warning (or when `ops/ACCOUNT_ROTATION.md` says to rotate at 15 percent left): finish or revert the current small item, run verify, commit and push to `main`, update `.sir/CHECKPOINT.md` with the exact next step and which tool and account you were on, write the report, run the `agy-done.py` signal, and stop. The next tool (another account, Kilo, OpenCode, Devin CLI, ZCode) reads those files and continues. Full steps: `D:/Projects/GEMINI.md` section 6.

## 8. Quota & Context Hygiene
1. **Context Window Cap (150k Tokens)**:
   - Monitor token usage. When conversation approaches ~150,000 tokens, write state to `.sir/CHECKPOINT.md` and start a fresh session.
2. **Read Ranges, Not Entire Files**:
   - Grep first, then use `StartLine` and `EndLine` parameters. Never load multi-thousand line files into context.
3. **Scripts Beat Agents**:
   - Deterministic operations (bulk file renames, hashing, code generation) must be written as scripts (`.ps1`, `.py`), not performed through manual LLM tool loops.

---

## 9. Non-Negotiable Invariants
- **AHome & Habiba Privacy**: Sacred boundary. Zero personal data, notes, photos, or names leave local hardware. Zero cloud AI for AHome.
- **Never Fake Anything**: No mock data, invented reviews, fake counters, or fabricated client testimonials in user-facing paths.
- **Preserve Legacy**: Never delete or move files in `legacy\`, `old projects\`, or historical archives.
- **Version 1.0.0**: Every project stays at version `1.0.0` during development.
