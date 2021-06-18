from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from .forms import UserRegistrationForm
from .utils import verify


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            passport_image = form.cleaned_data.get('passport_image')
            cam_image = form.cleaned_data.get('cam_image')
            if verify(passport_image, cam_image)[0]:
                form.save()
                email = form.cleaned_data.get('email')
                messages.success(request, f'Аккаунт {email} создан!')
                return redirect('login')
            else:
                messages.warning(request, _('Лица на фотографиях не совпадают!'))
                return redirect('registration')
        else:
            messages.warning(request, _('Ошибка!'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
