from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # Token authentication endpoint: POST username & password, get token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # All API routes
    path('api/', include('api.urls')),
]
