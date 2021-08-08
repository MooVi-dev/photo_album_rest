"""module for forms"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Форма создания пользователей"""

    class Meta(UserCreationForm):
        """meta"""
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """Форма редактирования пользователей"""

    class Meta:
        """meta"""
        model = User
        fields = ('username', 'email')
