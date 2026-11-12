#!/usr/bin/env python3
"""video_digest.py - turn a short video into a Markdown digest.

Usage:
    python video_digest.py <url-or-local-video-file> [--force] [--no-vision]

Pipeline: yt-dlp download (Chrome cookies only as a retry, never printed)
-> ffmpeg audio extract -> Groq whisper-large-v3-turbo transcription
(fallback: local faster-whisper) -> 6 evenly spaced frames -> Gemini vision
scene notes + takeaways/product ideas -> _local/videos/<id>/digest.md.

Everything lands under D:/Projects/_SIR/_local/videos/ which is gitignored.
Keys are read from _local/api-keys.env and never printed.
Stdlib only for this file; the local whisper fallback uses a separate
interpreter that has faster-whisper installed.
"""
import argparse
import base64
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

SIR_ROOT = Path(__file__).resolve().parent.parent
LOCAL_DIR = SIR_ROOT / "_local"
KEYS_ENV = LOCAL_DIR / "api-keys.env"
VIDEOS_DIR = LOCAL_DIR / "videos"

# Python that has faster-whisper + requests installed (verified 2026-11-12).
LOCAL_WHISPER_PYTHON = os.environ.get(
    "VIDEO_LOCAL_PYTHON",
    r"C:\Users\a7med\AppData\Local\Python\bin\python.exe",
)
LOCAL_WHISPER_SCRIPT = Path(__file__).resolve().parent / "video_transcribe_local.py"
LOCAL_WHISPER_MODEL = os.environ.get("VIDEO_LOCAL_WHISPER_MODEL", "base")

GROQ_MODEL = os.environ.get("VIDEO_GROQ_MODEL", "whisper-large-v3-turbo")
GEMINI_MODELS = [
    m.strip()
    for m in os.environ.get("VIDEO_GEMINI_MODELS", "gemini-3.6-flash,gemini-3.5-flash,gemini-flash-latest").split(",")
    if m.strip()
]
FRAME_COUNT = 6
MAX_AUDIO_BYTES = 24 * 1024 * 1024  # stay under Groq's ~25 MB upload cap
DOWNLOAD_TIMEOUT = 600


class StepError(RuntimeError):
    pass


def log(msg: str) -> None:
    print(f"[video_digest] {msg}", flush=True)


def load_keys() -> dict:
    keys = {}
    if KEYS_ENV.exists():
        for line in KEYS_ENV.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            keys[k.strip()] = v.strip().strip('"').strip("'")
    return keys


def run(cmd: list, timeout: int = 300, cwd: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=cwd,
        encoding="utf-8",
        errors="replace",
    )


def which(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise StepError(f"{name} not found on PATH")
    return path


def slugify(text: str, maxlen: int = 48) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return (slug[:maxlen].strip("-") or "video")


# ---------------------------------------------------------------- metadata

def yt_dlp_id(url: str) -> str:
    """Cheap id fetch; falls back to a stable hash of the URL."""
    try:
        proc = run([which("yt-dlp"), "--get-id", "--no-playlist", url], timeout=60)
        vid = proc.stdout.strip().splitlines()[0].strip() if proc.stdout.strip() else ""
        if proc.returncode == 0 and vid:
            return re.sub(r"[^A-Za-z0-9_-]+", "-", vid)[:80]
    except Exception:
        pass
    return "u-" + hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]


def fetch_info(url: str, workdir: Path) -> dict:
    info_path = workdir / "info.json"
    proc = run([which("yt-dlp"), "-J", "--no-playlist", "--skip-download", url], timeout=120)
    if proc.returncode != 0 or not proc.stdout.strip():
        raise StepError(f"yt-dlp info failed: {proc.stderr.strip()[-400:]}")
    info_path.write_text(proc.stdout, encoding="utf-8")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise StepError(f"yt-dlp info JSON unparsable: {exc}") from exc


def probe_duration(path: Path) -> float:
    proc = run(
        [
            which("ffprobe"), "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ],
        timeout=60,
    )
    try:
        return float(proc.stdout.strip())
    except ValueError:
        return 0.0


def probe_has_video(path: Path) -> bool:
    proc = run(
        [
            which("ffprobe"), "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(path),
        ],
        timeout=60,
    )
    return "video" in proc.stdout


# ---------------------------------------------------------------- download

def download_url(url: str, workdir: Path, info: dict | None) -> Path:
    ytdlp = which("yt-dlp")
    out_tmpl = str(workdir / "source.%(ext)s")
    base_cmd = [ytdlp, "-f", "bv*[height<=720]+ba/b[height<=720]/b", "--merge-output-format", "mp4"]
    attempts = [base_cmd, base_cmd + ["--cookies-from-browser", "chrome"]]
    if info is not None:
        info_path = workdir / "info.json"
        attempts = [[*a, "--load-info-json", str(info_path)] for a in attempts]
    last_err = ""
    for i, cmd in enumerate(attempts):
        full = cmd + ["-o", out_tmpl, url]
        log(f"yt-dlp download attempt {i + 1}")
        proc = run(full, timeout=DOWNLOAD_TIMEOUT)
        if proc.returncode == 0:
            files = sorted(workdir.glob("source.*"), key=lambda p: p.stat().st_size, reverse=True)
            media = [p for p in files if p.suffix.lower() in {".mp4", ".mkv", ".webm", ".mov"}]
            if media:
                return media[0]
            if files:
                return files[0]
        last_err = (proc.stderr or proc.stdout).strip()[-400:]
    raise StepError(f"download failed: {last_err}")


# ---------------------------------------------------------------- audio

def extract_audio(video: Path, workdir: Path) -> Path:
    ffmpeg = which("ffmpeg")
    wav = workdir / "audio.wav"
    proc = run(
        [ffmpeg, "-y", "-v", "error", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000",
         "-c:a", "pcm_s16le", str(wav)],
        timeout=300,
    )
    if proc.returncode != 0 or not wav.exists():
        raise StepError(f"ffmpeg audio extraction failed: {proc.stderr.strip()[-300:]}")
    if wav.stat().st_size > MAX_AUDIO_BYTES:
        mp3 = workdir / "audio.mp3"
        proc = run(
            [ffmpeg, "-y", "-v", "error", "-i", str(wav), "-ac", "1", "-ar", "16000",
             "-c:a", "libmp3lame", "-b:a", "32k", str(mp3)],
            timeout=300,
        )
        if proc.returncode == 0 and mp3.exists():
            wav.unlink(missing_ok=True)
            return mp3
    return wav


def transcribe_groq(audio: Path, keys: dict) -> dict | None:
    key = keys.get("GROQ_API_KEY")
    if not key:
        log("GROQ_API_KEY missing, skipping Groq")
        return None
    boundary = uuid.uuid4().hex
    mime = mimetypes.guess_type(audio.name)[0] or "application/octet-stream"
    if audio.suffix.lower() == ".wav":
        mime = "audio/wav"
    elif audio.suffix.lower() == ".mp3":
        mime = "audio/mpeg"
    parts = []

    def field(name: str, value: str) -> None:
        parts.append(
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n".encode()
        )

    field("model", GROQ_MODEL)
    field("response_format", "verbose_json")
    field("temperature", "0")
    fname = audio.name
    head = (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{fname}\"\r\n"
        f"Content-Type: {mime}\r\n\r\n"
    ).encode()
    parts.append(head + audio.read_bytes() + b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode())
    body = b"".join(parts)

    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/audio/transcriptions",
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Content-Length": str(len(body)),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        text = (data.get("text") or "").strip()
        if text:
            return {"text": text, "language": data.get("language") or "", "engine": "groq"}
        log("Groq returned empty transcript")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:300]
        log(f"Groq HTTP {exc.code}: {detail}")
    except Exception as exc:
        log(f"Groq transcription failed: {exc}")
    return None


def transcribe_local(audio: Path, workdir: Path) -> dict | None:
    candidates = [LOCAL_WHISPER_PYTHON, sys.executable]
    for py in candidates:
        if not py or not Path(py).exists():
            continue
        out_json = workdir / "transcript_local.json"
        try:
            proc = run(
                [py, str(LOCAL_WHISPER_SCRIPT), str(audio), str(out_json), LOCAL_WHISPER_MODEL],
                timeout=1800,
            )
        except Exception as exc:
            log(f"local whisper launch failed ({py}): {exc}")
            continue
        if proc.returncode == 0 and out_json.exists():
            try:
                data = json.loads(out_json.read_text(encoding="utf-8"))
                data["engine"] = "faster-whisper"
                return data
            except json.JSONDecodeError:
                pass
        log(f"local whisper attempt failed with {py}: {(proc.stderr or '')[-300:]}")
    return None


# ---------------------------------------------------------------- frames

def grab_frames(video: Path, duration: float, workdir: Path) -> list[Path]:
    if duration <= 0 or not probe_has_video(video):
        return []
    ffmpeg = which("ffmpeg")
    frames = []
    for i in range(FRAME_COUNT):
        t = duration * (i + 0.5) / FRAME_COUNT
        out = workdir / f"frame_{i}.jpg"
        proc = run(
            [
                ffmpeg, "-y", "-v", "error", "-ss", f"{t:.2f}", "-i", str(video),
                "-frames:v", "1", "-vf", "scale='min(1280,iw)':-2", "-q:v", "3", str(out),
            ],
            timeout=120,
        )
        if proc.returncode == 0 and out.exists() and out.stat().st_size > 0:
            frames.append(out)
    return frames


# ---------------------------------------------------------------- gemini

def gemini_generate(prompt: str, images: list[Path], keys: dict) -> str | None:
    key = keys.get("GOOGLE_AI_STUDIO_KEY")
    if not key:
        log("GOOGLE_AI_STUDIO_KEY missing, skipping Gemini")
        return None
    parts = [{"text": prompt}]
    for img in images:
        b64 = base64.b64encode(img.read_bytes()).decode("ascii")
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": b64}})
    body = json.dumps({"contents": [{"parts": parts}], "generationConfig": {"temperature": 0.2}})
    last_status = None
    for model in GEMINI_MODELS:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        for attempt in range(3):
            req = urllib.request.Request(
                url,
                data=body.encode("utf-8"),
                headers={
                    "x-goog-api-key": key,
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
                },
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=180) as resp:
                    payload = json.loads(resp.read().decode("utf-8"))
                text = (
                    payload.get("candidates", [{}])[0]
                    .get("content", {})
                    .get("parts", [{}])[0]
                    .get("text", "")
                ).strip()
                if text:
                    return text
                log(f"Gemini {model} returned empty text")
                break
            except urllib.error.HTTPError as exc:
                last_status = exc.code
                detail = exc.read().decode("utf-8", errors="replace")[:200]
                if exc.code == 404:
                    log(f"Gemini model {model} not found, trying next")
                    break
                if exc.code in (429, 500, 502, 503, 504):
                    wait = 5 * (attempt + 1)
                    log(f"Gemini {model} HTTP {exc.code}, retry in {wait}s ({detail})")
                    time.sleep(wait)
                    continue
                log(f"Gemini {model} HTTP {exc.code}: {detail}")
                break
            except Exception as exc:
                log(f"Gemini {model} failed: {exc}")
                break
    log(f"Gemini vision unavailable (last status {last_status})")
    return None


def parse_json_loose(text: str):
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except json.JSONDecodeError:
                return None
    return None


def scene_notes(frames: list[Path], keys: dict, title: str, duration: float) -> str:
    if not frames:
        return "_No video frames available (audio-only source)._"
    prompt = (
        "You are analyzing frames sampled evenly across a short video. "
        f"Title: {title!r}. Duration about {duration:.0f} seconds. "
        "The images are in chronological order. Describe what happens visually in each frame "
        "and how the video is edited (cuts, text overlays, captions, memes, b-roll). "
        "Reply with ONLY a JSON object: {\"scenes\": [{\"index\": 0, \"time_hint\": \"~Xs\", \"description\": \"...\"}], "
        "\"visual_style\": \"...\", \"on_screen_text\": \"...\"}. No markdown fences."
    )
    raw = gemini_generate(prompt, frames, keys)
    if not raw:
        return "_Scene description unavailable (Gemini call failed)._"
    data = parse_json_loose(raw)
    if isinstance(data, dict):
        lines = []
        for s in data.get("scenes", []):
            if isinstance(s, dict):
                lines.append(f"- Frame {s.get('index', '?')} ({s.get('time_hint', '?')}): {s.get('description', '')}")
        if data.get("visual_style"):
            lines.append(f"- Visual style: {data['visual_style']}")
        if data.get("on_screen_text"):
            lines.append(f"- On-screen text: {data['on_screen_text']}")
        if lines:
            return "\n".join(lines)
    return raw[:4000]


def digest_analysis(title: str, transcript: str, scenes_md: str, keys: dict) -> dict:
    prompt = (
        "You are summarizing a short-form video for a solo founder who runs several small products. "
        f"Title: {title!r}\n\nTranscript:\n{transcript[:12000] or '(no speech)'}\n\n"
        f"Visual scene notes:\n{scenes_md[:6000]}\n\n"
        "Reply with ONLY a JSON object with keys: "
        "\"one_line\" (what the video is about in one sentence), "
        "\"takeaways\" (exactly 5 short strings, the most useful concrete ideas), "
        "\"product_ideas\" (up to 5 short strings: concrete feature or product ideas this video suggests "
        "for small apps like a job board, a study app, a laptop manager, a content studio, a business suite). "
        "No markdown fences."
    )
    raw = gemini_generate(prompt, [], keys)
    if not raw:
        return {"one_line": "", "takeaways": [], "product_ideas": []}
    data = parse_json_loose(raw)
    if not isinstance(data, dict):
        return {"one_line": "", "takeaways": [], "product_ideas": []}
    takeaways = [str(t) for t in data.get("takeaways", []) if str(t).strip()][:5]
    ideas = [str(t) for t in data.get("product_ideas", []) if str(t).strip()][:5]
    return {"one_line": str(data.get("one_line", "")).strip(), "takeaways": takeaways, "product_ideas": ideas}


# ---------------------------------------------------------------- main

def process(source: str, force: bool = False, no_vision: bool = False) -> Path:
    source_path = Path(source)
    is_local = source_path.exists() and source_path.is_file()
    keys = load_keys()

    if is_local:
        video = source_path.resolve()
        vid = "local-" + slugify(video.stem)[:40] + "-" + hashlib.sha1(str(video).encode()).hexdigest()[:6]
        workdir = VIDEOS_DIR / vid
        title = video.stem
        uploader = "local file"
        webpage = str(video)
        info = None
    else:
        url = source.strip()
        vid = yt_dlp_id(url)
        workdir = VIDEOS_DIR / vid
        webpage = url
        title, uploader, info = "", "", None

    digest_path = workdir / "digest.md"
    if digest_path.exists() and not force:
        log(f"digest already exists, skipping: {digest_path}")
        return digest_path

    workdir.mkdir(parents=True, exist_ok=True)

    # metadata + download / local probe
    if is_local:
        duration = probe_duration(video)
    else:
        info = fetch_info(url, workdir)
        title = str(info.get("title") or vid)
        uploader = str(info.get("uploader") or info.get("channel") or "")
        try:
            duration = float(info.get("duration") or 0)
        except (TypeError, ValueError):
            duration = 0.0
        video = download_url(url, workdir, info)

    log(f"source: {title!r} ({duration:.0f}s)")

    # audio + transcription
    audio = extract_audio(video, workdir)
    transcript = transcribe_groq(audio, keys)
    if transcript is None:
        log("Groq unavailable, trying local faster-whisper")
        transcript = transcribe_local(audio, workdir)
    if transcript is None:
        transcript = {"text": "", "language": "", "engine": "none"}
        log("no transcription engine succeeded; digest will rely on visuals only")
    log(f"transcript engine={transcript.get('engine')} lang={transcript.get('language') or '?'} chars={len(transcript.get('text',''))}")

    # frames + vision
    frames = [] if no_vision else grab_frames(video, duration, workdir)
    scenes_md = "_Visual analysis disabled (--no-vision)._" if no_vision else scene_notes(frames, keys, title, duration)

    analysis = {"one_line": "", "takeaways": [], "product_ideas": []}
    if not no_vision and keys.get("GOOGLE_AI_STUDIO_KEY"):
        analysis = digest_analysis(title, transcript.get("text", ""), scenes_md, keys)

    # write digest
    ts = time.strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# {title}",
        "",
        f"- Source: {webpage}",
        f"- Uploader: {uploader or 'unknown'}",
        f"- Duration: {duration:.0f}s" if duration else "- Duration: unknown",
        f"- Language: {transcript.get('language') or 'unknown'}",
        f"- Transcription: {transcript.get('engine', 'none')}",
        f"- Digested: {ts}",
        "",
        "## Summary",
        "",
        analysis["one_line"] or "_No summary generated._",
        "",
        "## Transcript",
        "",
        transcript.get("text") or "_No speech detected or transcription unavailable._",
        "",
        "## Scene notes",
        "",
        scenes_md,
        "",
        "## Key takeaways",
        "",
    ]
    if analysis["takeaways"]:
        lines += [f"{i}. {t}" for i, t in enumerate(analysis["takeaways"], 1)]
    else:
        lines.append("_No takeaways generated._")
    lines += ["", "## Ideas for SIR products", ""]
    if analysis["product_ideas"]:
        lines += [f"- {t}" for t in analysis["product_ideas"]]
    else:
        lines.append("_No product ideas generated._")
    lines += [
        "",
        "---",
        f"_Raw files (video, audio, frames, info.json) live next to this file in `{workdir}`. "
        "This folder is under `_local/` and is never committed._",
        "",
    ]
    digest_path.write_text("\n".join(lines), encoding="utf-8")
    log(f"digest written: {digest_path} ({digest_path.stat().st_size} bytes)")
    return digest_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Digest a short video URL or local file into Markdown.")
    ap.add_argument("source", help="Video URL (YouTube/TikTok/Instagram/...) or local video file")
    ap.add_argument("--force", action="store_true", help="Re-digest even if digest.md exists")
    ap.add_argument("--no-vision", action="store_true", help="Skip frame extraction and Gemini calls")
    args = ap.parse_args()
    try:
        out = process(args.source, force=args.force, no_vision=args.no_vision)
    except StepError as exc:
        log(f"FAILED: {exc}")
        return 1
    except Exception as exc:  # noqa: BLE001 - report any unexpected failure cleanly
        log(f"FAILED unexpected: {exc}")
        return 1
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
