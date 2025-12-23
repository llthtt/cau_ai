# extensions/self_awareness_ai.py
import json, os, time

AWARENESS_FILE = "ai_self_awareness.json"

def load_awareness():
    if not os.path.exists(AWARENESS_FILE):
        return []
    try:
        with open(AWARENESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_upgrade(name: str, description: str):
    data = load_awareness()
    data.append({
        "time": time.time(),
        "name": name,
        "description": description
    })
    data = data[-20:]  # giữ 20 nâng cấp gần nhất
    with open(AWARENESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def summarize_awareness():
    data = load_awareness()
    if not data:
        return "Hiện tại Bé Cậu chưa ghi nhận nâng cấp nào."

    lines = []
    for item in data[-5:]:
        lines.append(f"- {item['name']}: {item['description']}")

    return "Bé Cậu đã được nâng cấp với các khả năng:\n" + "\n".join(lines)

def detect_awareness_question(text: str) -> bool:
    keywords = [
        "nâng cấp",
        "mới thêm",
        "cập nhật",
        "khả năng mới",
        "giờ làm được gì"
    ]
    t = text.lower()
    return any(k in t for k in keywords)
