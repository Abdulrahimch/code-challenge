from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse('users:create')
TOKEN_URL = reverse('users:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        payload = {
            'email': 'audrey@tests.com',
            'password': 'testtest123',
            'name': 'Audrey'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_exists(self):
        payload = {
            'email': 'audrey@tests.com',
            'password': 'testtest123',
        }

        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_token(self):
        payload = {
            'email': 'tests@tests.com',
            'password': 'testtest123'
        }
        create_user(**payload)

        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        payload = {
            'email': 'wrongtest@tests.com',
            'password': 'testtest123'
        }

        create_user(email='tests@tests.com', password='test123')

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)



