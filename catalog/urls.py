from django.contrib import admin
from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("contacts/", views.Contact.as_view(), name="contacts"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product"),
    path("add_product/", views.ProductCreateView.as_view(), name="add_product"),
    path("update_product/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product"),
    path("delete_product/<int:pk>/", views.ProductDeleteView.as_view(), name="delete_product"),
    path("unpublish_product/<int:pk>/", views.unpublish_product, name="unpublish_product")
]
