# Напишите программу, которая получает целое число и 
# возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

num_dec = int(input("введите число: "))
res = ''
DIVIDER = 16
hex_digits = '0123456789abcdef'

print(hex(num_dec)) 

while num_dec > 0:
    remainder = num_dec % DIVIDER
    res = hex_digits[remainder] + res
    num_dec //= DIVIDER

print(res)
