from stats import count_words, count_characters, list_of_counts, stats_printer
import sys
if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

text = get_book_text(book_path)

def sort_by_count(item):
    return item['count']


def main():
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print ('Found ' + str(count_words(text)) + ' total words')
    print('--------- Character Count -------')
    counted_characters = count_characters(text)
    listed_dictionary = list_of_counts(counted_characters)
    stats_printer(listed_dictionary)
    print('============= END ===============')

main()