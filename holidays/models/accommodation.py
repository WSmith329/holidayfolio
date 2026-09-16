from django.db import models
from django.utils.translation import gettext_lazy as _

from ..fields import TimePickerField


class Accommodation(models.Model):
    class Type(models.TextChoices):
        HOTEL = "HOT", _("Hotel")
        HOSTEL = "HOS", _("Hostel")
        RESORT = "RES", _("Resort")
        APARTMENT = "APA", _("Apartment / Flat")
        BNB = "BNB", _("Bed and Breakfast") 
        HOMESTAY = "HOM", _("Homestay / Guesthouse")
        GLAMPING = "GLA", _("Glamping")
        CAMPSITE = "CAM", _("Campsite")
        CARAVAN = "CAR", _("Caravan")
        CABIN = "CAB", _("Cabin")

    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    check_in = TimePickerField(blank=True, null=True)
    check_out = TimePickerField(blank=True, null=True)
    booking_reference = models.CharField(max_length=30, blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=3, choices=Type, default=Type.HOTEL)
    notes = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='accommodation_covers/')