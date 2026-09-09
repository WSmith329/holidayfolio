from urllib.parse import urlparse

from django.shortcuts import render
from django.urls import reverse_lazy, resolve, Resolver404
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Destination, Holiday

# Mixins
class DestinationSuccessUrlMixin:
    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')

        if next_url and url_has_allowed_host_and_scheme(
            next_url, allowed_hosts={self.request.get_host()}
        ):
            path = urlparse(next_url).path
            try:
                match = resolve(path)
                if match.url_name == 'holiday-destination-update':
                    return next_url
            except Resolver404:
                pass

        return reverse_lazy('holiday-list')

# Display views
class DestinationDetailView(LoginRequiredMixin, DetailView):
    model = Destination

# Editing views
# DestinationCreateView is removed as destination creation is only handled in HolidayDestinationCreateView.

class DestinationUpdateView(LoginRequiredMixin, DestinationSuccessUrlMixin, UpdateView):
    model = Destination
    fields = ['name', 'description', 'image', 'country']

class DestinationDeleteView(LoginRequiredMixin, DestinationSuccessUrlMixin, DeleteView):
    model = Destination
