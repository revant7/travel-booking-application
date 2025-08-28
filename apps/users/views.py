from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.views import LoginView


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        user = CustomUser.objects.create_user(
            username=username, email=email, password=password1
        )
        login(request, user)
        return redirect("dashboard")

    return render(request, "users/register.html")


class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request, "users/login.html")


@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")


@login_required
def profile(request):
    return render(request, "users/profile.html")


@login_required
def profile_edit(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.phone_number = request.POST.get("phone_number")
        user.address = request.POST.get("address")

        if request.FILES.get("profile_picture"):
            user.profile_picture = request.FILES["profile_picture"]

        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")

    return render(request, "users/profile_edit.html", {"user": request.user})


@login_required
def custom_logout(request):
    logout(request)
    return redirect("home")
