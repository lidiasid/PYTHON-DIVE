"""
Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""

import time

class MyString(str):
    def __new__(cls, content, author):
        obj = str.__new__(cls, content)
        obj.author = author
        obj.creation_time = time.time()
        return obj

my_str = MyString("Hello, world!", "Lidiia")

print(my_str.lower())
print(my_str.upper())
print(my_str.startswith("Hello"))

print("Author: {my_str.author}")
print("Creation Time: {my_str.creation_time}")

