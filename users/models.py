from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    avatar = models.ImageField(upload_to="users", blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email