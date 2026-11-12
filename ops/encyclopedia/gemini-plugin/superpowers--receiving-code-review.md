# receiving-code-review

Tools: gemini-plugin (superpowers). Source: C:\Users\a7med\.gemini\config\plugins\superpowers\skills\receiving-code-review\SKILL.md (205 lines, read in full)

## Summary
Behavioral protocol for receiving code review feedback: verify before implementing, never perform agreement, clarify unclear items before touching anything, evaluate external reviewers skeptically against codebase reality, push back with technical reasoning when wrong, implement one item at a time with tests, and reply to GitHub inline comments in their threads.

## When to use / not use
Use whenever receiving code review feedback — from the human partner, external reviewers, or automated tools. Not for GIVING review (that's requesting-code-review or a reviewer role); this is the receiver's discipline.

## Inputs, outputs, dependencies
Input: review feedback (list of items, possibly partially unclear). Output: verified, tested changes or reasoned pushback. Needs: codebase access for verification, test suite for per-item verification, gh api for GitHub thread replies.

## Key rules
1. Sequence: READ all → UNDERSTAND (restate) → VERIFY against code → EVALUATE → RESPOND → IMPLEMENT one at a time. Never "You're absolutely right!" — banned phrases are performative agreement; actions > words.
2. ANY unclear item = STOP everything; items may be related and partial understanding produces wrong implementation. "I understand 1,2,3,6; need clarification on 4,5" is the correct move.
3. External reviewers get 5 checks before implementing: technically correct here? breaks existing functionality? reason for current impl? all platforms/versions? full context? YAGNI-check "proper" features by grepping actual usage.
4. Implementation order: blocking (breaks/security) → simple → complex; test each fix individually, verify no regressions.
5. Push back with technical reasoning when wrong (cite working tests/code); if uncomfortable, name the tension and tell the partner. If you pushed back wrongly, correct factually — no long apology.

## Risks / owner items
- Trusted feedback (from the human partner) skips deep verification but NOT scope clarification.
- Conflicts with prior owner/partner decisions always escalate to the partner first.
- "Can't verify without X" must be stated with a proposed path, not silently proceeded.

## Category and tags
build, ops — code-review, feedback, teamwork, verification, anti-sycophancy.

## Revision note
Single superpowers revision; pairs with requesting-code-review (sender side).
