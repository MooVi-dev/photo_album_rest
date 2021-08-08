"""module for admin panel"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Пользователи"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['id', 'email', 'username',]
