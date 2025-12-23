def build_behavior(relation: str, emotion: str) -> str:
    hints = []

    if relation == "direct":
        hints.append("Trả lời nối tiếp, đi sâu hơn.")
    elif relation == "indirect":
        hints.append("Nhắc ngắn gọn bối cảnh rồi trả lời.")
    else:
        hints.append("Chủ đề mới, không nhắc chuyện cũ.")

    if emotion == "sad":
        hints.append("Giọng nhẹ nhàng, an ủi.")
    elif emotion == "angry":
        hints.append("Giữ bình tĩnh, không tranh cãi.")
    elif emotion == "stress":
        hints.append("Động viên, giảm áp lực.")
    elif emotion == "happy":
        hints.append("Giữ năng lượng tích cực.")

    return " ".join(hints)
