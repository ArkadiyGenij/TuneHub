from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginForm, RegisterForm
from users.models import User


# Create your views here.
class LoginPage(LoginView):
    form_class = LoginForm
    extra_context = {'title': 'TuneHub | Авторизация'}


class RegistrationPage(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'TuneHub | Регистрация'}
