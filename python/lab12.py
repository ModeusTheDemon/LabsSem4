"""
Решить дискретную задачу о рюкзаке
"""

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

# Пример использования
weights = [2, 3, 4]
values = [3, 4, 5]
capacity = 5
print("Максимальная стоимость:", knapsack(weights, values, capacity))  # Вывод: 7
