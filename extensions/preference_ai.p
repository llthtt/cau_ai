# extensions/preference_ai.py
"""
Ghi nhớ sở thích cá nhân của người dùng
KHÔNG phụ thuộc app.py
"""

import json
import os
import time

PREF_FILE = "user_preferences.json"

KEYWORDS = {
    "thích": "like",
    "không thích": "dislike",
    "ghét": "dislike",
    "muốn": "want",
    "quan tâm": "interest"
}

def _load():
    if not os.path.exists(PREF_FILE):
        return []
    try:
        with open(PREF_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def _save(data):
    with open(PREF_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def extract_preferences(text: str):
    text_l = text.lower()
    prefs = _load()
    for k, t in KEYWORDS.items():
        if k in text_l:
            prefs.append({
                "type": t,
                "text": text,
                "time": time.time()
            })
    prefs = prefs[-50:]  # giữ 50 sở thích gần nhất
    _save(prefs)
    return prefs

def summarize_preferences():
    prefs = _load()
    if not prefs:
        return "Mình chưa ghi nhận rõ sở thích nào của bạn."
    likes = [p["text"] for p in prefs if p["type"] == "like"]
    dislikes = [p["text"] for p in prefs if p["type"] == "dislike"]

    lines = ["📌 Mình ghi nhận:"]
    if likes:
        lines.append("👍 Bạn thích:")
        lines.extend(f"- {t}" for t in likes[-3:])
    if dislikes:
        lines.append("👎 Bạn không thích:")
        lines.extend(f"- {t}" for t in dislikes[-3:])
    return "\n".join(lines)
