"""
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

lst_1 = [5, "string", 0.15, True, None]
for el in lst_1:
    print(type(el))

lst_1 = [5, "string", 0.15, True, None]
for i in range(len(lst_1)):
    print(type(lst_1[i]))