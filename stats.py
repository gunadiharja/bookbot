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

# helper function
def sort_on(text):
    return text["num"]

def sort_count(text):
    data = count_char(text)
    list_dict = []
    for k, v in data.items():
        data_dict = {}
        data_dict["char"] = k
        data_dict["num"] = v
        list_dict.append(data_dict)

    list_dict.sort(reverse=True, key=sort_on)   
    return list_dict
