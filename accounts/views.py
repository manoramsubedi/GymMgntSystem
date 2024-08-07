from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import LoginForm, SignupForm, ProfileForm
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


def UserDashboard(request):
    return render(request, 'accounts/dashboard.html')

#edit form
@login_required
def update_profile(request):
    if request.method=="POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            #msg='Profile updated successfully!'

    form = ProfileForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/update-profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in after password change
            messages.success(request, 'Your password has been successfully changed.')
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request, 'accounts/registration/change_password.html', context)

