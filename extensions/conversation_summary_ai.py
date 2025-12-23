# extensions/conversation_summary_ai.py
"""
Tóm tắt hội thoại dài để giữ ý quan trọng
KHÔNG phụ thuộc app.py
"""

import json
import os
import time

SUMMARY_FILE = "conversation_summary.json"
TRIGGER_COUNT = 20  # sau 20 lượt thì tóm tắt

def _load(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def summarize(memory: list):
    """
    memory: list các dict {role, content, time}
    """
    if len(memory) < TRIGGER_COUNT:
        return None

    important = []
    for m in memory[-TRIGGER_COUNT:]:
        text = m.get("content", "")
        if any(k in text.lower() for k in ["quan trọng", "thích", "không thích", "cần", "mục tiêu"]):
            important.append(text)

    if not important:
        important = [m["content"] for m in memory[-5:]]

    summary = {
        "time": time.time(),
        "summary": important[:5]  # giữ 5 ý chính
    }

    summaries = _load(SUMMARY_FILE, [])
    summaries.append(summary)
    summaries = summaries[-10:]  # giữ 10 bản tóm tắt gần nhất
    _save(SUMMARY_FILE, summaries)

    return summary
