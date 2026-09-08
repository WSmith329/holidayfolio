from django.urls import reverse_lazy

# Mixins
class HolidaySuccessUrlMixin:
    def get_success_url(self):
        return reverse_lazy('holiday-detail', kwargs={'slug': self.object.holiday.slug})