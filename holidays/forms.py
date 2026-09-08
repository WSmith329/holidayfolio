from django import forms

from .models import Holiday, Destination, HolidayDestination, Country

class HolidayDestinationForm(forms.ModelForm):
    destination = forms.ModelChoiceField(queryset=Destination.objects.all(), required=False)
    new_destination_name = forms.CharField(required=False, label="Or create new destination")
    new_destination_country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        required=False,
        label="Country (for new destination)",
    )

    class Meta:
        model = HolidayDestination
        fields = ['destination', 'arrival_date', 'departure_date']

    def __init__(self, *args, holiday=None, **kwargs):
        if holiday is None:
            raise ValueError("HolidayDestinationForm requires a holiday instance")
        self.holiday = holiday
        super().__init__(*args, **kwargs)

        self.order_fields([
            'destination',
            'new_destination_name',
            'new_destination_country',
            'arrival_date',
            'departure_date'
        ])

    def get_initial(self):
        initial = super().get_initial()
        initial['order'] = HolidayDestination.objects.filter(holiday=self.get_holiday()).count()
        return initial

    def clean(self):
        cleaned_data = super().clean()
        destination = cleaned_data.get('destination')
        new_name = cleaned_data.get('new_destination_name')
        new_country = cleaned_data.get('new_destination_country')

        if not destination and not new_name:
            raise forms.ValidationError("Select an existing destination or provide a name for a new one.")
        if destination and new_name:
            raise forms.ValidationError("Choose either an existing destination or a new one, not both.")

        if new_name and not new_country:
            raise forms.ValidationError("Country is required when creating a new destination.")

        if not destination:
            new_name = new_name.strip()
            destination, _ = Destination.objects.get_or_create(
                name__iexact=new_name,
                country=new_country,
                defaults={'name': new_name},
            )
        cleaned_data['destination'] = destination
        print(destination.id)

        arrival = cleaned_data.get('arrival_date')
        departure = cleaned_data.get('departure_date')
        if arrival and departure and departure < arrival:
            raise forms.ValidationError("Departure date can't be before arrival date.")

        if HolidayDestination.objects.filter(holiday=self.holiday, destination=destination).exists():
            raise forms.ValidationError("This relation already exists.")

        return cleaned_data

    def save(self, commit=True):
        self.instance.holiday = self.holiday
        self.instance.destination = self.cleaned_data['destination']
        return super().save(commit=commit)