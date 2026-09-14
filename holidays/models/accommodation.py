from django.db import models


class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    check_in = models.TimeField()
    check_out = models.TimeField()
    booking_reference = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()
    accommodation_type