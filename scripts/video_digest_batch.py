#!/usr/bin/env python3
"""video_digest_batch.py - digest many videos, skipping finished ones.

Usage:
    python video_digest_batch.py --urls urls.txt [--dir /path/to/mp4s] [--force] [--no-vision]

urls.txt: one URL per line, blank lines and lines starting with # ignored.
--dir: every video file (.mp4 .mkv .webm .mov .avi) in the folder is digested.
Each item runs scripts/video_digest.py logic in-process; an item is skipped
when its digest.md already exists under _local/videos/<id>/.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import video_digest  # noqa: E402

VIDEO_EXTS = {".mp4", ".mkv", ".webm", ".mov", ".avi", ".m4v"}


def collect_sources(urls_file: str | None, folder: str | None) -> list[str]:
    sources = []
    if urls_file:
        for line in Path(urls_file).read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                sources.append(line)
    if folder:
        for p in sorted(Path(folder).iterdir()):
            if p.is_file() and p.suffix.lower() in VIDEO_EXTS:
                sources.append(str(p))
    return sources


def main() -> int:
    ap = argparse.ArgumentParser(description="Batch video digest: URL list file and/or folder of videos.")
    ap.add_argument("--urls", help="Text file with one video URL per line")
    ap.add_argument("--dir", help="Folder containing video files")
    ap.add_argument("--force", action="store_true", help="Re-digest everything")
    ap.add_argument("--no-vision", action="store_true", help="Skip Gemini vision steps")
    args = ap.parse_args()

    if not args.urls and not args.dir:
        ap.error("provide --urls and/or --dir")

    sources = collect_sources(args.urls, args.dir)
    if not sources:
        print("no sources found")
        return 1

    ok = failed = skipped = 0
    for i, src in enumerate(sources, 1):
        print(f"=== [{i}/{len(sources)}] {src}", flush=True)
        try:
            out = video_digest.process(src, force=args.force, no_vision=args.no_vision)
            print(f"    -> {out}", flush=True)
            ok += 1
        except Exception as exc:  # noqa: BLE001 - batch must continue past failures
            print(f"    FAILED: {exc}", flush=True)
            failed += 1
    print(f"done: {ok} digested, {failed} failed, {len(sources)} total")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
