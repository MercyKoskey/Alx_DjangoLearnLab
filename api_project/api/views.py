from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing YourModel instances.
    Only accessible to authenticated users.
    """
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users allowed
