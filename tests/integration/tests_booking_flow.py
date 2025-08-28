from ...apps.travel.models import TravelOption
from ...apps.bookings.models import Booking
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class EndToEndBookingTests(TestCase):
    def test_full_booking_flow(self):
        # Register & Login
        self.client.post(
            reverse("register"),
            {
                "username": "flowuser",
                "email": "flow@example.com",
                "password1": "ComplexPass123!",
                "password2": "ComplexPass123!",
            },
        )
        self.client.login(username="flowuser", password="ComplexPass123!")

        # Create TravelOption
        travel = TravelOption.objects.create(
            type="bus",
            source="Delhi",
            destination="Jaipur",
            departure_datetime=timezone.now() + timedelta(days=1),
            price=700,
            available_seats=10,
        )

        # Book
        booking = Booking.objects.create(
            user=User.objects.get(username="flowuser"),
            travel_option=travel,
            number_of_seats=2,
            total_price=1400,
            status="confirmed",
        )

        # Cancel
        self.client.get(reverse("booking_cancel", args=[booking.pk]))
        booking.refresh_from_db()
        self.assertEqual(booking.status, "cancelled")
