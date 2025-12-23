#!/data/data/com.termux/files/usr/bin/bash
# ==================================================
# cu Tí – GOD MODE Installer
# Mode: FULL FEATURE + TERMUX SAFE
# Author: llthtt
# ==================================================

set -e

echo "=============================================="
echo "🤖 cu Tí – GOD MODE Installer"
echo "Safe Research Mode for Termux"
echo "=============================================="

# 1️⃣ Update Termux (KHÔNG đụng pip)
echo "🔄 Updating Termux packages..."
pkg update -y

# 2️⃣ System dependencies (GIỮ ĐẦY ĐỦ)
echo "📦 Installing system dependencies..."
pkg install -y \
  python \
  git \
  curl \
  wget \
  termux-api \
  mpg123 \
  pulseaudio \
  clang \
  make \
  pkg-config \
  libffi \
  openssl

# 3️⃣ Check Python
echo "🐍 Python version:"
python --version

# 4️⃣ Check pip (Termux default – KHÔNG upgrade)
echo "📌 pip version:"
pip --version || {
  echo "❌ pip missing – Termux Python broken"
  exit 1
}

# 5️⃣ Python libraries (SAFE – không động pip)
echo "📚 Installing Python libraries..."
PY_LIBS=(
  requests
)

for lib in "${PY_LIBS[@]}"; do
  if python - <<EOF 2>/dev/null
import $lib
EOF
  then
    echo "✔ $lib already installed"
  else
    echo "➕ Installing $lib"
    pip install "$lib"
  fi
done

# 6️⃣ GOD MODE config (GIỮ TÍNH NĂNG CŨ)
echo "🔥 Initializing GOD MODE..."
GODMODE_FILE="$HOME/.cu_ti_godmode.json"

if [ ! -f "$GODMODE_FILE" ]; then
cat <<EOF > "$GODMODE_FILE"
{
  "name": "cu Ti",
  "god_mode": true,
  "safe_mode": true,
  "research_only": true,
  "internet_access": true,
  "auto_update": false,
  "level": 5.5
}
EOF
  echo "🧠 GOD MODE config created"
else
  echo "🧠 GOD MODE config already exists"
fi

# 7️⃣ Final check
echo "🧪 Final environment test..."
python - << 'EOF'
import requests, json
print("✔ Python OK")
print("✔ requests OK")
EOF

echo "=============================================="
echo "✅ cu Tí installation COMPLETE"
echo "👉 Run: python app.py"
echo "=============================================="
