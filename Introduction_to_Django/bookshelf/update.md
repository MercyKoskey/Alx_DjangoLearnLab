# Update a Book Entry
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.price = 15.00
book.save()
