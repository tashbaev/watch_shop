from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')


class LogInView(LoginView):
    model = CustomUser
    template_name = 'login.html'
    redirect_field_name = reverse_lazy('home')


