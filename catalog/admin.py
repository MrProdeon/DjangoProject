from django.contrib import admin
from catalog.models import Category, Product, Contacts
from users.models import CustomUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "description", "is_publicated")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "number")
    list_filter = ("id", "name")
    search_fields = ("name", "number")

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
