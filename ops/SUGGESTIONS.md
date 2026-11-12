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
**Status:** pending
**Id:** sug-or-html-simplex-tableau-svg-has--ed3bbf7f

---
## 2026-11-12T04:45 | SIR Jobs | medium

**Finding:** The two search inputs (#pipeline-search, #jobs-search) still show hardcoded English placeholders and aria-labels in Arabic mode — live probe at 390px AR shows placeholder 'Filter applications...' and 'Filter by skill (React, Python, AI)...' with dirCss rtl, while the palette input correctly localizes to 'اكتب أمراً أو ابحث...'
**Evidence:** src/public/index.html:156 and :225 lack data-i18n-placeholder/data-i18n-aria-label (contrast :698 which has it); no matching keys in src/public/i18n/{en,ar}.json; D:/Projects/_SIR/ops/scout-evidence/scout-ar-390-openings-search.png + INPUT-STATE probe output (dirCss:'rtl', placeholder English)
**Proposed Brief:** r43-jobs-search-i18n-placeholders
**Project:** SIR Jobs
**Severity:** medium
**Category:** bug
**Status:** pending
**Id:** sug-the-two-search-inputs-pipeline-s-ff484c83

---
## 2026-11-12T04:45 | SIR Jobs | medium

**Finding:** No text input does per-character bidi detection: every input/textarea inherits direction:rtl in Arabic mode with dir attribute null, so typing Latin company names or mixed notes keeps RTL caret/alignment — violates shared lesson L8 (live per-char direction, dir=auto or equivalent)
**Evidence:** INPUT-STATE probe: pipelineSearch/jobsSearch/palette all {dir:null, dirCss:'rtl'}; inputs at src/public/index.html:156,225,698 and textarea src/public/js/views/proposals.js:137 have no dir attr; grep finds no input-direction code in src/public/js (only output-side bdiHtml in i18n.js:64)
**Proposed Brief:** r43-jobs-input-bidi-live
**Project:** SIR Jobs
**Severity:** medium
**Category:** bug
**Status:** pending
**Id:** sug-no-text-input-does-per-character-7ece94d0

---
