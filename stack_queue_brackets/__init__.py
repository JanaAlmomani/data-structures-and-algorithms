
def validate_brackets(input):
    """
    Validate the balance of brackets in a given input string.

    Arguments:
    - input: A string containing various types of brackets.

    Returns:
    - A boolean value indicating whether the brackets are balanced or not.
      True if the brackets are balanced, False otherwise.
      
    """
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    
    for item in input:
        if item in bracket_pairs:
            stack.append(item)
        elif item in bracket_pairs.values():
            if not stack:
                return False
            opening_bracket = stack.pop()
            if item != bracket_pairs[opening_bracket]:
                return False
    
    return len(stack) == 0

print(validate_brackets("{}"))  # True
print(validate_brackets("{}(){}"))  # True
print(validate_brackets("()[[Extra Characters]]"))  # True
print(validate_brackets("(){}[[]]"))  # True
print(validate_brackets("{}{Code}[Fellows](())"))  # True
print(validate_brackets("[({}]"))  # False
print(validate_brackets("(]("))  # False
print(validate_brackets("{(})")) #False