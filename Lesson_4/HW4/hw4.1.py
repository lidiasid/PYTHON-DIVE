# Напишите функцию для транспонирования матрицы

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose(matrix)
for row in transposed:
    print(row)
