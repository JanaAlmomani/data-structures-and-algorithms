import pytest
from hashtable.hashtable.HashmapRepeatedWord import *

def test_find_first_repeated_word1(): # No_repetition
    input_string = "Jana Almomani"
    assert find_first_repeated_word(input_string) == "No Repetition"

def test_find_first_repeated_word2():
    input_string = "Once upon a time, there was a brave princess who..."
    assert find_first_repeated_word(input_string) == "a"

def test_find_first_repeated_word3():
    input_string = "It was the best of times, it was the worst of times, it was the age of wisdom,it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert find_first_repeated_word(input_string) == "it"

def test_find_first_repeated_word4():
    input_string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t  know what I was doing in New York..."
    assert find_first_repeated_word(input_string) == "summer"

