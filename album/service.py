from django_filters import rest_framework as filters

from album.models import Photo


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PhotoFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags_name', lookup_expr='in')
    album = CharFilterInFilter(field_name='album', lookup_expr='eq')

    class Meta:
        model = Photo
        fields = ['tags', 'album']
