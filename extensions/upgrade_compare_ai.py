# extensions/upgrade_compare_ai.py
"""
So sánh năng lực AI trước và sau các lần nâng cấp
KHÔNG phụ thuộc app.py
"""

from extensions.self_awareness_ai import load_awareness

def compare_latest(limit=2):
    """
    So sánh 2 trạng thái nâng cấp gần nhất
    """
    data = load_awareness()
    if len(data) < 2:
        return "Chưa đủ dữ liệu để so sánh trước và sau."

    before = data[-2]
    after = data[-1]

    lines = []
    lines.append("🔍 So sánh năng lực Bé Cậu:")
    lines.append(f"• Trước: {before['name']} – {before['description']}")
    lines.append(f"• Sau: {after['name']} – {after['description']}")

    return "\n".join(lines)

def full_progress_report():
    """
    Báo cáo toàn bộ tiến hoá AI
    """
    data = load_awareness()
    if not data:
        return "Bé Cậu chưa có lịch sử nâng cấp."

    lines = ["📈 Tiến hoá của Bé Cậu theo thời gian:"]
    for i, item in enumerate(data, start=1):
        lines.append(f"{i}. {item['name']} – {item['description']}")

    return "\n".join(lines)
