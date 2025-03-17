from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import RegistrationForm, customRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def sign_up(request):
    form = customRegistrationForm()

    if request.method == 'POST':
        form = customRegistrationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form': form}

    return render(request, 'registration/register.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')


    return render(request, 'registration/login.html')

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')