from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name="наименование", unique=True)
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(upload_to='products/', verbose_name="изображение",
                              blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(verbose_name="цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата обновления")
    is_in_stock = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["price"]

class Contacts(models.Model):

    name = models.CharField(max_length=150, verbose_name="название")
    number = models.CharField(max_length=12, verbose_name="номер телефона")

    def __str__(self):
        return f"{self.name} {self.number}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
        ordering = ["name"]