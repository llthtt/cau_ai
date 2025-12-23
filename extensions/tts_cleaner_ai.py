# extensions/tts_cleaner_ai.py
"""
Làm sạch văn bản trước khi TTS đọc
XOÁ TRIỆT ĐỂ các ký tự gây chói tai như:
— — — , ___ , *** , ###
"""

import re

def clean_for_tts(text: str) -> str:
    if not text:
        return text

    # ❌ XOÁ CỨNG separator gây chói
    text = text.replace("— — —", " ")
    text = text.replace("---", " ")
    text = text.replace("___", " ")

    # ❌ XOÁ mọi dạng gạch lặp
    text = re.sub(r"[—\-]{2,}", " ", text)

    # ❌ XOÁ ký tự markdown
    text = re.sub(r"[\*#]{2,}", " ", text)

    # ❌ XOÁ emoji khi đọc
    text = re.sub(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F900-\U0001F9FF"
        "]",
        "",
        text
    )

    # Chuẩn hoá khoảng trắng
    text = re.sub(r"\s+", " ", text)

    return text.strip()
