"""Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре."""

def clean_text(text):
    cleaned = "".join(char for char in text if char.isascii() and (char.isalpha() or char.isspace()))
    return cleaned.lower()

text = "Привет, Lidiia! How's it going?"
cleaned_text = clean_text(text)
print(cleaned_text)  


