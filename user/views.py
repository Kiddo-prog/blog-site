from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UpdateProfileForm
from django.urls import reverse_lazy

# from django.contrib import messages
from django.contrib.auth.views import LoginView


@login_required
def profile(request):
    return render(request, "profile/profile.html", {})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:article-list")
    else:
        form = UserRegisterForm()
    return render(request, "auth/register.html", {"form": form})


class LoginUsers(LoginView):
    template_name = "auth/login.html"


# install django-cors-header for cors policy


def update_profile(request):
    if request.method == "POST":
        update_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse_lazy("users:profile"))
    else:
        update_form = UpdateProfileForm(instance=request.user.profile)
    context = {"title": "Profile Edit", "profile_form": update_form}
    return render(request, "profile/profile_edit.html", context)
