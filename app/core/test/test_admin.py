from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@tests.com',
            password='testtest123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@tests.com',
            password='testtest123'
        )

