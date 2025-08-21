from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username


#Users that follow this user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

    #Helper methods
    def follow(self, user):
        """Follow another user"""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user"""
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        """Check if following a user"""
        return self.following.filter(id=user.id).exists()

    def is_followed_by(self, user):
        """Check if followed by a user"""
        return self.followers.filter(id=user.id).exists()
