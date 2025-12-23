# extensions/eq_history_ai.py
import re
from collections import Counter

EMOTION_WORDS = {
    "stress": ["mệt", "áp lực", "chán", "đuối", "căng"],
    "confused": ["không biết", "rối", "mơ hồ"],
    "positive": ["ổn", "vui", "ok", "tốt"]
}

def detect_emotion(text: str) -> str:
    t = text.lower()
    for emo, words in EMOTION_WORDS.items():
        for w in words:
            if w in t:
                return emo
    return "neutral"

def analyze_history(memory: list) -> str:
    emotions = []
    for m in memory:
        if m["role"] == "user":
            emotions.append(detect_emotion(m["content"]))

    if not emotions:
        return "neutral"

    most_common = Counter(emotions).most_common(1)[0][0]
    return most_common

def history_prefix(history_emotion: str) -> str:
    if history_emotion == "stress":
        return "Dạo này mình thấy bạn hay căng, nên mình sẽ nói chậm và nhẹ hơn nhé.\n\n"
    if history_emotion == "confused":
        return "Có vẻ bạn đang hay rối, nên mình sẽ nói ngắn gọn và rõ ràng.\n\n"
    if history_emotion == "positive":
        return "Mình thấy tinh thần bạn khá ổn, nên mình sẽ trao đổi thoải mái hơn chút.\n\n"
    return ""

def apply_history_eq(reply: str, memory: list) -> str:
    emo = analyze_history(memory)
    prefix = history_prefix(emo)
    return prefix + reply
