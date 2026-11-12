"""Clean contact names in a Google Contacts CSV and an Apple vCard file, locally. Prints COUNTS ONLY, never a name or number.

Rules (owner, 2026-11-12): a title such as Dr or دكتور goes to the Name Prefix field in canonical form (Dr., د., Eng., م., ...);
the first name field holds one given name; middle names go to the middle field; the last word is the family name; a word
repeated in a row (first and last field equal, 'Ahmed Ahmed') is kept once.

Usage: python contacts_clean.py <google.csv> <apple.vcf>   (either may be '-'); writes *_clean.csv and *_clean.vcf next to the inputs.
"""
import csv
import re
import sys
from pathlib import Path

import nowindow  # noqa: F401

PREFIXES = {
    "dr": "Dr.", "doctor": "Dr.", "eng": "Eng.", "engineer": "Eng.", "mr": "Mr.", "mrs": "Mrs.", "ms": "Ms.", "miss": "Ms.",
    "prof": "Prof.", "professor": "Prof.", "sir": "Sir",
    "دكتور": "د.", "دكتوره": "د.", "الدكتور": "د.", "الدكتوره": "د.", "د": "د.",
    "مهندس": "م.", "مهندسه": "م.", "المهندس": "م.", "المهندسه": "م.", "م": "م.",
    "استاذ": "أ.", "استاذه": "أ.", "الاستاذ": "أ.", "الاستاذه": "أ.", "أستاذ": "أ.", "أستاذة": "أ.", "الأستاذ": "أ.", "الأستاذة": "أ.",
    "حاج": "الحاج", "الحاج": "الحاج", "حاجه": "الحاجة", "الحاجه": "الحاجة", "الحاجة": "الحاجة",
}
ARABIC_FIX = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ة": "ه", "ى": "ي"})
stats = {"spellings_unified": 0, "contacts": 0, "changed": 0, "prefix_moved": 0, "repeats_removed": 0, "split_full_name": 0}


def key(word: str) -> str:
    return word.strip(" .،,-_").lower().translate(ARABIC_FIX)


ARABIC_CANON = {  # one spelling per name (owner, 2026-11-12); keys are compared after key()
    "عبدالله": "عبد الله", "عبد الله": "عبد الله", "عبد اللة": "عبد الله", "عبداللة": "عبد الله", "عبد اللَه": "عبد الله",
    "عبدالرحمن": "عبد الرحمن", "عبدالرحمان": "عبد الرحمن", "عبد الرحمان": "عبد الرحمن",
    "معاذ": "معاذ", "معاد": "معاذ", "كريم": "كريم", "كريـم": "كريم", "يوسف": "يوسف", "يوسـف": "يوسف",
}
LATIN_CANON = {  # transliteration variants and franco spellings -> one form
    "abdullah": "Abdullah", "abdallah": "Abdullah", "abdulla": "Abdullah", "abdalla": "Abdullah", "abdelah": "Abdullah", "3bdallah": "Abdullah", "3bdullah": "Abdullah",
    "mohamed": "Mohamed", "mohammed": "Mohamed", "muhammad": "Mohamed", "mohamad": "Mohamed", "mo7amed": "Mohamed", "mo7med": "Mohamed", "mohmed": "Mohamed",
    "ahmed": "Ahmed", "ahmad": "Ahmed", "a7med": "Ahmed", "ahmmed": "Ahmed",
    "karim": "Karim", "kareem": "Karim", "kerim": "Karim",
    "moaz": "Moaz", "muaz": "Moaz", "mo3az": "Moaz", "moaaz": "Moaz", "muath": "Moaz",
    "omar": "Omar", "umar": "Omar", "3omar": "Omar",
    "youssef": "Youssef", "yousef": "Youssef", "yusuf": "Youssef", "youssif": "Youssef", "yosef": "Youssef",
    "mostafa": "Mostafa", "mustafa": "Mostafa", "moustafa": "Mostafa", "mostfa": "Mostafa",
    "mahmoud": "Mahmoud", "mahmod": "Mahmoud", "mahmood": "Mahmoud",
    "ibrahim": "Ibrahim", "ebrahim": "Ibrahim", "abraham": "Ibrahim",
    "hossam": "Hossam", "hosam": "Hossam", "hussam": "Hossam", "hussein": "Hussein", "hosain": "Hussein", "hossein": "Hussein",
    "sherif": "Sherif", "shereef": "Sherif", "sharif": "Sherif",
}
ABD_SPLIT = re.compile(r"^(عبد)(ال\w+)$")  # عبدالمجيد -> عبد المجيد


def canon_word(word: str) -> str:
    k = key(word)
    if k in ARABIC_CANON:
        return ARABIC_CANON[k]
    m = ABD_SPLIT.match(word.strip())
    if m and key(m.group(2)) not in ("الله",):
        return f"{m.group(1)} {m.group(2)}"
    if k in LATIN_CANON:
        stats["spellings_unified"] += 1
        return LATIN_CANON[k]
    return word


def canon_name(words):
    out = []
    for w in words:
        c = canon_word(w)
        if c != w:
            stats["spellings_unified"] += 0 if w.isascii() else 1
        out.append(c)
    return out


COMPOUND = {"عبد", "ابو", "أبو", "ام", "أم", "بن", "ابن", "بنت", "ذو", "abd", "abdel", "abdul", "abu", "umm", "bin", "ibn", "bint"}


def join_compounds(words):
    """Keep names such as 'عبد الله' or 'Abu Bakr' as one word so they are not split into given and family names."""
    out = []
    i = 0
    while i < len(words):
        if key(words[i]) in {key(c) for c in COMPOUND} and i + 1 < len(words):
            out.append(words[i] + " " + words[i + 1])
            i += 2
        else:
            out.append(words[i])
            i += 1
    return out


def clean_name(prefix: str, first: str, middle: str, last: str, suffix: str):
    """Return (prefix, first, middle, last, suffix, changed?)."""
    original = (prefix, first, middle, last, suffix)
    words = " ".join(x for x in (prefix, first, middle, last) if x and x.strip()).split()
    canon = ""
    while words and key(words[0]) in PREFIXES and len(words) > 1:
        canon = canon or PREFIXES[key(words[0])]
        words = words[1:]
    if canon and not prefix.strip():
        stats["prefix_moved"] += 1
    final_prefix = canon or (prefix.strip() if prefix else "")
    deduped = []
    for w in words:
        if deduped and key(w) == key(deduped[-1]) and key(w):
            stats["repeats_removed"] += 1
            continue
        deduped.append(w)
    deduped = join_compounds(canon_name(deduped))
    if len(deduped) >= 2 and not middle.strip() and not last.strip():
        stats["split_full_name"] += 1
    # owner rule (2026-11-12): only Prefix and First Name; the first-name field holds the full name; no middle, last or company
    if final_prefix:
        ptoks = [key(x) for x in final_prefix.split()]
        while len(deduped) > 1 and key(deduped[0]) in ptoks:
            deduped = deduped[1:]
    given, mid, fam = " ".join(deduped), "", ""
    result = (final_prefix, given, mid, fam, suffix.strip() if suffix else "")
    return (*result, tuple(x.strip() for x in original) != result)


def clean_google(src: Path, suffix: str = "_clean") -> int:
    with src.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
        fields = list(rows[0].keys()) if rows else []
    cols = {"prefix": "Name Prefix", "first": "First Name", "middle": "Middle Name", "last": "Last Name", "suffix": "Name Suffix"}
    if not all(c in fields for c in cols.values()):
        print("google csv: expected columns missing; found", len(fields), "columns")
        return 0
    for row in rows:
        stats["contacts"] += 1
        p, f, m, l, s, changed = clean_name(row[cols["prefix"]], row[cols["first"]], row[cols["middle"]], row[cols["last"]], row[cols["suffix"]])
        if changed:
            stats["changed"] += 1
            row[cols["prefix"]], row[cols["first"]], row[cols["middle"]], row[cols["last"]], row[cols["suffix"]] = p, f, m, l, s
    out = src.with_name(src.stem + suffix + ".csv")
    with out.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"google: {len(rows)} contacts -> {out.name}")
    return len(rows)


CRLF_SP = chr(13) + chr(10) + " "


def fold(line: str, limit: int = 74) -> str:
    """RFC 6350 line folding (75 octets)."""
    if len(line.encode("utf-8")) <= limit:
        return line
    parts, cur, size = [], "", 0
    for ch in line:
        n = len(ch.encode("utf-8"))
        if size + n > limit:
            parts.append(cur)
            cur, size = "", 1
        cur += ch
        size += n
    parts.append(cur)
    return CRLF_SP.join(parts)


def clean_vcf(src: Path, suffix: str = "_clean") -> int:
    text = src.read_text(encoding="utf-8-sig", errors="replace")
    text = re.sub(r"\r?\n[ \t]", "", text)  # unfold
    cards = re.split(r"(?=BEGIN:VCARD)", text)
    out_cards = []
    count = 0
    for card in cards:
        if "BEGIN:VCARD" not in card:
            continue
        count += 1
        stats["contacts"] += 1
        lines = card.strip().splitlines()
        n_idx = next((i for i, ln in enumerate(lines) if re.match(r"N[;:]", ln)), None)
        if n_idx is not None:
            head, _, value = lines[n_idx].partition(":")
            parts = (value.split(";") + [""] * 5)[:5]
            fam, giv, mid, pre, suf = parts
            p, f, m, l, s, changed = clean_name(pre, giv, mid, fam, suf)
            if changed:
                stats["changed"] += 1
                lines[n_idx] = f"{head}:{l};{f};{m};{p};{s}"
                fn = " ".join(x for x in (p, f, m, l, s) if x)
                for i, ln in enumerate(lines):
                    if re.match(r"FN[;:]", ln):
                        lines[i] = f"FN:{fn}"
        out_cards.append("\r\n".join(fold(ln) for ln in lines))
    out = src.with_name(src.stem + suffix + ".vcf")
    # bytes, not write_text: Windows newline translation turned CRLF into CR CR LF and iCloud rejected the file
    out.write_bytes(("\r\n".join(out_cards) + "\r\n").encode("utf-8"))
    print(f"apple: {count} contacts -> {out.name}")
    return count


def main(argv: list) -> int:
    g, a, suffix = (argv + ["-", "-", "_clean"])[:3]
    if g != "-":
        clean_google(Path(g), suffix)
    if a != "-":
        clean_vcf(Path(a), suffix)
    print("counts:", stats)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
