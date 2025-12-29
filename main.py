from stats import count_words, count_by_chars, sort_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    text_string = get_book_text("books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text_string)} total words")
    print("--------- Character Count -------")
    char_sorted_list = sort_counts(count_by_chars(text_string))
    for entry in char_sorted_list:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()