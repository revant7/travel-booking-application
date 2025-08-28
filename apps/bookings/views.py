from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from ..travel.models import TravelOption
from .models import Booking
from django.contrib import messages


@login_required
def booking_list(request):
    upcoming = Booking.objects.filter(
        user=request.user, travel_option__departure_datetime__gte=timezone.now()
    ).order_by("travel_option__departure_datetime")

    past = Booking.objects.filter(
        user=request.user, travel_option__departure_datetime__lt=timezone.now()
    ).order_by("-travel_option__departure_datetime")

    return render(
        request,
        "bookings/booking_list.html",
        {"upcoming": upcoming, "past": past, "now": timezone.now()},
    )


@login_required
def checkout(request, travel_id):
    travel = get_object_or_404(TravelOption, travel_id=travel_id)

    if request.method == "POST":
        seats = int(request.POST["number_of_seats"])
        if seats > travel.available_seats:
            return render(
                request,
                "bookings/checkout.html",
                {"travel": travel, "error": "Not enough seats available."},
            )

        total_price = travel.price * seats
        booking = Booking.objects.create(
            user=request.user,
            travel_option=travel,
            number_of_seats=seats,
            total_price=total_price,
            status="confirmed",
        )

        return redirect("booking_success", pk=booking.pk)

    return render(request, "bookings/checkout.html", {"travel": travel})


@login_required
def booking_success(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, "bookings/booking_success.html", {"booking": booking})


@login_required
def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    travel = booking.travel_option

    if travel.departure_datetime <= timezone.now():
        messages.error(
            request, "This booking cannot be cancelled after departure time."
        )
        return redirect("booking_list")

    booking.cancel()
    messages.success(request, "Your booking has been cancelled successfully.")

    return redirect("booking_cancelled")


@login_required
def booking_cancelled(request):
    return render(request, "bookings/booking_cancelled.html")
