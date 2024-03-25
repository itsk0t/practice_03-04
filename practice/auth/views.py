from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from auth.forms import RegisterUserForm, LoginUserForm


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('auth:login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('doc:doc_list')