"""module for service classes and funcs"""
from django.conf import settings
from django_filters import rest_framework as filters
from django.core.exceptions import ValidationError


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """Char filter"""
    pass


def validate_size_image(fieldfileobj):
    """Validate image size"""
    filesize = fieldfileobj.size
    print(filesize)
    if filesize > settings.PHOTO_SIZE_LIMIT_MB*1024*1024:
        raise ValidationError(f'Max file size is {str(settings.PHOTO_SIZE_LIMIT_MB)}Mb')
