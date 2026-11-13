#!/usr/bin/env python3
"""Report where the local voice models live on disk.

Covers the two local voice assets the owner asked about:
- Whisper speech-to-text: faster-whisper models under AI_Models_Hub/whisper
  and the Hugging Face cache copy under AI_Models_Hub/huggingface.
- Kokoro text-to-speech: the Kokoro-82M ONNX pack under
  AI_Models_Hub/kokoro (model + voice embeddings), provisioned for local
  synthesis on Windows through kokoro-onnx.

Stdlib only. Prints JSON by default; --text prints one line per model.
The hub root is resolved relative to this file, so it works from any
checkout of the _SIR repo on this machine.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

SIR_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_HUB_ROOT = os.path.join(os.path.dirname(SIR_ROOT), "AI_Models_Hub")


def _dir_size(path):
    total = 0
    for base, _dirs, files in os.walk(path):
        for name in files:
            try:
                total += os.path.getsize(os.path.join(base, name))
            except OSError:
                pass
    return total


def _entry(hub_root, model_id, label, rel_path, expect, note=""):
    path = os.path.join(hub_root, rel_path)
    if os.path.isdir(path):
        size = _dir_size(path)
        exists = all(os.path.exists(os.path.join(path, e)) for e in expect)
    elif os.path.isfile(path):
        size = os.path.getsize(path)
        exists = True
    else:
        size = 0
        exists = False
    return {
        "id": model_id,
        "label": label,
        "path": path,
        "exists": exists,
        "size_bytes": size,
        "note": note,
    }


def collect(hub_root=None):
    """Return the voice-model inventory. hub_root defaults to the sibling AI_Models_Hub."""
    hub_root = os.path.abspath(hub_root or DEFAULT_HUB_ROOT)
    entries = [
        _entry(
            hub_root,
            "whisper-faster-base",
            "Whisper STT (faster-whisper base, int8 CPU)",
            os.path.join("whisper", "faster-whisper-base"),
            ["model.bin", "config.json", "tokenizer.json", "vocabulary.txt"],
            "Used by scripts/video_transcribe_local.py via faster-whisper.",
        ),
        _entry(
            hub_root,
            "whisper-hf-cache",
            "Whisper STT (Hugging Face cache copy)",
            os.path.join("huggingface", "hub", "models--Systran--faster-whisper-base"),
            [],
            "Hugging Face hub cache of the same faster-whisper-base model.",
        ),
        _entry(
            hub_root,
            "kokoro-model",
            "Kokoro TTS (Kokoro-82M ONNX fp16)",
            os.path.join("kokoro", "model", "kokoro-v1.0.fp16.onnx"),
            [],
            "ONNX weights for local Kokoro-82M synthesis (kokoro-onnx).",
        ),
        _entry(
            hub_root,
            "kokoro-voices",
            "Kokoro TTS (voice embeddings v1.0)",
            os.path.join("kokoro", "model", "voices-v1.0.bin"),
            [],
            "All Kokoro voice embeddings in one file (kokoro-onnx voices-v1.0.bin).",
        ),
        _entry(
            hub_root,
            "kokoro-runtime",
            "Kokoro TTS (Python runtime)",
            os.path.join("kokoro", ".venv"),
            [os.path.join("Scripts", "python.exe"), os.path.join("Lib", "site-packages", "kokoro_onnx")],
            "venv with kokoro-onnx + soundfile; run kokoro\\synthesize.py.",
        ),
    ]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "hub_root": hub_root,
        "models": entries,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Report local voice model locations.")
    parser.add_argument("--text", action="store_true", help="one line per model instead of JSON")
    parser.add_argument("--hub", default=None, help="override the AI_Models_Hub root")
    args = parser.parse_args(argv)

    report = collect(args.hub)
    if args.text:
        for m in report["models"]:
            state = "OK" if m["exists"] else "MISSING"
            size_mb = m["size_bytes"] / (1024 * 1024)
            print(f"{state:7} {m['id']:22} {size_mb:8.1f} MB  {m['path']}")
        return 0
    json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
