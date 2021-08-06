from django.shortcuts import render
from rest_framework import viewsets
from django.db import models
from .models import Album, Photo
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required

from .serializers import AlbumListSerializer, AlbumDetailSerializer, AlbumCreateSerializer, PhotoCreateSerializer, \
    PhotoDetailSerializer, PhotoListSerializer, AlbumUpdateSerializer, PhotoUpdateSerializer
from .service import PhotoFilter


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод альбомов"""
    filter_backends = (DjangoFilterBackend,)

    # @login_required
    def get_queryset(self):
        albums = Album.objects.filter(creator=self.request.user)
        return albums

    def get_serializer_class(self):
        if self.action == 'list':
            return AlbumListSerializer
        elif self.action == "retrieve":
            return AlbumDetailSerializer


class AlbumCreateViewSet(viewsets.ModelViewSet):
    """Создание альбома"""

    def get_serializer_class(self):
        if self.action == 'create':
            return AlbumCreateSerializer
        elif self.action == "update":
            return AlbumUpdateSerializer



class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод фотографий"""
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = PhotoFilter

    def get_queryset(self):
        albums = Photo.objects.filter(album__creator=self.request.user)
        return albums

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        elif self.action == "retrieve":
            return PhotoDetailSerializer


class PhotoCreateViewSet(viewsets.ModelViewSet):
    """Добавление фотограии"""

    def get_serializer_class(self):
        if self.action == 'create':
            return PhotoCreateSerializer
        elif self.action == "update":
            return PhotoUpdateSerializer
