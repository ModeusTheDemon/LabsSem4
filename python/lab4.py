"""
Реализовать алгоритм Кнута-Морриса-Пратта для поиска по образцу
"""


def compute_lps(pattern):
    """Вычисляет префикс-функцию (longest prefix suffix) для образца."""
    m = len(pattern)
    lps = [0] * m  # Инициализация массива lps нулями
    length = 0  # Длина предыдущего наибольшего префикса-суффикса

    for i in range(1, m):
        # Если символы не совпадают, возвращаемся к предыдущему lps
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]

        # Если символы совпадают, увеличиваем длину префикса-суффикса
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
        else:
            lps[i] = 0
    return lps

def kmp_search(text, pattern):
    """Ищет все вхождения образца в текст с помощью алгоритма КМП."""
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    lps = compute_lps(pattern)  # Вычисляем префикс-функцию
    occurrences = []  # Список для хранения позиций вхождений
    i = 0  # Индекс для текста
    j = 0  # Индекс для образца

    while i < n:
        if text[i] == pattern[j]:
            # Символы совпали, двигаемся дальше
            i += 1
            j += 1

            if j == m:
                # Найдено полное вхождение образца
                occurrences.append(i - j)
                j = lps[j - 1]  # Сдвигаем образец на длину lps
        else:
            if j > 0:
                # Используем lps для сдвига образца
                j = lps[j - 1]
            else:
                # Если j == 0, просто двигаемся по тексту
                i += 1

    return occurrences

# Пример использования
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(text, pattern)
    print(f"Образец найден на позициях: {matches}")  # Ожидаемый вывод: [10]