from django.test import TestCase

# Create your tests here.

from .models import ContactMessage
from django.urls import reverse


# Tests For Contact Form Submission
class ContactTests(TestCase):
    def test_contact_form_submission(self):
        response = self.client.post(
            reverse("contact"),
            {"name": "John", "email": "john@example.com", "message": "Test message"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            ContactMessage.objects.filter(email="john@example.com").exists()
        )
