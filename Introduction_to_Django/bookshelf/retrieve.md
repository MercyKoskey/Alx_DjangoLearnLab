# Retrieve Book Entry

To retrieve a book entry by title or author:

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.author)  # Output: George Orwell
