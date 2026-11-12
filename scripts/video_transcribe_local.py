#!/usr/bin/env python3
"""Transcribe an audio file with faster-whisper (local fallback for video_digest.py).

Usage: python video_transcribe_local.py <audio_file> <out.json> [model_size]
Writes {"text": ..., "language": ..., "segments": [...]} to out.json.
Stdlib + faster_whisper + PyAV only; run with the Python that has faster-whisper.
"""
import json
import os
import sys


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: video_transcribe_local.py <audio> <out.json> [model]", file=sys.stderr)
        return 2
    audio, out_path = sys.argv[1], sys.argv[2]
    model_size = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("VIDEO_LOCAL_WHISPER_MODEL", "base")

    from faster_whisper import WhisperModel

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio, vad_filter=True)
    segs = []
    parts = []
    for seg in segments:
        segs.append({"start": round(seg.start, 2), "end": round(seg.end, 2), "text": seg.text.strip()})
        parts.append(seg.text.strip())
    data = {
        "text": " ".join(p for p in parts if p),
        "language": info.language,
        "language_probability": round(info.language_probability, 3),
        "segments": segs,
    }
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
