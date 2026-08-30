from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser

class CustomUserCreationForms(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["email"]

class CustomUserAuthenticationForm(AuthenticationForm):
    model = CustomUser