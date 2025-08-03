from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api.views import YourModelViewSet  # Import your API viewset here

router = DefaultRouter()
router.register(r'yourmodel', YourModelViewSet, basename='yourmodel')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Token authentication endpoint: POST username & password, get token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Include router URLs for your API
    path('api/', include(router.urls)),
]
