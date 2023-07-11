def is_unique_string(text):
    text = text.replace(" ", "").lower()
    char_set = set()
    
    for char in text:
        if char in char_set:
            return False
        char_set.add(char)
    
    return True
