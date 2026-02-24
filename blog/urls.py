from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("contacts/", views.Contact.as_view(), name="contacts"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product"),
    path("add_product/", views.ProductCreateView.as_view(), name="add_product")
]
