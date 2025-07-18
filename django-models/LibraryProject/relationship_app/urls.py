from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
]

#Task 2
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # ✅ Use these direct imports
from . import views  # ✅ Required for "views.register"

urlpatterns = [
    # Authentication views
    path("register/", views.register, name="register"),  # ✅ "views.register"
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # ✅ exact string
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # ✅ exact string
]
