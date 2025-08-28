from django.test import TestCase

# Create your tests here.
from apps.travel.models import TravelOption
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse


# Travel Option Creation Tests
class TravelOptionTests(TestCase):
    def test_travel_option_str(self):
        travel = TravelOption.objects.create(
            type="flight",
            source="Delhi",
            destination="Mumbai",
            departure_datetime=timezone.now() + timedelta(days=1),
            price=5000,
            available_seats=10,
        )
        self.assertEqual(str(travel), "Flight Delhi → Mumbai")


# Travel Search Filter Tests
class TravelSearchTests(TestCase):
    def setUp(self):
        self.travel = TravelOption.objects.create(
            type="bus",
            source="Delhi",
            destination="Agra",
            departure_datetime=timezone.now() + timedelta(days=1),
            price=800,
            available_seats=20,
        )

    def test_filter_by_source(self):
        response = self.client.get(reverse("travel_list"), {"source": "Delhi"})
        self.assertContains(response, "Delhi")
