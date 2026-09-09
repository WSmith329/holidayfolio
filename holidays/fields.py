from django import forms
from django.db import models

class DatePickerField(models.DateField):
    def formfield(self, **kwargs):
        kwargs['widget'] = forms.DateInput(attrs={'type': 'date'})
        return super().formfield(**kwargs)