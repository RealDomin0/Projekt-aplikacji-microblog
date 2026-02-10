from django.db import models
from django.conf import settings
from urllib.parse import quote


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d',
        default='users/default/avatar.png',
        blank=True
    )

    def get_avatar_url(self, size=200):
        """Zwraca URL zdjęcia profilowego lub wygenerowany avatar"""
        if self.photo and self.photo.name != 'users/default/avatar.png':
            return self.photo.url

        username = quote(self.user.username)
        return f"https://api.dicebear.com/7.x/bottts/svg?seed={username}&size={size}"

    def __str__(self):
        return f'Profil użytkownika {self.user.username}'
