from django.db import models
from django.utils.translation import gettext_lazy as _


class Accommodation(models.Model):
    class AccommodationType(models.TextChoices):
        HOTEL = "HOT", _("Hotel")
        HOSTEL = "HOS", _("Hostel")
        RESORT = "RES", _("Resort")
        APARTMENT = "APA", _("Apartment")
        BNB = "BNB", _("Bed and Breakfast") 
        HOMESTAY = "HOM", _("Homestay")
        GLAMPING = "GLA", _("Glamping")
        CAMPSITE = "CAM", _("Campsite")
        CARAVAN = "CAR", _("Caravan")
        CABIN = "CAB", _("Cabin")

    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    check_in = models.TimeField()
    check_out = models.TimeField()
    booking_reference = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()
    accommodation_type = models.CharField(max_length=3, choices=AccommodationType, default=AccommodationType.HOTEL)
    notes = models.TextField(blank=True, null=True)