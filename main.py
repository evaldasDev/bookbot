def read_book(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_couts(text):
    chars = {}
    for char in text:
        low_char = char.lower()
        if low_char in chars:
            chars[low_char] += 1
        else:
            chars[low_char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sorted_char_dict(char_dict):
    sorted_dict = []
    for char in char_dict:
        sorted_dict.append({"char": char, "num": char_dict[char]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def print_report(book_text):
    word_cnt = word_count(book_text)
    char_dict = char_couts(book_text)
    char_dict = sorted_char_dict(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_cnt} words found in the document\n")
    
    for char in char_dict:
        if char["char"].isalpha():
            print(f"The '{char["char"]}' character was found {char["num"]} times")
    
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    book_contents = read_book(book_path)
    print_report(book_contents)

main()