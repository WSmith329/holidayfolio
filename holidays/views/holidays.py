from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Holiday

# Display views
class HolidayListView(LoginRequiredMixin, ListView):
    model = Holiday

    def get_queryset(self):
        return Holiday.objects.filter(owner=self.request.user)

class HolidayDetailView(LoginRequiredMixin, DetailView):
    model = Holiday

# Editing views
class HolidayCreateView(LoginRequiredMixin, CreateView):
    model = Holiday
    fields = ['name', 'start_date', 'end_date', 'description', 'cover_image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class HolidayUpdateView(LoginRequiredMixin, UpdateView):
    model = Holiday
    fields = ['name', 'start_date', 'end_date', 'description', 'cover_image']

class HolidayDeleteView(LoginRequiredMixin, DeleteView):
    model = Holiday
    success_url = reverse_lazy('holiday-list')
