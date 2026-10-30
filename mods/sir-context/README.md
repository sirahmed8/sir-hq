# SIR Context

Adds a short, always-current section to the system prompt of every Claude chat so each project chat knows the SIR main plan without being told: the path of the main plan and the wave study, which project this chat belongs to with its wave, task count and next task, how many unread messages other projects left for it, and Ahmed's standing rules (no pull requests, never delete legacy, use the computer for any task, keep AHome private). In the HQ chat it says so instead. It reads the project files each time, so it is never stale. Change the text in `hooks/register.ts`.
