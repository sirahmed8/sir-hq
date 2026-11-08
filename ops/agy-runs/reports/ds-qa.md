# Independent QA Report: Data Structures Midterm Study Pack (CS211)

**Date:** 2026-11-08 (Exam: 11:30 AM Cairo Time, Hall 533)  
**Target:** `guides/data-structures.html`  
**Course:** CS211 Data Structures — Higher Obour Institute (Lecturer: Dr. Ashraf Heikal)  
**Auditor:** Antigravity (SIR Quality Assurance)  
**Verdict:** **PASS WITH FIXES** (All critical bugs resolved, verified with GCC 16.2.0, HTML/CSS/JS validated)

---

## 1. Executive Summary
An independent quality assurance audit was conducted on the Data Structures midterm study guide (`guides/data-structures.html`) against official course lecture materials, cram guides, and the Malhotra textbook. Five confirmed technical bugs (including C++ compiler syntax errors and visual arrow inversions) were fixed directly in `guides/data-structures.html`. Six coverage gaps were closed to align 1:1 with Dr. Ashraf Heikal's exam scope.

---

## 2. Lecture Sources Inspected & Curriculum Discrepancies
1. **`Lec 01 - Algorithms Analysis.pdf` (37 slides):**
   - Verified: Big-O definitions, time/space trade-offs, step counts.
   - Gap identified: Asymptotic triad ($\Omega$, $\Theta$) and formal constant proof ($T(n) = 5n + 4 \le cn$) were missing from Tab 1.
2. **`Lec 02 - Recursion.pdf` (31 slides):**
   - Verified: Base condition, recursive call stack, activation records.
   - Gap identified: Algorithm vs. Program distinction and Tower of Hanoi ($2^n - 1$ moves) omitted.
3. **`Lec 03 - Stack Data Structure.pdf` (39 slides):**
   - Verified: LIFO, overflow/underflow, array vs. linked representations.
   - Gap identified: Historical context of Polish notation (Jan Łukasiewicz), prefix conversion, and specific lecture numerical examples omitted.
4. **`Lec 04 - Queue Data Structure.pdf` (Moodle Upload Discrepancy):**
   - *Audit Finding:* The file uploaded to Moodle as `Lec 04 - Queue Data Structure.pdf` contains slides titled "Lecture 06 - Linked Lists".
   - *Resolution:* Queue curriculum was verified directly against the official 7-page Cram Guide (`دليل_المراجعة_الشاملة_والتحضير_للميدترم_هياكل_البيانات.pdf`) and Malhotra Textbook Chapter 5. A transparency notice was added to the guide so students understand the discrepancy.
5. **`Lec 05 - Linked Lists Data Structure.pdf` (Moodle Upload Discrepancy):**
   - *Audit Finding:* The file uploaded as `Lec 05` is an identical duplicate of `Lec 03 - Stack`.
   - *Resolution:* Linked list operations were audited against the Cram Guide, Malhotra Chapter 3, and Assignment 5.
6. **`دليل_المراجعة_الشاملة_والتحضير_للميدترم_هياكل_البيانات.pdf` (7-page official cram guide):**
   - Primary authoritative source for the exam questions, numerical traces, and terminology.

---

## 3. Confirmed Errors Fixed in `guides/data-structures.html`

| # | Item / Component | Issue (Before) | Fix Applied (After) | Source / Justification |
|---|------------------|----------------|---------------------|------------------------|
| 1 | **Stack Visual Diagram (CSS)** | `.stack-cell.top-cell::after` had `content: '← TOP;'` pointing away from the top element. | Inverted to `content: 'TOP →;'` pointing directly into the top element cell. | Visual clarity and correct pointer orientation. |
| 2 | **Circular Queue Deletion Rule (Table 2)** | Dequeue rule omitted the single-element queue reset: only stated `front = (front + 1) % MAX`. | Updated text and formula to: `if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`. | Malhotra Ch 5; Cram Guide p. 3; avoids dangling indices on empty queue. |
| 3 | **C++ Stack Code Snippet** | String literal contained unescaped raw newlines: `cout << "Stack Overflow!\n\n";` causing GCC failure: `missing terminating " character`. | Fixed string newlines to clean `\n`, added `#include <iostream>`, verified clean compilation. | GCC 16.2.0 compilation error. |
| 4 | **C++ Circular Queue Snippet** | Missing queue reset handling and output mismatch: dequeue did not reset indices or log `(front, rear)` pairs as shown in visual output box. | Implemented complete queue reset (`front = rear = -1`), destructor `~CircularQueue()`, and synchronized console output. | C++ best practice; matches sample output. |
| 5 | **C++ Singly Linked List Snippet** | Snippet only provided `insertAtHead(10), (20), (30)`, resulting in list `30 -> 20 -> 10`, while expected output was `10 -> 20 -> 30`. Also missing head deletion. | Added `insertAtTail(int val)` and `deleteHead()` with proper dynamic memory deallocation (`delete`). Output now matches `10 -> 20 -> 30 -> NULL`. | Lecture 06 / Assignment 5 specs; prevents memory leaks. |

---

## 4. Coverage Gaps Closed

1. **Asymptotic Notations ($O, \Omega, \Theta$) & Formal Proof:**
   - Added full definitions for Big-O (upper bound), Big-Omega (lower bound), and Big-Theta (tight bound).
   - Added Dr. Ashraf Heikal's formal proof for $T(n) = 5n + 4 \in O(n)$: demonstrating $5n + 4 \le 6n$ for all $n \ge 4$ with $c = 6, n_0 = 4$.
2. **Algorithm vs. Program & Efficiency Metrics:**
   - Added explicit comparison table (Design vs. Implementation, Machine-independent vs. Machine-dependent).
   - Documented key efficiency parameters: input size, time complexity, space complexity.
3. **Recursion & Tower of Hanoi:**
   - Added formula for minimum moves: $M(n) = 2^n - 1$ with recurrence $T(n) = 2T(n-1) + 1$.
   - Added memory stack overhead explanation and stack overflow risks.
4. **Polish Notation & Expression Conversion:**
   - Added historical background (Jan Łukasiewicz, 1924) and distinction between prefix, infix, and postfix.
   - Added Dr. Ashraf Heikal's official lecture trace examples:
     - `8 5 4 + * 7 - = 65`
     - `(A + B) * C = 30` (with $A=2, B=4, C=5$)
     - `(A + B * C) / D = 2` (with $A=4, B=3, C=2, D=5$)
     - `12 6 * 8 4 / / 7 5 - * = 72`
5. **Linked List Polynomials & 3-Pointer Reversal:**
   - Added polynomial representation using linked list nodes (`coeff`, `pow`, `next`): $10x^2 - 6x + 7$.
   - Added 3-pointer iterative reversal algorithm (`prev`, `curr`, `next`) with $O(n)$ time and $O(1)$ space.
6. **Moodle File Discrepancy Transparency:**
   - Embedded advisory callout in Lecture 4 tab alerting students to the file mismatch on Moodle and directing them to the verified queue material.

---

## 5. Items Unsure / Out-of-Scope (Preserved Without Change)
- **Course Assignment Homework:** Graded assignment problem sets under `materials/` were strictly referenced for syllabus alignment and not answered or mutated.
- **Other Course Guides:** Files `guides/or.html` and `guides/sad.html` remain untouched; changes were strictly confined to `guides/data-structures.html`.

---

## 6. Verification & Test Evidence
- **C++ Compilation Test:**
  - Command: `g++ -Wall -Wextra -std=c++17 <extracted_snippet>.cpp -o snippet.exe`
  - Result: 0 errors, 0 warnings across all 3 code blocks (Stack, Circular Queue, Linked List). Execution outputs match HTML `<div class="output-box">` verbatim.
- **HTML Tag Hierarchy:**
  - Audited using node script: all 298 `div`, 7 `section`, 29 `p`, 4 `table`, 3 `pre`, 90 `code`, 72 `button`, 14 `ul`, 3 `ol`, 58 `li` tags are properly nested and balanced.
- **JavaScript & Interactivity:**
  - Verified script syntax using `node --check`: valid, no errors.
  - Tab switching, filter chips, copy buttons, and accordion toggle functions intact.
- **Responsive Layout:**
  - Tested flex/grid wraps, horizontal scroll on code blocks and tables (`overflow-x: auto`), preserving layout at 390px mobile viewport.
