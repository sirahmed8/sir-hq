from products_a import A
from products_b import B
from products_c import C
from products_d import D
from products_e import E
from products_f import F

REQUIRED = [
    "slug",
    "display",
    "folder",
    "repo",
    "firebase",
    "replaces",
    "wave",
    "mission",
    "platforms",
    "money",
    "why",
    "port",
    "screens",
    "entities",
    "ai",
    "security_extra",
    "m1",
    "m2",
    "m4",
    "m6",
    "risks",
]
PRODUCTS = A + B + C + D + E + F
for p in PRODUCTS:
    missing = [k for k in REQUIRED if k not in p]
    assert not missing, (p.get("slug"), missing)

import json, os

_wf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "waves.json")
if os.path.isfile(
    _wf
):  # studied wave order (plans/WAVE_STUDY.md), written by wave_study.py
    _w = json.load(open(_wf, encoding="utf-8"))
    for p in PRODUCTS:
        if p["slug"] in _w:
            p["wave"] = _w[p["slug"]]

REMOVED_SLUGS = {
    "sir-odysseus"
}  # Ahmed 2026-11-01: not his project; source moved into SIR AI/legacy
PRODUCTS = [p for p in PRODUCTS if p["slug"] not in REMOVED_SLUGS]
