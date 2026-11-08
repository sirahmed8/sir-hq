# Independent QA Report: Human-Computer Interaction (HCI) Midterm Study Pack (طرق اتصال الإنسان بالحاسب)

**Date**: 2026-11-08  
**Scope**: `D:/Projects/SIR Study/guides/hci.html`  
**Course**: طرق اتصال الإنسان بالحاسب (Human-Computer Interaction - HCI)  
**Course Code**: `CS212` (Second Year, First Term - معاهد العبور للهندسة والتكنولوجيا - شعبة علوم الحاسب)  
**Exam Date**: 18/11/2026 at 11:30 AM (مدرج 513)  
**Teaching Staff**: د. إسراء عيسى / د. جابر حسن | م. إسراء حديب  
**Status**: PASSED / VERIFIED ALL GREEN (0 CONSOLE ERRORS, 0 HORIZONTAL OVERFLOW AT 390PX)

---

## 1. Executive Summary

An exhaustive independent academic QA and code audit was conducted on the Human-Computer Interaction (HCI) midterm study pack (`guides/hci.html`). The pack was verified and hardened across three key areas:
1. **Technical & Factual Integrity**:
   - Corrected course code from the third-year code `CS 314` to the true second-year Obour CS curriculum code `CS212`.
   - Updated the instructional team metadata to accurately reflect both course professors (د. إسراء عيسى / د. جابر حسن) and teaching assistant (م. إسراء حديب).
   - Injected fundamental human cognitive and interaction design frameworks: Donald Norman's Execution-Evaluation Action Cycle (7 stages) & The Two Gulfs (Gulf of Execution and Gulf of Evaluation), HCI Empirical Laws (Fitts's Law, Hick-Hyman Law, Miller's $7 \pm 2$ Law, Doherty Threshold), Jakob Nielsen's 10 Usability Heuristics, Whitney Quesenbery's 5 E's, Crampton Smith & Kevin Silver's 5 Dimensions, the 4 core activities of the ID Lifecycle, and WCAG POUR accessibility principles.
2. **Curriculum Reconciliation & Bridging**:
   - Reconciled against original lecture text extractions under `D:/Projects/SIR Study/materials/_text/07 - طرق اتصال الإنسان بالحاسب (HCI)/`.
   - Verified that Lectures 2 and 3 duplicate Chapter 1 of Sharp, Rogers & Preece (2019).
   - Bridged the college archive gap where Lecture 5 is missing between Lecture 4 and Lecture 6 by synthesizing textbook-authentic conceptual design, interface metaphors, and interaction paradigms (WIMP, Direct Manipulation, Touch/Voice).
3. **Display, Accessibility & Mobile Usability (390px Viewport)**:
   - Evaluated live in Google Chrome via Chrome DevTools MCP on emulated 390x844 mobile viewport with touch emulation.
   - Cleared all console errors and deprecations (dynamic HTTP-only manifest loader, purged deprecated apple-mobile-web-app-capable meta tag, added unique `id` and `name` attributes to all form search inputs).
   - Confirmed zero horizontal overflow (`scrollWidth === innerWidth === 390px`) across all 6 tab panes.
   - Verified interactive flashcards (expanded to 24 with 3-way mastery filter: All, Need Review, Mastered) and quiz bank (expanded to 20 questions with live scoreboard and hardened regex answer checking).

---

## 2. Reconciled Sources & Curriculum Audit

| Source File / Subject | Source Type | Status | Content Verified & Integrated |
|---|---|---|---|
| `Lec 01 - Introduction to HCI.pdf.txt` | Lecture 1 | 100% Covered | CLI vs GUI (DOS vs Windows), usability disparities, elevator controls case, parking permit vending machine (convention violation), voicemail vs Bishop's Marble Answering Machine (1995), TiVo peanut remote ergonomics, smart TV interaction dilemma, 3 core design considerations. |
| `Lec 02` & `Lec 03` (`Chapter 1 - Sharp et al.`) | Lectures 2 & 3 | 100% Covered | Interaction Design definition, Winograd's definition, Whitney Quesenbery's 5 E's (Effectiveness, Efficiency, Engagement, Error Tolerance, Ease of Learning), Gillian Crampton Smith & Kevin Silver's 5 Dimensions (1D 1D-Words to 5D 5D-Behavior), Stanford d.school 5 Design Thinking phases (Empathize, Define, Ideate, Prototype, Test), contributing disciplines. |
| `Lec 04 - Usability and User Experience Goals.pdf.txt` | Lecture 4 | 100% Covered | Accessibility vs Inclusiveness, Impairments (Sensory, Physical, Cognitive; Permanent, Temporary, Situational), 6 Usability Goals vs UX Goals (Desirable vs Undesirable feelings), Donald Norman's Design Principles (Visibility, Feedback, Constraints, Consistency, Affordance, Mapping, Signifiers). |
| `Lec 05` (Curriculum Archive Gap) | Lecture 5 | 100% Bridged | Conceptual Models, Interface Metaphors (Desktop, Trash Can, Shopping Cart), Interaction Paradigms (WIMP, Direct Manipulation, Post-WIMP, Touch/Voice). |
| `Lec 06 - Understanding Users & UX.pdf.txt` | Lecture 6 | 100% Covered | User Experience definitions (Garrett & ISO 9241-210), iPod Nano Touch case study (wearable smartwatch precursor), Usability vs UI vs UX car analogy, Cultural differences in UX (IKEA Anna virtual assistant UK vs US), 4 core ID Lifecycle activities. |

---

## 3. Discrepancies Found & Surgical Fixes Applied

### A. Academic Course Code & Faculty Metadata
- **Before**: Header displayed `CS 314` (third-year course code) and listed single doctor name.
- **After**: Fixed to `CS212` (Second Year Computer Science, First Term) and updated staff to `د. إسراء عيسى / د. جابر حسن | م. إسراء حديب`.

### B. Missing Core HCI Frameworks
- **Before**: Cram sheet and lecture summary lacked explicit formulations for Norman's 7 stages of action, the two Gulfs, mathematical empirical laws, and Nielsen's heuristics.
- **After**:
  1. **Concept 7 Added**: Norman's Execution-Evaluation Cycle (Goal -> Plan -> Specify -> Perform -> Perceive -> Interpret -> Compare) and the Two Gulfs (Gulf of Execution bridged by Affordances/Signifiers/Mapping/Constraints; Gulf of Evaluation bridged by immediate Feedback).
  2. **Concept 8 Added**: HCI Empirical Laws:
     - Fitts's Law: $MT = a + b \log_2\left(\frac{2D}{W}\right)$ explaining why screen edges and corners have infinite virtual width ($W = \infty$).
     - Hick-Hyman Law: $T = b \log_2(n + 1)$ for decision time and progressive disclosure.
     - Miller's Law: $7 \pm 2$ chunks in working memory.
     - Doherty Threshold: $< 400\text{ ms}$ feedback latency to keep user attention engaged.
  3. **Concept 9 Added**: Jakob Nielsen's 10 Usability Heuristics with practical software examples.
  4. **Concept 10 Added**: The 4 Activities of Interaction Design Lifecycle (Establishing requirements, Designing alternatives, Prototyping, Evaluating).
  5. **Concept 11 Added**: WCAG Core Accessibility Principles (POUR: Perceivable, Operable, Understandable, Robust).

### C. Flashcards Bank Expansion & Mastery Filter
- **Before**: 20 flashcards, basic mastery toggle without view filtering.
- **After**:
  - Expanded to 24 flashcards (added cards on Fitts's Law, Gulfs of Action, Recognition vs Recall, and ID Lifecycle activities).
  - Added 3-way mastery filter (`الكل`, `بحاجة لمراجعة`, `تم إتقانها`) with dynamic real-time progress bar.
  - Updated tab count badge to 24.

### D. Simulation Quiz Bank Expansion & Regex Hardening
- **Before**: 14 questions, answer checker used loose `includes('true')` substring matching, missing recent syllabus topics.
- **After**:
  - Expanded to 20 questions (added Q15 on Fitts's Law screen edge physics, Q16 on Gulf of Evaluation, Q17 on Recognition vs Recall, Q18 on Interface Metaphors, Q19 on the 4 ID Lifecycle activities, Q20 on WCAG POUR).
  - Hardened `checkAnswer()` with regex `/checkAnswer\s*\(\s*this\s*,\s*true\s*,/` to prevent false positive matching.
  - Updated quiz badges and header to 20 questions.
  - Verified live score updates: `🎯 النتيجة: 0 من 20 (0%) • تم حل 0`.

### E. Console Errors & Zero-Deprecation Hardening
- **Before**:
  1. Opening via `file:///` provoked `ERR_FAILED` on static `<link rel="manifest" href="manifest.json">`.
  2. Chrome console warned `<meta name="apple-mobile-web-app-capable" content="yes"> is deprecated`.
  3. Form validation warned `A form field element should have an id or name attribute` on search inputs.
- **After**:
  1. Replaced static manifest tag with protocol-aware dynamic injection: `if (location.protocol.startsWith('http'))`. Manifest loads on hosted servers and avoids `file:///` CORS blocking.
  2. Purged deprecated apple meta tag, retained `<meta name="mobile-web-app-capable" content="yes">`.
  3. Assigned explicit `id="search-flashcards"` / `name="search-flashcards"` and `id="search-quiz"` / `name="search-quiz"`.
  4. Result: Exactly 0 console errors and 0 warnings.

---

## 4. Mobile Responsiveness & Interactivity Verification (390px Viewport)

Using Chrome DevTools MCP on emulated 390x844 mobile viewport with touch emulation:
- **Console Errors**: Exactly 0 console messages found on load and interaction.
- **Horizontal Overflow Test**: Evaluated `scrollWidth` vs `innerWidth` across all 6 tab panes:
  - `⚡ كبسولة الإنجاز (Cram Sheet)`: `scrollWidth: 390, innerWidth: 390, overflow: false`
  - `📚 ملخص المحاضرات (1-6)`: `scrollWidth: 390, innerWidth: 390, overflow: false`
  - `💼 الحالات والأجهزة (Cases)`: `scrollWidth: 390, innerWidth: 390, overflow: false`
  - `📇 بنك الكروت السريعة (24)`: `scrollWidth: 390, innerWidth: 390, overflow: false`
  - `📝 بنك الأسئلة (20)`: `scrollWidth: 390, innerWidth: 390, overflow: false`
  - `⏱️ خطة المذاكرة (Plan)`: `scrollWidth: 390, innerWidth: 390, overflow: false`
- **Interactive Verification**:
  - Flashcard flip test: `firstFlashcardFlipped: true`.
  - Q15 interactive answer test: Clicked option A ($W = \infty$) -> Green highlight applied, explanation rendered (`q15ExpVisible: true`), live score updated to `🎯 النتيجة: 1 من 20 (5%) • تم حل 1`.
  - State reset test: Cleaned test states via `resetGenericQuiz('sir_study_hci')` -> Score restored to `🎯 النتيجة: 0 من 20 (0%) • تم حل 0`.

---

## 5. Artifacts & Deliverables

- Hardened Guide: `D:/Projects/SIR Study/guides/hci.html`
- Full QA Report: `D:/Projects/_SIR/ops/agy-runs/reports/study-hci-qa.md`
- Mobile Viewport Snapshot: Resource offloaded and verified in step trajectory (`390x844` viewport).
- Git Commit Policy: Preserved uncommitted per brief instructions ("Commit nothing. This is a study aid only").
