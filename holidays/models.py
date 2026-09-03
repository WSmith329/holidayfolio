from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Holiday(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
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
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE, related_name='destinations')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='destinations')

    def __str__(self):
        return f"{self.name} ({self.holiday.name})"