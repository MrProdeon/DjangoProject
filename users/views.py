from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import CustomUserCreationForms
from django.urls import reverse_lazy
from django.contrib.auth import login



class RegisterView(CreateView):
    form_class = CustomUserCreationForms
    template_name = "register.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)


    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать на наш сайт!"
        message = "Благодарим за регистрацию!"
        from_email = "Prodeon21@yandex.ru" # NEED TO CREATE
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

class CustomLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("catalog:home")

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:home')