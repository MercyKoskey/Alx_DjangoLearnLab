from django.urls import path
from . import views

urlpatterns = [
    # =====================
    # Authentication URLs
    # =====================
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # =====================
    # Blog Post CRUD URLs
    # =====================
    path('', views.PostListView.as_view(), name='post-list'),                       # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),     # Post detail
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),          # Create new post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
