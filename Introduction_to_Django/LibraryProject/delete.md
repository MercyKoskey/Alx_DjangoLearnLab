```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
print(Book.objects.all())
```
---

# Expected output:
<QuerySet []>
```