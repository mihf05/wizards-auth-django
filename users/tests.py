from django.test import TestCase, Client
from django.contrib.auth.models import User
from django_login_history2.models import Login
from django.urls import reverse
from rest_framework import status

class LoginHistoryTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_history_recorded(self):
        # Perform login
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expecting successful login

        # Check if login history is recorded
        login_history = Login.objects.filter(user=self.user)
        self.assertEqual(login_history.count(), 1)

        # Verify login details
        latest_login = login_history.first()
        self.assertIsNotNone(latest_login.ip)
        self.assertIsNotNone(latest_login.user_agent)
        self.assertIsNotNone(latest_login.created_at)

    def test_multiple_logins(self):
        # Perform multiple logins
        for _ in range(3):
            response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.client.logout()

        # Check if all logins are recorded
        login_history = Login.objects.filter(user=self.user)
        self.assertEqual(login_history.count(), 3)

    def test_failed_login_not_recorded(self):
        # Attempt a failed login
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Check that no login history is recorded for failed attempt
        login_history = Login.objects.filter(user=self.user)
        self.assertEqual(login_history.count(), 0)
