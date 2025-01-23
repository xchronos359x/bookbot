def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counts = get_num_letters(text)
    nice_list = get_only_letters(text)  
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter, count in nice_list.items():
        print(f"The '{letter}' character was found {count} times")
        

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):    
    words = text.split()
    return len(words)

def get_num_letters(text):
    letter_counts = {}
    for letter in text.lower():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def get_only_letters(text):
    letters_only = {}
    for letter in text.lower():
        if letter.isalpha():
            letters_only[letter] = letters_only.get(letter, 0) + 1
    return letters_only


    return letters

   
main()