from django.contrib import admin
from .models import Holiday, Country, Destination

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'owner')
    search_fields = ('name', 'description', 'owner__username')
    list_filter = ('start_date', 'end_date')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'description', 'country__name')
    list_filter = ('country',)

admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Destination, DestinationAdmin)
