#!/data/data/com.termux/files/usr/bin/bash
echo "🔄 Updating cu Tí from GitHub..."

cd ~/cau_ai || exit 1
git pull origin main

echo "📦 Re-checking Python libraries..."
pip install requests

echo "✅ Update completed"
