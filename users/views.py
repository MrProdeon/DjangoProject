from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import CustomUserCreationForms
from django.urls import reverse_lazy



class RegisterView(CreateView):
    form_class = CustomUserCreationForms
    template_name = "register.html"
    success_url = reverse_lazy("catalog:home")
