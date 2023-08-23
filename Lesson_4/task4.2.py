# Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def unique_unicode_codes(text):
    unicode_codes = {ord(char) for char in text}
    
    return sorted(unicode_codes, reverse=True)

text = "hello world"
print(unique_unicode_codes(text))
