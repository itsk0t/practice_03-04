from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Логин'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control w-75', 'placeholder': 'Email-адрес'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control w-75', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control w-75', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder':'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control w-75', 'placeholder':'Пароль'}))