import re
from collections import Counter

def words_count_in_sentence(sentence: str) -> int:
    return len(get_words(sentence))


def shortest_and_longest(sentences: list[str]) -> tuple[str, str]:
    if not sentences:
        return ("", "")
    shortest = min(sentences, key=words_count_in_sentence)
    longest = max(sentences, key=words_count_in_sentence)
    return shortest, longest


def replace_word(text: str, target: str, replacement: str) -> str:
    pattern = r"\b" + re.escape(target) + r"\b"
    return re.sub(pattern, replacement, text)


def reverse_words_in_each_sentence(text: str) -> str:
    parts = re.split(r"([.!?]+)", text)
    result = []

    for i in range(0, len(parts), 2):
        sentence = parts[i]
        punct = parts[i + 1] if i + 1 < len(parts) else ""

        sentence_words = get_words(sentence)
        reversed_sentence = " ".join(reversed(sentence_words))

        result.append(reversed_sentence + punct)

    return "".join(result).strip()
