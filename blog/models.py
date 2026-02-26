from django.db import models

# Create your models here.
class BlogEntry(models.Model):

    name = models.CharField(max_length=150, verbose_name="Название")
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to='blogs/', verbose_name="изображение",
                              blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_publicated = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"Название поста: {self.name}"
    