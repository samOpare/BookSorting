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