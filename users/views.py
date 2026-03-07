from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
from users.forms import CustomUserCreationForms
from django.urls import reverse_lazy



class RegisterView(CreateView):
    form_class = CustomUserCreationForms
    template_name = "register.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать на наш сайт!"
        message = "Благодарим за регистрацию!"
        from_email = "" # NEED TO CREATE
        recipient_list = [user_email]
        send_mail(subject, message, recipient_list, from_email)
