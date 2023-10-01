import unittest
from hw_14_2 import Matrix, MatrixDimensionError

class TestMatrixFunctions(unittest.TestCase):

    def test_matrix_addition(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        m3 = Matrix([[6, 8], [10, 12]])
        self.assertEqual(m1 + m2, m3)

    def test_matrix_multiplication(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        m3 = Matrix([[19, 22], [43, 50]])
        self.assertEqual(m1 * m2, m3)

    def test_matrix_equality(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2], [3, 4]])
        self.assertEqual(m1, m2)

    def test_matrix_dimension_error(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2]])
        with self.assertRaises(MatrixDimensionError):
            m1 + m2
        with self.assertRaises(MatrixDimensionError):
            m1 == m2

if __name__ == '__main__':
    unittest.main()
