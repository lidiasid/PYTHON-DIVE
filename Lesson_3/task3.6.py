# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.


input_string = input("Введите строку текста: ")

words = input_string.split()

words.sort()

max_length = max(len(word) for word in words)

for index, word in enumerate(words, start=1):
    print(f"{index}. {word.rjust(max_length + 1)}")


texts = "vsdsdsdsdsds dfsfdf fdfdfd fdfdfd".split()
shift = len(max(texts))
for n, el in enumerate(sorted(texts), 1):
    print(f"{n}, {el:>{shift}}")