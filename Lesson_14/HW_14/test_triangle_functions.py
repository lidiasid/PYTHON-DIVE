import pytest
from hw_14_1 import is_triangle, triangle_type, NegativeLengthError

def test_is_triangle():
    assert is_triangle(3, 4, 5) == True
    assert is_triangle(5, 12, 13) == True
    assert is_triangle(1, 1, 3) == False
    assert is_triangle(5, 5, 12) == False
    with pytest.raises(NegativeLengthError):
        is_triangle(-1, 2, 2)
    with pytest.raises(NegativeLengthError):
        is_triangle(0, 2, 2)

def test_triangle_type():
    assert triangle_type(3, 3, 3) == 'равносторонний'
    assert triangle_type(5, 12, 13) == 'разносторонний'
    assert triangle_type(5, 5, 8) == 'равнобедренный'

