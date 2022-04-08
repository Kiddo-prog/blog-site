from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "info"]


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"label": "Name", "placeholder": "Name here"}),
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"label": "Email", "placeholder": "Email here..."}
        ),
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={"label": "Subject", "placeholder": "Subject here..."}
        ),
        required=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "label": "Message",
                "placeholder": "Message",
                "class": "contact_form",
            },
        ),
        required=False,
    )