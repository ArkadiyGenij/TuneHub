from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import LoginPage, RegistrationPage

app_name = 'users'

urlpatterns = [
    path('login', LoginPage.as_view(template_name='users/login.html'), name='login'),
    path('registration', RegistrationPage.as_view(template_name='users/registration.html'), name='registration'),
    path('logout', LogoutView.as_view(), name='logout'),
]
