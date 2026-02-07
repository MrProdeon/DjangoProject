from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


class Product(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='/static/images/')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["price"]
