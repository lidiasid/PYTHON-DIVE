"""
Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""

from collections import deque
import math
import json

class FactorialFunction:
    def __init__(self, k):
        self.k = k
        self.history = deque(maxlen=k)  # Очередь с ограниченным размером для хранения истории

    def __call__(self, n):
        result = math.factorial(n)  # Вычисление факториала
        self.history.append((n, result))  # Сохранение в историю
        return result

    def show_history(self):
        print("История последних {} вызовов:".format(self.k))
        for n, fact in self.history:
            print(f"{n}! = {fact}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open('history.json', 'w') as f:
            json.dump(list(self.history), f)

# Пример использования менеджера контекста
with FactorialFunction(3) as factorial_function:
    print(factorial_function(5))  # 120
    print(factorial_function(4))  # 24
    print(factorial_function(6))  # 720
    factorial_function.show_history()  # Показывает историю

# После выхода из блока with, история будет сохранена в файле history.json
