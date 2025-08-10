from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        
        # Create an author
        self.author = Author.objects.create(name="Test Author")
        
        # Create some books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author)
        
        # URLs
        self.list_url = reverse('book-list')  # Assuming router registered with basename 'book'
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_book_list_unauthenticated(self):
        # List view should be accessible without authentication (read-only)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_create_book_unauthenticated(self):
        # Creating book should fail for unauthenticated users
        data = {"title": "Book Three", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_book_authenticated(self):
        # Authenticated user can create a book
        self.client.login(username='testuser', password='testpass')
        data = {"title": "Book Three", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.client.logout()

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        data = {"title": "Book One Updated", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Book One Updated")
        self.client.logout()

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.detail_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.filter(id=self.book2.id).exists(), False)
        self.client.logout()

    def test_filter_books_by_publication_year(self):
        # Filter books by publication_year
        response = self.client.get(self.list_url, {'publication_year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_search_books_by_title(self):
        # Search books by title text
        response = self.client.get(self.list_url, {'search': 'Two'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book Two")

    def test_order_books_by_title(self):
        # Order books ascending by title
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_order_books_by_publication_year_desc(self):
        # Order books descending by publication_year
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
