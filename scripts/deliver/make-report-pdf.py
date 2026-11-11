#!/usr/bin/env python3
"""Turn a Markdown or HTML report into a clean A4 PDF and optionally send it to Ahmed on Telegram.

Usage:
    python scripts/deliver/make-report-pdf.py report.md out.pdf [--title "..."] [--send [caption]]
    python scripts/deliver/make-report-pdf.py report.html out.pdf --send

Pipeline: markdown-it (Markdown) -> styled HTML -> headless Chromium printToPDF over CDP
(A4, embedded fonts, page numbers in the footer, headings kept with their text, RTL aware).
Requires the pythoncore Python with playwright + markdown-it-py installed. Nothing is sent
unless --send is passed; sending goes through scripts/deliver/send-telegram.mjs (sendDocument).
"""
import argparse
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEND = ROOT / "scripts" / "deliver" / "send-telegram.mjs"
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]")

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Segoe UI", Tahoma, Arial, "Noto Sans Arabic", sans-serif;
  font-size: 10.5pt; line-height: 1.65; color: #1a1a1a; margin: 0;
}
h1, h2, h3, h4 { line-height: 1.3; margin: 1.1em 0 0.45em; break-after: avoid; page-break-after: avoid; }
h1 { font-size: 19pt; border-bottom: 2px solid #2b5f8f; padding-bottom: 6px; }
h2 { font-size: 14.5pt; color: #2b5f8f; }
h3 { font-size: 12pt; }
p { margin: 0.45em 0; orphans: 3; widows: 3; }
ul, ol { margin: 0.4em 0; padding-inline-start: 1.4em; }
li { margin: 0.2em 0; }
blockquote { margin: 0.8em 0; padding: 0.5em 1em; border-inline-start: 3px solid #2b5f8f;
  background: #f2f6fa; color: #333; }
code { font-family: Consolas, "Courier New", monospace; font-size: 9pt;
  background: #f0f0f0; padding: 0.1em 0.3em; border-radius: 3px; }
pre { background: #1e1e1e; color: #e8e8e8; padding: 10px 12px; border-radius: 6px;
  overflow-x: auto; font-size: 8.5pt; line-height: 1.5; break-inside: avoid; page-break-inside: avoid; }
pre code { background: none; padding: 0; color: inherit; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.5pt;
  break-inside: avoid; page-break-inside: avoid; }
th, td { border: 1px solid #c9d4de; padding: 5px 8px; text-align: start; vertical-align: top; }
th { background: #2b5f8f; color: #fff; }
tr:nth-child(even) td { background: #f4f7fa; }
img { max-width: 100%; }
hr { border: none; border-top: 1px solid #d5dde5; margin: 1.2em 0; }
a { color: #1a5fb4; text-decoration: none; }
.title { font-size: 21pt; font-weight: 700; margin: 0 0 0.3em; break-after: avoid; }
.meta { color: #666; font-size: 9pt; margin-bottom: 1.4em; }
"""

FOOTER = """
<div style="width:100%;font-family:'Segoe UI',Tahoma,sans-serif;font-size:8pt;color:#888;
  display:flex;justify-content:space-between;padding:0 16mm;">
  <span>SIR</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>
"""


def md_to_html(text: str) -> str:
    from markdown_it import MarkdownIt
    return MarkdownIt("commonmark", {"html": True, "linkify": True}).enable("table").render(text)


def page_dir(text: str) -> str:
    return "rtl" if ARABIC.search(text) else "ltr"


def build_html(source: Path, title: str | None) -> str:
    raw = source.read_text(encoding="utf-8")
    if source.suffix.lower() in (".md", ".markdown"):
        body = md_to_html(raw)
    else:
        m = re.search(r"<body[^>]*>(.*)</body>", raw, re.S | re.I)
        body = m.group(1) if m else raw
    direction = page_dir(raw)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    doc_title = title or (re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "") or source.stem
    return f"""<!doctype html>
<html dir="{direction}" lang="{'ar' if direction == 'rtl' else 'en'}">
<head><meta charset="utf-8"><title>{html.escape(doc_title)}</title><style>{CSS}</style></head>
<body>{body}</body></html>"""


def render_pdf(html_doc: str, out_pdf: Path) -> None:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=["--mute-audio"])
        try:
            page = browser.new_page()
            page.set_content(html_doc, wait_until="load")
            page.emulate_media(media="print")
            cdp = page.context.new_cdp_session(page)
            result = cdp.send("Page.printToPDF", {
                "printBackground": True,
                "preferCSSPageSize": True,
                "displayHeaderFooter": True,
                "headerTemplate": "<div></div>",
                "footerTemplate": FOOTER,
                "marginTop": 0, "marginBottom": 0, "marginLeft": 0, "marginRight": 0,
            })
        finally:
            browser.close()
    import base64
    out_pdf.write_bytes(base64.b64decode(result["data"]))


def main() -> int:
    ap = argparse.ArgumentParser(description="Markdown/HTML report -> A4 PDF -> Telegram")
    ap.add_argument("source", help="input .md or .html file")
    ap.add_argument("output", help="output .pdf path")
    ap.add_argument("--title", help="document title override")
    ap.add_argument("--send", nargs="?", const="", default=None,
                    help="send the PDF with send-telegram.mjs; optional caption text")
    args = ap.parse_args()

    source, out = Path(args.source), Path(args.output)
    if not source.is_file():
        print(f"error: input not found: {source}", file=sys.stderr)
        return 2
    if out.suffix.lower() != ".pdf":
        out = out.with_suffix(".pdf")
    out.parent.mkdir(parents=True, exist_ok=True)

    html_doc = build_html(source, args.title)
    tmp = Path(tempfile.mkdtemp(prefix="report-pdf-")) / "doc.html"
    tmp.write_text(html_doc, encoding="utf-8")
    try:
        render_pdf(html_doc, out)
    except Exception as exc:
        print(f"error: PDF render failed: {exc}", file=sys.stderr)
        return 1
    print(f"pdf: {out} ({out.stat().st_size} bytes)")

    if args.send is not None:
        caption = args.send or f"تقرير جاهز: {source.stem}"
        res = subprocess.run(["node", str(SEND), str(out), caption],
                             capture_output=True, text=True, timeout=120)
        print(res.stdout.strip() or res.stderr.strip())
        if res.returncode != 0:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
