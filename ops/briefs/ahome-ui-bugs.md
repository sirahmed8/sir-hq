Use your skills and tools as you see fit: plan first, use teamwork/sub-agents for independent parts, use the browser and computer-use tools to look at the real result on screen, keep going until the done-when checks pass. 

Task: fix real UI bugs in AHome's web app. Work in D:/Projects/AHome (read its AGENTS.md and .sir/CHECKPOINT.md first).
The owner took screenshots of the bugs: look at ALL files in C:/Users/a7med/Pictures/Screenshots (the six named Screenshot 2026-11-08 0534..0539). PRIVACY: the screenshots show a private app. Never copy any personal text, names or messages from them into any file, commit, report or log; describe only the visual defect; test with dummy data only.
Bugs to find, reproduce in the browser and fix at the root (grep the components; fix the cause, not a patch):
1. The upload window/sheet: its backdrop is not fully dark (looks about 14 percent dark). It must be a full dark backdrop, and the message/type box must be visible with it.
2. Banner: a glitch where a strip has a different colour from the banner and the banner is cropped from the middle or the side.
3. Duplicated buttons to add something (find every screen with two add buttons for the same action and keep one).
4. The three-dots menu: the dark backdrop opens and closes immediately, then the menu opens, then the backdrop appears dark and the menu opens normally. Fix the flicker (one mount, one transition, no double toggle).
5. Then hunt more: open every tab at 390 px and desktop, light/dark, RTL, with the browser tools, list and fix glitches (overflow, cropped images, wrong colours, overlapping, dead clicks, double animations).
Run the web dev server yourself (see package.json), look at each screen on screen before and after, run the tests (npm test / the repo's verify script), keep all existing tests green, add a test for each fix where possible. Do not deploy and do not push; commit locally with clear messages (git commit) if tests pass.
Done when: each of the four bugs is reproduced, fixed, shown fixed on screen, tests green; list of extra bugs fixed or reported.
