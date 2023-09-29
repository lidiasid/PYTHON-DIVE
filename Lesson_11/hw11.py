# Создайте класс Матрица. Добавьте методы для: - вывода на печать,сравнения,сложения,*умножения матриц

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        return '\n'.join([str(row) for row in self.data])

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add")
        
        new_data = []
        for i in range(self.rows):
            new_row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            new_data.append(new_row)
        return Matrix(new_data)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                new_element = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                new_row.append(new_element)
            new_data.append(new_row)
        return Matrix(new_data)

if __name__ == '__main__':
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
