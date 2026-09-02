from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Holiday

# Display views
class HolidayListView(ListView):
    model = Holiday

    def get_queryset(self):
        return Holiday.objects.filter(owner=self.request.user)

class HolidayDetailView(DetailView):
    model = Holiday

# Editing views
class HolidayCreateView(CreateView):
    model = Holiday
    fields = ['name', 'start_date', 'end_date', 'description', 'cover_image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class HolidayUpdateView(UpdateView):
    model = Holiday
    fields = ['name', 'start_date', 'end_date', 'description', 'cover_image']

class HolidayDeleteView(DeleteView):
    model = Holiday
    success_url = reverse_lazy('holiday-list')
