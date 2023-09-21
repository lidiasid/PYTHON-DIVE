"""
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.

"""

class Rectangle:
    def __init__(self, side_a, side_b=0):
        self._width = side_a
        if side_b == 0:
            side_b = side_a
        self._length = side_b

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_len):
        if new_len <= 0:
            raise ValueError("Длина должна быть больше 0")
        self._length = new_len

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError("Ширина должна быть больше 0")
        self._width = new_width

    def get_perimeter(self):
        return 2 * (self._width + self._length)

    def get_area(self):
        return self._width * self._length

    # ... оставшийся код не меняется

rectangle1 = Rectangle(7, 11)

print(rectangle1)
try:
    rectangle1.width = 11
except ValueError as e:
    print(f"Ошибка: {e}")
print(rectangle1)

try:
    rectangle1.length = -9  # Теперь здесь будет перехвачено исключение
except ValueError as e:
    print(f"Ошибка: {e}")

print(rectangle1)
