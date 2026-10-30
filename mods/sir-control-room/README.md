# SIR Control Room

A pane that stays beside the chat and shows every SIR project: wave, task progress with a bar, and the next open task. It reads each project's `.sir/TASKS.md` and `.sir/project.yml` under `D:/Projects` and refreshes every 30 seconds, so it updates by itself as project chats tick tasks. AHome appears as "AHome (private)" with counts only. Open it with `/sir`; it also opens when a session starts and puts a short total in the status line. Change the folder with the `ROOT` constant in `hooks/register.tsx`.
