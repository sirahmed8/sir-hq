// Narrow-phone layout scout: 320/390 px, both locales, public routes.
// Detects: horizontal overflow, elements clipped wider than viewport, one-letter wrapping.
import { chromium } from "playwright-core";
import { mkdirSync } from "node:fs";

const BASE = "http://127.0.0.1:4173/";
const OUT = "D:/Projects/_SIR/ops/scout-evidence";
mkdirSync(OUT, { recursive: true });

const ROUTES = ["", "download", "legal/privacy", "legal/terms", "legal/refunds", "legal/cookies", "admin", "settings", "agents", "telegram", "checkin"];
const WIDTHS = [320, 390];

const findings = [];
const note = (combo, where, msg) => { findings.push({ combo, where, msg }); console.log(`[FIND] ${combo} ${where}: ${msg}`); };

async function audit(page, combo, where) {
  const res = await page.evaluate(() => {
    const iw = window.innerWidth;
    const out = { overflow: false, clipped: [], oneLetter: [] };
    if (document.documentElement.scrollWidth > iw + 1) out.overflow = true;
    // elements wider than viewport (visible clipping)
    for (const el of document.querySelectorAll("body *")) {
      const r = el.getBoundingClientRect();
      if (r.width > iw + 2 && r.height > 4) {
        const tag = el.tagName.toLowerCase();
        const cls = (el.className?.toString() ?? "").slice(0, 80);
        out.clipped.push(`${tag}.${cls} w=${Math.round(r.width)} left=${Math.round(r.left)}`);
        if (out.clipped.length >= 8) break;
      }
    }
    // one-letter wrapping heuristic: text nodes whose rendered lines average <4 chars
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walker.nextNode())) {
      const txt = n.textContent.trim();
      if (txt.length < 14 || !/[A-Za-z\u0600-\u06FF]/.test(txt)) continue;
      const range = document.createRange();
      range.selectNodeContents(n);
      const rects = [...range.getClientRects()].filter((r) => r.width > 2 && r.height > 2);
      // group rects into lines by top
      const lines = new Set(rects.map((r) => Math.round(r.top / 6)));
      const lineCount = lines.size || 1;
      const charsPerLine = txt.length / lineCount;
      if (lineCount >= 4 && charsPerLine < 4) {
        const p = n.parentElement;
        out.oneLetter.push(`${txt.slice(0, 50)} -> ${lineCount} lines, ~${charsPerLine.toFixed(1)} ch/line (${p?.tagName}.${(p?.className?.toString() ?? "").slice(0, 60)})`);
        if (out.oneLetter.length >= 6) break;
      }
    }
    return out;
  });
  if (res.overflow) note(combo, where, `horizontal overflow scrollWidth>innerWidth`);
  for (const c of res.clipped) note(combo, where, `clipped/wide element: ${c}`);
  for (const l of res.oneLetter) note(combo, where, `possible one-letter wrap: ${l}`);
  await page.screenshot({ path: `${OUT}/phone-${combo}-${where.replace(/\//g, "_")}.png`, fullPage: true });
}

const browser = await chromium.launch({ headless: true });
try {
  for (const w of WIDTHS) {
    for (const locale of ["ar", "en"]) {
      const combo = `${w}-${locale}`;
      const ctx = await browser.newContext({
        viewport: { width: w, height: w === 320 ? 640 : 844 },
        locale: locale === "ar" ? "ar-EG" : "en-GB",
        hasTouch: true,
        colorScheme: "light",
      });
      const page = await ctx.newPage();
      await page.addInitScript((loc) => {
        try { localStorage.setItem("sirai.locale", loc); localStorage.setItem("sirai.consent", "rejected"); } catch {}
      }, locale);
      for (const route of ROUTES) {
        const where = route || "auth";
        try {
          await page.goto(`${BASE}#/${route}`, { waitUntil: "networkidle", timeout: 20000 });
          await page.waitForTimeout(700);
          await audit(page, combo, where);
        } catch (e) {
          note(combo, where, `load failed: ${String(e).slice(0, 120)}`);
        }
      }
      await ctx.close();
    }
  }
} finally {
  await browser.close();
}
console.log(`DONE findings=${findings.length}`);
