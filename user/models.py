from django.contrib.auth.models import User
from django.db import models


class Avatar(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares')

    def __str__(self):
        return f"Avatar: '{self.username}' - '{self.imagen}"