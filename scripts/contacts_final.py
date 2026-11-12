"""Build the final contact set (owner order 2026-11-12): Google and Apple contain the same people.
Input (already name-cleaned): _local/contacts/google_v2.csv and apple_v2.vcf. Output (same folder, local only, counts printed, no names):
  final_google.csv   Google rows + the contacts that exist only in Apple
  final_apple.vcf    Apple cards + the contacts that exist only in Google
  duplicates_review.csv   people sharing a phone number inside one source, for the owner to look at (names stay in this local file)
A contact counts as 'the same' when it shares a normalized phone number (last 10 digits). Nothing is merged automatically.
"""
import csv
import re
from pathlib import Path

import nowindow  # noqa: F401
import contacts_clean as cc

D = Path("D:/Projects/_SIR/_local/contacts")
CRLF = chr(13) + chr(10)


def norm(p: str) -> str:
    d = re.sub(r"\D", "", p)
    if d.startswith("0020"):
        d = d[4:]
    if d.startswith("20") and len(d) >= 12:
        d = d[2:]
    if d.startswith("0"):
        d = d[1:]
    return d[-10:] if len(d) >= 10 else d


def vcard_fields(card: str) -> dict:
    lines = [ln for ln in card.strip().splitlines() if ln]
    out = {"phones": [], "emails": [], "bday": "", "org": "", "n": ("", "", "", "", "")}
    for ln in lines:
        if re.match(r"N[;:]", ln):
            parts = (ln.partition(":")[2].split(";") + [""] * 5)[:5]
            out["n"] = (parts[3], parts[1], parts[2], parts[0], parts[4])  # prefix, given, middle, family, suffix
        elif re.match(r"TEL", ln):
            out["phones"].append(ln.partition(":")[2].strip())
        elif re.match(r"EMAIL", ln):
            out["emails"].append(ln.partition(":")[2].strip())
        elif ln.startswith("BDAY"):
            out["bday"] = ln.partition(":")[2].strip()
        elif ln.startswith("ORG"):
            out["org"] = ln.partition(":")[2].replace(";", " ").strip()
    return out


def load_apple() -> list:
    t = (D / "apple_v2.vcf").read_text(encoding="utf-8")
    t = re.sub(r"\r?\n[ ]", "", t)
    cards = ["BEGIN:VCARD" + c for c in t.split("BEGIN:VCARD") if "END:VCARD" in c]
    return [{"raw": c.strip(), **vcard_fields(c)} for c in cards]


def main() -> None:
    apple = load_apple()
    with (D / "google_v2.csv").open(encoding="utf-8-sig", newline="") as fh:
        grows = list(csv.DictReader(fh))
        gfields = list(grows[0].keys())
    for a in apple:
        a["keys"] = {norm(p) for p in a["phones"] if norm(p)}
    for r in grows:
        r["_keys"] = set()
        for k, v in r.items():
            if k and "Phone" in k and "Value" in k and v:
                for part in v.split(":::"):
                    if norm(part):
                        r["_keys"].add(norm(part))
    akeys = set().union(*[a["keys"] for a in apple])
    gkeys = set().union(*[r["_keys"] for r in grows])
    apple_only = [a for a in apple if a["keys"] and not (a["keys"] & gkeys)]
    apple_nophone = [a for a in apple if not a["keys"]]
    google_only = [r for r in grows if r["_keys"] and not (r["_keys"] & akeys)]

    # final_google.csv: Google rows plus Apple-only people and Apple cards without a phone (family and own card)
    cols = {"prefix": "Name Prefix", "first": "First Name", "middle": "Middle Name", "last": "Last Name", "suffix": "Name Suffix"}
    extra = []
    for a in apple_only + apple_nophone:
        row = {c: "" for c in gfields}
        pre, giv, mid, fam, suf = a["n"]
        row[cols["prefix"]], row[cols["first"]], row[cols["middle"]], row[cols["last"]], row[cols["suffix"]] = pre, giv, mid, fam, suf
        if "Phone 1 - Value" in row and a["phones"]:
            row["Phone 1 - Value"] = ":::".join(a["phones"])
        if "E-mail 1 - Value" in row and a["emails"]:
            row["E-mail 1 - Value"] = a["emails"][0]
        if "Birthday" in row and a["bday"]:
            b = a["bday"].replace("-", "")
            row["Birthday"] = f"{b[:4]}-{b[4:6]}-{b[6:8]}" if len(b) == 8 else a["bday"]
        if "Organization Name" in row:
            row["Organization Name"] = a["org"]
        extra.append(row)
    with (D / "final_google.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=gfields)
        w.writeheader()
        w.writerows([{k: r.get(k, "") for k in gfields} for r in grows] + extra)

    # final_apple.vcf: Apple cards plus Google-only people as simple cards
    cards = [a["raw"] for a in apple]
    for r in google_only:
        pre, giv, mid, fam, suf = (r.get(cols[k], "") for k in ("prefix", "first", "middle", "last", "suffix"))
        fn = " ".join(x for x in (pre, giv, mid, fam, suf) if x)
        lines = ["BEGIN:VCARD", "VERSION:3.0", f"N:{fam};{giv};{mid};{pre};{suf}", f"FN:{fn}"]
        for k, v in r.items():
            if k and "Phone" in k and "Value" in k and v:
                lines += [f"TEL;TYPE=CELL:{p.strip()}" for p in v.split(":::") if p.strip()]
            if k and "E-mail" in k and "Value" in k and v:
                lines += [f"EMAIL;TYPE=INTERNET:{x.strip()}" for x in v.split(":::") if x.strip()]
        bd = (r.get("Birthday") or "").replace("-", "")
        if bd:
            lines.append(f"BDAY:{bd}")
        if r.get("Organization Name"):
            lines.append(f"ORG:{r['Organization Name']}")
        lines.append("END:VCARD")
        cards.append(CRLF.join(cc.fold(x) for x in lines))
    (D / "final_apple.vcf").write_bytes((CRLF.join(cards) + CRLF).encode("utf-8"))

    # duplicates inside each source
    dup_rows = []
    for source, items in (("apple", [(" ".join(x for x in (a["n"][0], a["n"][1], a["n"][2], a["n"][3]) if x), a["keys"]) for a in apple]),
                          ("google", [(" ".join(x for x in (r.get(cols["prefix"], ""), r.get(cols["first"], ""), r.get(cols["middle"], ""), r.get(cols["last"], "")) if x), r["_keys"]) for r in grows])):
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
    print(f"apple {len(apple)} cards ({len(apple_nophone)} without a phone), google {len(grows)} contacts")
    print(f"apple-only with phone: {len(apple_only)}; google-only: {len(google_only)}")
    print(f"final_google.csv: {len(grows) + len(extra)} contacts; final_apple.vcf: {len(cards)} cards; shared-phone groups for review: {len(dup_rows)}")


if __name__ == "__main__":
    main()
