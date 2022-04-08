from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LogoutView
from user import views as user_view

app_name = "users"

urlpatterns = [
    path(
        "login/",
        user_view.LoginUsers.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="auth/logout.html"),
        name="logout",
    ),
    path("profile/", user_view.profile, name="profile"),
    path("register/", user_view.register, name="register"),
    path(
        "profile/edit",
        user_view.update_profile,
        name="profile_edit",
    ),
]