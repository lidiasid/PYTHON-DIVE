# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

__all__ = ["guess_the_number"]


import random

def guess_the_number(lower, upper, attempts):
    
    number_to_guess = random.randint(lower, upper)
    
    for _ in range(attempts):
        try:
            user_guess = int(input(f"Попробуйте угадать число между {lower} и {upper}: "))
            
            if user_guess < lower or user_guess > upper:
                print("Число вне указанного диапазона. Попробуйте ещё раз.")
                continue
                
            if user_guess == number_to_guess:
                print("Поздравляем, вы угадали!")
                return True
            elif user_guess < number_to_guess:
                print("Больше!")
            else:
                print("Меньше!")
                
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    print(f"Вы исчерпали все попытки. Загаданное число было: {number_to_guess}.")
    return False

lower= int(input("Введите нижнее значение"))
upper= int(input("Введите верхнее значение"))
attempts = int(input("Введите количество попыток"))

if __name__ == "__main__":
    guess_the_number(lower, upper, attempts)

