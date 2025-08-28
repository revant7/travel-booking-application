from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import TravelOption
from django.utils import timezone


def travel_list(request):
    travels = TravelOption.objects.filter(departure_datetime__gte=timezone.now())

    source = request.GET.get("source")
    destination = request.GET.get("destination")
    date = request.GET.get("date")
    t_type = request.GET.get("type")

    if source:
        travels = travels.filter(source__icontains=source)
    if destination:
        travels = travels.filter(destination__icontains=destination)
    if t_type:
        travels = travels.filter(type=t_type)
    if date:
        travels = travels.filter(departure_datetime__date=date)

    context = {
        "travel_options": travels,
        "source": source or "",
        "destination": destination or "",
        "selected_type": t_type or "",
        "date": date or "",
    }
    return render(request, "travel/travel_list.html", context)


def travel_detail(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    return render(request, "travel/travel_detail.html", {"travel": travel})
