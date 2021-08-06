from datetime import date

from django.db import models
from django.contrib.auth.models import User
from app import settings


class Album(models.Model):
    """Альбомы"""
    name = models.CharField("Имя", max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Создатель", on_delete=models.CASCADE, null=True)
    created_at = models.DateField("Дата создания", default=date.today)
    photos_count = models.PositiveIntegerField("Количество фотографий", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Tag(models.Model):
    """Теги"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Photo(models.Model):
    """Фотографии"""
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="photos/")
    album = models.ForeignKey(Album, verbose_name="Альбом", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="теги")
    created_at = models.DateField("Дата создания", default=date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
