from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Username', 'id': 'username', 'name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Contraseña', 'id': 'password', 'name': 'password'}))
