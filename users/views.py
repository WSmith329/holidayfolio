from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "users/user_create.html"
    success_url = reverse_lazy('login')

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile

    def get_object(self):
        return self.request.user.profile
