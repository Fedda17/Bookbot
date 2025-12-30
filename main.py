from stats import count_words, count_by_chars, sort_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        text_string = get_book_text(sys.argv[1])
        print("----------- Word Count ----------")
        print(f"Found {count_words(text_string)} total words")
        print("--------- Character Count -------")
        char_sorted_list = sort_counts(count_by_chars(text_string))
        for entry in char_sorted_list:
            print(f"{entry["char"]}: {entry["num"]}")
        print("============= END ===============")


main()