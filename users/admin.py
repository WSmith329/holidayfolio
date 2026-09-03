from django.contrib import admin
from django.conf import settings
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date')
    search_fields = ('user__username',)
    list_filter = ('birth_date',)

admin.site.register(Profile, ProfileAdmin)
