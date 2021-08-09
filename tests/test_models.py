"""module for tests"""
from datetime import datetime

from django.contrib.auth import get_user_model, authenticate
from django.core.files import File
from django.test import TestCase

from album.models import Album, Tag, Photo

TEST_IMAGE = 'media/photos/test.jpg'


class SigninTest(TestCase):
    """Тестирование авторизации и создания пользователей"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user0', password='user0123456')
        self.user.save()

    def tearDown(self):
        self.user.delete()


class AlbumModelTest(TestCase):
    """Тестирование модели Альбомов"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user0', password='user0123456')
        self.user.save()
        self.album = Album.objects.create(name='Test album', creator=self.user,
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

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user0', password='user0123456')
        self.user.save()
        self.tag = Tag.objects.create(name='Test tag')

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

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user0', password='user0123456')
        self.user.save()
        self.album = Album.objects.create(name='Test album', creator=self.user,
                                          created_at=datetime.now())
        self.tag = Tag.objects.create(name='Test tag')
        file = open(TEST_IMAGE, 'rb')
        file = File(file)
        self.photo = Photo.objects.create(name='Test photo', image=file,
                                          album=self.album, created_at=datetime.now())
        self.photo.tags.add(self.tag)

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
