```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Display all attributes
print(book.id, book.title, book.author, book.publication_year)
```
---
# Expected output: 
```
1 1984 George Orwell 1949
```