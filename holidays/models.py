from django.db import models

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

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"
