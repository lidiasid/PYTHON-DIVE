"""Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно."""

def generate_unicode_dict(input_str):
    start, end = sorted(map(int, input_str.split()))
    return {chr(i): i for i in range(start, end + 1)}

input_str = "65 70"
print(generate_unicode_dict(input_str))


