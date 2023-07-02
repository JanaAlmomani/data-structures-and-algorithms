import re

def find_first_repeated_word(input_string):
    word_freq = {}
    # Remove punctuation marks using regular expressions
    words = re.findall(r'\b\w+\b', input_string.lower())
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
        if word_freq[word] > 1:
            return word
    return "No Repetition"


input_string= "Once upon a time, there was a brave princess who..."
print(find_first_repeated_word(input_string))
