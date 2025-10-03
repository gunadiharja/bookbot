from stats import count_words, sort_count

def get_book_path(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_path("books/frankenstein.txt")
    count = count_words(text)
    char_count = sort_count(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(count)
    print("--------- Character Count -------")
    for i in char_count:
        if i['char'].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
        

main()