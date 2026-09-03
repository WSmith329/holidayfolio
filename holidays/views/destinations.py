from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Destination, Holiday

# Mixins
class HolidaySuccessUrlMixin:
    def get_success_url(self):
        return reverse_lazy('holiday-detail', kwargs={'slug': self.object.holiday.slug})

# Display views
class DestinationDetailView(LoginRequiredMixin, DetailView):
    model = Destination

# Editing views
class DestinationCreateView(LoginRequiredMixin, HolidaySuccessUrlMixin, CreateView):
    model = Destination
    fields = ['name', 'description', 'image', 'country']

    def form_valid(self, form):
        form.instance.holiday = Holiday.objects.get(slug=self.kwargs['holiday'])
        return super().form_valid(form)

class DestinationUpdateView(LoginRequiredMixin, HolidaySuccessUrlMixin, UpdateView):
    model = Destination
    fields = ['name', 'description', 'image', 'country']

class DestinationDeleteView(LoginRequiredMixin, HolidaySuccessUrlMixin, DeleteView):
    model = Destination
