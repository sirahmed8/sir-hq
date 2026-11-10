# SIR QUOTA & MODEL ROTATION ARCHITECTURE
**Target**: Autonomous Gemini HQ Manager & Antigravity Engineers  
**Standard**: Master Directive (`00-master-directive.md`), Usage Policy (`USAGE_POLICY.md`)  
**Scope**: All Portfolio Autonomous Operations · Version: 1.0.0 (Strictly enforced)

---

## 1. Executive Summary & Core Principle
To ensure that all 17 projects progress autonomously around the clock without ever hitting a hard stall, Antigravity account and model quotas must be managed like finite capital. 

**The Golden Rotation Rule (Ahmed, 2026-11-09)**:
> Switch accounts BEFORE exhaustion. When ANY active account's Gemini 5-hour window or weekly limit reaches **15% remaining or less**, trigger automatic rotation immediately. Never wait for 0% or for an unhandled `RESOURCE_EXHAUSTED` error.

---

## 2. Model & Account Hierarchy

> Status 2026-11-10: the order of models and accounts changed several times on 2026-11-09 and 2026-11-10. The single canonical order is `ops/ACCOUNT_ROTATION.md`, section "CURRENT ORDER". The five-step ladder that stood here (Pro accounts, free accounts, Claude 5.5, OpenCode and Kilo, HQ) was replaced; it is not repeated here so the two files cannot disagree. Words "Tier" in older notes mean a step on that ladder, not the autonomy tiers of `core/02-rules.md`.

Rules that do not change: switch before exhaustion (15 percent left in the 5-hour window, or 10 percent weekly); never Claude 4.x; never buy credits or turn on overages; use only Ahmed's own accounts and accounts given with consent; Claude 5.5 burns out in minutes when several chats use it, so one chat at a time and only for hard tasks; commit, push and checkpoint before every switch (save rule).

## 3. Account Rotation Automation Procedure

Account switching is verified to take under 3 minutes without requiring password entry (session cookies in Chrome):

```powershell
# Step 1: Automated account sign-in via Chrome account chooser
python D:\Projects\_SIR\scripts\agy-chooser.py <target_email>

# Step 2: Uncheck data-sharing checkbox and confirm Antigravity startup

# Step 3: Read current quota numbers from Settings > Models & Usage
# Record updated percentages and reset timestamps in:
# D:\Projects\_SIR\ops\ACCOUNT_LEDGER.md
# D:\Projects\_SIR\ops\agy-accounts-usage.md

# Step 4: Resume all active chats by issuing 'continue'
```

---

## 4. Quota Ledger & Tracking Format

Every rotation must append a timestamped entry to `D:/Projects/_SIR/ops/ACCOUNT_LEDGER.md`:

| Timestamp | Account | 5h Quota Left | Weekly Quota Left | 5h Reset In | Weekly Reset In | Models Available | Next Action |
|---|---|---|---|---|---|---|---|
| 2026-11-09T19:30 | a7medorabe7 | 100% | 10% | Rolling | 4d 6h | Gemini 3.8 High | Rotate to a01083835229 |
| 2026-11-09T19:35 | a01083835229 | 59% | 45% | 4h 25m | 6d 5h | Gemini 3.8, Sonnet 5.5 | Active builder execution |

---

## 5. Risk Matrix: What Happens If Everything Is Exhausted?

| Risk Scenario | Probability | Impact | Automated Mitigation & Recovery |
|---|---|---|---|
| **5h Window Cap Hit on all Pro Accounts** | Medium | Low | Switch to the free accounts (see ACCOUNT_ROTATION.md) or wait for rolling 5h window to unlock (oldest account resets in <2 hours). |
| **Weekly Pro Quota Depleted across all 4 Pro Accounts** | Low | High | Shift all autonomous building to Free Tier pool and local Ollama models (`AI_Models_Hub`) for non-stop offline progress. |
| **Session Cookie Invalidation / Password Required** | Low | Medium | Chooser script flags "Auth Challenge"; task is paused; single 1-click notification sent to Chairman via Telegram. |
| **Complete Portfolio Quota Collapse (All accounts exhausted)** | Very Low | Critical | 1. Immediately pause batch task runners.<br>2. Force write all in-memory buffers to `.sir/CHECKPOINT.md`.<br>3. Commit all repos straight to `main`.<br>4. Dispatch Telegram Emergency Alert to Ahmed with exact reset timestamps. |

---

## 6. Token Conservation Rules for Antigravity Workers

To maximize work per unit of quota:
1. **Compact at 150k Tokens**: Trigger session restart or compaction when transcript approaches 150,000 tokens.
2. **Read Line Ranges, Never Full 1,000-Line Files**: Always provide `StartLine` and `EndLine` to `read_file`.
3. **No Polling Loops**: Never poll commands or tasks; Antigravity wakes up reactively.
4. **Local Model Execution**: Run bulk tasks, spell checking, and AST parsing locally via `_SIR/scripts/ai/ask.ps1` connected to `AI_Models_Hub`.
