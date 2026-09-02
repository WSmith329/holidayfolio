from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "users/user_create.html"
    success_url = reverse_lazy('login')
