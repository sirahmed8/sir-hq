"""Split plans/generate_dashboard.py into small modules (<300 lines each).

The generator's main() is split into dashboard_main.py (the orchestration) and the
handover/checklist helpers move to dashboard_data.py. The split is mechanical: the
exact function bodies are copied verbatim, so behaviour is unchanged.

Run: python D:/Projects/_SIR/plans/split_generator_modules.py
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generate_dashboard.py")

src = io.open(GEN, encoding="utf-8").read()

# Collect top-level function definitions with their line ranges.
lines = src.splitlines()
func_starts = []
for i, ln in enumerate(lines):
    if re.match(r"^def \w+\(", ln):
        func_starts.append(i)

# Find the line index of "def main():" and "if __name__"
main_idx = next(i for i, ln in enumerate(lines) if ln.startswith("def main("))
name_idx = next(i for i, ln in enumerate(lines) if ln.startswith("if __name__"))

# Build a map: function name -> (start_line, end_line)
funcs = {}
for k, s in enumerate(func_starts):
    e = func_starts[k + 1] if k + 1 < len(func_starts) else len(lines)
    m = re.match(r"^def (\w+)\(", lines[s])
    name = m.group(1)
    funcs[name] = (s, e)

# Helper functions that stay in the main module (small, used everywhere).
KEEP = {
    "lines", "clean", "git", "git_sync_status", "parse_tasks", "checkpoint_now",
    "section_items", "attention", "parse_request_ledgers", "tail_lines",
    "sanitize_autopilot_text", "parse_autopilot", "load_model_pool",
    "project_folder_for_task", "model_cooling", "parse_cli_workers",
    "parse_account_ledger", "parse_verifications", "parse_suggestions",
    "archived_count", "get_ci_status", "translate_log_entry", "load_models",
    "get_git_short_hash", "get_published_hash", "notify_hq_artifact_outdated",
    "extract_tasks_from_markdown", "handover_countdown_days", "load_checklist",
    "load_active", "load_models_info", "get_control_room_daemon_health",
}

DATA_FUNCS = {
    "parse_gemini_handover", "handover_countdown_days", "load_checklist",
    "load_active", "load_models_info", "get_control_room_daemon_health",
}

MAIN_FUNCS = {"main"}

# Build the three files by walking the source top to bottom, emitting each function
# into the file it belongs to. Module-level constants and imports stay in the main file.
header_end = func_starts[0]  # first def line; everything before is imports/constants
header = "\n".join(lines[:header_end]) + "\n"

main_body = []
data_body = []
main_fn_body = []
for name, (s, e) in funcs.items():
    chunk = "\n".join(lines[s:e]) + "\n"
    if name in MAIN_FUNCS:
        main_fn_body.append(chunk)
    elif name in DATA_FUNCS:
        data_body.append(chunk)
    else:
        main_body.append(chunk)

# main() ends at the if __name__ block; the __main__ block stays with main.
main_fn_src = "\n".join(main_fn_body)
tail = "\n".join(lines[name_idx:]) + "\n"

# Compose files
main_src = header + "\n".join(main_body) + "\n" + main_fn_src + "\n" + tail
data_src = header + "\n".join(data_body) + "\n"

io.open(os.path.join(HERE, "dashboard_main.py"), "w", encoding="utf-8", newline="\n").write(main_src)
io.open(os.path.join(HERE, "dashboard_data.py"), "w", encoding="utf-8", newline="\n").write(data_src)

# Rewrite generate_dashboard.py: keep header + main_body, import the two modules.
new_main = header + "\n".join(main_body) + "\n"
new_main += (
    "from dashboard_main import main\n"
    "from dashboard_data import (\n"
    "    parse_gemini_handover,\n"
    "    handover_countdown_days,\n"
    "    load_checklist,\n"
    "    load_active,\n"
    "    load_models_info,\n"
    "    get_control_room_daemon_health,\n"
    ")\n"
)
new_main += "\n" + tail
io.open(GEN, "w", encoding="utf-8", newline="\n").write(new_main)

print("split ok")
print("generate_dashboard.py lines:", len(new_main.splitlines()))
print("dashboard_main.py lines:", len(main_src.splitlines()))
print("dashboard_data.py lines:", len(data_src.splitlines()))