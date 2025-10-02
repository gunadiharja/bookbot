def count_words(text):
    text_to_count = text.split()
    num_words = len(text_to_count)
    return f"Found {num_words} total words"

def count_char(text):
    char = {}
    for i in text.lower():
        if i not in char:
            char[i] = 0
        char[i] += 1 
    return(char)
