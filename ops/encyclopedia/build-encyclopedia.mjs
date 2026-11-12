// r47 skills encyclopedia builder. Read-only over skill sources; writes only under ops/encyclopedia/.
// Usage: node build-encyclopedia.mjs [--tool <name>]   (no arg = all)
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const ENC = 'D:/Projects/_SIR/ops/encyclopedia';
const HOME = 'C:/Users/a7med';
const PROJ = 'D:/Projects';

// ---- sources ----
const SOURCES = [
  { tool: 'claude',       dirs: [`${HOME}/.claude/skills`] },
  { tool: 'codex',        dirs: [`${HOME}/.codex/skills`] },
  { tool: 'windsurf',     dirs: [`${HOME}/.codeium/windsurf/skills`] },
  { tool: 'cursor',       dirs: [`${HOME}/.cursor/skills`] },
  { tool: 'opencode',     dirs: [`${HOME}/.config/opencode/skills`] },
  { tool: 'kilo',         dirs: [`${HOME}/.config/kilo/skills`] },
  { tool: 'agents',       dirs: [`${HOME}/.agents/skills`] },
  { tool: 'gemini',       dirs: [`${HOME}/.gemini/skills`] },
  { tool: 'antigravity-builtin', dirs: [`${HOME}/.gemini/antigravity/builtin/skills`] },
  { tool: 'antigravity-scratch', dirs: [`${HOME}/.gemini/antigravity/scratch/skills`] },
  { tool: 'workspace',    dirs: [`${PROJ}/.agents/skills`] },
];
// gemini plugins: every dir containing SKILL.md files, attributed to plugin name
const PLUGIN_ROOT = `${HOME}/.gemini/config/plugins`;

const onlyTool = process.argv.includes('--tool') ? process.argv[process.argv.indexOf('--tool') + 1] : null;

function* walkSkillDirs(root) {
  if (!fs.existsSync(root)) return;
  for (const e of fs.readdirSync(root, { withFileTypes: true })) {
    if (!e.isDirectory()) continue;
    const p = path.join(root, e.name);
    if (fs.existsSync(path.join(p, 'SKILL.md'))) yield { name: e.name, dir: p };
  }
}
function* walkSkillMdDeep(root, maxDepth = 4) {
  // for plugin dirs: find SKILL.md anywhere up to depth
  if (!fs.existsSync(root)) return;
  const stack = [{ dir: root, depth: 0 }];
  while (stack.length) {
    const { dir, depth } = stack.pop();
    let ents;
    try { ents = fs.readdirSync(dir, { withFileTypes: true }); } catch { continue; }
    for (const e of ents) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) {
        if (depth < maxDepth && e.name !== 'node_modules') stack.push({ dir: p, depth: depth + 1 });
      } else if (e.name === 'SKILL.md') {
        yield { file: p, dir: path.dirname(p), plugin: path.relative(PLUGIN_ROOT, p).split(path.sep)[0] };
      }
    }
  }
}

function parseFrontmatter(text) {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return { fm: {}, body: text };
  const fm = {};
  let key = null;
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^(\w[\w-]*):\s*(.*)$/);
    if (kv && !/^\s/.test(line)) { key = kv[1]; fm[key] = kv[2].replace(/^['"]|['"]$/g, ''); }
    else if (key && /^\s+\S/.test(line)) fm[key] = (fm[key] ? fm[key] + ' ' : '') + line.trim();
  }
  return { fm, body: text.slice(m[0].length) };
}

const RULE_RE = /\b(must|never|always|do not|don't|avoid|only use|require[sd]?\b|before|after|instead of|prohibit)/i;
const RISK_RE = /\b(destructive|irreversible|delete|drop|payment|billing|secret|token|password|credential|prod|production|permission|risk|warning|danger|ban|legal|privacy)/i;

function extractDigest(skillName, tool, skillPath, skillMdPath, fm, body, allFiles) {
  const lines = body.split(/\r?\n/);
  const headings = lines.filter(l => /^#{1,3}\s/.test(l)).map(l => l.replace(/^#+\s*/, '').trim());
  const bullets = lines.map(l => l.trim()).filter(l => /^[-*]\s|^\d+\.\s/.test(l) && l.length > 20 && l.length < 400);
  const ruleLines = bullets.filter(l => RULE_RE.test(l)).slice(0, 6);
  const riskLines = bullets.filter(l => RISK_RE.test(l)).slice(0, 4);
  // first substantive paragraph = what it does
  const para = lines.map(l => l.trim()).filter(l => l && !l.startsWith('#') && !/^[-*]\s|^\d+\./.test(l) && l.length > 40).slice(0, 2).join(' ');
  const desc = (fm.description || para || '').replace(/\s+/g, ' ').trim();
  const triggers = lines.filter(l => /trigger|use when|use this/i.test(l)).slice(0, 3);

  const fileList = allFiles.filter(f => f !== 'SKILL.md').map(f => {
    let note = '';
    if (/\.(md|txt)$/i.test(f)) {
      try {
        const fp = path.join(skillPath, f);
        const t = fs.readFileSync(fp, 'utf8').slice(0, 4000);
        const h = t.match(/^#\s+(.+)$/m) || t.split(/\r?\n/).find(l => l.trim().length > 10);
        if (h) note = ` — "${(h[0] || '').replace(/^#+\s*/, '').trim().slice(0, 90)}"`;
      } catch {}
    }
    return `- \`${f}\`${note}`;
  });

  const toolsNeeded = [];
  if (fm['allowed-tools']) toolsNeeded.push(`allowed-tools: ${fm['allowed-tools']}`);
  const mcpMentions = [...new Set((body.match(/\b(mcp|MCP)[:\s][\w-]+/g) || []))].slice(0, 8);
  if (mcpMentions.length) toolsNeeded.push('MCP mentions: ' + mcpMentions.join(', '));

  return { name: fm.name || skillName, desc, headings, ruleLines, riskLines, triggers, fileList, toolsNeeded, allowedTools: fm['allowed-tools'] || '' };
}

function categoryOf(name, desc) {
  const s = (name + ' ' + desc).toLowerCase();
  const rules = [
    ['security', /secur|vulnerab|owasp|auth|zero-trust|reverse.engineer|penetrat|leak|privacy|compliance|legal/],
    ['design', /design|ui|ux|motion|css|tailwind|figma|typst|theme|visual|a11y|accessib|chrome.extension|landing|copywrit|seo/],
    ['data', /firestore|database|sql|bigquery|spanner|data|analytics|excel|sheet|docs|drive|calendar|notion|linear|stripe|supabase|postgres|firebase/],
    ['media', /image|video|remotion|ffmpeg|audio|music|youtube|thumbnail|motion.graphics|pdf|typst|dubbing|suno|media/],
    ['research', /research|search|find|gem|trend|knowledge|docs|skill.finder|internet|web|stock|market|youtube.video/],
    ['automation', /automat|workflow|orchestrat|cron|mcp|connect|deploy|ci|cd|vercel|hosting|api|cli|android|xcode|chrome.devtools|device.hub|bootstrap|env/],
    ['study', /study|learn|course|exam|quiz|teach|tutor|academic/],
    ['jobs', /job|career|cv|resume|recruit|application|linkedin/],
    ['business', /business|market|customer|support|chatbot|pricing|monetiz|sales|financial|stock/],
    ['ops', /ops|admin|storage|disk|laptop|session|memory|agent|skill|customiz|checkpoint|preamble|orchestrat|paperclip|council|direct.action|yagni|karpathy|production|modern|next|react|shadcn|vercel|gemini|firebase|gcloud|cloud|mcp|gateway|model|omniroute|repomix|graphify|excel|extension|composer|dataflow|airflow|spark|lakehouse|form|autoclean|notebook|ml\.|composer/],
    ['build', /build|code|engineer|next|react|typescript|python|node|rust|swift|kotlin|android|ios|app|web|frontend|backend|api|test|debug|refactor|architecture|system.design|turbopack|deploy|extension_to|chat.sdk|ai.sdk|sdk|migrate|upgrade|compose|preview|device|bootstrap|env.vars|marketplace|knowledge.update|retrieving|gemini|firebase|vercel|turbopack|next.forge|next.upgrade|xcode|android|chrome|compose|device.hub|bootstrap|deployments|env.vars|marketplace|turbopack|next.forge|next.upgrade|extension_to|chat.sdk|ai.sdk|ai.gateway|all.skills|auth|verification|troubleshooting|memory.leak|debug.optimize|cookie|a11y|excel|financial|stock|music|typst|google.maps|maps|gsheets|gslides|gdocs|gdrive|gcalendar|gmail|preferred|live.api|omni|api.dev|multi.agent|superpowers|browse|canva|figma|context7|linear|notion|postman|qodo|stripe|supabase|unity|invideo|netlify|atlassian|auth0|base44|twg|gemini.api|developer.knowledge|advanced.engineering|creator.studio|agent.reach|sir.|laptop|autonomy|mobile|ergonomics|commercial|high.conversion|website.traffic|open.seo|pulse|modern.app|system.design|database.rel|production.eng|vibe.auth|zero.trust|accidental|agent.supercharged|binary|claude.council|cognitive|customization|direct.action|emil|firebase|firestore|github.gem|google.antigravity|graphify|imagegen|internet.skill|karpathy|legal|managing.python|master.production|meta.social|mimic|modern.ui|motion|nextjs|omniroute|owasp|paperclip|pc.storage|ponytail|react.best|repomix|review.agent|shadcn|sir|skill|social.creator|system.design|taste|vibe|website|youtube|zero/],
  ];
  for (const [cat, re] of rules) if (re.test(s)) return cat;
  return 'build';
}

const index = []; // {name, tool, plugin?, category, desc, digestRel, hash, size}
const digestCounts = new Map();
const seenContent = new Map(); // hash -> first digest rel path
let processed = 0, skipped = 0;

function listFiles(dir) {
  const out = [];
  (function rec(d, rel) {
    let ents; try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return; }
    for (const e of ents) {
      const p = path.join(d, e.name); const r = rel ? rel + '/' + e.name : e.name;
      if (e.isDirectory()) { if (e.name !== 'node_modules' && out.length < 200) rec(p, r); }
      else out.push(r);
    }
  })(dir, '');
  return out;
}

function processSkill(name, tool, dir, plugin) {
  const mdPath = path.join(dir, 'SKILL.md');
  if (!fs.existsSync(mdPath)) return;
  let text; try { text = fs.readFileSync(mdPath, 'utf8'); } catch { return; }
  const { fm, body } = parseFrontmatter(text);
  const files = listFiles(dir);
  const d = extractDigest(name, tool, dir, mdPath, fm, body, files);
  const cat = categoryOf(name, d.desc);
  const hash = crypto.createHash('sha1').update(text).digest('hex');
  const toolSlug = tool.replace(/[^a-z0-9-]/gi, '-');
  let digestName = plugin ? `${plugin}--${name}` : name;
  // same plugin+name can appear under skills/, antigravity/skills/, agents/ etc.
  const base = `${toolSlug}/${digestName}`;
  let n = (digestCounts.get(base) || 0) + 1;
  digestCounts.set(base, n);
  if (n > 1) digestName = `${digestName}--copy${n}`;
  const digestRel = `encyclopedia/${toolSlug}/${digestName}.md`;
  const digestAbs = path.join(ENC, toolSlug, `${digestName}.md`);

  fs.mkdirSync(path.dirname(digestAbs), { recursive: true });
  const dupOf = seenContent.get(hash);
  const out = [];
  out.push(`# ${name}`);
  out.push('');
  out.push(`- Tool: \`${tool}\`${plugin ? ` (plugin: \`${plugin}\`)` : ''}`);
  out.push(`- Category: ${cat}`);
  out.push(`- Source: \`${mdPath}\``);
  out.push(`- SKILL.md size: ${text.length} chars`);
  if (dupOf && dupOf !== digestRel) out.push(`- Identical content to: \`${dupOf}\``);
  out.push('');
  if (dupOf && dupOf !== digestRel) {
    out.push(`Auto-generated stub: this SKILL.md is byte-identical to \`${dupOf}\`. Read that digest for full details.`);
    out.push('');
    out.push(`Description: ${d.desc || '(none)'}`);
  } else {
    seenContent.set(hash, digestRel);
    out.push('## What it does'); out.push(''); out.push(d.desc || '(no description found)'); out.push('');
    if (d.triggers.length) { out.push('## When to use (from skill text)'); out.push(''); d.triggers.forEach(t => out.push(`- ${t.trim().slice(0, 300)}`)); out.push(''); }
    out.push('## Structure (headings inside SKILL.md)'); out.push('');
    (d.headings.slice(0, 25).forEach(h => out.push(`- ${h}`)) || out.push('- (none)')); out.push('');
    out.push('## Tools / MCPs it needs'); out.push('');
    if (d.toolsNeeded.length) d.toolsNeeded.forEach(t => out.push(`- ${t}`)); else out.push('- none declared');
    if (d.allowedTools) out.push(`- allowed-tools (frontmatter): \`${d.allowedTools.slice(0, 300)}\``);
    out.push('');
    out.push('## Risks / cautions found in text'); out.push('');
    if (d.riskLines.length) d.riskLines.forEach(r => out.push(`- ${r.slice(0, 300)}`)); else out.push('- none flagged by keyword scan'); out.push('');
    out.push('## Key rules (verbatim lines from SKILL.md)'); out.push('');
    const rules = d.ruleLines.length ? d.ruleLines.slice(0, 5) : bulletsFallback(body).slice(0, 3);
    rules.forEach((r, i) => out.push(`${i + 1}. ${r.slice(0, 300)}`)); out.push('');
    out.push('## Files inside the skill'); out.push('');
    if (d.fileList.length) d.fileList.slice(0, 60).forEach(f => out.push(f)); else out.push('- (SKILL.md only)'); out.push('');
  }
  fs.writeFileSync(digestAbs, out.join('\n'), 'utf8');
  index.push({ name, tool, plugin: plugin || '', category: cat, desc: d.desc.slice(0, 220), digestRel, hash, size: text.length });
  processed++;
}

function bulletsFallback(body) {
  return body.split(/\r?\n/).map(l => l.trim())
    .filter(l => /^[-*]\s|^\d+\.\s/.test(l) && l.length > 25 && l.length < 350).slice(0, 6);
}

// main
const results = {};
for (const src of SOURCES) {
  if (onlyTool && src.tool !== onlyTool) continue;
  const found = [];
  for (const dir of src.dirs) {
    for (const s of walkSkillDirs(dir)) {
      processSkill(s.name, src.tool, s.dir);
      found.push(s.name);
    }
  }
  results[src.tool] = found;
}
// gemini plugins
if (!onlyTool || onlyTool === 'gemini-plugin') {
  const found = [];
  for (const { file, dir, plugin } of walkSkillMdDeep(PLUGIN_ROOT)) {
    const name = path.basename(dir);
    processSkill(name, 'gemini-plugin', dir, plugin);
    found.push(`${plugin}/${name}`);
  }
  results['gemini-plugin'] = found;
}

fs.writeFileSync(path.join(ENC, 'index.json'), JSON.stringify({ generated: new Date().toISOString(), results, index }, null, 1), 'utf8');
console.log(`processed=${processed} uniqueNames=${new Set(index.map(i => i.name)).size}`);
for (const [t, f] of Object.entries(results)) console.log(`${t}: ${f.length}`);
