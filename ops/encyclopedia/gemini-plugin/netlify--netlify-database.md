# netlify-database

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-database\SKILL.md`
- SKILL.md size: 19332 chars

## What it does

Zero-config Postgres for Netlify apps via.

## Structure (headings inside SKILL.md)

- Netlify Database
- Modern client (reach for this)
- Where things go
- Querying
- Transactions — use `pool`
- Drizzle ORM
- Migrations
- Local development
- Setup
- CLI reference (`netlify database`)
- REST API
- Testing
- Database branches (deploy-time)
- Runtime gotchas
- Constraints
- Switch an existing Postgres project to Netlify Database
- Netlify house rules (database)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Production deploy: applied immediately before publish; a failure blocks publish. With auto-publish off, Netlify waits for manual publish before applying.
- - Prefer backwards-compatible migrations. Breaking changes (rename/drop column) → expand-and-contract across multiple deploys. New table / nullable column → single migration is fine.
- - **`branch limit reached: maximum <N> branches...`** — each active deploy preview consumes a branch; delete unneeded branches or upgrade.
- - **`cannot reset the production branch`** — reset is non-production only.

## Key rules (verbatim lines from SKILL.md)

1. - `sql.raw(value)` — **injects unparameterized SQL; bypasses injection protection. Only for trusted constants (e.g. `"DESC"`), never user input.**
2. - Production deploy: applied immediately before publish; a failure blocks publish. With auto-publish off, Netlify waits for manual publish before applying.
3. - Deploy preview: applied on every deploy before it goes live; a failure fails the deploy.
4. - **Never edit an applied migration** — checksum drift: `migration "<name>" has been modified after being applied`. Write a new corrective migration.
5. - **Never remove an applied migration** — `... has been removed after being applied`. Restore it.

## Files inside the skill

- `references/cli-commands.md` — "Netlify CLI commands for Netlify Database"
- `references/legacy-extension.md` — "Legacy Netlify DB extension (deprecated)"
- `references/local-dev.md` — "Local development"
- `references/migration-from-extension.md` — "Switching to Netlify Database"
- `references/migrations.md` — "Migrations"
- `references/operational-footguns.md` — "Netlify Database — operational footguns"
