"""Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка."""

def sum_between_indices(nums, start_idx, end_idx):
    start_idx = max(0, start_idx)  # Если индекс меньше 0, принимаем его за 0
    end_idx = min(len(nums), end_idx + 1)  # Если индекс больше длины списка, принимаем его за длину списка
    return sum(nums[start_idx:end_idx])

numbers = [1, 2, 3, 4, 5]
print(sum_between_indices(numbers, 1, 3))  # Вернет 9, так как 2 + 3 + 4 = 9
print(sum_between_indices(numbers, -1, 10))  # Вернет 15, так как это сумма всех элементов списка

