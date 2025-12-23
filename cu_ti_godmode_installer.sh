#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "🧠 Installing cu Tí – GOD MODE (Safe Research Mode)"

# ===== KIỂM TRA TERMUX =====
if [ ! -d /data/data/com.termux ]; then
  echo "❌ Phải chạy trong Termux"
  exit 1
fi

# ===== BIẾN ĐƯỜNG DẪN =====
BASE=$HOME/cu_ti
ROOTD=$BASE/root
LOGS=$BASE/logs

# ===== CÀI GÓI CẦN THIẾT =====
pkg update -y
pkg install -y python git termux-api mpg123
pip install --upgrade pip
pip install openai gtts vosk psutil requests

# ===== TẠO CẤU TRÚC =====
mkdir -p $BASE/{brain,voice,root,logs,memory,autonomy,learning}
mkdir -p /data/cu_ti

# ===== KILL SWITCH =====
touch /data/cu_ti/ALLOW
chmod 600 /data/cu_ti/ALLOW

# ===== PERSONA =====
cat > $BASE/brain/persona.py << 'EOF'
PERSONA = """
Tên: cu Tí
Vai trò: AI hệ điều hành cá nhân (Research Mode)
Nguyên tắc:
- Không đoán
- Không phá hệ thống
- Có thể học, có thể hành động, nhưng phải an toàn
"""
EOF

# ===== HARD RULES (KHÔNG THỂ TẮT) =====
cat > $ROOTD/hard_rules.sh << 'EOF'
#!/system/bin/sh
case "$*" in
  *"rm -rf /"*|*"dd "*|*"mkfs"*|*"format"*|*"flash"*|*"bootloader"*|*"fastboot"*)
    echo "⛔ HARD RULE BLOCKED"
    exit 13 ;;
esac
EOF
chmod +x $ROOTD/hard_rules.sh

# ===== ROOT EXECUTOR =====
cat > $ROOTD/exec.sh << 'EOF'
#!/system/bin/sh
. "$HOME/cu_ti/root/hard_rules.sh"
[ ! -f /data/cu_ti/ALLOW ] && { echo "⛔ KILL SWITCH ACTIVE"; exit 99; }

LOG="$HOME/cu_ti/logs/audit.log"
CMD="$*"

case "$CMD" in
  wifi_on) svc wifi enable ;;
  wifi_off) svc wifi disable ;;
  status) dumpsys battery | head -n 6 ;;
  *) echo "⚠️ UNKNOWN ROOT CMD" ;;
esac

echo "$(date) :: $CMD" >> "$LOG"
EOF
chmod +x $ROOTD/exec.sh

# ===== CORE CHÍNH =====
cat > $BASE/brain/core.py << 'EOF'
import os, subprocess
from openai import OpenAI
from brain.persona import PERSONA
from voice.tts import speak

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def root(cmd):
    return subprocess.getoutput(f"su -c '$HOME/cu_ti/root/exec.sh {cmd}'")

def chat(q):
    if "bật wifi" in q:
        r = root("wifi_on"); speak(r); return r
    if "tắt wifi" in q:
        r = root("wifi_off"); speak(r); return r
    if "pin" in q:
        r = root("status"); speak(r); return r

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":PERSONA},
            {"role":"user","content":q}
        ]
    )
    ans = res.choices[0].message.content
    speak(ans)
    return ans
EOF

# ===== TTS =====
cat > $BASE/voice/tts.py << 'EOF'
from gtts import gTTS
import os, time

def speak(text):
    f = f"/tmp/cu_ti_{int(time.time())}.mp3"
    gTTS(text=text, lang="vi").save(f)
    os.system(f"mpg123 {f} >/dev/null 2>&1")
EOF

# ===== RUN =====
cat > $BASE/run.py << 'EOF'
from brain.core import chat
print("🤖 cu Tí GOD MODE đã sẵn sàng (exit để thoát)")
while True:
    q = input("Bạn: ")
    if q == "exit":
        break
    print("cu Tí:", chat(q))
EOF

chmod +x $BASE/run.py

echo "✅ cu Tí GOD MODE cài xong"
echo "👉 Chạy: cd ~/cu_ti && python run.py"
