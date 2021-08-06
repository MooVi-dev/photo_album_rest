from rest_framework import serializers

from .models import Album, Tag, Photo


class AlbumListSerializer(serializers.ModelSerializer):
    """Список альбомов"""

    class Meta:
        model = Album
        fields = ('__all__')


class AlbumCreateSerializer(serializers.ModelSerializer):
    """Добавление альбома"""

    class Meta:
        model = Album
        fields = ('name', )


class AlbumUpdateSerializer(serializers.ModelSerializer):
    """Редактирование альбома"""

    class Meta:
        model = Album
        fields = ('name', )


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Полное описание фильма"""
    creator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Album
        fields = ('__all__')


class PhotoListSerializer(serializers.ModelSerializer):
    """Список фотографий"""

    class Meta:
        model = Photo
        fields = ('__all__')


class PhotoCreateSerializer(serializers.ModelSerializer):
    """Добавление фотографии"""

    class Meta:
        model = Photo
        fields = ('album', 'image', 'tags', 'title', )


class PhotoUpdateSerializer(serializers.ModelSerializer):
    """Редактирование фотографии"""

    class Meta:
        model = Photo
        fields = ('tags', 'title', )


class PhotoDetailSerializer(serializers.ModelSerializer):
    """Полная информация по фотографии"""
    album = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Photo
        fields = ('__all__')

