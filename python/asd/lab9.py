"""
Задача коммивояжера - поиск кратчайшего возможного маршрута,
который проходит через заданный набор городов и возвращается в начальный город.
Маршруты заданы матрицей связности.

Алгоритм Хелда-Карпа
"""

from itertools import combinations


def tsp(graph):
    n = len(graph)
    memo = {}

    # Инициализация: стоимость пути из стартового города (0) в другие города
    for i in range(1, n):
        memo[(1 << i, i)] = graph[0][i]

    # Перебор всех размеров подмножеств (исправлено: range(1, n))
    for r in range(1, n):
        for subset in combinations(range(1, n), r):
            bits = 0
            for node in subset:
                bits |= 1 << node  # Корректная битовая маска

            for next_node in subset:
                prev_bits = bits & ~(1 << next_node)
                min_cost = float('inf')

                # Перебор всех предыдущих узлов в подмножестве
                for last_node in subset:
                    if last_node == next_node:
                        continue
                    key = (prev_bits, last_node)
                    if key in memo:
                        cost = memo[key] + graph[last_node][next_node]
                        if cost < min_cost:
                            min_cost = cost

                if min_cost != float('inf'):
                    memo[(bits, next_node)] = min_cost

    # Поиск минимального пути с возвратом в стартовый город
    full_bits = (1 << n) - 1 - 1  # Все города, кроме стартового (0)
    min_total = float('inf')
    for i in range(1, n):
        key = (full_bits, i)
        if key in memo:
            total_cost = memo[key] + graph[i][0]
            min_total = min(min_total, total_cost)

    return min_total if min_total != float('inf') else -1


# Пример использования
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(tsp(graph))  # Вывод: 80
