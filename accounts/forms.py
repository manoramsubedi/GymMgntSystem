from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import PasswordInput, TextInput

#from .models import Record

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User   #build-in model
#         fields = ['username', 'password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name' ,'email', 'username', 'password1', 'password2']