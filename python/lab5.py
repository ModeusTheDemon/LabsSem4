"""
Реализовать алгоритм Бойера-Мура для поиска по образцу
"""


def bad_character_heuristic(pattern):
    """Создает таблицу плохих символов для правила плохого символа."""
    bad_char = {}  # Словарь для хранения последнего вхождения каждого символа
    m = len(pattern)

    for i in range(m):
        # Сохраняем последнее вхождение символа
        bad_char[pattern[i]] = i
    return bad_char

def good_suffix_heuristic(pattern):
    """Создает таблицу хороших суффиксов для правила хорошего суффикса."""
    m = len(pattern)
    good_suffix = [0] * (m + 1)  # Инициализация массива для хороших суффиксов
    border = [0] * (m + 1)  # Массив для хранения границ

    # Первый этап: вычисление границ
    i = m
    j = m + 1
    border[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j

    # Второй этап: заполнение оставшихся значений
    j = border[0]
    for i in range(m + 1):
        if good_suffix[i] == 0:
            good_suffix[i] = j
        if i == j:
            j = border[j]

    return good_suffix

def boyer_moore_search(text, pattern):
    """Ищет все вхождения образца в текст с помощью алгоритма Бойера-Мура."""
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    # Создаем таблицы для правил плохого символа и хорошего суффикса
    bad_char = bad_character_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)

    occurrences = []  # Список для хранения позиций вхождений
    s = 0  # Сдвиг образца относительно текста

    while s <= n - m:
        j = m - 1

        # Сравниваем символы справа налево
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # Найдено полное вхождение образца
            occurrences.append(s)
            # Сдвигаем образец на длину хорошего суффикса
            s += good_suffix[0]
        else:
            # Сдвигаем образец на максимум из правил плохого символа и хорошего суффикса
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            s += max(bad_char_shift, good_suffix_shift)

    return occurrences

# Пример использования
if __name__ == "__main__":
    text = "ABAAABCDABC"
    pattern = "ABC"
    matches = boyer_moore_search(text, pattern)
    print(f"Образец найден на позициях: {matches}")  # Ожидаемый вывод: [4, 8]