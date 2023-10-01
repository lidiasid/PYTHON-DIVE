import re
import doctest

def clean_text(text):
    """
    Remove all characters from the text except for Latin letters and spaces. 
    Returns the string in lowercase.

    >>> clean_text("Hello World!")
    'hello world'

    >>> clean_text("HELLO")
    'hello'

    >>> clean_text("Hello, Lidiia!")
    'hello lidiia'

    >>> clean_text("Привет, Lidiia!")
    ' lidiia'

    >>> clean_text("Hello,Lidiia!123!@# Привет")
    'hellolidiia '

    """
    clean = re.sub(r'[^a-zA-Z\s]', '', text)
    return clean.lower()

if __name__ == "__main__":
    doctest.testmod()
