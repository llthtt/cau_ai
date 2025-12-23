# extensions/tts_prosody_ai.py
"""
Phân tích nội dung để điều chỉnh nhịp đọc (prosody)
Giống người nói chuyện thật
"""

import re

def analyze_prosody(text: str):
    """
    Trả về gợi ý cho TTS:
    - rate: tốc độ đọc (0.8 – 1.2)
    - pauses: vị trí nên ngắt nhịp
    """

    rate = 1.0
    pauses = []

    t = text.lower()

    # 1️⃣ Chậm lại khi cảm xúc nặng
    if any(k in t for k in ["lo lắng", "áp lực", "buồn", "mệt", "stress"]):
        rate = 0.85

    # 2️⃣ Chậm & nhấn mạnh khi trấn an
    if any(k in t for k in ["mình hiểu", "không sao", "bình tĩnh", "mình ở đây"]):
        rate = 0.8

    # 3️⃣ Nhanh hơn khi hướng dẫn / liệt kê
    if any(k in t for k in ["bước", "đầu tiên", "tiếp theo", "cách", "nên làm"]):
        rate = 1.1

    # 4️⃣ Ngắt nhịp trước ý quan trọng
    for m in re.finditer(r"(nhưng|tuy nhiên|điều quan trọng|lưu ý)", t):
        pauses.append(m.start())

    return {
        "rate": round(rate, 2),
        "pauses": pauses
    }
