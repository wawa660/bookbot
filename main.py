from stats import *
import sys


def get_book_text(path):
    with open(path, 'r', encoding = 'utf-8-sig') as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    nwords = count_words(text)
    nchars = count_char(text)
    print(f"Found {nwords} total words")
    for i in sort_on(nchars):
        if i['char'].isalpha():
            print(f"{i['char']}: {i['count']}")

main()
