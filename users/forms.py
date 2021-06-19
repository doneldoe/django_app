from django import forms
from .models import Profile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    agree_text = 'Я соглашаюсь с условиями и даю свое согласие на обработку и использование моих персональных данных ' \
                 'и разрешаю сделать запрос в бюро кредитных историй '

    last_name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Фамилия'})
    )

    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )

    patronymic = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Отчество'})
    )

    CHOICES = [('М', 'Мужской'),
               ('Ж', 'Женский')]

    sex = forms.ChoiceField(
        label='Пол',
        choices=CHOICES,
        widget=forms.RadioSelect()
    )

    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Электронная почта'})
    )

    phone_number = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Мобильный телефон'})
    )

    agree = forms.BooleanField(
        label='',
        help_text=agree_text
    )

    passport_image = forms.ImageField(label='Фотография паспорта')

    cam_image = forms.ImageField(label='Ваша фотография')

    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'patronymic', 'sex', 'email', 'phone_number', 'agree', 'passport_image',
                  'cam_image', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    error_messages = {
        'invalid_login': _(
            "Ваша фотография не совпадает с владельцем данного аккаунта"
        )
    }
    username = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Электронная почта'
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль'
            }
        )
    )
