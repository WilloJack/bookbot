def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_chars = character_count(text)
    alpha_chars = sorted_char(num_chars)
    print(f"--- begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in alpha_chars:
        print(f"The '{item['name']}' character was found {item['num']} times")
    
    print("--- End of report ---")


def word_count(text): 
    words = text.split()
    return len(words)

def character_count(text):
    chars = {}
    for i in text:
        lower_c = i.lower()
        if lower_c in chars:
            chars[lower_c] += 1
        else:
            chars[lower_c] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sorted_char(num_chars):
    char_list = []
    for char, count in num_chars.items():
        if char.isalpha():
            char_list.append({"name":char, "num":count})
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()