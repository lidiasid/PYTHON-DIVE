
class MatrixDimensionError(Exception):
    pass

class Matrix:
    def __init__(self, data):
        """
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m.rows
        2
        >>> m.cols
        2
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        return '\n'.join([str(row) for row in self.data])

    def __eq__(self, other):
        """
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = Matrix([[1, 2], [3, 4]])
        >>> m1 == m2
        True
        """
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
    import doctest
    doctest.testmod()
