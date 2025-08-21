from rest_framework import serializers
from .models import Notification
from posts.serializers import PostSerializer
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_type = serializers.SerializerMethodField()
    target_id = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_type', 'target_id', 'timestamp', 'is_read']

    def get_target_type(self, obj):
        return obj.content_type.model

    def get_target_id(self, obj):
        return obj.object_id
