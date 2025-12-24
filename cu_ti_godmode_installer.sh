#!/data/data/com.termux/files/usr/bin/bash

# ================================
#  CU TÍ - GOD MODE INSTALLER
#  Safe Research Mode (Termux)
# ================================

set -e

echo "========================================"
echo "🤖 Installing CU TÍ - GOD MODE"
echo "📱 Environment: Termux (Android)"
echo "🛡️ Mode: Safe Research Mode"
echo "========================================"

# --- Check Termux ---
if [ ! -d "/data/data/com.termux/files" ]; then
  echo "❌ This installer must be run inside Termux."
  exit 1
fi

# --- Update repo & base tools ---
echo "🔄 Updating Termux packages..."
pkg update -y
pkg upgrade -y

echo "📦 Installing base dependencies..."
pkg install -y \
  python \
  git \
  termux-api \
  curl

# --- Python version check ---
echo "🐍 Checking Python..."
python - <<'EOF'
import sys
assert sys.version_info >= (3, 10)
print("✔ Python OK:", sys.version)
EOF

# --- Ensure pip user base ---
echo "📦 Ensuring pip user environment..."
mkdir -p ~/.local/bin
export PATH="$HOME/.local/bin:$PATH"

# --- Install Python dependencies (USER SPACE ONLY) ---
echo "📦 Installing Python libraries (user mode)..."
pip install --user --no-warn-script-location requests flask

# --- Verify Python libraries ---
echo "🔍 Verifying Python libraries..."
python - <<'EOF'
import requests, flask
print("✔ requests OK:", requests.__version__)
print("✔ flask OK:", flask.__version__)
EOF

# --- Create GOD MODE config ---
echo "🧠 Initializing CU TÍ identity..."
mkdir -p config

cat > config/cu_ti_identity.json <<'EOF'
{
  "name": "Cu Tí",
  "version": "1.0",
  "mode": "GOD MODE - Safe Research",
  "persona": {
    "style": "Gần gũi, ngắn gọn, thực tế",
    "identity": "AI Cu Tí, không phải Bé Cậu hay AI khác",
    "language": "vi",
    "rules": [
      "Luôn xưng là Cu Tí",
      "Không sử dụng lời chào hay phong cách của Bé Cậu",
      "Trả lời trung thực, rõ ràng",
      "Ưu tiên hỗ trợ kỹ thuật và nghiên cứu"
    ]
  }
}
EOF

echo "✔ CU TÍ identity created"

# --- Final environment test ---
echo "🧪 Final environment test..."
python - <<'EOF'
print("✔ Environment ready for CU TÍ")
EOF

echo "========================================"
echo "✅ CU TÍ installation COMPLETE"
echo "👉 Run CU TÍ with:"
echo "   python app.py"
echo "========================================"
