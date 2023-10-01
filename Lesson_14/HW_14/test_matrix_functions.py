import pytest
from hw_14_2 import Matrix, MatrixDimensionError

def test_matrix_addition():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = Matrix([[6, 8], [10, 12]])
    assert (m1 + m2) == m3

def test_matrix_multiplication():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = Matrix([[19, 22], [43, 50]])
    assert (m1 * m2) == m3

def test_matrix_equality():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2], [3, 4]])
    assert m1 == m2

def test_matrix_dimension_error():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2]])
    with pytest.raises(MatrixDimensionError):
        m1 + m2
    with pytest.raises(MatrixDimensionError):
        m1 == m2
