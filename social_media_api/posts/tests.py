from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Post, Comment

User = get_user_model()

class PostCommentAPITests(APITestCase):

    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username="mercy", email="mercy@example.com", password="pass1234")
        self.user2 = User.objects.create_user(username="other", email="other@example.com", password="pass5678")

        # Generate tokens
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)

        # Auth headers for both users
        self.auth_headers_user1 = {"HTTP_AUTHORIZATION": f"Token {self.token1.key}"}
        self.auth_headers_user2 = {"HTTP_AUTHORIZATION": f"Token {self.token2.key}"}

    # ---------------------- POSTS ----------------------

    def test_create_post_authenticated(self):
        data = {"title": "My First Post", "content": "Hello from Mercy!"}
        response = self.client.post("/posts/", data, **self.auth_headers_user1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().author, self.user1)

    def test_create_post_unauthenticated(self):
        data = {"title": "Should Fail", "content": "No auth here"}
        response = self.client.post("/posts/", data)  # No token
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_post_only_author(self):
        post = Post.objects.create(author=self.user1, title="Secure Post", content="Original content")
        data = {"title": "Hacked", "content": "Trying to hack"}
        response = self.client.put(f"/posts/{post.id}/", data, **self.auth_headers_user2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_posts_pagination_and_search(self):
        # Create 7 posts
        for i in range(7):
            Post.objects.create(author=self.user1, title=f"Post {i}", content="Test content")

        response = self.client.get("/posts/?page=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.json())

        # Search
        response = self.client.get("/posts/?search=Post 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.json()["count"], 1)

    # ---------------------- COMMENTS ----------------------

    def test_create_comment_authenticated(self):
        post = Post.objects.create(author=self.user1, title="Commented Post", content="Testing comments")
        data = {"post": post.id, "content": "Nice post!"}
        response = self.client.post("/comments/", data, **self.auth_headers_user2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().author, self.user2)

    def test_update_comment_only_author(self):
        post = Post.objects.create(author=self.user1, title="Another Post", content="For comments")
        comment = Comment.objects.create(post=post, author=self.user1, content="Original comment")

        data = {"post": post.id, "content": "Trying to edit someone else's comment"}
        response = self.client.put(f"/comments/{comment.id}/", data, **self.auth_headers_user2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
from django.test import TestCase

# Create your tests here.
