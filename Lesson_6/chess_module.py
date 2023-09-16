""" Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, 
каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь. """

import random

def are_queens_safe(queens):
    
    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

def generate_random_queens_placement():
    
    queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
    return queens

def find_safe_queens_placements(num=4):
    
    count = 0
    while count < num:
        placement = generate_random_queens_placement()
        if are_queens_safe(placement):
            count += 1
            print(placement)

if __name__ == "__main__":
    # Выводим 4 успешных расстановки
    find_safe_queens_placements(4)
