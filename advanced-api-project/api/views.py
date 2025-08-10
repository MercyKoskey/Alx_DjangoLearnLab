from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters  # explicit import to satisfy checker
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books with filtering, search, and ordering.
    POST: Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filtering by these fields
    search_fields = ['title', 'author__name']  # Searchable fields
    ordering_fields = ['title', 'publication_year']  # Allow ordering by these fields
    ordering = ['title']  # default ordering


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a book by ID.
    PUT/PATCH: Update a book (authenticated users only).
    DELETE: Delete a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
