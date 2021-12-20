from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = "__all__"


class RegisterForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'requests_admin_right']

