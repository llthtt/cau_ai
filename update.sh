#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "🔄 Updating cu Tí from GitHub..."

REPO=$HOME/cu-ti-ai
BASE=$HOME/cu_ti

if [ ! -d "$REPO" ]; then
  echo "❌ Repo chưa tồn tại. Hãy git clone trước."
  exit 1
fi

cd $REPO
git pull origin main

if [ -f cu_ti_godmode_installer.sh ]; then
  echo "➡️ Chạy installer mới nhất"
  bash cu_ti_godmode_installer.sh
else
  echo "⚠️ Không tìm thấy installer"
fi

echo "✅ Update hoàn tất"
