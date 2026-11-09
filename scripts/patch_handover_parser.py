import re

target_file = "D:/Projects/_SIR/plans/generate_dashboard.py"

with open(target_file, "r", encoding="utf-8") as f:
    code = f.read()

helper_function = r'''def extract_tasks_from_markdown(file_path, limit=10):
    """Robustly extracts up to limit tasks from any MASTER_PLAN.md, *-DEEP.md, or TASKS.md file."""
    tasks = []
    if not os.path.isfile(file_path):
        return tasks
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        in_tasks = False
        for line in lines:
            line_str = line.strip()
            # Recognize section headers like:
            # ## 6. The Next 25 Prioritized Tasks
            # ## 5. The First 25 Prioritized Tasks
            # ## 4. Prioritized Engineering Backlog (First 25 Tasks)
            # ## Next 10 Tasks
            # ## Current Sprint
            if line_str.startswith("## ") and re.search(r"(?:Tasks|Backlog|Sprint|Blueprint)", line_str, re.I):
                in_tasks = True
                continue
            if in_tasks and line_str.startswith("## ") and not re.search(r"(?:Tasks|Backlog|Sprint|Blueprint)", line_str, re.I):
                break
            if in_tasks:
                # 1. Table row: | **01** | Task Title | ...
                m_tbl = re.match(r"^\|\s*\*{0,2}\d+\*{0,2}\s*\|\s*([^|]+?)\s*\|", line_str)
                # 2. H3 heading: ### CR-101 | ... or ### Task 1: ...
                m_h3 = re.match(r"^###\s*(?:Task\s*\d+:|[A-Z0-9]+-\d+\s*\||\d+\.)\s*(.*)", line_str)
                # 3. Numbered list: 1. ...
                m_num = re.match(r"^\d+\.\s*(.*)", line_str)
                # 4. Checkbox item: - [ ] ...
                m_chk = re.match(r"^-\s*\[\s*\]\s*(.*)", line_str)

                clean_t = None
                if m_tbl and not m_tbl.group(1).startswith("---") and "Task Title" not in m_tbl.group(1):
                    clean_t = m_tbl.group(1)
                elif m_h3:
                    clean_t = m_h3.group(1)
                elif m_num:
                    clean_t = m_num.group(1)
                elif m_chk:
                    clean_t = m_chk.group(1)

                if clean_t:
                    clean_t = re.sub(r"\|\s*owner:\s*[^|]+\|", "", clean_t)
                    clean_t = re.sub(r"[*_`]", "", clean_t).strip()
                    if clean_t and not clean_t.startswith("---") and clean_t not in tasks:
                        tasks.append(clean_t[:120])
                        if len(tasks) >= limit:
                            break
    except Exception:
        pass
    return tasks
'''

# Check if helper already in file
if "def extract_tasks_from_markdown(" not in code:
    code = code.replace("def parse_gemini_handover(projects):", helper_function + "\n\ndef parse_gemini_handover(projects):")

# Now replace the task extraction inside parse_gemini_handover
old_handover_logic_pattern = re.compile(
    r'    # 1\. First add Control Room / HQ itself.*?'
    r'        # Double check privacy filter on tasks',
    re.DOTALL
)

new_handover_logic = '''    # 1. First add Control Room / HQ itself
    hq_folder = os.path.normpath(os.path.join(HERE, ".."))
    hq_mp = os.path.join(hq_folder, ".sir", "MASTER_PLAN.md")
    hq_tasks = extract_tasks_from_markdown(hq_mp)

    handover_projects.append({
        "slug": "control",
        "name": "SIR Control Room (HQ)",
        "name_ar": "غرفة التحكم — المقر الرئيسي",
        "color": "#0F766E",
        "status": "verified",
        "has_master_plan": os.path.isfile(hq_mp),
        "master_plan_path": "_SIR/.sir/MASTER_PLAN.md",
        "plan_file_display": "_SIR/.sir/MASTER_PLAN.md",
        "tasks": hq_tasks[:10],
    })

    # 2. Add all portfolio projects
    for p in projects:
        slug = p["slug"]
        private = slug == "ahome"
        folder = os.path.join(ROOT, "AHome") if private else p["folder"]
        mp_path = os.path.join(folder, ".sir", "MASTER_PLAN.md")
        deep_plan = os.path.join(HERE, f"{slug}-DEEP.md")
        tasks_file = os.path.join(folder, ".sir", "TASKS.md")

        has_mp = False
        tasks = []
        display_path = f"_SIR/plans/{slug}.md"

        if private:
            has_mp = True
            tasks = [
                "1. Viewport flex column keyboard alignment in messaging UI",
                "2. Friends Mode camouflage cloak wording refinement",
                "3. Custom dropdown component replacing native select",
                "4. Eliminate white focus flashes on tab switches",
                "5. Responsive arcade HUD computed grid layout",
                "6. Active-only tab label styling across all navigation bars",
                "7. Smooth spring physics expansion for voice recording",
                "8. Safe 7-to-4 page consolidation with redirects",
                "9. Verified two-way app connection states without mock data",
                "10. Bespoke project emblem brand verification in top bar",
            ]
            display_path = "AHome/.sir/MASTER_PLAN.md (protected)"
        elif os.path.isfile(mp_path):
            has_mp = True
            tasks = extract_tasks_from_markdown(mp_path)
            display_path = f"{p['name']}/.sir/MASTER_PLAN.md"
        
        if not tasks and os.path.isfile(deep_plan):
            has_mp = True
            tasks = extract_tasks_from_markdown(deep_plan)
            display_path = f"_SIR/plans/{slug}-DEEP.md"
            
        if not tasks and os.path.isfile(tasks_file):
            tasks = extract_tasks_from_markdown(tasks_file)
            display_path = f"{p['name']}/.sir/TASKS.md"

        # Double check privacy filter on tasks'''

code = old_handover_logic_pattern.sub(new_handover_logic, code, count=1)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(code)

print("generate_dashboard.py updated with robust extract_tasks_from_markdown!")
