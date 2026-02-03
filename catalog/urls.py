from django.contrib import admin
from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("contacts/", views.contact, name="contacts")
]
