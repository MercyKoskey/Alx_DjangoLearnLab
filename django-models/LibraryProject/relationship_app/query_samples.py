import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# Query 2: List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)  # ← this line must match
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print(book.title)
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# Query 3: Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian at {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"Librarian for '{library_name}' not found.")
