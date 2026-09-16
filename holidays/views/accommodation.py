from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
)

from ..models import Accommodation, HolidayDestination


# Mixins
class HolidaySuccessUrlMixin:
    def get_success_url(self):
        return reverse_lazy('holiday-detail', kwargs={'slug': self.holiday_destination.holiday.slug})


class HolidayDestinationMixin:
    """Looks up the HolidayDestination from the URL and exposes it as
    self.holiday_destination, both in context and for subclasses."""

    def dispatch(self, request, *args, **kwargs):
        self.holiday_destination = get_object_or_404(
            HolidayDestination, pk=kwargs['holiday_destination']
        )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['holiday_destination'] = self.holiday_destination
        return context


# Editing views
class AccommodationCreateView(LoginRequiredMixin, HolidaySuccessUrlMixin, HolidayDestinationMixin, CreateView):
    model = Accommodation
    fields = '__all__'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.holiday_destination.accommodation = self.object
        self.holiday_destination.save(update_fields=['accommodation'])
        return response


class AccommodationUpdateView(LoginRequiredMixin, HolidaySuccessUrlMixin, HolidayDestinationMixin, UpdateView):
    model = Accommodation
    fields = '__all__'

    def get_object(self, queryset=None):
        if self.holiday_destination.accommodation_id is None:
            raise Http404("This destination has no accommodation to update yet.")
        return self.holiday_destination.accommodation

class AccommodationDeleteView(LoginRequiredMixin, HolidaySuccessUrlMixin, HolidayDestinationMixin, DeleteView):
    model = Accommodation

    def get_object(self, queryset=None):
        if self.holiday_destination.accommodation_id is None:
            raise Http404("This destination has no accommodation to delete.")
        return self.holiday_destination.accommodation

    def form_valid(self, form):
        response = super().form_valid(form)
        self.holiday_destination.accommodation = None
        self.holiday_destination.save(update_fields=['accommodation'])
        return response