"""
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""

from collections import deque
import math

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

# Создание экземпляра класса, который запоминает последние 3 значения
factorial_function = FactorialFunction(3)

print(factorial_function(5))  
print(factorial_function(4))  
print(factorial_function(6))  
print(factorial_function(3))  

# Просмотр истории
factorial_function.show_history()  # Должно показать последние 3 значения и их факториалы
