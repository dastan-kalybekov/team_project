from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username
