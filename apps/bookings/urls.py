from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_list, name="booking_list"),
    path("<int:pk>/cancel/", views.booking_cancel, name="booking_cancel"),
    path("<int:travel_id>/checkout/", views.checkout, name="booking_create"),
    path("success/<int:pk>/", views.booking_success, name="booking_success"),
    path("cancelled/", views.booking_cancelled, name="booking_cancelled"),
]
