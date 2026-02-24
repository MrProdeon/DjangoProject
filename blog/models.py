from django.db import models

# Create your models here.
class BlogEntry(models.Model):

    name = models.CharField(max_length=150)
    context = models.TextField()
    preview = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_publicated = models.BooleanField()
    views_count = models.IntegerField()
    