import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

for book in bookshelf:
    print(book['title_lower'])


def by_title_ascending(book_a, book_b):
    if book_a['title_lower'] > book_b['title_lower']:
        return True
    return False


sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

for book in sort_1:
    print(book['title'])


# function to sort books by author
def by_author_ascending(book_a, book_b):
    if book_a['author_lower'] > book_b['author_lower']:
        return True
    return False

bookshelf_v1 = bookshelf[:]

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

for book in sort_2:
    print(book['title'])

bookshelf_v2 = bookshelf[:]

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

def by_total_length(book_a, book_b):
    if book_a['author_lower'] > book_b['author_lower']:
        return True
    return False

