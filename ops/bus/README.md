# Message bus between projects (durable; live talk uses ListAgents and SendMessage)

One file per project: `ops/bus/<slug>.md` is that project's inbox. To message a project, append a line to its file:
`- [ ] 2026-10-30 from sir-platform: owner-auth 0.2 is published; change `verifyOwner(token)` to `verifyOwner(token, opts)`.`
The owner of the inbox ticks `[x]` when handled and may add a reply line starting `  reply:`. Keep messages short and actionable; say what you need, by when, and where the details are. The SIR Control Room pane and the status line show unread counts. `ops/bus/all.md` is for notices to every project.
