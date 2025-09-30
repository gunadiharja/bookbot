def get_book_path(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    text_to_count = text.split()
    num_words = len(text_to_count)
    return f"Found {num_words} total words"

def main():
    text = get_book_path("books/frankenstein.txt")
    print(count_words(text))

main()