"""module for tests"""
from datetime import datetime
from io import BytesIO

from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files import File
from django.test import TestCase

from album.models import Album, Tag, Photo

TEST_IMAGE = 'media/test.jpg'


def get_image(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


class SigninTest(TestCase):
    """Тестирование авторизации и создания пользователей"""
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='user0', password='user0123456')
        cls.user.save()

    def tearDown(self):
        self.user.delete()


class AlbumModelTest(TestCase):
    """Тестирование модели Альбомов"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='user0', password='user0123456')
        cls.user.save()
        cls.album = Album.objects.create(name='Test album', creator=cls.user,
                                          created_at=datetime.now())

    def tearDown(self):
        self.album.delete()
        self.user.delete()

    def test_instance(self):
        """Проверка созданного экземпляра"""
        inst = Album.objects.get(pk=self.album.pk)
        self.assertEqual(inst, self.album)

    def test_name_label(self):
        """Проверка наименования"""
        inst = Album.objects.get(pk=self.album.pk)
        self.assertEqual(str(inst), 'Test album')

    def test_creator(self):
        """Проверка создателя"""
        inst = Album.objects.get(pk=self.album.pk)
        field = inst.creator
        self.assertEqual(field, self.user)

    def test_created_at(self):
        """Проверка даты создания"""
        inst = Album.objects.get(pk=self.album.pk)
        field = inst.created_at
        self.assertEqual(field, datetime.now().date())

    def test_photos_count(self):
        """Проверка количества фотографий альбома"""
        inst = Album.objects.get(pk=self.album.pk)
        field = inst.photos_count
        self.assertEqual(field, 0)


class TagModelTest(TestCase):
    """Тестирование модели Тегов"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='user0', password='user0123456')
        cls.user.save()
        cls.tag = Tag.objects.create(name='Test tag')

    def tearDown(self):
        self.tag.delete()
        self.user.delete()

    def test_instance(self):
        """Проверка созданного экземпляра"""
        inst = Tag.objects.get(pk=self.tag.pk)
        self.assertEqual(inst, self.tag)

    def test_name_label(self):
        """Проверка наименования"""
        inst = Tag.objects.get(pk=self.tag.pk)
        self.assertEqual(str(inst), 'Test tag')


class PhotoModelTest(TestCase):
    """Тестирование модели Фотографий"""

    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(username='user0', password='user0123456')
        cls.user = user
        album = Album.objects.create(name='Test album', creator=user,
                                          created_at=datetime.now())
        cls.album = album
        cls.tag = Tag.objects.create(name='Test tag')
        file = open(TEST_IMAGE, 'rb')
        cls.file = File(file=file)
        cls.photo = Photo.objects.create(name='Test photo', image=File(file=file),
                                          album=album, created_at=datetime.now())
        cls.photo.tags.add(cls.tag)

    def tearDown(self):
        self.photo.delete()
        self.tag.delete()
        self.album.delete()
        self.user.delete()

    def test_instance(self):
        """Проверка созданного экземпляра"""
        inst = Photo.objects.get(pk=self.photo.pk)
        print(inst)
        self.assertEqual(inst, self.photo)

    def test_name_label(self):
        """Проверка наименования"""
        inst = Photo.objects.get(pk=self.photo.pk)
        self.assertEqual(str(inst), 'Test photo')

    def test_album(self):
        """Проверка альбома"""
        inst = Photo.objects.get(pk=self.photo.pk)
        field = inst.album
        self.assertEqual(field, self.album)

    def test_created_at(self):
        """Проверка даты создания"""
        inst = Photo.objects.get(pk=self.photo.pk)
        field = inst.created_at
        self.assertEqual(field, datetime.now().date())

    def test_tags(self):
        """Проверка тегов"""
        inst = Photo.objects.get(pk=self.photo.pk)
        field = inst.tags.all()[0]
        self.assertEqual(field, self.tag)

    def test_image(self):
        """Проверка картинок"""
        inst = Photo.objects.get(pk=self.photo.pk)
        field = inst.image
        print(field.name)
        # print(self.file)
        # self.assertEqual(field, self.file)
