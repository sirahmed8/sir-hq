# notion-organize-my-semester

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-organize-my-semester\SKILL.md (+ reference/design.md, reference/study-desk-layout.md, examples/fall-semester.md)

## Summary
Builds a Notion "study desk" for a course or semester: course navigation, a notes library (title, course, lecture date, source), and — only when there is real work — an assignments tracker with due dates and status, plus an undated queue so nothing hides. It preserves equations, citations, and source fidelity.

## When to use / not use
Use for organizing a semester or course from notes, syllabi, and assignments. Not for routine edits inside existing study pages, and not for teacher/student-org workflows, which get their own audience handling rather than a personal dashboard.

## Inputs, outputs, dependencies
Input: courses, term, supplied notes/syllabi/assignments, optional destination. Output: Notion home + notes library + optional assignments database with views. Needs Notion MCP tools and the design/study-desk-layout references.

## Key rules
1. Scale to scope: a single course may need only a notes collection; a semester gets a home with navigation, library, and tracker.
2. Notes sort newest-first by course groups; assignment views show upcoming incomplete work by due date AND a visible undated queue — a calendar alone hides undated work.
3. Reconcile syllabus dates against explicit instructor updates; keep conflicts visible instead of silently picking a deadline.
4. Never invent grades, progress percentages, study schedules, or completion states; generated study questions are labeled suggestions.
5. Keep the next academic action above the full library; preserve citations and equations; extracurricular/personal tracking stays out unless requested.

## Risks / owner items
- Deadline conflicts between syllabus and instructor updates must surface to the user, not be auto-resolved.
- Same Notion safety rails as the family: no sharing changes, verify by read-back, disclose unverified visuals.

## Category and tags
study, ops — notion, semester, courses, notes, assignments, mcp.

## Revision note
Single plugin revision; student-facing counterpart to the engineering wiki skill.
