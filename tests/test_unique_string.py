from unique_string.unique_string import is_unique_string
import pytest

def test_unique_string1():
    text = "The quick brown fox jumps over the lazy dog"
    assert is_unique_string(text) == False

def test_unique_string2():
    text = "I love cats"
    assert is_unique_string(text) == True

def test_unique_string3():
    text = "Donald the duck"
    assert is_unique_string(text) == False
