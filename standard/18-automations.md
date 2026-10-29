# 18 — AI automations (n8n)

- **Purpose:** automations do real work instead of Ahmed. They read, decide, write and act within limits. AI handles judgment (classify, summarize, extract, draft, prioritize, choose the next step); ordinary nodes handle the plumbing (triggers, HTTP calls, file moves, schedules). That split keeps automations reliable and cheap.
- **Engine:** the local n8n instance (Phase 1.11), bound to localhost. AI steps go through `_SIR/scripts/ai/ask.ps1`, so the fallback chain and usage ledger apply everywhere. Preference order:
  1. Ollama (local, private, free)
  2. `agy -p` (Gemini)
  3. `opencode run`
  4. `claude -p` (subscription usage; high-value steps only)
  n8n's own AI Agent node can also use Ollama directly.
- **Where workflows live:** `<project>/automations/n8n/<name>.json` (exported, credentials stripped) next to `<name>.md` (trigger, purpose, inputs and outputs, AI steps and providers, cost per run, failure behavior). Automations that don't belong to a project, and all PC automations, live in `D:\Projects\Laptop Manager\automations\`.
- **Design rules:**
  - Every workflow has a dry-run mode, an error branch that alerts and logs, retries with backoff for network steps, and idempotency (re-running doesn't duplicate work).
  - AI output that triggers an action is validated against a schema first. Public posts follow the content calendar and its veto window; anything financial or destructive, and anything a platform reserves for a human, goes on Ahmed's list instead of executing. Nothing else waits.
  - Prompts are versioned with the workflow; inputs are trimmed to what the step needs; personal data stays on local models.
  - Credentials live only in n8n's credential store, never in exported JSON.
  - Schedules use odd minutes; heavy runs happen at night.
- **Catalog to build** (prioritize by hours saved per week):
  - **Per product:**
    - a release produces multilingual changelog posts (published on the calendar's schedule)
    - store reviews get triage and reply drafts
    - the support inbox gets classified, with drafted answers
    - weekly Search Console and Bing data turns into insights and BOARD tasks
    - an uptime or CI failure produces an AI diagnosis summary and a push
    - a digest of signups and feedback
  - **Business:**
    - lead capture with AI qualification into a pipeline sheet
    - proposals for new freelance posts that match Ahmed's skills (sent under the 8.3 rules)
    - invoice and payment reminders
  - **Personal (Laptop Manager):**
    - morning digest; Downloads organizer; disk watcher
    - Obour Drive watcher (summaries, flashcards, deadlines)
    - job-feed scorer
    - content-idea collector (saves links and voice notes into the content backlog)
- **Testing:** each workflow has a set of test inputs with expected outputs and is run before it's enabled. A weekly health check reports failing workflows.
