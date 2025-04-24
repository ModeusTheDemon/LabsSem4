"""
Реализовать алгоритм Рабина для поиска по образцу
"""


def rabin_karp_search(text, pattern):
    """Ищет все вхождения образца в текст с помощью алгоритма Рабина-Карпа."""
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    # Простое число для хеширования
    prime = 101
    # Количество символов в алфавите (ASCII)
    d = 256

    # Вычисляем h = d^(m-1) % prime
    h = pow(d, m - 1, prime)

    # Вычисляем хеш-значение для образца и первой подстроки текста
    pattern_hash = 0
    text_hash = 0
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    occurrences = []  # Список для хранения позиций вхождений

    # Проходим по тексту
    for i in range(n - m + 1):
        # Если хеш-значения совпадают, проверяем символы
        if pattern_hash == text_hash:
            # Поэлементное сравнение
            if text[i:i + m] == pattern:
                occurrences.append(i)

        # Вычисляем хеш-значение для следующей подстроки
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Убедимся, что хеш-значение не отрицательное
            if text_hash < 0:
                text_hash += prime

    return occurrences

# Пример использования
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = rabin_karp_search(text, pattern)
    print(f"Образец найден на позициях: {matches}")  # Ожидаемый вывод: [10]