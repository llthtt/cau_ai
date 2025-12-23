# extensions/upgrade_recorder.py
"""
Module ghi nhận nâng cấp AI.
Dùng thủ công hoặc tự động sau mỗi lần chỉnh code.
KHÔNG đụng app.py
"""

import time
from extensions.self_awareness_ai import save_upgrade

def record_upgrade(name: str, description: str):
    """
    Ghi nhận một nâng cấp mới cho AI
    """
    save_upgrade(
        name=name,
        description=description
    )

def record_batch(upgrades: list):
    """
    Ghi nhận nhiều nâng cấp cùng lúc
    upgrades = [
        ("Tên nâng cấp", "Mô tả"),
        ...
    ]
    """
    for name, desc in upgrades:
        record_upgrade(name, desc)
