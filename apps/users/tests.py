from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


# User Registration Test
class UserRegistrationTests(TestCase):
    def test_register_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "testuser",
                "email": "test@example.com",
                "password1": "ComplexPass123!",
                "password2": "ComplexPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)  # redirect after register
        self.assertTrue(User.objects.filter(username="testuser").exists())


# Login & Logout Tests


class UserAuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass1234")

    def test_login_success(self):
        response = self.client.post(
            reverse("login"), {"username": "test", "password": "pass1234"}
        )
        self.assertEqual(response.status_code, 302)

    def test_login_fail(self):
        response = self.client.post(
            reverse("login"), {"username": "test", "password": "wrong"}
        )
        self.assertContains(response, "Invalid username or password", status_code=200)
