# extensions/upgrade_ai.py

def enhance_input(user_text: str, memory: list):
    """
    Phân tích câu người dùng:
    - Có liên quan hội thoại trước không
    - Chủ đề đang nói
    - Phong cách trả lời
    """

    user_text = user_text.strip()
    topic = None
    style = ""
    suggestion = None

    # ===== 1. XÁC ĐỊNH CHỦ ĐỀ =====
    keywords = {
        "giá": "mua_ban",
        "bao nhiêu": "mua_ban",
        "tiền": "mua_ban",
        "ăn": "doi_song",
        "ngủ": "doi_song",
        "mệt": "suc_khoe",
        "đầu tư": "tai_chinh",
        "coin": "tai_chinh",
        "crypto": "tai_chinh",
    }

    for k, v in keywords.items():
        if k in user_text.lower():
            topic = v
            break

    # ===== 2. KIỂM TRA LIÊN QUAN NGỮ CẢNH =====
    if memory:
        last = memory[-1]
        if topic and last.get("topic") == topic:
            style = "Người dùng đang nói tiếp cùng một chủ đề."
        else:
            style = "Chủ đề mới, cần trả lời rõ ràng."

    # ===== 3. GỢI Ý NHẸ =====
    if topic == "mua_ban":
        suggestion = "Bạn muốn mình so sánh giá hay tư vấn thêm không?"
    elif topic == "tai_chinh":
        suggestion = "Bạn muốn phân tích rủi ro hay xu hướng không?"

    return {
        "text": user_text,
        "topic": topic,
        "style": style,
        "suggestion": suggestion
    }
