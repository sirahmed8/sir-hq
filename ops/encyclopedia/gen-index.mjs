// Generate SKILLS_INDEX.md + SOURCES.md from index.json
import fs from 'node:fs';
import path from 'node:path';

const ENC = 'D:/Projects/_SIR/ops/encyclopedia';
const { index, results } = JSON.parse(fs.readFileSync(path.join(ENC, 'index.json'), 'utf8'));

// group by name
const byName = new Map();
for (const e of index) {
  if (!byName.has(e.name)) byName.set(e.name, { name: e.name, tools: new Set(), plugins: new Set(), cats: new Set(), desc: e.desc, digest: e.digestRel });
  const g = byName.get(e.name);
  g.tools.add(e.tool); if (e.plugin) g.plugins.add(e.plugin); g.cats.add(e.category);
  if (!g.desc && e.desc) g.desc = e.desc;
  // prefer non-plugin digest as canonical link
  if (e.tool !== 'gemini-plugin' || g.digest.includes('gemini-plugin')) g.digest = e.digestRel;
}
const rows = [...byName.values()].sort((a, b) => a.name.localeCompare(b.name));

const catOrder = ['build', 'design', 'security', 'data', 'research', 'media', 'automation', 'study', 'jobs', 'business', 'ops'];
let md = `# SKILLS_INDEX: every agent skill on this machine (r47)

Generated ${new Date().toISOString().slice(0, 10)} by \`ops/encyclopedia/build-encyclopedia.mjs\` from \`index.json\`.
${rows.length} unique skill names across ${index.length} installed copies. Digest files live in \`ops/encyclopedia/<tool>/<name>.md\`; identical copies are stubs pointing at the canonical digest.
Categories are heuristic (keyword match on name+description); refine per skill when a digest is hand-checked.

| Skill | Tools that have it | Category | Purpose | Digest |
|---|---|---|---|---|
`;
for (const r of rows) {
  const tools = [...r.tools].sort().join(', ');
  const cat = [...r.cats].sort((a, b) => catOrder.indexOf(a) - catOrder.indexOf(b))[0];
  const purpose = (r.desc || '').replace(/\|/g, '/').replace(/\s+/g, ' ').slice(0, 140);
  md += `| ${r.name} | ${tools} | ${cat} | ${purpose} | [digest](${r.digest.replace('encyclopedia/', '')}) |\n`;
}
fs.writeFileSync('D:/Projects/_SIR/ops/SKILLS_INDEX.md', md, 'utf8');

// SOURCES.md
const srcLines = [];
srcLines.push('# SOURCES: where every skill/plugin/MCP definition was found (r47, verified ' + new Date().toISOString().slice(0, 10) + ')\n');
srcLines.push('| Source | Path | Exists | Skill dirs found | Notes |');
srcLines.push('|---|---|---|---|---|');
const table = [
  ['Claude skills', 'C:/Users/a7med/.claude/skills', results.claude?.length],
  ['Codex skills', 'C:/Users/a7med/.codex/skills', results.codex?.length],
  ['Windsurf skills', 'C:/Users/a7med/.codeium/windsurf/skills', results.windsurf?.length],
  ['Cursor skills', 'C:/Users/a7med/.cursor/skills', results.cursor?.length],
  ['OpenCode skills', 'C:/Users/a7med/.config/opencode/skills', results.opencode?.length],
  ['Kilo skills', 'C:/Users/a7med/.config/kilo/skills', results.kilo?.length],
  ['Shared .agents skills', 'C:/Users/a7med/.agents/skills', results.agents?.length],
  ['Gemini CLI skills', 'C:/Users/a7med/.gemini/skills', results.gemini?.length],
  ['Antigravity builtin skills', 'C:/Users/a7med/.gemini/antigravity/builtin/skills', results['antigravity-builtin']?.length],
  ['Antigravity scratch skills', 'C:/Users/a7med/.gemini/antigravity/scratch/skills', results['antigravity-scratch']?.length],
  ['Gemini plugins (skills inside)', 'C:/Users/a7med/.gemini/config/plugins/*/skills', results['gemini-plugin']?.length],
  ['Workspace skills', 'D:/Projects/.agents/skills', results.workspace?.length],
];
for (const [label, p, count] of table) {
  const exists = fs.existsSync(p.includes('*') ? p.split('*')[0] : p);
  srcLines.push(`| ${label} | \`${p}\` | ${exists ? 'yes' : 'NO'} | ${count ?? 0} | |`);
}
srcLines.push('');
srcLines.push('## Tools checked with no skill store found');
srcLines.push('');
srcLines.push('- **Goose**: `goose.exe` on PATH (WinGet Links) but no `~/.config/goose`, no AppData config, no skills.');
srcLines.push('- **Cline**: `~/.cline` has data/tasks/cron only; no skills dir, no mcp settings file found.');
srcLines.push('- **Kimi Code**: `~/.kimi-code` has config.toml (providers/models), sessions, telemetry; no skills or MCP tables.');
srcLines.push('- **Devin CLI**: `~/AppData/Local/devin/cli` binary + docs only; skills are builtin (declarative-repo-setup, upload-secrets). No user skill dir found.');
srcLines.push('- **Windsurf / Cursor MCP**: no `mcp_config.json` / `mcp.json` found; Cursor `~/.cursor` holds only AGENTS.md and skills/.');
srcLines.push('- **Project skill folders**: `D:/Projects/*/.claude`, `.agents`, `.sir` contain `agents/` subagent definitions (one per project), not SKILL.md skills, except `D:/Projects/.agents/skills/sir-session-end`. `D:/Projects/AHome` was NOT opened (private project). Legacy bundled SKILL.md files under `SIR AI/legacy/**` are research artifacts, excluded from the index.');
srcLines.push('- **Claude plugins**: 84 installed plugins catalogued in `mcp-inventory.json` (`claude.plugins`); their skills live in the plugin cache, not user skill dirs.');
srcLines.push('');
srcLines.push('## MCP / connector definitions per tool');
srcLines.push('');
srcLines.push('Names only (secrets stripped): see `ops/encyclopedia/mcp-inventory.json`. Summary:');
srcLines.push('- Claude (`~/.claude.json`): no `mcpServers` configured at user or project level.');
srcLines.push('- OpenCode & Kilo (`opencode.jsonc` / `kilo.jsonc`): only `nvidia-app` MCP.');
srcLines.push('- Gemini CLI (`~/.gemini/settings.json`, `~/.gemini/config/mcp_config.json`): chrome-devtools, dart, datacloud_* (BigQuery, Cloud SQL, Knowledge Catalog, Spanner), firebase, github, gmail, gdrive, gsheets, gslides, gdocs, gcalendar, linear, notion, stripe, supabase, verkle etc. (full list in JSON).');
srcLines.push('- Antigravity (`~/.gemini/antigravity/mcp_config.json`): same Google stack as Gemini CLI.');
srcLines.push('- Workspace `D:/Projects/.mcp.json` and `.agents/mcp_config.json`: AgentsRoom-* servers (AgentsRoom retired 2026-11-08, likely stale) plus everything-app, 100hires, 0bridge.');
srcLines.push('- Devin: `cli/mcp/descriptions.json` is empty `{}`; built-in skills only.');
srcLines.push('- Kimi: no MCP; config.toml defines providers/models only.');
srcLines.push('- Cline, Goose: no MCP config found.');
fs.writeFileSync(path.join(ENC, 'SOURCES.md'), srcLines.join('\n'), 'utf8');
console.log(`SKILLS_INDEX rows=${rows.length}, digests=${index.length}`);
