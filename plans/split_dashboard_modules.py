"""Split plans/generate_dashboard.py and plans/dashboard_template.html into modules.

Goal: reduce the two single large files into small modules (<300 lines each) while
keeping the generated output byte-for-byte identical. The generator still loads the
template by concatenating the module files in the same order as the original single
file, so the substitution string /*__DATA__*/{} lands in exactly the same place.

Run: python D:/Projects/_SIR/plans/split_dashboard_modules.py
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "dashboard_template.html")
GEN = os.path.join(HERE, "generate_dashboard.py")

CSS_PARTS = 6
JS_PARTS = 10
HTML_PARTS = 3


def split_at_keepends(text, parts, is_cut):
    """Split `text` into `parts` chunks of roughly equal size, cutting only at indices
    where is_cut(text, i) is True. Returns exact slices of `text` (no trimming) so the
    concatenation is byte-identical to the original."""
    n = len(text)
    cuts = [i for i in range(n) if is_cut(text, i)]
    if len(cuts) < parts - 1:
        cuts = list(range(0, n, max(1, n // parts)))
    chosen = []
    for p in range(parts - 1):
        idx = int(round((p + 1) * (len(cuts) - 1) / parts))
        chosen.append(cuts[idx])
    out = []
    start = 0
    for end in chosen:
        out.append(text[start:end])
        start = end
    out.append(text[start:])
    return out


def is_css_cut(text, i):
    if i == 0 or text[i - 1] not in "\n\r":
        return False
    ch = text[i]
    if ch in " \t\r\n":
        return False
    if ch in "}@":
        return False
    return True


def is_js_cut(text, i):
    if i == 0 or text[i - 1] not in "\n\r":
        return False
    if text[i:].startswith("const D ="):
        return False
    return text[i:].startswith(("const ", "let ", "function ", "// ---", "async function ", "document.addEventListener"))


def is_html_cut(text, i):
    if i == 0 or text[i - 1] not in "\n\r":
        return False
    return text[i:].lstrip().startswith(("<div", "<section", "<header", "<nav", "<main", "<aside",
                          "<table", "<button", "<details", "<form", "<svg", "<title", "<body", "<html", "<head", "<style", "<link", "<meta"))


# --- 1. Split the template -------------------------------------------------
tpl = io.open(TPL, encoding="utf-8").read()
assert tpl.count("/*__DATA__*/{}") == 1, "expected exactly one data placeholder"
data_idx = tpl.index("/*__DATA__*/{}")

head = tpl[:data_idx + len("/*__DATA__*/{}")]
tail = tpl[data_idx + len("/*__DATA__*/{}"):]
assert head.endswith("const D = /*__DATA__*/{};") or head.endswith("/*__DATA__*/{}"), repr(head[-60:])
assert tail.startswith((";", "const")), repr(tail[:40])

style_open = head.index("<style>")
style_close = head.index("</style>") + len("</style>")
css = head[style_open:style_close]
head_before_css = head[:style_open]
head_after_css = head[style_close:]

css_parts = split_at_keepends(css, CSS_PARTS, is_css_cut)

script_close = tail.index("</script>") + len("</script>")
js = tail[:script_close]
trailer = tail[script_close:]
js_parts = split_at_keepends(js, JS_PARTS, is_js_cut)

html_parts = split_at_keepends(head_after_css, HTML_PARTS, is_html_cut)

names = ["dashboard_template_head.html"]
for i, part in enumerate(css_parts, 1):
    name = "dashboard_template_css.html" if i == 1 else f"dashboard_template_css{i}.html"
    io.open(os.path.join(HERE, name), "w", encoding="utf-8", newline="").write(part)
    names.append(name)
for i, part in enumerate(html_parts, 1):
    name = "dashboard_template_body.html" if i == 1 else f"dashboard_template_body{i}.html"
    io.open(os.path.join(HERE, name), "w", encoding="utf-8", newline="").write(part)
    names.append(name)
for i, part in enumerate(js_parts, 1):
    name = "dashboard_template_js.html" if i == 1 else f"dashboard_template_js{i}.html"
    io.open(os.path.join(HERE, name), "w", encoding="utf-8", newline="").write(part)
    names.append(name)

io.open(os.path.join(HERE, "dashboard_template_head.html"), "w", encoding="utf-8", newline="").write(head_before_css)
io.open(os.path.join(HERE, "dashboard_template_js%d.html" % JS_PARTS), "w", encoding="utf-8", newline="").write(js_parts[-1] + trailer)

# --- 2. Patch dashboard_main.py to load modules ----------------------------
GM = os.path.join(HERE, "dashboard_main.py")
g = io.open(GM, encoding="utf-8").read()
old = (
    '    tpl = "".join(\n'
    '        io.open(os.path.join(HERE, name), encoding="utf-8").read()\n'
    '        for name in (\n'
    + "".join(f'            "dashboard_template_{i}.html",\n' for i in ["head", "css", "css2", "css3", "css4", "css5", "body", "body2", "body3", "js", "js2", "js3", "js4", "js5", "js6", "js7", "js8", "js9"]) +
    '        )\n'
    '    )\n'
)
# The old block may use different names; match generically by the tpl = join block
import re as _re
m = _re.search(r'    tpl = "".join\(\n        io\.open\(os\.path\.join\(HERE, name\), encoding="utf-8"\)\.read\(\)\n        for name in \(.*?\n    \)\)\n', g, _re.S)
assert m, "template-load block not found in dashboard_main.py"
old = m.group(0)
new = (
    '    tpl = "".join(\n'
    '        io.open(os.path.join(HERE, name), encoding="utf-8").read()\n'
    '        for name in (\n'
    + "".join(f'            "{n}",\n' for n in names) +
    '        )\n'
    '    )\n'
)
g = g.replace(old, new)
io.open(GM, "w", encoding="utf-8", newline="\n").write(g)

print("split ok; modules:")
for n in names:
    p = os.path.join(HERE, n)
    print(" ", n, len(io.open(p, encoding="utf-8").read().splitlines()), "lines")