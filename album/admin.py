from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Album, Tag, Photo


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Теги"""
    list_display = ("name", )
    list_display_links = ("name",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Фотографии"""
    list_display = ("title", )
    list_display_links = ("title",)


class PhotosInline(admin.TabularInline):
    model = Photo
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Фотография"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Альбомы"""
    list_display = ("name", )
    list_display_links = ("name",)
    inlines = [PhotosInline]
