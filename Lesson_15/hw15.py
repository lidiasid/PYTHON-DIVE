"""Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров."""

import logging
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
    parser = argparse.ArgumentParser(description='Определение типа треугольника по сторонам')
    parser.add_argument('--a', type=float, help='Длина стороны a', required=True)
    parser.add_argument('--b', type=float, help='Длина стороны b', required=True)
    parser.add_argument('--c', type=float, help='Длина стороны c', required=True)

    args = parser.parse_args()

    try:
        a, b, c = args.a, args.b, args.c
        logging.info(f'Проверка на существование треугольника со сторонами: {a}, {b}, {c}')

        if is_triangle(a, b, c):
            logging.info(f'Треугольник существует')
            print(f"Треугольник с сторонами {a}, {b}, {c} существует и он {triangle_type(a, b, c)}.")
        else:
            logging.warning(f'Треугольник не существует')
            print("Треугольник не существует.")

    except NegativeLengthError as e:
        logging.error(f'Ошибка: {e}')
        print(e)



"""logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MatrixDimensionError(Exception):
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
            logging.error("MatrixDimensionError: Matrices must have the same dimensions for equality comparison")
            raise MatrixDimensionError("Matrices must have the same dimensions for equality comparison")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            logging.error("MatrixDimensionError: Matrices must have the same dimensions to add")
            raise MatrixDimensionError("Matrices must have the same dimensions to add")
        
        new_data = []
        for i in range(self.rows):
            new_row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            new_data.append(new_row)
        return Matrix(new_data)

    def __mul__(self, other):
        if self.cols != other.rows:
            logging.error("MatrixDimensionError: Number of columns in the first matrix must be equal to the number of rows in the second matrix")
            raise MatrixDimensionError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                new_element = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                new_row.append(new_element)
            new_data.append(new_row)
        return Matrix(new_data)

def parse_matrix(matrix_str):
    return [[int(elem) for elem in row.split(",")] for row in matrix_str.split(";")]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Matrix operations')
    parser.add_argument('--add', nargs=2, help='Add two matrices')
    parser.add_argument('--mul', nargs=2, help='Multiply two matrices')
    parser.add_argument('--eq', nargs=2, help='Check if two matrices are equal')

    args = parser.parse_args()

    if args.add:
        m1 = parse_matrix(args.add[0])
        m2 = parse_matrix(args.add[1])
        result = Matrix(m1) + Matrix(m2)
        logging.info("Result of addition: ")
        print(result)

    if args.mul:
        m1 = parse_matrix(args.mul[0])
        m2 = parse_matrix(args.mul[1])
        result = Matrix(m1) * Matrix(m2)
        logging.info("Result of multiplication: ")
        print(result)

    if args.eq:
        m1 = parse_matrix(args.eq[0])
        m2 = parse_matrix(args.eq[1])
        result = Matrix(m1) == Matrix(m2)
        logging.info(f"Matrices are equal: {result}")"""