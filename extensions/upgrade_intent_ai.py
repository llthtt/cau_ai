# extensions/upgrade_intent_ai.py
"""
Nhận biết câu hỏi về nâng cấp / tiến hoá AI
"""

KEYWORDS = [
    "nâng cấp",
    "đã làm gì",
    "vừa làm gì",
    "có gì mới",
    "khác gì",
    "trước và sau",
    "tiến hoá"
]

def is_upgrade_question(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(k in t for k in KEYWORDS)
