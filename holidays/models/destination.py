from django.db import models

from holidays.fields import DatePickerField
from holidays.models import Country
from holidays.models.holiday import Holiday


class Destination(models.Model):
    holiday = models.ManyToManyField(Holiday, related_name='destinations', through='HolidayDestination')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='destinations')
    accommodation = models.ForeignKey

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