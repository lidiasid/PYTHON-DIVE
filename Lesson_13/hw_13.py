""" Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации. 
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины."""


class NegativeLengthError(Exception):
    def __init__(self, side):
        self.side = side
        super().__init__(f"Отрицательная длина стороны: {self.side}")


class InvalidTriangleError(Exception):
    def __init__(self, sides):
        self.sides = sides
        super().__init__(f"Невозможно создать треугольник с такими сторонами: {', '.join(map(str, self.sides))}")


def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise NegativeLengthError(a if a <= 0 else (b if b <= 0 else c))

    return a + b > c and a + c > b and b + c > a


def triangle_type(a, b, c):
    if a == b and b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"


try:
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    c = float(input("Введите сторону c: "))

    if is_triangle(a, b, c):
        print(f"Треугольник с сторонами {a}, {b}, {c} существует и он {triangle_type(a, b, c)}.")
    else:
        raise InvalidTriangleError([a, b, c])

except (ValueError, NegativeLengthError) as e:
    print("Ошибка:", e)

except InvalidTriangleError as e:
    print("Ошибка:", e)






"""class MatrixDimensionError(Exception):
    pass


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        return '\n'.join([str(row) for row in self.data])

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError("Matrices must have the same dimensions for equality comparison")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError("Matrices must have the same dimensions to add")
        
        new_data = []
        for i in range(self.rows):
            new_row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            new_data.append(new_row)
        return Matrix(new_data)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise MatrixDimensionError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                new_element = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                new_row.append(new_element)
            new_data.append(new_row)
        return Matrix(new_data)


if __name__ == '__main__':
    try:
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        m3 = Matrix([[1, 2], [3, 4]])

        print("Matrix 1:")
        print(m1)
        print("Matrix 2:")
        print(m2)

        print("\nMatrix 1 + Matrix 2:")
        print(m1 + m2)

        print("\nMatrix 1 * Matrix 2:")
        print(m1 * m2)

        print("\nMatrix 1 == Matrix 3?")
        print(m1 == m3)

    except MatrixDimensionError as e:
        print("Ошибка:", e)
"""