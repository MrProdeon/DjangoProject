from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForms(UserCreationForm):

    class Meta:
        template_name = ""
        fields = ["email", "password"]