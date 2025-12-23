EMOTION_RULES = {
    "sad": ["buồn", "mệt", "chán", "áp lực", "cô đơn"],
    "angry": ["bực", "cáu", "tức", "khó chịu"],
    "happy": ["vui", "thoải mái", "hạnh phúc"],
    "stress": ["lo", "sợ", "căng thẳng"]
}

def detect_emotion(text: str) -> str:
    text = text.lower()
    for emo, words in EMOTION_RULES.items():
        for w in words:
            if w in text:
                return emo
    return "neutral"
