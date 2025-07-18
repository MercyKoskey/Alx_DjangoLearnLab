# Delete Book Entry

To delete a book:

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.delete()
