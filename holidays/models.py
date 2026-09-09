from django.db import models
from django.utils.text import slugify
from django.conf import settings

from .fields import DatePickerField

class Holiday(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    start_date = DatePickerField()
    end_date = DatePickerField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('planned', 'Planned'), ('upcoming', 'Upcoming'), ('completed', 'Completed')], default='planned')
    cover_image = models.ImageField(upload_to='holiday_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='holidays')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy('holiday-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name

class Destination(models.Model):
    holiday = models.ManyToManyField(Holiday, related_name='destinations', through='HolidayDestination')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='destinations')

    def __str__(self):
        return self.name

class HolidayDestination(models.Model):
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE, related_name='holiday_destinations')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='destination_holidays')
    arrival_date = DatePickerField(blank=True, null=True)
    departure_date = DatePickerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('holiday', 'destination')

    def __str__(self):
        return f"{self.holiday.name} - {self.destination.name}"