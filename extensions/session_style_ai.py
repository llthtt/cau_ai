import os, json, random

SESSION_DIR = "sessions"

STYLES = [
    "EQ cao, nói nhẹ nhàng, dễ hiểu.",
    "Trả lời ngắn gọn, tập trung giải pháp.",
    "Giọng thân thiện như bạn bè.",
    "Phân tích logic, rõ ràng từng bước."
]

def style_file(sid):
    return os.path.join(SESSION_DIR, f"{sid}.meta.json")

def get_style(sid):
    file = style_file(sid)

    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f).get("style", STYLES[0])

    style = random.choice(STYLES)

    with open(file, "w", encoding="utf-8") as f:
        json.dump({"style": style}, f, ensure_ascii=False, indent=2)

    return style
