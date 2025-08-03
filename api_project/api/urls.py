from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Set up the router and register the viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ListAPIView route (optional if you're keeping it for list-only purposes)
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes registered with the router (CRUD)
    path('', include(router.urls)),
]
