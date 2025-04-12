"""
Проблема размена монет: поиск количества способов внести сдачу на заданную сумму денег,
используя заданный набор номиналов монет.
"""

def coin_change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

print(coin_change([1,2,5,10], 15))
