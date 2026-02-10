from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    body = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        blank=True
    )

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created']),
        ]


    def __str__(self):
        return f'{self.author.username}: {self.body[:30]}'
    
    def total_likes(self):
        """Zwraca liczbę polubień."""
        return self.likes.count()
    
    def is_liked_by(self, user):
        """Sprawdza czy użytkownik polubił post."""
        return self.likes.filter(id=user.id).exists()