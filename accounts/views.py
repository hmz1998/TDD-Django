from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import UserRegistrationForm, UserLoginForm


def register_user(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('accounts:login_page'))

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_page(request):
    form = UserLoginForm()
    return render(request, 'accounts/login.html')
