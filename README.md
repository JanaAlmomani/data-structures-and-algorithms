# Challenge Title: Find the first repeated word in a book.
## Write a function called repeated word that finds the first word to occur more than once in a string
## - Arguments: string
## - Return: string
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency

1. Start by defining the function find_first_repeated_word that takes an input_string as a parameter.
2. Create an empty dictionary called word_freq to store the frequency of each word.
3. Use regular expressions to remove punctuation marks from the input_string. This ensures that words are properly separated.
4. Convert the input_string to lowercase and split it into a list of words.
5. Iterate over each word in the list of words.
6. Check if the word is already in the word_freq dictionary.
    - If it is not present, add it to the dictionary and set its frequency to 1.
    - If it is already present, increment its frequency by 1.
7. Check if the frequency of the word is greater than 1.
    - If it is, return the word as the first repeated word.
8. If no repeated words are found, return the string "No Repetition" to indicate that no words were repeated.

### The time complexity of find_first_repeated_word is O(n + m), and the space complexity is O(m), where n is the length of the input string and m is the number of words in the input string.


## Solution
[The Code Link](./hashtable/hashtable/HashmapRepeatedWord.py)
[The Test Code Link](./tests/test_find_first_repeated_word.py)

- To run the code :

    python3 -m venv .venv

    source .venv/bin/activate
    
- To run the Test:

    pytest

