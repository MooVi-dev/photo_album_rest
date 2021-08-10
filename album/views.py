"""module for controllers"""
from django.http import Http404
from rest_framework import viewsets, filters, status, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins

from .models import Album, Photo
from .serializers import (
    AlbumListSerializer,
    AlbumDetailSerializer,
    AlbumCreateSerializer,
    PhotoCreateSerializer,
    PhotoDetailSerializer,
    PhotoListSerializer,
    AlbumUpdateSerializer,
    PhotoUpdateSerializer)


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод альбомов"""
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created_at', 'photos_count']

    def get_queryset(self):
        user = self.request.user
        albums = Album.objects.filter(creator=user)
        return albums

    def get_serializer_class(self):
        if self.action == 'list':
            return AlbumListSerializer
        if self.action == "retrieve":
            return AlbumDetailSerializer
        return None


class AlbumCreateViewSet(viewsets.ModelViewSet):
    """Редактирование альбома"""

    def get_serializer_class(self):
        if self.action == 'create':
            return AlbumCreateSerializer
        if self.action == "update":
            return AlbumUpdateSerializer
        # return None


class AlbumDeleteViewSet(mixins.DestroyModelMixin, generics.GenericAPIView):
    """Удаление альбома"""
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        album = Album.objects.filter(creator=user)
        return album

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод фотографий"""
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['album', 'tags']
    ordering_fields = ['album', 'created_at']

    def get_queryset(self):
        user = self.request.user
        photos = Photo.objects.filter(album__creator=user)
        return photos

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        if self.action == "retrieve":
            return PhotoDetailSerializer
        return None


class PhotoCreateViewSet(viewsets.ModelViewSet):
    """Добавление фотограии"""

    def get_serializer_class(self):
        if self.action == 'create':
            return PhotoCreateSerializer
        if self.action == "update":
            return PhotoUpdateSerializer
        return None


class PhotoDeleteViewSet(mixins.DestroyModelMixin, generics.GenericAPIView):
    """Удаление альбома"""
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        album = Photo.objects.filter(album__creator=user)
        return album

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
