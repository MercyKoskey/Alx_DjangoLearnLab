# Create a Book Entry
from bookshelf.models import Book

Book.objects.create(
    title="Things Fall Apart",
    author="Chinua Achebe",
    published_date="1958-06-17",
    isbn="9780435905255",
    price=12.50
)
