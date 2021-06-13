from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
