from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, UpdateUserForm


# Register view
def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(request, "Registration successful.")

            return redirect("profile")

    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


# Profile view
@login_required
def profile_view(request):

    if request.method == "POST":

        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():

            form.save()

            messages.success(request, "Profile updated successfully.")

            return redirect("profile")

    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})


# Logout view
def logout_view(request):

    logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("login")
