import re

dashboard_py = "D:/Projects/_SIR/plans/generate_dashboard.py"

with open(dashboard_py, "r", encoding="utf-8") as f:
    code = f.read()

old_fallback_pattern = """        else:
            # Fallback to .sir/TASKS.md
            tasks_file = os.path.join(folder, ".sir", "TASKS.md")
            if os.path.isfile(tasks_file):
                try:
                    with open(tasks_file, "r", encoding="utf-8") as tf:
                        for l in tf:
                            ls = l.strip()
                            if ls.startswith("- [ ]"):
                                clean_t = re.sub(r"^-\\s*\\[\\s*\\]\\s*", "", ls)
                                clean_t = re.sub(r"\\|\\s*owner:\\s*[^|]+\\|", "", clean_t)
                                clean_t = re.sub(r"[*_`]", "", clean_t).strip()
                                tasks.append(clean_t[:120])
                                if len(tasks) >= 10:
                                    break
                except Exception:
                    pass
            display_path = f"_SIR/plans/{slug}.md (Charter Master Plan pending R10)\""""

new_deep_plan_logic = """        else:
            # Check for deep plan authored by Planner in _SIR/plans/<slug>-DEEP.md
            deep_plan = os.path.join(HERE, f"{slug}-DEEP.md")
            if os.path.isfile(deep_plan):
                has_mp = True
                display_path = f"_SIR/plans/{slug}-DEEP.md"
                try:
                    with open(deep_plan, "r", encoding="utf-8") as dpf:
                        lines = dpf.readlines()
                    in_tasks = False
                    for line in lines:
                        line_str = line.strip()
                        if re.match(r"^##\\s*(?:\\d+\\.?)?\\s*(?:The First\\s*\\d+\\s*Prioritized\\s*Tasks|Next\\s*10\\s*Tasks)", line_str, re.I):
                            in_tasks = True
                            continue
                        if in_tasks and re.match(r"^##\\s+[A-Za-z0-9]", line_str) and not re.search(r"Prioritized\\s*Tasks|Next\\s*10", line_str, re.I):
                            break
                        if in_tasks:
                            m_h3 = re.match(r"^###\\s*(?:Task\\s*\\d+:|[A-Z0-9]+-\\d+\\s*\\||\\d+\\.)\\s*(.*)", line_str)
                            m_num = re.match(r"^\\d+\\.\\s*(.*)", line_str)
                            if m_h3:
                                clean_t = re.sub(r"[*_`]", "", m_h3.group(1)).strip()
                                tasks.append(clean_t)
                            elif m_num:
                                clean_t = re.sub(r"[*_`]", "", m_num.group(1)).strip()
                                tasks.append(clean_t)
                            if len(tasks) >= 10:
                                break
                except Exception:
                    pass
            else:
                # Fallback to .sir/TASKS.md
                tasks_file = os.path.join(folder, ".sir", "TASKS.md")
                if os.path.isfile(tasks_file):
                    try:
                        with open(tasks_file, "r", encoding="utf-8") as tf:
                            for l in tf:
                                ls = l.strip()
                                if ls.startswith("- [ ]"):
                                    clean_t = re.sub(r"^-\\s*\\[\\s*\\]\\s*", "", ls)
                                    clean_t = re.sub(r"\\|\\s*owner:\\s*[^|]+\\|", "", clean_t)
                                    clean_t = re.sub(r"[*_`]", "", clean_t).strip()
                                    tasks.append(clean_t[:120])
                                    if len(tasks) >= 10:
                                        break
                    except Exception:
                        pass
                display_path = f"_SIR/plans/{slug}.md (Charter Master Plan pending R10)\""""

assert old_fallback_pattern in code, "old_fallback_pattern not found"
code = code.replace(old_fallback_pattern, new_deep_plan_logic)

with open(dashboard_py, "w", encoding="utf-8") as f:
    f.write(code)

print("generate_dashboard.py updated with DEEP plans indexing!")
