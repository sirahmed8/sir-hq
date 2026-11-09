# Round 9 Self-Review Report: AHome [التطبيق الخاص]
**Auditor**: Antigravity (Gemini 3.8 Flash High)
**Date**: 2026-11-09 07:20
**Scope**: Mandated Round 9 Self-Review (Private Couple Sanctuary — Exempt from Cross-Chat Review)
**Device**: Xiaomi RubyPro HyperOS (`ronf6d5hrkqsuoaa`) via ADB & Chrome CDP (PID 30645)

---

## 1. 30-Prompt AI Benchmark Pass / Fail Numbers
Evaluated using the automated test suite in `apps/local-core/tests/ai_eval/run_eval.py` against local Ollama models on loopback (`http://127.0.0.1:11434`):

| Config / Profile | N | TTFT (Median) | Total (Median) | Total (P90) | Tokens/s | Timeouts | Repetitive Loops | Lang Ok % | Length Ok % | Correct % (N) |
|---|---|---|---|---|---|---|---|---|---|---|
| **legacy_routed** | 30 | 0.55 s | 2.36 s | 14.22 s | 17.75 | 0 | 0 | 100.0% | 100.0% | **87.5% (21/24)** |
| **q15_a** | 30 | 0.21 s | 0.36 s | 0.70 s | 133.20 | 0 | 1 | 100.0% | 100.0% | **79.2% (19/24)** |
| **q15_b** | 30 | 0.21 s | 0.40 s | 1.05 s | 134.60 | 0 | 0 | 100.0% | 96.7% | **75.0% (18/24)** |
| **q8_a** | 30 | 0.44 s | 1.14 s | 4.14 s | 21.00 | 0 | 0 | 89.3% | 100.0% | **75.0% (18/24)** |
| **q8_b** | 30 | 0.43 s | 1.33 s | 4.83 s | 21.10 | 0 | 0 | 89.3% | 100.0% | **83.3% (20/24)** |
| **q8_legacyprompt**| 30 | 0.43 s | 1.15 s | 5.42 s | 20.95 | 0 | 0 | 82.1% | 100.0% | **79.2% (19/24)** |

### Qualitative Analysis: What Still Sounds Wrong or Fails
1. **Context Overwrite on Prior Bias (`ar11`)**:
   - *Prompt*: User states `"اسمي سلمى وبحب القهوة."`, followed by assistant greeting, then user asks `"إيه اسمي؟"`.
   - *Failure*: In smaller models (`qwen2.5:1.5b`), the model responded `"اسمك هو أحمد."` because system-prompt default biasing toward Ahmed overpowered the conversation history context.
   - *Remediation*: Explicit history turn weighting and strict session participant priming in system prompt for multi-turn chats.
2. **Nonsense Rejection Failure (`ar10`)**:
   - *Prompt*: `"كام لون في طعم الصوت؟"` (nonsense query).
   - *Failure*: Model hallucinated poetics: `"الأصوات الأفريقية تأتي غالبًا بطعم الرمال."` instead of identifying the prompt as a nonsensical category error.
   - *Remediation*: Add gentle common-sense sanity calibration for sensory mixed-metaphor detection.
3. **Regex Nuance in Arabic Polite Rewrites (`ar07`)**:
   - *Prompt*: `"اكتب الجملة دي بشكل مهذب أكتر: «هات الملف بسرعة»"`.
   - *Reply*: `"أرجو أن ترسل الملف بسرعة."`
   - *Assessment*: While semantically polite, the regex expected colloquial Egyptian polite tokens (`من فضلك`, `لو سمحت`), causing an automated test deduction despite human acceptability.

---

## 2. Notification Channels Verification on Phone (ADB)
Verified live on connected phone `ronf6d5hrkqsuoaa` via `adb shell dumpsys notification --noredact`:

```text
NotificationChannel{mId='ahome_v2_calendar', mName=التقويم والمناسبات, mImportance=4}
NotificationChannel{mId='ahome_v2_prayers', mName=مواقيت الصلاة, mImportance=4}
NotificationChannel{mId='ahome_v2_chat', mName=رسائل المحادثة, mImportance=4, mLights=true}
NotificationChannel{mId='ahome_v2_security', mName=أمان الحساب والجهاز, mImportance=4}
NotificationChannel{mId='ahome_v2_app_status', mName=حالة التطبيق والاتصال, mImportance=2}
NotificationChannel{mId='ahome_v2_couple_moments', mName=لحظاتنا المشتركة, mImportance=3}
NotificationChannel{mId='ahome_v2_study_exams', mName=أوقات المذاكرة والامتحانات, mImportance=4}
NotificationChannel{mId='ahome_v2_medicine', mName=مواعيد الدواء والصحة, mImportance=4}
NotificationChannel{mId='ahome_v2_reminders', mName=التذكيرات والمواعيد, mImportance=4}
NotificationChannel{mId='ahome_v2_calls', mName=المكالمات الواردة, mImportance=4, mLights=true}
NotificationChannel{mId='ahome_v2_tasks', mName=المهام المشتركة, mImportance=3}
NotificationChannel{mId='ahome_v2_voice', mName=الرسائل الصوتية, mImportance=4}
```

- **Cleanliness**: 0 emoji, 0 English brackets, 100% Arabic native titles.
- **Waveform Vibrations**: Configured via `getChannelVibrationPattern` in `MainActivity.java` with distinctive tactile pulses per channel.
- **In-App Customization**: Verified in **Settings > Notification Preferences** with Web Audio tone preview and native vibration bridge.

---

## 3. Responsive Multi-Viewport & Layout Audit
Audited live across 320 px (Foldable Cover), 390 px (Standard Phone), and 768 px (Tablet Portrait):

- **Live Device CDP Query (Phone `ronf6d5hrkqsuoaa`)**:
  - `dir`: `"rtl"`
  - `lang`: `"ar-EG"`
  - `innerWidth`: `392`
  - `scrollWidth`: `392`
  - `overflow`: `false` (0px horizontal overflow, perfect edge clipping).
- **Keyboard Handling**:
  - Chat input box in both Normal Chat and AI Studio Chat is structured as a relative flex column child inside `100dvh` container driven by `--vvh: 724px`.
  - Zero `position: fixed` bottom overlap hacks; composer remains immediately above the software keyboard upon focus.
- **Touch Ergonomics**: All actionable buttons (island, send, tabs, quick-add) maintain >= 44px tap targets with tactile active feedback.

---

## 4. Habiba's Private Corner & Privacy Invariant
- **Notice Verified**: Prominently displayed in `HabibaPrivateCorner.tsx`:
  > *"يرى أحمد ملخصاً لطيفاً لرعايتكِ مما تسجلينه هنا فقط، ولا يرى ملاحظاتكِ الخاصة أبداً."*
- **Default State**: Care summary sharing is ON by default so Ahmed receives loving support recommendations and prayer exemptions without requiring manual configuration, while private notes are strictly local and encrypted.
- **Control**: An instant toggle switch allows pausing or resuming sharing at any time.
- **Reporting Invariant**: Only counts and telemetry are reported to HQ. Zero personal messages, notes, calendar entries, or health details ever leave the local device or enter git logs.

---

## 5. Perpetual Loop Cycle 4 Battery Optimization Summary
- **Chat Outbox**: Stopped unthrottled 1000ms polling when outbox is empty, saving 86,400 daily empty loop executions.
- **Presence Heartbeat**: Automatically suspends 25-second RTDB pings when tab is hidden; immediately resumes on visible.
- **Screen WakeLock**: Added `useScreenWakeLock` across Cinema playback, guided breathing sessions, and Pomodoro study timers to prevent unwanted screen dimming.
- **Audio DSP Coprocessor**: Suspends `AudioContext` on page hide to allow hardware audio DSP sleep.

---

## 6. Verification Status & Production Deploys
- `scripts/verify.ps1`: **100% all green**.
  - 1006 / 1006 Python core tests pass.
  - 871 / 871 Web unit tests pass.
  - 0 TypeScript compiler errors.
  - 0 ESLint errors.
  - 0 Gitleaks findings across 315 commits.
  - 0 Privacy denylist matches across 948 files.
- Firebase Hosting: `https://ahmed-habiba.web.app` (105 files uploaded, release complete).
- Vercel Production: `https://ahmed-and-habiba.vercel.app` (Aliased, build successful).
- Debug APK: `apps/web/public/downloads/AHome-v1.0.0.apk` (sha256 `2b998707...`, 6.98 MB, installed on connected device).
