from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


def homepage(request):
    travel_options = [
        {
            "id": 1,
            "type": "bus",
            "source": "Delhi",
            "destination": "Jaipur",
            "departure_datetime": timezone.now() + timedelta(hours=5),
            "price": 750,
            "available_seats": 12,
        },
        {
            "id": 2,
            "type": "train",
            "source": "Mumbai",
            "destination": "Goa",
            "departure_datetime": timezone.now() + timedelta(days=1, hours=3),
            "price": 1200,
            "available_seats": 30,
        },
        {
            "id": 3,
            "type": "flight",
            "source": "Bangalore",
            "destination": "Hyderabad",
            "departure_datetime": timezone.now() + timedelta(hours=8),
            "price": 3500,
            "available_seats": 5,
        },
    ]
    return render(request, "homepage.html", {"travel_options": travel_options})


def about(request):
    return render(request, "about.html")


def terms(request):
    return render(request, "terms.html")


def privacy(request):
    return render(request, "privacy.html")


def offers(request):
    return render(request, "offers.html")
