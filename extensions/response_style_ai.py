# extensions/response_style_ai.py

def detect_style(text: str) -> str:
    length = len(text.split())
    if length <= 6:
        return "short"
    if length <= 15:
        return "normal"
    return "long"

def apply_style(reply: str, user_text: str) -> str:
    style = detect_style(user_text)

    if style == "short":
        # rút gọn nhẹ
        lines = reply.split("\n")
        return lines[0]

    if style == "normal":
        return reply

    if style == "long":
        # thêm nhịp nói chuyện
        return reply + "\n\nNếu bạn muốn, mình có thể nói sâu hơn."

    return reply
