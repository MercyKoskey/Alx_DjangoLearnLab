# Retrieve Book Entries
from bookshelf.models import Book

# Get all books
Book.objects.all()

# Get a specific book
Book.objects.get(id=1)
