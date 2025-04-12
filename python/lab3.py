"""
Реализовать алгоритм поиска по образцу с помощью конечного автомата
"""


def compute_lps(pattern):
    """Вычисляет префикс-функцию (longest prefix suffix) для образца."""
    m = len(pattern)
    lps = [0] * m
    length = 0  # длина предыдущего наибольшего префикса-суффикса

    for i in range(1, m):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
        else:
            lps[i] = 0
    return lps

def build_transition_table(pattern):
    """Строит таблицу переходов для конечного автомата."""
    m = len(pattern)
    if m == 0:
        return []

    alphabet = set(pattern)
    lps = compute_lps(pattern)
    transition = [{} for _ in range(m + 1)]

    for q in range(m + 1):
        for c in alphabet:
            if q < m and c == pattern[q]:
                transition[q][c] = q + 1
            else:
                # Используем префикс-функцию для определения перехода
                if q == 0:
                    transition[q][c] = 0
                else:
                    # Переходим к состоянию lps[q-1] и проверяем переход оттуда
                    k = lps[q-1]
                    transition[q][c] = transition[k].get(c, 0)
    return transition

def finite_automaton_match(text, pattern):
    """Ищет все вхождения образца в текст с помощью конечного автомата."""
    m = len(pattern)
    if m == 0:
        return []

    n = len(text)
    transition = build_transition_table(pattern)
    q = 0  # текущее состояние
    occurrences = []

    for i in range(n):
        c = text[i]
        # Переход по таблице; если символ не найден, переходим в состояние 0
        q = transition[q].get(c, 0)
        if q == m:
            # Найдено вхождение, добавляем начальный индекс
            start = i - m + 1
            occurrences.append(start)

    return occurrences

# Пример использования
if __name__ == "__main__":
    text = "ABABABCABABC"
    pattern = "ABABC"
    matches = finite_automaton_match(text, pattern)
    print(f"Образец найден на позициях: {matches}")  # Ожидаемый вывод: [2, 7]