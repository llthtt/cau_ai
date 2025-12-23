import os, json, time, re, requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ================= CONFIG =================
API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o-mini"
MEMORY_FILE = "memory.json"
MAX_MEMORY = 20

# ================= MEMORY =================
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_memory(role, content):
    mem = load_memory()
    mem.append({"role": role, "content": content, "time": time.time()})
    mem = mem[-MAX_MEMORY:]
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, ensure_ascii=False, indent=2)

def build_context():
    return [{"role": m["role"], "content": m["content"]} for m in load_memory()]

# ================= TEXT CLEANER (CỐT – KHÓA) =================
def clean_text(text: str) -> str:
    if not text:
        return text
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\n\s*-\s*", "\n- ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

# ================= ROUTES =================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"reply": "Mình chưa nghe rõ, bạn nói lại nhé."})

    save_memory("user", text)

    messages = [
        {
            "role": "system",
            "content": (
                "Bạn là Bé Cậu – trợ lý cá nhân tiếng Việt.\n"
                "QUY TẮC BẮT BUỘC:\n"
                "- Trình bày rõ ràng, xuống dòng gọn gàng\n"
                "- Mục lớn đánh số 1,2,3\n"
                "- Ý con dùng dấu '-'\n"
                "- Không dùng ###, **, ký tự thừa\n"
                "- Văn phong đời, dễ nghe, dễ đọc\n"
                "- Tối ưu cho đọc giọng nói"
            )
        }
    ] + build_context() + [{"role": "user", "content": text}]

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.55,
        "max_tokens": 700
    }

    try:
        r = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=30
        )
        data = r.json()
        reply = data["choices"][0]["message"]["content"]

        # ===== FINAL CLEAN – KHÓA =====
        reply = clean_text(reply)
        # ==============================

        save_memory("assistant", reply)
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Lỗi hệ thống: {e}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
