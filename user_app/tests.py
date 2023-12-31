from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            'username': 'testcase',
            'email': 'testcase@example.com',
            'password': 'NewPassword@123',
            'password2': 'NewPassword@123',
        }
        url = reverse('register')
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testcase')
        self.assertEqual(User.objects.get().email, 'testcase@example.com')
        self.assertTrue(User.objects.get().check_password('NewPassword@123'))
        self.assertTrue(Token.objects.get(user=User.objects.get()))


class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example',
                                             password='NewPassword@123')

    def test_login(self):
        data = {
            'username': 'example',
            'password': 'NewPassword@123',
        }
        url = reverse('login')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Token.objects.get(user=self.user))

    def test_logout(self):
        self.token = Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        
        url = reverse('logout')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

