import utils
import sorts
import copy

bookshelf = utils.load_books('books_small.csv')


# for book in bookshelf:
#   print(book['title_lower'])

def by_title_ascending(book_a, book_b):
    if book_a['title_lower'] > book_b['title_lower']:
        return True
    return False


sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)


# for book in sort_1:
#   print(book['title'])

# function to sort books by author
def by_author_ascending(book_a, book_b):
    if book_a['author_lower'] > book_b['author_lower']:
        return True
    return False


bookshelf_v1 = bookshelf[:]

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

# for book in sort_2:
#   print(book['title']) 

# run bubble sort using by_total_length as comparison
bookshelf_v2 = bookshelf[:]

# run bubble sort using by_total_length as comparison
quicksort_1 = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in quicksort_1:
    print(book['lower_authors'])


# run bubble sort using by_total_length as comparison
def by_total_length(book_a, book_b):
    if len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(
            book_b['title_lower']):
        return True
    return False


# load large books collection
long_bookshelf = utils.load_books('books_large.csv')

# run bubble sort using by_total_length as comparison
# print(sorts.bubble_sort(long_bookshelf, by_total_length))

# run quick sort using by_total_length as comparison
quicksort_2 = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

for book in quicksort_2:
    print(book['lower_authors'])


