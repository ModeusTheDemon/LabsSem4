"""
Задача о самом большом подмассиве: поиск непрерывного подмассива в одномерном массиве чисел с наибольшей суммой.
Алгоритм Кадана
"""
import random as rnd


def max_subarray(nums):
    if not nums:
        return None

    current_max = global_max = nums[0]
    start = end = 0
    global_start = global_end = 0

    for i in range(1, len(nums)):
        num = nums[i]
        if num > current_max + num:
            current_max = num
            start = end = i
        else:
            current_max += num
            end = i

        if current_max > global_max:
            global_max = current_max
            global_start = start
            global_end = end

    return {
        "sum": global_max,
        "subarray": nums[global_start: global_end + 1],
        "start_index": global_start,
        "end_index": global_end
    }

print(max_subarray([rnd.randint(-10, 10) for i in range(20)]))
