from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    username = models.CharField(max_length=15, unique=True)
    about = models.TextField()

