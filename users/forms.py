from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    username = forms.CharField(label=("Nazwa użytkownika"))
    password1 = forms.CharField(label=("Hasło"), widget=forms.PasswordInput, help_text=("Hasło musi zawierać co najmniej 8 liter"))
    password2 = forms.CharField(label=("Powtórz hasło"), help_text=("Powtórz powyższe hasło"), widget=forms.PasswordInput)
