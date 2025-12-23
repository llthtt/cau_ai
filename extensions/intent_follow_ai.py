# extensions/intent_follow_ai.py
"""
Nhận biết câu nói nối tiếp hội thoại trước
"""

FOLLOW_KEYWORDS = [
    "thế còn",
    "vậy còn",
    "ý trên",
    "ý đó",
    "cái đó",
    "tiếp theo",
    "như đã nói",
    "còn nữa"
]

def is_follow_up(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(k in t for k in FOLLOW_KEYWORDS)
