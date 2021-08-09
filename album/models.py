"""module for models of project"""
from datetime import date

from django.core.validators import FileExtensionValidator
from django.db import models
from album.service import validate_size_image
from app import settings


class Album(models.Model):
    """Альбомы"""
    name = models.CharField("Имя", max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name="Создатель", on_delete=models.CASCADE, null=True)
    created_at = models.DateField("Дата создания", default=date.today)
    photos_count = models.PositiveIntegerField("Количество фотографий", default=0)

    def __str__(self):
        return str(self.name)

    def add_photo(self, count):
        """Изменение количества фотографий в альбоме"""
        self.photos_count += count

    class Meta:
        """meta"""
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Tag(models.Model):
    """Теги"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        """meta"""
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Photo(models.Model):
    """Фотографии"""
    name = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="photos/",
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'],
                                                         message='File extension is not allowed. '
                                                                 'Allowed extensions are: '
                                                                 '[jpeg, jpg, png]'),
                                  validate_size_image
                              ], )
    album = models.ForeignKey(Album, verbose_name="Альбом", on_delete=models.CASCADE,)
    tags = models.ManyToManyField(Tag, verbose_name="теги")
    created_at = models.DateField("Дата создания", default=date.today)

    def __str__(self):
        return str(self.name)

    class Meta:
        """meta"""
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
