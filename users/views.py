from django.shortcuts import render
from django.views import View
from users.forms import CustomUserCreationForms
from django.urls import reverse_lazy

class RegisterView(View):
    form_class = CustomUserCreationForms
    template_name = "register.html"
    success_url = reverse_lazy("catalog:home")
