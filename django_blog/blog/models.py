from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Blog Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date_posted = models.DateTimeField(auto_now_add=True)  # creation timestamp
    updated_at = models.DateTimeField(auto_now=True)       # last update timestamp
    tags = TaggableManager(blank=True)                     # Tags for categorization

    class Meta:
        ordering = ['-date_posted']  # newest first

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # creation timestamp
    updated_at = models.DateTimeField(auto_now=True)      # last update timestamp

    class Meta:
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return f'Comment by {self.author.username} on "{self.post.title}"'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})
