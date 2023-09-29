"""Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
2-5 тестов на задание в трёх вариантах:
doctest,
unittest,
pytest."""


class NegativeLengthError(Exception):
    pass

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise NegativeLengthError("Стороны треугольника должны быть положительными.")
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if is_triangle(a, b, c):
        if a == b == c:
            return 'равносторонний'
        elif a == b or b == c or a == c:
            return 'равнобедренный'
        else:
            return 'разносторонний'

if __name__ == '__main__':
    try:
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))
        
        if is_triangle(a, b, c):
            print(f"Треугольник с сторонами {a}, {b}, {c} существует и он {triangle_type(a, b, c)}.")
        else:
            print("Треугольник не существует.")
    except NegativeLengthError as e:
        print(e)
