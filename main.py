import re
from collections import Counter


def read_text() -> str:
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def get_words(text: str) -> list[str]:
    return re.findall(r"[A-Za-zА-Яа-яІіЇїЄє0-9']+", text)


def count_chars(text: str) -> int:
    return len(text)


def top5_words(words: list[str]) -> list[tuple[str, int]]:
    freq = Counter(w.lower() for w in words)
    return freq.most_common(5)


def avg_word_len(words: list[str]) -> float:
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"[.!?]+", text)
    return [p.strip() for p in parts if p.strip()]
