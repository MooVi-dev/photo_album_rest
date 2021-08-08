"""module for apps configs"""
from django.apps import AppConfig


class AlbumConfig(AppConfig):
    """Album config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'album'
