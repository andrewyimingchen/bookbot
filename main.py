from stats import word_count 
from stats import char_count
from stats import sort_on
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
        
    
# file_path = "./books/frankenstein.txt"
if __name__ == "__main__":
    book_text = get_book_text(file_path)
    a = word_count(book_text)
    b = char_count(book_text)
    c = sort_on(b)
    # print(book_text)
    print(f"============ BOOKBOT ============\n Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------\n Found {a} total words")
    print(f"--------- Character Count -------\n")
    for i in c:
        print(f" {i['char']}: {i['num']}")
    print("============= END ===============")

    # print(f"{char_count(book_text)} characters found in the document")
    # print(f"{sort_on(char_count(book_text))} characters found in the document")

