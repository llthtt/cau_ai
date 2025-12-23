def keywords(text: str) -> set:
    return set(text.lower().split())


def relevance_score(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def detect_relation(new_text: str, memory: list) -> str:
    recent = " ".join(m["content"] for m in memory[-6:])
    score = relevance_score(
        keywords(new_text),
        keywords(recent)
    )

    if score > 0.25:
        return "direct"
    elif score > 0.1:
        return "indirect"
    else:
        return "new"
