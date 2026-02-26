from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path("create/", views.BlogCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.BlogUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.BlogDeleteView.as_view(), name="delete")
]
