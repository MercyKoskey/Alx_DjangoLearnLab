from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    # Book-related views
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),

    # Authentication views
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Role-based access views
    path('admin-role/', admin_view, name='admin-view'),
    path('librarian-role/', librarian_view, name='librarian-view'),
    path('member-role/', member_view, name='member-view'),
]

from .views import add_book, edit_book, delete_book

urlpatterns += [
    path("add_book/", add_book, name="add-book"),
    path("edit_book/<int:pk>/", edit_book, name="edit-book"),
    path("delete_book/<int:pk>/", delete_book, name="delete-book"),
]
