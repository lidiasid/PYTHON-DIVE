# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

original_list = [1, 2, 3, 4, 2, 5, 3, 6, 7, 8, 9, 4]

# Используем set comprehension для определения элементов, встречающихся ровно дважды
duplicates = {item for item in set(original_list) if original_list.count(item) == 2}

# Фильтруем список, чтобы исключить дубликаты
filtered_list = list(filter(lambda x: x not in duplicates, original_list))

print(filtered_list)
