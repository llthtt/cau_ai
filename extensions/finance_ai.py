import os, json, time

FINANCE_FILE = "finance.json"

def _load():
    if not os.path.exists(FINANCE_FILE):
        return []
    try:
        with open(FINANCE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def _save(data):
    with open(FINANCE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def record(text: str) -> bool:
    keywords = ["mua", "chi", "tiền", "trả", "đóng", "nạp", "giá"]
    if not any(k in text.lower() for k in keywords):
        return False

    data = _load()
    data.append({
        "text": text,
        "time": time.time()
    })
    _save(data)
    return True

def summary() -> str:
    data = _load()
    if not data:
        return ""
    return f"Bạn đã có {len(data)} ghi chú liên quan đến chi tiêu."
