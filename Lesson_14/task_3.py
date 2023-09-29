import unittest
import re

def clean_text(text):
    clean = re.sub(r'[^a-zA-Z\s]', '', text)
    return clean.lower()

class TestCleanText(unittest.TestCase):
    
    def test_no_change(self):
        self.assertEqual(clean_text("Hello World"), "hello world")
    
    def test_case_conversion(self):
        self.assertEqual(clean_text("HELLO"), "hello")
        
    def test_remove_punctuation(self):
        self.assertEqual(clean_text("Hello, Lidiia!"), "hello lidiia")
        
    def test_remove_non_latin(self):
        self.assertEqual(clean_text("Привет, Lidiia!"), " lidiia")
        
    def test_combined(self):
        self.assertEqual(clean_text("Hello, Lidiia! 123 !@# Привет"), "hello lidiia   ")
        
if __name__ == "__main__":
    unittest.main()
