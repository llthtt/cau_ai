import json, os, time

LONG_MEMORY_FILE = "long_memory.json"

IMPORTANT_RULES = [
    "tôi thích",
    "tôi không thích",
    "tôi thường",
    "tôi hay",
    "từ giờ",
    "mục tiêu của tôi"
]

def load_long_memory():
    if not os.path.exists(LONG_MEMORY_FILE):
        return []
    try:
        with open(LONG_MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_long_memory(text: str):
    mem = load_long_memory()
    mem.append({
        "content": text,
        "time": time.time()
    })
    mem = mem[-50:]
    with open(LONG_MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, ensure_ascii=False, indent=2)

def extract_and_save(text: str):
    low = text.lower()
    for rule in IMPORTANT_RULES:
        if rule in low:
            save_long_memory(text)
            return True
    return False
