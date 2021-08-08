"""module for serializers"""
from rest_framework import serializers

from .models import Album, Photo


class AlbumListSerializer(serializers.ModelSerializer):
    """Список альбомов"""

    class Meta:
        """meta"""
        model = Album
        fields = ('__all__')


class AlbumCreateSerializer(serializers.ModelSerializer):
    """Добавление альбома"""

    class Meta:
        """meta"""
        model = Album
        fields = ('name', )


class AlbumUpdateSerializer(serializers.ModelSerializer):
    """Редактирование альбома"""

    class Meta:
        """meta"""
        model = Album
        fields = ('name', )


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Полное описание фильма"""
    creator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """meta"""
        model = Album
        fields = ('__all__')


class PhotoListSerializer(serializers.ModelSerializer):
    """Список фотографий"""
    album = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        """meta"""
        model = Photo
        fields = ('__all__')


class PhotoCreateSerializer(serializers.ModelSerializer):
    """Добавление фотографии"""

    class Meta:
        """meta"""
        model = Photo
        fields = ('album', 'image', 'tags', 'title', )


class PhotoUpdateSerializer(serializers.ModelSerializer):
    """Редактирование фотографии"""

    class Meta:
        """meta"""
        model = Photo
        fields = ('tags', 'title', )


class PhotoDetailSerializer(serializers.ModelSerializer):
    """Полная информация по фотографии"""
    album = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        """meta"""
        model = Photo
        fields = ('__all__')
