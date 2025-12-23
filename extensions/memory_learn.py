# extensions/memory_learn.py
import json
import os
import re

MEMORY_FILE = "memory_profile.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "style": None,
            "topics": [],
            "avoid": [],
            "habits": [],
            "goals": []
        }
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(mem):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, ensure_ascii=False, indent=2)


def learn_from_text(text: str):
    mem = load_memory()
    t = text.lower()

    # --- style ---
    if any(x in t for x in ["trả lời ngắn", "ngắn gọn", "nói ngắn"]):
        mem["style"] = "ngắn gọn"

    # --- avoid ---
    if any(x in t for x in ["đừng dài", "không thích dài", "ghét vòng vo"]):
        if "nói vòng vo" not in mem["avoid"]:
            mem["avoid"].append("nói vòng vo")

    # --- goals ---
    if any(x in t for x in ["tôi muốn", "mục tiêu của tôi"]):
        goal = re.sub(r"(tôi muốn|mục tiêu của tôi)", "", t).strip()
        if goal and goal not in mem["goals"]:
            mem["goals"].append(goal)

    # --- topics ---
    for topic in ["tài chính", "chi tiêu", "đầu tư", "tiền bạc"]:
        if topic in t and topic not in mem["topics"]:
            mem["topics"].append(topic)

    # --- habits ---
    if "buổi tối" in t and "hay hỏi buổi tối" not in mem["habits"]:
        mem["habits"].append("hay hỏi buổi tối")

    save_memory(mem)
