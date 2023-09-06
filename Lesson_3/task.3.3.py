# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

tuple_elements = (1, "apple", 3.14, True, "banana", 42, 2.71, "cat")

dictionary = {}

for item in tuple_elements:
    item_type = type(item)
    if item_type not in dictionary:
        dictionary[item_type] = [item]
    else:
        dictionary[item_type].append(item)

for key, value in dictionary.items():
    print(f"{key}: {value}")
