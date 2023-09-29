import unittest
from hw_14_1 import is_triangle
from hw_14_1 import triangle_type
from hw_14_1 import NegativeLengthError


class TestTriangleFunctions(unittest.TestCase):
    def test_is_triangle(self):
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(5, 12, 13))
        self.assertFalse(is_triangle(1, 1, 3))
        self.assertFalse(is_triangle(5, 5, 12))
        self.assertRaises(NegativeLengthError, is_triangle, -1, 2, 2)
        self.assertRaises(NegativeLengthError, is_triangle, 0, 2, 2)

    def test_triangle_type(self):
        self.assertEqual(triangle_type(3, 3, 3), 'равносторонний')
        self.assertEqual(triangle_type(5, 12, 13), 'разносторонний')
        self.assertEqual(triangle_type(5, 5, 8), 'равнобедренный')

if __name__ == '__main__':
    unittest.main()
