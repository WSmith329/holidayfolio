from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import HolidayDestinationForm
from ..models import Destination, Holiday, HolidayDestination

# Mixins
class HolidaySuccessUrlMixin:
    def get_success_url(self):
        return reverse_lazy('holiday-detail', kwargs={'slug': self.object.holiday.slug})

# Editing views
class HolidayDestinationCreateView(LoginRequiredMixin, HolidaySuccessUrlMixin, CreateView):
    model = HolidayDestination
    form_class = HolidayDestinationForm

    def get_holiday(self):
        return get_object_or_404(Holiday, slug=self.kwargs['holiday'], owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['holiday'] = self.get_holiday()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['holiday'] = self.get_holiday()
        return context

class HolidayDestinationUpdateView(LoginRequiredMixin, HolidaySuccessUrlMixin, UpdateView):
    model = HolidayDestination
    fields = ['arrival_date', 'departure_date']

class HolidayDestinationDeleteView(LoginRequiredMixin, HolidaySuccessUrlMixin, DeleteView):
    model = HolidayDestination