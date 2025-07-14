# Update Book Entry

To update an existing book:

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.author = "G. Orwell"
book.save()


