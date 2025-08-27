from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

# Create your views here.


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")

        if not name or not email or not message_text:
            messages.error(request, "All fields are required.")
        else:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")

    return render(request, "pages/contact.html")
