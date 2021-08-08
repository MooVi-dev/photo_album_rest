"""module for models of project"""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Users for prev extend"""

    class Meta:
        """meta"""
        db_table = "t_users"
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
