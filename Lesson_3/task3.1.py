# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.


def unique_elements_short(lst):
    return list(set(lst))

def unique_elements_long(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

original_list = [1, 2, 3, 2, 4, 3, 5, 6, 7, 5, 8]
print(unique_elements_short(original_list))
print(unique_elements_long(original_list))

def unique_elements_comprehension(lst):
    return [item for index, item in enumerate(lst) if item not in lst[:index]]

original_list = [1, 2, 3, 2, 4, 3, 5, 6, 7, 5, 8]
print(unique_elements_comprehension(original_list))
