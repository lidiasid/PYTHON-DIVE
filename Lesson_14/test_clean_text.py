from task_1 import clean_text 

def test_no_change():
    assert clean_text("Hello World") == "hello world"

def test_case_conversion():
    assert clean_text("HELLO") == "hello"

def test_remove_punctuation():
    assert clean_text("Hello, Lidiia!") == "hello lidiia"

def test_remove_non_latin():
    assert clean_text("Привет, Lidiia!") == " lidiia"

def test_combined():
    assert clean_text("Hello, Lidiia! 123 !@# Привет") == "hello lidiia   "
