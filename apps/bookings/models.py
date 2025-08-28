# Create your models here.
from django.db import models
from django.conf import settings
from ..travel.models import TravelOption


class Booking(models.Model):
    STATUS_CHOICES = [
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="confirmed"
    )

    def __str__(self):
        return f"Booking {self.booking_id} - {self.user.username} - {self.status}"

    def save(self, *args, **kwargs):
        if not self.pk and self.status == "confirmed":
            if self.number_of_seats > self.travel_option.available_seats:
                raise ValueError("Not enough seats available.")
            self.travel_option.available_seats -= self.number_of_seats
            self.travel_option.save()
        super().save(*args, **kwargs)

    def cancel(self):
        if self.status == "confirmed":
            self.travel_option.available_seats += self.number_of_seats
            self.travel_option.save()
            self.status = "cancelled"
            self.save()
