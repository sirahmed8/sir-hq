# AHome R5 Report: Evening Banner Elimination & Telegram Bot Plain-Language Overhaul

**Agent**: Antigravity (Gemini)  
**Date**: 2026-11-09 03:52 (Pass 76)  
**Target Repository**: `D:\Projects\AHome`  
**Status**: Completed & Verified  

---

## 1. Directive Breakdown & Executed Actions

### 1.1 Delete Evening Greeting Banner Card 'مساء الورد' with 'تمام' Button Everywhere
- **Root Cause Analysis**:
  - The banner was broadcasted through Firebase Realtime Database at `shared_broadcasts/active_banner` and statically embedded as a fallback across tabs via `<DynamicBroadcastBanner>` components with IDs like `page_banner_today_v1`, `page_banner_notes_v1`, `page_banner_arcade_v1`.
  - When mounted, it displayed an intrusive full-width banner containing "مساء الورد" or generic greeting text with a "تمام" action button that cluttered the mobile experience.
- **Remediation**:
  1. Purged the banner from Firebase Realtime Database at `shared_broadcasts/active_banner` via an administrative script.
  2. Updated `scripts/ingest_all_dynamic_data.py` to ensure `shared_broadcasts/active_banner` is deleted and never repopulated with unrequested greeting strings.
  3. Added an explicit rejection filter in `apps/web/src/components/ui/DynamicBroadcastBanner.tsx`:
     ```tsx
     if (
       banner.message?.includes("مساء الورد") ||
       banner.message?.includes("مساء الخير") ||
       banner.message?.includes("صباح الورد") ||
       banner.message?.includes("صباح الخير") ||
       banner.id?.startsWith("page_banner_")
     ) {
       return null;
     }
     ```
  4. Completely removed `<DynamicBroadcastBanner>` and its import from all tabs where it was unrequested:
     - `apps/web/src/components/tabs/TodayTab.tsx`
     - `apps/web/src/components/tabs/ChatTab.tsx`
     - `apps/web/src/components/tabs/ArcadeTab.tsx`
     - `apps/web/src/components/tabs/DatesTab.tsx`
     - `apps/web/src/components/tabs/LifeTab.tsx`
     - `apps/web/src/components/tabs/MemoriesTab.tsx`
     - `apps/web/src/components/tabs/NotesTab.tsx`
     - `apps/web/src/components/tabs/SettingsTab.tsx`
     - `apps/web/src/components/tabs/VoiceAIStudioTab.tsx`
     - `apps/web/src/components/watch/CinemaPage.tsx`
  5. Verified on a 390px mobile viewport: screenshot saved at `D:/Projects/_SIR/ops/agy-runs/reports/ahome_today_390px.png`. Zero banner artifacts remain.

---

### 1.2 Telegram Bot Texts Plain-Language & Gender Rewrite
- **Owner Directive**: The previous bot texts were overly technical and complicated (mentioning Local Core, APK, PWA, Firebase, Vercel). Rewrite EVERY bot message, command description, and reply in very simple warm Arabic with no technical words (say "التطبيق" not APK/PWA; no hosting names), short, with at most 5 commands shown in `/start`, strictly gender-aware (Ahmed masculine, Habiba feminine). Antigravity owns all bot code now.
- **Remediation**:
  1. In `infra-daemons/telegram_commands.py`:
     - Rewrote `/start` to display warm greeting and exactly 5 essential commands: `/today`, `/app`, `/status`, `/privacy`, `/help`.
     - Rewrote `/app` to provide simple links and PWA home-screen guidance without mentioning Vercel, Firebase, APK, or PWA jargon.
     - Rewrote `/help`, `/status`, `/privacy`, `/newchat`, `/mode`, `/kitty`, `/games`, and `/banner` in warm, caring Egyptian/standard Arabic tailored specifically to the recipient.
     - Strictly gender-differentiated:
       - Ahmed (masculine): `أهلاً بيك يا أحمد`, `اسأل في أي وقت`, `شوف تذكيراتك`, `اكتب /app`.
       - Habiba (feminine): `أهلاً بيكي يا حبيبة`, `اسأليني أي سؤال`, `شوفي تذكيراتك`, `اكتبي مثلاً`, `نورتي بيتك`.
  2. In `infra-daemons/telegram_dispatch.py`:
     - Purged phone emoji from APK document caption (`caption="ملف تثبيت التطبيق لهاتفك"`).
  3. Restarted bot daemon via `powershell scripts/restart-daemons.ps1`. Confirmed daemon log: `Bot authenticated: Personal1AI1Bot`.

---

## 2. Test Verification

1. **Telegram Command & Gender Test Suite**:
   ```
   D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe -m pytest tests/test_telegram_gender_and_commands.py -v
   ============================== 8 passed in 4.59s ==============================
   ```
2. **Bot Commands Integration Suite**:
   ```
   D:\Projects\AHome\apps\local-core\.venv\Scripts\python.exe -m pytest tests/test_bot_commands.py -v
   ============================= 12 passed in 2.48s ==============================
   ```
3. **Core Pytest Full Suite**:
   - **1006 tests passed, 0 failures**.

---

## 3. Evidence Artifacts
- Screenshot (390px mobile viewport, clean interface without evening greeting banner):
  `D:\Projects\_SIR\ops\agy-runs\reports\ahome_today_390px.png`
