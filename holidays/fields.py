from django import forms
from django.db import models


class DatePickerField(models.DateField):
    """DateField with DateInput widget set as default form widget."""
    def formfield(self, **kwargs):
        kwargs['widget'] = forms.DateInput(attrs={'type': 'date'})
        return super().formfield(**kwargs)


class TimePickerField(models.TimeField):
    """TimeField with TimeInput widget set as default form widget."""
    def formfield(self, **kwargs):
        kwargs['widget'] = forms.TimeInput(attrs={'type': 'time'})
        return super().formfield(**kwargs)