from django.contrib import admin
from .models import Utilisateur
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = Utilisateur
    add_form = CustomUserCreationForm



admin.site.register(Utilisateur, CustomUserAdmin)