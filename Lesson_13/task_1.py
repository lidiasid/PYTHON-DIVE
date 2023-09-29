"""
Задание №1
📌 Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
📌 Обрабатывайте не числовые данные как исключения.
"""

def get_number():
    while True:
        num = input('введите число:> ')
        try:
            return int(num)
        except ValueError as e:
            try:
                return float(num)
            except ValueError as e:
                print(f'Неверный формат ввода, {e}')




print(get_number())