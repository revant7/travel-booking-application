from django.contrib import admin

# Register your models here.

from .models import TravelOption


@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = (
        "travel_id",
        "type",
        "source",
        "destination",
        "departure_datetime",
        "price",
        "available_seats",
    )
    list_filter = ("type", "source", "destination")
    search_fields = ("source", "destination")
    ordering = ("departure_datetime",)
