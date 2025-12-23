import os, json, time

SESSION_DIR = "sessions"
INDEX_FILE = os.path.join(SESSION_DIR, "index.json")

# Tạo thư mục sessions nếu chưa có
os.makedirs(SESSION_DIR, exist_ok=True)

def load_index():
    if not os.path.exists(INDEX_FILE):
        return []
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_index(index):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

def register_session(sid, first_message):
    """
    Lưu session mới + đặt tên hội thoại
    """
    index = load_index()

    # Không ghi trùng session
    for s in index:
        if s["sid"] == sid:
            return

    title = first_message[:40]  # lấy 40 ký tự đầu làm tiêu đề

    index.insert(0, {
        "sid": sid,
        "title": title,
        "created": time.time()
    })

    # Giữ tối đa 30 session gần nhất
    index = index[:30]
    save_index(index)

def list_sessions():
    return load_index()
