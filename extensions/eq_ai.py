# extensions/eq_ai.py

import re

EMOTION_PATTERNS = {
    "stress": [
        r"mệt", r"căng", r"áp lực", r"chán", r"đuối", r"khó quá"
    ],
    "confused": [
        r"không biết", r"rối", r"mơ hồ", r"sao", r"tại sao"
    ],
    "positive": [
        r"vui", r"ổn", r"ok", r"tốt", r"cảm ơn"
    ]
}

def detect_emotion(text: str) -> str:
    t = text.lower()
    for emotion, patterns in EMOTION_PATTERNS.items():
        for p in patterns:
            if re.search(p, t):
                return emotion
    return "neutral"

def eq_prefix(emotion: str) -> str:
    if emotion == "stress":
        return "Mình nghe có vẻ bạn đang hơi căng. Mình ở đây, nói chậm lại nhé.\n\n"
    if emotion == "confused":
        return "Không sao đâu, mình sẽ nói gọn và rõ cho bạn.\n\n"
    if emotion == "positive":
        return "Nghe bạn nói vậy là mình thấy yên tâm rồi 😊\n\n"
    return ""

def apply_eq(user_text: str, reply: str) -> str:
    emotion = detect_emotion(user_text)
    prefix = eq_prefix(emotion)
    return prefix + reply
