# extensions/emotional_intelligence_ai.py
"""
Lớp EQ – trí tuệ cảm xúc cho Bé Cậu
Không phán xét – không dạy đời – không máy móc
"""

EMOTION_MAP = {
    "lo lắng": ["lo", "sợ", "bất an", "hoang mang"],
    "áp lực": ["áp lực", "mệt", "đuối", "kiệt sức"],
    "buồn": ["buồn", "chán", "trống rỗng", "cô đơn"],
    "tức giận": ["bực", "tức", "cay", "khó chịu"],
    "tự ti": ["kém", "thua", "không bằng", "vô dụng"],
    "do dự": ["phân vân", "không biết", "do dự", "lưỡng lự"]
}

def detect_emotion(text: str):
    t = text.lower()
    for emotion, keywords in EMOTION_MAP.items():
        if any(k in t for k in keywords):
            return emotion
    return None

def empathy_prefix(emotion: str):
    if emotion == "lo lắng":
        return "Mình cảm nhận được bạn đang khá lo lắng. Cứ bình tĩnh, mình ở đây cùng bạn."
    if emotion == "áp lực":
        return "Nghe có vẻ bạn đang chịu nhiều áp lực. Không sao, mình cùng gỡ từng chút."
    if emotion == "buồn":
        return "Mình hiểu cảm giác buồn này không dễ chịu. Bạn không cần phải gồng lên."
    if emotion == "tức giận":
        return "Mình cảm nhận được sự khó chịu trong lời bạn nói. Mình nghe bạn đây."
    if emotion == "tự ti":
        return "Có vẻ bạn đang tự trách mình. Nhưng bạn không hề vô dụng như bạn nghĩ."
    if emotion == "do dự":
        return "Bạn đang phân vân là điều rất bình thường. Mình giúp bạn nhìn rõ hơn nhé."
    return ""

def apply_emotional_intelligence(user_text: str, answer: str):
    emotion = detect_emotion(user_text)
    if not emotion:
        return answer

    prefix = empathy_prefix(emotion)
    if not prefix:
        return answer

    return f"{prefix}\n\n{answer}"
