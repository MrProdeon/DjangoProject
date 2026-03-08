from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    avatar = models.ImageField(upload_to="users", blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)

    username = None
    email = models.EmailField(unique=True, verbose_name='email address')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone_number', 'country']

    def __str__(self):
        return self.email