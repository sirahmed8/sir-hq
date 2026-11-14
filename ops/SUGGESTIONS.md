# Suggestions from Scouts (HQ)

Scouts append findings here daily. HQ (manager) reads each watch, approves good items by running `scripts/queue-add.py`, and rejects the rest with a reason in this same file. Items the owner rejects through Telegram buttons are recorded in `ops/suggestion-rejects.json` and never proposed again.

Format: `## <timestamp> | <project> | <severity>` then Finding, Evidence, Proposed Brief, Project, Severity, Category, Status (pending/approved/rejected), HQ Note, Id.

---

## 2026-11-12T04:37 | SIR Study | high

**Finding:** 14 study tables across 7 guide pages (data-structures, sad, or, human-rights, business-admin, hci, electronics) are 1.6x-4.3x wider than their .table-responsive wrapper at 320/390px (e.g. electronics 'نوع المادة' table 1052px in a 254px wrap), forcing horizontal scrolling to read cell labels with no scroll affordance - violates shared lesson L4 which requires card layout for narrow tables on phones.
**Evidence:** D:/Projects/_SIR/ops/scout-evidence/scout-mobile-refined.json (tableW vs wrapW per page); guides/electronics.html:411-417,760-781 (.table-responsive is overflow-x:auto with no mobile card fallback); screenshots refined-elec-320-rtl.png, refined-ds-320-rtl.png
**Proposed Brief:** r43-study-mobile-card-tables
**Project:** SIR Study
**Severity:** high
**Category:** bug
**Status:** done
**HQ Note:** queued as r43-study-mobile-card-tables (HQ auto-approved: clear defect); fixed: data-label on every table cell + @media (max-width:390px) card CSS + test_13 in tests/test_browser.py
**Id:** sug-14-study-tables-across-7-guide-p-a4bcbc34

---
## 2026-11-12T04:37 | SIR Study | medium

**Finding:** or.html SIMPLEX tableau SVG has inline min-width:580px inside a 212px-wide wrapper at 320px viewport, so ~63% of the diagram is hidden behind horizontal scroll and its labels are unreadable on phones.
**Evidence:** guides/or.html:2795-2796 (<div style="width:100%;overflow-x:auto"> wrapping <svg viewBox="0 0 620 220" style="width:100%;min-width:580px">); probe output 'or 320 ltr div clientW=212 scrollW=580' in D:/Projects/_SIR/ops/scout-evidence/scout-mobile-refined.json; screenshot refined-or-320-rtl.png
**Proposed Brief:** r43-study-or-svg-minwidth
**Project:** SIR Study
**Severity:** medium
**Category:** bug
**Status:** approved
**HQ Note:** queued 2026-11-12 as r45 scout fixes
**Id:** sug-or-html-simplex-tableau-svg-has--ed3bbf7f

---
## 2026-11-12T04:45 | SIR Jobs | medium

**Finding:** The two search inputs (#pipeline-search, #jobs-search) still show hardcoded English placeholders and aria-labels in Arabic mode — live probe at 390px AR shows placeholder 'Filter applications...' and 'Filter by skill (React, Python, AI)...' with dirCss rtl, while the palette input correctly localizes to 'اكتب أمراً أو ابحث...'
**Evidence:** src/public/index.html:156 and :225 lack data-i18n-placeholder/data-i18n-aria-label (contrast :698 which has it); no matching keys in src/public/i18n/{en,ar}.json; D:/Projects/_SIR/ops/scout-evidence/scout-ar-390-openings-search.png + INPUT-STATE probe output (dirCss:'rtl', placeholder English)
**Proposed Brief:** r43-jobs-search-i18n-placeholders
**Project:** SIR Jobs
**Severity:** medium
**Category:** bug
**Status:** approved
**HQ Note:** queued 2026-11-12 as r45 scout fixes
**Id:** sug-the-two-search-inputs-pipeline-s-ff484c83

---
## 2026-11-12T04:45 | SIR Jobs | medium

**Finding:** No text input does per-character bidi detection: every input/textarea inherits direction:rtl in Arabic mode with dir attribute null, so typing Latin company names or mixed notes keeps RTL caret/alignment — violates shared lesson L8 (live per-char direction, dir=auto or equivalent)
**Evidence:** INPUT-STATE probe: pipelineSearch/jobsSearch/palette all {dir:null, dirCss:'rtl'}; inputs at src/public/index.html:156,225,698 and textarea src/public/js/views/proposals.js:137 have no dir attr; grep finds no input-direction code in src/public/js (only output-side bdiHtml in i18n.js:64)
**Proposed Brief:** r43-jobs-input-bidi-live
**Project:** SIR Jobs
**Severity:** medium
**Category:** bug
**Status:** approved
**HQ Note:** queued 2026-11-12 as r45 scout fixes
**Id:** sug-no-text-input-does-per-character-7ece94d0

---
## 2026-11-14T04:04 | SIR Study | high

**Finding:** The closed side drawer is hidden only by CSS transform (translateX off-screen) with no visibility:hidden, aria-hidden or inert, so all ~12 drawer links/buttons remain in the keyboard Tab order and accessibility tree on every page; Tab trace shows drawer-brand, drawer-close-btn and drawer-nav-items as stops 9-15+ before main content is reached.
**Evidence:** D:/Projects/_SIR/ops/scout-evidence/scout-a11y-20261114.json tab_first15 for hub/data-structures/sad/or/electronics; guides/study-r11.css:369-394 (.side-drawer has no closed-state visibility rule, unlike .settings-modal at study-r11.css:206-233 which correctly uses visibility:hidden); guides/study-shell.js:79-93 toggleSideDrawer toggles only .open class
**Proposed Brief:** r82-study-drawer-hidden-from-taborder
**Project:** SIR Study
**Severity:** high
**Category:** bug
**Status:** approved
**HQ Note:** queued as r82-study-drawer-hidden-from-taborder (HQ auto-approved: clear defect)
**Id:** sug-the-closed-side-drawer-is-hidden-b425c23f

---
## 2026-11-14T04:04 | SIR Study | medium

**Finding:** Guide pages skip heading levels: content uses h2.card-title sections but subheads are h5, producing h2->h5 skips (9 on data-structures, 13 on electronics) and confusing screen-reader outline navigation.
**Evidence:** scout-a11y-20261114.json headingSkips counts; guides/data-structures.html:2386 (h2) -> :2448/:2457 (h5); guides/electronics.html:2222 (h2) -> :2276 (h5)
**Proposed Brief:** r82-study-heading-level-hierarchy
**Project:** SIR Study
**Severity:** medium
**Category:** bug
**Status:** pending
**Id:** sug-guide-pages-skip-heading-levels--b51a3b52

---
## 2026-11-14T04:04 | SIR Study | low

**Finding:** The 'ابدأ المذاكرة' streak CTA link on the hub renders at 68x24px, below the 44px minimum touch target, and is appended inline after the streak sentence so it is easy to miss for keyboard/touch users.
**Evidence:** scout-a11y-20261114.json hub audit.small [{w:68,h:24,cls:'streak-cta'}]; guides/START_HERE.html:959-968 (.streak-cta has no min-height) and :3009 (injected inline into streak sub text)
**Proposed Brief:** r82-study-streak-cta-target
**Project:** SIR Study
**Severity:** low
**Category:** polish
**Status:** pending
**Id:** sug-the-streak-cta-link-on-the-hub-r-2f4ce05e

---
## 2026-11-14T04:37 | _SIR | high

**Finding:** AI chat toggle unmounts on open so keyboard focus is dropped to <body> and never moved into the dialog; on close, focus is not restored to the toggle, forcing keyboard users to re-tab through the whole page to reach the chat input.
**Evidence:** src/components/AIChat.tsx:342-358 ({!isOpen && <button>} unmounts, no focus effect); tab probe D:/Projects/_SIR/ops/scout-evidence/tabprobe.py output
**Proposed Brief:** r83-portfolio-chat-focus
**Project:** _SIR
**Severity:** high
**Category:** bug
**Status:** done
**HQ Note:** fixed by worker round r83 - focus moved into the AI chat dialog on open and back to the toggle on close (portfolio commit b3df4e0, pushed to main); status flipped after the fix shipped.
**Id:** sug-ai-chat-toggle-unmounts-on-open--814d358f

---
## 2026-11-14T04:37 | _SIR | medium

**Finding:** Chat textarea sets inline outline:none which overrides the global :focus-visible ring, so keyboard focus inside the AI chat input is invisible (WCAG 2.4.7).
**Evidence:** src/components/AIChat.tsx:264 (outline: "none") vs src/app/globals.css:112-115 (:focus-visible outline, not !important)
**Proposed Brief:** r84-portfolio-chat-focus-ring
**Project:** _SIR
**Severity:** medium
**Category:** bug
**Status:** pending
**Id:** sug-chat-textarea-sets-inline-outlin-7b4f89f0

---
## 2026-11-14T04:37 | _SIR | medium

**Finding:** Chat messages container is a plain div with no role=log or aria-live, so screen reader users get no announcement when the assistant replies.
**Evidence:** src/components/AIChat.tsx:398 (<div style={styles.messages}> has no live-region semantics)
**Proposed Brief:** r85-portfolio-chat-aria-live
**Project:** _SIR
**Severity:** medium
**Category:** bug
**Status:** pending
**Id:** sug-chat-messages-container-is-a-pla-e5917c86

---
## 2026-11-14T04:37 | _SIR | medium

**Finding:** Contact form has no submit button (send is an <a href={mailto}>), so pressing Enter inside the name/email fields does nothing; implicit submission requires a submit control.
**Evidence:** src/components/ContactForm.tsx:60-121 (form onSubmit exists but no <button type=submit>; only mailto/WhatsApp links and a copy button)
**Proposed Brief:** r86-portfolio-form-keyboard-submit
**Project:** _SIR
**Severity:** medium
**Category:** bug
**Status:** pending
**Id:** sug-contact-form-has-no-submit-butto-1c877930

---
## 2026-11-14T04:37 | _SIR | low

**Finding:** Header 'CV' nav link renders at 30px wide (43px for the Arabic 'حقائق' link), below the 44px touch-target bar (lesson L19); height is fine via min-h-11 but width is text-driven.
**Evidence:** D:/Projects/_SIR/ops/scout-evidence/scout-portfolio-a11y.json en-home/ar-home smallTargets; screenshots scout-portfolio-a11y-en-home-390.png
**Proposed Brief:** r87-portfolio-nav-target-size
**Project:** _SIR
**Severity:** low
**Category:** polish
**Status:** pending
**Id:** sug-header-cv-nav-link-renders-at-30-8527b66a

---
