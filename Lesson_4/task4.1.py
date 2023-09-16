"""Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки."""

def print_sorted_words(text):
    words = sorted(text.split())  # Сортируем слова
    max_length = max(len(word) for word in words) + 1  # Находим длину самого длинного слова и добавляем 1 для пробела

    for index, word in enumerate(words, 1):  # Нумерация начинается с 1
        # Выводим слово, выравнивая по правому краю
        print(f"{index}. {word.rjust(max_length)}")

text = "apple banana cherry date elephant"
print_sorted_words(text)
