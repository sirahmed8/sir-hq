const fs = require("fs");
const base = "D:/Projects/_SIR/ops/encyclopedia/";
const lines = fs.readFileSync(base + "slices/slice-2.txt", "utf8").replace(/\r/g, "").split("\n").filter(Boolean);
const out = [];
for (const l of lines) {
  const parts = l.split("\t");
  const name = parts[0].trim();
  const tools = parts[1].trim();
  const digestRel = parts[2].replace(/\[digest\]\(/, "").replace(/\)/, "").trim();
  const full = base + digestRel;
  let txt = "";
  try { txt = fs.readFileSync(full, "utf8"); } catch (e) { out.push(name + "\t" + tools + "\t" + digestRel + "\t" + "MISSING:" + full); continue; }
  const src = (txt.match(/^- Source: (.+)$/m) || [])[1] || "";
  out.push(name + "\t" + tools + "\t" + digestRel + "\t" + src);
}
fs.writeFileSync(base + "slice2map.tsv", out.join("\n") + "\n");
console.log(out.length + " skills mapped");