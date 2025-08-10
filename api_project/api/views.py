from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Multiple authentication schemes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    # Example: allow only authenticated users to access
    permission_classes = [permissions.IsAuthenticated]
