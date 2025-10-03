from stats import count_words, sort_count
import sys

def get_book_path(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_path(sys.argv[1])
    count = count_words(text)
    char_count = sort_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(count)
    print("--------- Character Count -------")
    for i in char_count:
        if i['char'].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
            
main()