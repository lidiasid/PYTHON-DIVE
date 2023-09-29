class NegativeLengthError(Exception):
    pass

def is_triangle(a, b, c):
    """
    Determines if a triangle can be formed with sides a, b, and c.
    
    >>> is_triangle(3, 4, 5)
    True
    
    >>> is_triangle(1, 2, 3)
    False
    
    >>> is_triangle(-1, 2, 2)
    Traceback (most recent call last):
        ...
    NegativeLengthError: -1
    
    >>> is_triangle(0, 2, 2)
    Traceback (most recent call last):
        ...
    NegativeLengthError: 0
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise NegativeLengthError(a if a <= 0 else (b if b <= 0 else c))
    
    return a + b > c and a + c > b and b + c > a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
