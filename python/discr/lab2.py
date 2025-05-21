from itertools import combinations, permutations


# 1
# Частоты букв в слове "ЧЕРЕСПОЛОСИЦА"
# (мы учитываем только уникальные буквы — не более одного раза в слово)
word = "ЧЕРЕСПОЛОСИЦА"
from collections import Counter

# Подсчитываем частоты
counter = Counter(word)

# Извлекаем уникальные буквы (те, которые можно взять хотя бы один раз)
unique_letters = list(counter.keys())

# Выбираем все комбинации по 4 разные буквы
letter_combinations = combinations(unique_letters, 4)

# Подсчёт всех возможных перестановок этих комбинаций
total_words = 0
for combo in letter_combinations:
    # Каждая комбинация даёт 4! перестановок
    total_words += len(list(permutations(combo)))

print(f"Общее количество различных 4-буквенных слов: {total_words}")

# 5

import math

def count_paths_without_restrictions(right, up):
    return math.comb(right + up, up)

print("Без ограничений:", count_paths_without_restrictions(17, 15))

def count_paths_with_restriction(right, up):
    if up > right + 1:
        return 0  # невозможно разместить без UU
    return math.comb(right + 1, up)

print("С ограничением (без двух U подряд):", count_paths_with_restriction(17, 15))

