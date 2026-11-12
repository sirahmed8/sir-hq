// Extract MCP server / plugin NAMES only (no secrets) per tool into mcp-inventory.json
import fs from 'node:fs';
import path from 'node:path';

const HOME = 'C:/Users/a7med';
const out = {};
const safe = (v) => (typeof v === 'string' ? v : JSON.stringify(v));

function readJson(p) { try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return null; } }
function readJsonc(p) {
  try {
    let t = fs.readFileSync(p, 'utf8').replace(/\/\/.*$/gm, '').replace(/\/\*[\s\S]*?\*\//g, '');
    // strip trailing commas
    t = t.replace(/,(\s*[}\]])/g, '$1');
    return JSON.parse(t);
  } catch (e) { return { __parseError: String(e).slice(0, 120) }; }
}

// Claude: top-level mcpServers + per-project mcpServers names
{
  const j = readJson(`${HOME}/.claude.json`);
  const names = new Set();
  if (j && j.mcpServers) Object.keys(j.mcpServers).forEach(k => names.add(k));
  if (j && j.projects) for (const [proj, pv] of Object.entries(j.projects)) {
    if (pv && pv.mcpServers) Object.keys(pv.mcpServers).forEach(k => names.add(`${k} (project:${proj})`));
  }
  out.claude = { mcpServers: [...names].sort() };
  const plugins = readJson(`${HOME}/.claude/plugins/installed_plugins.json`);
  if (plugins) {
    const list = [];
    const walk = (o) => {
      if (Array.isArray(o)) o.forEach(walk);
      else if (o && typeof o === 'object') {
        if (o.name || o.plugin) list.push(o.name || o.plugin);
        Object.values(o).forEach(walk);
      }
    };
    walk(plugins);
    out.claude.plugins = [...new Set(list)].sort();
  }
}
// opencode + kilo jsonc (mcp section names only)
for (const [tool, p] of [['opencode', `${HOME}/.config/opencode/opencode.jsonc`], ['kilo', `${HOME}/.config/kilo/kilo.jsonc`]]) {
  const j = readJsonc(p);
  out[tool] = { mcpServers: j && j.mcp ? Object.keys(j.mcp) : [], rawKeys: j ? Object.keys(j) : [], parseError: j && j.__parseError };
}
// gemini: settings.json + config/mcp_config.json + plugins.json + plugin.json files
{
  const names = new Set();
  const s = readJson(`${HOME}/.gemini/settings.json`);
  if (s && s.mcpServers) Object.keys(s.mcpServers).forEach(k => names.add(k));
  const mc = readJson(`${HOME}/.gemini/config/mcp_config.json`);
  if (mc) {
    if (mc.mcpServers) Object.keys(mc.mcpServers).forEach(k => names.add(k));
    if (mc.servers) Object.keys(mc.servers).forEach(k => names.add(k));
  }
  const pj = readJson(`${HOME}/.gemini/config/plugins.json`);
  if (pj) out.geminiPluginsJson = pj;
  // plugin.json name/description per plugin dir
  const pluginsDir = `${HOME}/.gemini/config/plugins`;
  const plist = [];
  if (fs.existsSync(pluginsDir)) for (const d of fs.readdirSync(pluginsDir)) {
    const pj2 = readJson(path.join(pluginsDir, d, 'plugin.json'));
    if (pj2) plist.push({ plugin: d, name: pj2.name || '', description: String(pj2.description || '').slice(0, 160), mcpServers: pj2.mcpServers ? Object.keys(pj2.mcpServers) : [] });
  }
  out.gemini = { mcpServers: [...names].sort(), plugins: plist };
  // antigravity mcp config candidates
  for (const cand of [`${HOME}/.gemini/antigravity/mcp_config.json`, `${HOME}/.gemini/antigravity/config/mcp_config.json`]) {
    const j = readJson(cand);
    if (j) out.antigravityMcp = { file: cand, keys: Object.keys(j.mcpServers || j.servers || j) };
  }
}
// devin
{
  const d = readJson(`${HOME}/AppData/Local/devin/cli/mcp/descriptions.json`);
  out.devin = { mcpDescriptions: d && typeof d === 'object' ? Object.keys(d) : d };
}
// cline: look for mcp settings
{
  const cands = [`${HOME}/.cline/data/settings/cline_mcp_settings.json`, `${HOME}/AppData/Roaming/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`];
  const found = {};
  for (const c of cands) { const j = readJson(c); if (j) found[c] = j.mcpServers ? Object.keys(j.mcpServers) : Object.keys(j); }
  out.cline = { mcpSettings: found };
}
// kimi config.toml: mcp server table names only
{
  try {
    const t = fs.readFileSync(`${HOME}/.kimi-code/config.toml`, 'utf8');
    const names = [...t.matchAll(/^\[mcp_servers\.([\w-]+)\]/gm)].map(m => m[1]);
    const other = [...t.matchAll(/^\[([\w.-]+)\]/gm)].map(m => m[1]).filter(x => !x.startsWith('mcp_servers'));
    out.kimi = { mcpServers: names, sections: [...new Set(other)] };
  } catch { out.kimi = { error: 'unreadable' }; }
}
// windsurf/cursor: common locations
{
  const cands = {
    windsurf: [`${HOME}/.codeium/windsurf/mcp_config.json`, `${HOME}/.codeium/mcp_config.json`],
    cursor: [`${HOME}/.cursor/mcp.json`, `${HOME}/.cursor/settings.json`],
  };
  for (const [tool, files] of Object.entries(cands)) {
    const found = {};
    for (const f of files) { const j = readJson(f); if (j) found[f] = j.mcpServers ? Object.keys(j.mcpServers) : Object.keys(j); }
    out[tool] = { files: found };
  }
}
// goose: no config dir found
out.goose = { note: 'goose.exe installed via WinGet links; no ~/.config/goose or AppData config found' };

fs.writeFileSync('D:/Projects/_SIR/ops/encyclopedia/mcp-inventory.json', JSON.stringify(out, null, 1), 'utf8');
console.log('written mcp-inventory.json');
for (const [k, v] of Object.entries(out)) console.log(k, '=>', JSON.stringify(v).slice(0, 200));
