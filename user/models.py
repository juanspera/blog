from django.contrib.auth.models import User
from django.db import models


class Avatar(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)