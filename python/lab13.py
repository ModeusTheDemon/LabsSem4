"""
Решить задачу о раскладке по ящикам
"""

def bin_packing(items, bin_capacity):
    items.sort(reverse=True)
    bins = []
    for item in items:
        placed = False
        for i in range(len(bins)):
            if sum(bins[i]) + item <= bin_capacity:
                bins[i].append(item)
                placed = True
                break
        if not placed:
            bins.append([item])
    return len(bins)

# Пример использования
items = [4, 8, 1, 4, 2, 1]
print("Минимальное количество ящиков:", bin_packing(items, 10))  # Вывод: 2
