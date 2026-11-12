"""Build the final contact set (owner orders 2026-11-12): Google and Apple hold the same people, names are only Prefix + First Name
(the first-name field holds the full name), no middle, last or company names are created, exact duplicates are dropped.
Input (name-cleaned by contacts_clean.py with suffix _v4): _local/contacts/google_v4.csv and apple_v4.vcf.
Output (same folder, local only, counts printed, no names):
  final_google.csv, final_apple.vcf, duplicates_review.csv (people sharing a phone inside one source, names stay in this local file).
Same person = shares a normalized phone number (last 10 digits). Nothing is merged except exact duplicates (same name and same phones).
"""
import csv
import re
from pathlib import Path

import nowindow  # noqa: F401
import contacts_clean as cc

D = Path("D:/Projects/_SIR/_local/contacts")
CRLF = chr(13) + chr(10)
RENAME_PHONE = "1119119255"  # owner: this Ahmed Gamal is 'Ahmed Jimmy'; the other Ahmed Gamal stays
COLS = {"prefix": "Name Prefix", "first": "First Name", "middle": "Middle Name", "last": "Last Name", "suffix": "Name Suffix"}


def norm(p: str) -> str:
    d = re.sub(r"\D", "", p)
    if d.startswith("0020"):
        d = d[4:]
    if d.startswith("20") and len(d) >= 12:
        d = d[2:]
    if d.startswith("0"):
        d = d[1:]
    return d[-10:] if len(d) >= 10 else d


def full(prefix: str, first: str) -> str:
    return " ".join(x for x in (prefix, first) if x)


def name_key(prefix: str, first: str) -> str:
    return " ".join(cc.key(w) for w in full(prefix, first).split())


def renamed(first: str, keys: set) -> str:
    if RENAME_PHONE in keys and cc.key(first) in ("ahmed gamal", "احمد جمال"):
        return "Ahmed Jimmy"
    return first


def vcard_fields(card: str) -> dict:
    out = {"phones": [], "emails": [], "bday": "", "n": ("", "", "", "", "")}
    for ln in [x for x in card.strip().splitlines() if x]:
        if re.match(r"N[;:]", ln):
            parts = (ln.partition(":")[2].split(";") + [""] * 5)[:5]
            out["n"] = (parts[3], parts[1], parts[2], parts[0], parts[4])  # prefix, given, middle, family, suffix
        elif re.match(r"TEL", ln):
            out["phones"].append(ln.partition(":")[2].strip())
        elif re.match(r"EMAIL", ln):
            out["emails"].append(ln.partition(":")[2].strip())
        elif ln.startswith("BDAY"):
            out["bday"] = ln.partition(":")[2].strip()
    return out


def load_apple() -> list:
    t = (D / "apple_v4.vcf").read_text(encoding="utf-8")
    t = re.sub(r"\r?\n[ ]", "", t)
    cards = ["BEGIN:VCARD" + c for c in t.split("BEGIN:VCARD") if "END:VCARD" in c]
    out = []
    for c in cards:
        f = vcard_fields(c)
        f["raw"] = c.strip()
        f["keys"] = {norm(p) for p in f["phones"] if norm(p)}
        out.append(f)
    return out


def fix_vcard_name(raw: str, new_first: str, prefix: str) -> str:
    lines = raw.splitlines()
    for i, ln in enumerate(lines):
        if re.match(r"N[;:]", ln):
            head = ln.partition(":")[0]
            lines[i] = f"{head}:;{new_first};;{prefix};"
        elif re.match(r"FN[;:]", ln):
            lines[i] = f"FN:{full(prefix, new_first)}"
    return CRLF.join(cc.fold(x) for x in lines if x)


def main() -> None:
    apple = load_apple()
    with (D / "google_v4.csv").open(encoding="utf-8-sig", newline="") as fh:
        grows = list(csv.DictReader(fh))
        gfields = list(grows[0].keys())
    for r in grows:
        r["_keys"] = set()
        for k, v in r.items():
            if k and "Phone" in k and "Value" in k and v:
                for part in v.split(":::"):
                    if norm(part):
                        r["_keys"].add(norm(part))
        r[COLS["first"]] = renamed(r.get(COLS["first"], ""), r["_keys"])
        r[COLS["prefix"]] = r.get(COLS["prefix"], "").strip()
    for a in apple:
        pre, giv = a["n"][0].strip(), renamed(a["n"][1], a["keys"])
        if giv != a["n"][1] or pre != a["n"][0]:
            a["raw"] = fix_vcard_name(a["raw"], giv, pre)
            a["n"] = (pre, giv, "", "", "")

    # exact duplicates (same name and same phones) are dropped inside each source
    def dedupe(items, keyf):
        seen, out, dropped = set(), [], 0
        for it in items:
            k = keyf(it)
            if k in seen:
                dropped += 1
                continue
            seen.add(k)
            out.append(it)
        return out, dropped

    grows, gdrop = dedupe(grows, lambda r: (name_key(r.get(COLS["prefix"], ""), r.get(COLS["first"], "")), tuple(sorted(r["_keys"]))))
    apple, adrop = dedupe(apple, lambda a: (name_key(a["n"][0], a["n"][1]), tuple(sorted(a["keys"]))))

    akeys = set().union(*[a["keys"] for a in apple])
    gkeys = set().union(*[r["_keys"] for r in grows])
    gnames = {name_key(r.get(COLS["prefix"], ""), r.get(COLS["first"], "")) for r in grows}
    anames = {name_key(a["n"][0], a["n"][1]) for a in apple}
    apple_only = [a for a in apple if a["keys"] and not (a["keys"] & gkeys)]
    apple_nophone_new = [a for a in apple if not a["keys"] and name_key(a["n"][0], a["n"][1]) not in gnames]
    google_only = [r for r in grows if r["_keys"] and not (r["_keys"] & akeys)]
    google_nophone_new = [r for r in grows if not r["_keys"] and name_key(r.get(COLS["prefix"], ""), r.get(COLS["first"], "")) not in anames]

    extra = []
    for a in apple_only + apple_nophone_new:
        row = {c: "" for c in gfields}
        row[COLS["prefix"]], row[COLS["first"]] = a["n"][0], a["n"][1]
        if "Phone 1 - Value" in row and a["phones"]:
            row["Phone 1 - Value"] = ":::".join(a["phones"])
        if "E-mail 1 - Value" in row and a["emails"]:
            row["E-mail 1 - Value"] = a["emails"][0]
        if "Birthday" in row and a["bday"]:
            b = a["bday"].replace("-", "")
            row["Birthday"] = f"{b[:4]}-{b[4:6]}-{b[6:8]}" if len(b) == 8 else a["bday"]
        extra.append(row)
    with (D / "final_google.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=gfields)
        w.writeheader()
        w.writerows([{k: r.get(k, "") for k in gfields} for r in grows] + extra)

    cards = [CRLF.join(cc.fold(ln) for ln in a["raw"].splitlines() if ln) for a in apple]
    for r in google_only + google_nophone_new:
        pre, giv = r.get(COLS["prefix"], ""), r.get(COLS["first"], "")
        lines = ["BEGIN:VCARD", "VERSION:3.0", f"N:;{giv};;{pre};", f"FN:{full(pre, giv)}"]
        for k, v in r.items():
            if k and "Phone" in k and "Value" in k and v:
                lines += [f"TEL;TYPE=CELL:{p.strip()}" for p in v.split(":::") if p.strip()]
            if k and "E-mail" in k and "Value" in k and v:
                lines += [f"EMAIL;TYPE=INTERNET:{x.strip()}" for x in v.split(":::") if x.strip()]
        bd = (r.get("Birthday") or "").replace("-", "")
        if bd:
            lines.append(f"BDAY:{bd}")
        lines.append("END:VCARD")
        cards.append(CRLF.join(cc.fold(x) for x in lines))
    (D / "final_apple.vcf").write_bytes((CRLF.join(cards) + CRLF).encode("utf-8"))

    dup_rows = []
    for source, items in (("apple", [(full(a["n"][0], a["n"][1]), a["keys"]) for a in apple]),
                          ("google", [(full(r.get(COLS["prefix"], ""), r.get(COLS["first"], "")), r["_keys"]) for r in grows])):
        seen = {}
        for name, keys in items:
            for k in keys:
                seen.setdefault(k, []).append(name)
        for k, names in seen.items():
            if len(names) > 1:
                dup_rows.append([source, k, " | ".join(names)])
    with (D / "duplicates_review.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["source", "phone (last 10 digits)", "contacts sharing it"])
        w.writerows(dup_rows)
    print(f"exact duplicates dropped: google {gdrop}, apple {adrop}")
    print(f"apple-only with phone {len(apple_only)}, apple-only no phone {len(apple_nophone_new)}, google-only {len(google_only)}, google-only no phone {len(google_nophone_new)}")
    print(f"final_google.csv: {len(grows) + len(extra)} contacts; final_apple.vcf: {len(cards)} cards; shared-phone groups left for review: {len(dup_rows)}")


if __name__ == "__main__":
    main()
