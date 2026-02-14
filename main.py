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

def main():
    print("Введіть текст. Порожній рядок завершує ввід.")
    text = read_text()

    words = get_words(text)
    sentences = split_sentences(text)

    print()
    print("Символів:", count_chars(text))
    print("Слів:", len(words))
    print("Речень:", len(sentences))

    print()
    print("Топ 5 слів:")
    for w, c in top5_words(words):
        print(f"{w}: {c}")

    print()
    print("Середня довжина слова:", f"{avg_word_len(words):.2f}")

    shortest, longest = shortest_and_longest(sentences)

    print()
    print("Найкоротше речення:")
    print(shortest if shortest else "")

    print()
    print("Найдовше речення:")
    print(longest if longest else "")

    print()
    target = input("Слово для пошуку: ").strip()
    replacement = input("Замінити на: ").strip()
    replaced_text = replace_word(text, target, replacement)

    print()
    print("Текст після заміни:")
    print(replaced_text)

    print()
    print("Реверс слів у реченнях:")
    print(reverse_words_in_each_sentence(text))


if __name__ == "__main__":
    main()
    return [p.strip() for p in parts if p.strip()]
