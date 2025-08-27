from django.contrib import admin

# Register your models here.

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "booking_id",
        "user",
        "travel_option",
        "number_of_seats",
        "total_price",
        "booking_date",
        "status",
    )
    list_filter = ("status", "booking_date")
    search_fields = (
        "user__username",
        "travel_option__source",
        "travel_option__destination",
    )
    ordering = ("-booking_date",)
