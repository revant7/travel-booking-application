from django.test import TestCase

# Create your tests here.

from apps.bookings.models import Booking
from apps.travel.models import TravelOption
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


# Booking Creation
class BookingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("booker", password="pass1234")
        self.travel = TravelOption.objects.create(
            type="train",
            source="Pune",
            destination="Goa",
            departure_datetime=timezone.now() + timedelta(days=2),
            price=1000,
            available_seats=50,
        )
        self.client.login(username="booker", password="pass1234")

    def test_booking_reduces_seats(self):
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=2,
            total_price=2000,
            status="confirmed",
        )
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 48)

    # Booking Cancellation Tets

    def test_cancel_restores_seats(self):
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=3,
            total_price=3000,
            status="confirmed",
        )
        self.client.get(reverse("booking_cancel", args=[booking.pk]))
        self.travel.refresh_from_db()
        booking.refresh_from_db()
        self.assertEqual(self.travel.available_seats, 50)
        self.assertEqual(booking.status, "cancelled")
