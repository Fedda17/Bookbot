def count_words(content):
    return f"{len(content.split())}"

def count_by_chars(content):
    chars_counting = {}
    for letter in content.lower():
        if letter in chars_counting:
            chars_counting[letter] += 1
        else:
            chars_counting[letter] = 1
    return chars_counting

def sort_on(items):
    return items["num"]

def sort_counts(chars_count_dict):
    char_count_list = []
    for char in chars_count_dict:
        if char.isalpha():
            char_count_list.append({"char": char, "num": chars_count_dict[char]})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list

    
