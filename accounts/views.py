from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm, SignupForm
from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required


def Login(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')

    context={'form':form}
    return render(request, 'accounts/registration/login.html', context)

def Logout(request):
    logout(request)
    return redirect('login')


def SignUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
    else:
        form = SignupForm()
            

    context = {'form':form}
    return render(request, 'accounts/registration/register.html', context)


