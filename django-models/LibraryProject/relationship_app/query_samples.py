import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
try:
    author = Author.objects.get(name="Chinua Achebe")
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(book.title)
except Author.DoesNotExist:
    print("Author not found.")

# Query 2: List all books in a library
try:
    library = Library.objects.get(name="Central Library")
    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(book.title)
except Library.DoesNotExist:
    print("Library not found.")

# Query 3: Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian at {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print("Librarian not found.")
