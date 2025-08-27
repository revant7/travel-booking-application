from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")


def about(request):
    return render(request, "about.html")


def terms(request):
    return render(request, "terms.html")


def privacy(request):
    return render(request, "privacy.html")


def offers(request):
    return render(request, "offers.html")
