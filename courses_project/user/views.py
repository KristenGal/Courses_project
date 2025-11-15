from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import RegistrationForm

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("course:list_courses")
    form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})

def profile_view(request):
    return render(request, "users/profile.html")