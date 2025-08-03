from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# This view handles GET /books/ — listing all books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This ViewSet handles full CRUD (GET, POST, PUT, DELETE)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
