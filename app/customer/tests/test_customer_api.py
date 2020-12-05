from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from customer.serializers import CustomerSerializer

from rest_framework.test import APIClient
from rest_framework import status

CREATE_CUSTOMER_URL = reverse('customer:create')
LIST_CUSTOMER_URL = reverse('customer:list')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class CustomerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_customer_is_unauthorized(self):
        payload = {
            'first_name': 'john',
            'last_name': 'Biden',
            'TC': '12531835135',
            'gsm': '+905531221455'
        }
        res = self.client.post(CREATE_CUSTOMER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_customer_is_unauthorized(self):
        res = self.client.get(LIST_CUSTOMER_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class AuthrizedCustomerAPITest(TestCase):
    def setUp(self):
        self.user = create_user(
            email='user@test.com',
            password='testtest123',
            name='name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_customer_success(self):
        payload = {
            'first_name': 'john',
            'last_name': 'Biden',
            'TC': '12531835135',
            'gsm': '+9055312455'
        }

        res = self.client.post(CREATE_CUSTOMER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_customer_exists(self):
        serializer_data = {
            'first_name': 'john',
            'last_name': 'Biden',
            'TC': '12531835135',
            'gsm': '+905531221455'
        }
        serializer = CustomerSerializer(data=serializer_data)
        serializer.is_valid()
        serializer.save()

        res = self.client.post(CREATE_CUSTOMER_URL, serializer_data)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_customer_invalid_TC(self):
        payload = {
            'first_name': 'john',
            'last_name': 'Biden',
            'TC': '125135',
            'gsm': '+9055312455'
        }
        res = self.client.post(CREATE_CUSTOMER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


