from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    passport_image = forms.ImageField()
    cam_image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'passport_image', 'cam_image', 'password1', 'password2']
