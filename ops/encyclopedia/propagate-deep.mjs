// Propagate deep digests to all tool folders
// Usage: node propagate-deep.mjs

import fs from 'node:fs';
import path from 'node:path';

const ENC = 'D:/Projects/_SIR/ops/encyclopedia';
const DEEP_DIR = path.join(ENC, 'deep');
const INDEX_FILE = path.join(ENC, 'index.json');

// Load index
const indexData = JSON.parse(fs.readFileSync(INDEX_FILE, 'utf8'));
const index = indexData.index; // array of {name, tool, plugin, category, desc, digestRel, hash, size}

// Build map: skillName -> set of {tool, plugin, digestRel}
const skillToDigests = new Map();
for (const entry of index) {
  const key = entry.name;
  if (!skillToDigests.has(key)) skillToDigests.set(key, []);
  skillToDigests.get(key).push({
    tool: entry.tool,
    plugin: entry.plugin || '',
    digestRel: entry.digestRel
  });
}

// Read all deep digests
const deepFiles = fs.readdirSync(DEEP_DIR).filter(f => f.endsWith('.md') && !f.startsWith('PROGRESS'));
console.log(`Found ${deepFiles.length} deep digests`);

let updated = 0;
let skipped = 0;
let notFound = 0;

for (const deepFile of deepFiles) {
  const skillName = deepFile.replace(/\.md$/, '');
  const deepPath = path.join(DEEP_DIR, deepFile);
  const deepContent = fs.readFileSync(deepPath, 'utf8');

  // Find matching skills in index (exact match or close match)
  const targets = skillToDigests.get(skillName);
  if (!targets) {
    // Try case-insensitive or with underscores
    let found = false;
    for (const [key, val] of skillToDigests) {
      if (key.toLowerCase() === skillName.toLowerCase() ||
          key.replace(/-/g, '_') === skillName.replace(/-/g, '_') ||
          key.replace(/_/g, '-') === skillName.replace(/_/g, '-')) {
        // Use this key's targets
for (const t of val) {
        const destPath = path.join('D:/Projects/_SIR/ops', t.digestRel);
        fs.mkdirSync(path.dirname(destPath), { recursive: true });
        fs.writeFileSync(destPath, deepContent, 'utf8');
        updated++;
      }
        found = true;
        break;
      }
    }
    if (!found) {
      console.log(`  SKIP: ${skillName} - not found in index`);
      notFound++;
    }
    continue;
  }

  for (const t of targets) {
    // digestRel is like "encyclopedia/claude/skill-name.md", so join from _SIR/ops
    const destPath = path.join('D:/Projects/_SIR/ops', t.digestRel);
    fs.mkdirSync(path.dirname(destPath), { recursive: true });
    fs.writeFileSync(destPath, deepContent, 'utf8');
    updated++;
  }
}

console.log(`Updated: ${updated} digest files`);
console.log(`Not found in index: ${notFound}`);