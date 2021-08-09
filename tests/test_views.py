"""module for tests"""
from datetime import datetime
from rest_framework.utils import json
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.test import TestCase
from rest_framework.test import APIClient

from users.models import User
from album.models import Album


class AlbumListViewTest(TestCase):
    """Тестирование вывода альбомов"""

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        cls.test_user1 = test_user1.save()
        cls.token_user1 = Token.objects.create(user=test_user1)
        album_list = []
        for item in range(5):
            album = Album.objects.create(name=f'{str(test_user1)} album {item}', creator=test_user1,
                                         created_at=datetime.now())
            album.save()
            album_list.append(album)
        cls.album_list1 = album_list

        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        cls.test_user2 = test_user2.save()
        cls.token_user2 = Token.objects.create(user=test_user2)
        album_list = []
        for item in range(5):
            album = Album.objects.create(name=f'{str(test_user2)} album {item}',
                                         creator=test_user2, created_at=datetime.now())
            album_list.append(album)
        cls.album_list2 = album_list

    def test_view_via_token(self):
        """Проверка получения списка альбомов"""
        client = APIClient(HTTP_AUTHORIZATION='Token ' + 'None')
        resp = client.get('/api/v1/album/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user__username='testuser1')
        client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)
        resp = client.get('/api/v1/album/', data={'format': 'json'})
        response_data = json.loads(resp.content)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        tested_data = []
        for item in self.album_list1:
            item_dict = dict(id=item.pk, name=item.name,
                             created_at=str(datetime.date(item.created_at)),
                             photos_count=item.photos_count, creator=item.creator.id)
            tested_data.append(item_dict)

        tested_data = json.dumps(tested_data)
        self.assertEqual(tested_data, json.dumps(response_data))

        token = Token.objects.get(user__username='testuser2')
        client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)
        resp = client.get('/api/v1/album/', data={'format': 'json'})
        response_data = json.loads(resp.content)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        tested_data = []
        tested_data = json.dumps(tested_data)
        self.assertNotEqual(tested_data, json.dumps(response_data))
