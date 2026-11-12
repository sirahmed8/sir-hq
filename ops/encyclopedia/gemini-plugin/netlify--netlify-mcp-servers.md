# netlify-mcp-servers

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-mcp-servers\SKILL.md`
- SKILL.md size: 16572 chars

## What it does

Build, deploy, and secure Model Context.

## When to use (from skill text)

- **"Netlify MCP" means two different things — make sure you're building the right one.** Netlify publishes its *own* hosted MCP server that lets an AI client operate the **Netlify platform** on your behalf — create projects, trigger deploys, manage env vars and infrastructure through your Netlify acc

## Structure (headings inside SKILL.md)

- Netlify MCP Servers
- Before you build
- Stack
- The server function
- Browser-based clients and CORS
- Defining tools
- Authentication
- Safety and permissions
- Rate limiting
- File uploads
- State doesn't survive between requests
- Connecting a client
- Local dev and deploy
- Cross-cutting rules
- Related skills and references
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP Servers, MCP server, MCP protocol, MCP endpoint, MCP SDK, MCP clients, MCP client, MCP support

## Risks / cautions found in text

- - **Who calls this server?** Just you (a personal/single-user server) → use a **single shared secret**. Multiple people, each acting as themselves → use **per-user API keys** backed by Netlify Identity. See [authentication](references/authentication.md).
- - **Expose the least that does the job.** Separate reads from writes, and think hard before exposing destructive tools. A common, sound choice is to **omit delete tools entirely** and keep destructive actions in a human-operated UI.
- - **Guard irreversible or public actions** by putting explicit instructions in the tool's description — e.g. "show the user the exact text and get confirmation before posting." This is a soft, model-level guard, so back it with a real kill switch: a token you can revoke instantly.
- - **Keep the client's credential separate from your backend's.** The client authenticates to your server (bearer/API key); your server authenticates to the database or third-party API with its *own* secret. Never pass your backend god-key out to the client.

## Key rules (verbatim lines from SKILL.md)

1. - **Expose the least that does the job.** Separate reads from writes, and think hard before exposing destructive tools. A common, sound choice is to **omit delete tools entirely** and keep destructive actions in a human-operated UI.
2. - **Guard irreversible or public actions** by putting explicit instructions in the tool's description — e.g. "show the user the exact text and get confirmation before posting." This is a soft, model-level guard, so back it with a real kill switch: a token you can revoke instantly.
3. - **Keep the client's credential separate from your backend's.** The client authenticates to your server (bearer/API key); your server authenticates to the database or third-party API with its *own* secret. Never pass your backend god-key out to the client.
4. - **Identity caveat:** Netlify Identity does **not** work under `netlify dev`, so per-user-key auth must be tested on a deploy preview. See the **netlify-identity** skill.
5. - **Secrets:** set tokens/keys as env vars (`netlify env:set MCP_BEARER_TOKEN <value> --secret`) — never in code.

## Files inside the skill

- `references/authentication.md` — "MCP Server Authentication"
- `references/connecting-clients.md` — "Connecting Clients"
- `references/file-uploads.md` — "File Uploads via MCP"
