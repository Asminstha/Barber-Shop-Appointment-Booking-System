from django import forms
from .models import Appointment
from django.utils import timezone
from datetime import datetime, timedelta

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['customer_name', 'service', 'date', 'time', 'notes']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'service': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'min': (timezone.now().date() + timedelta(days=2)).isoformat(),
                'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'min': '10:00',
                'max': '18:00',
                'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-black'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            appointment_datetime = datetime.combine(date, time)
            appointment_datetime = timezone.make_aware(appointment_datetime)

            # Minimum booking 2 days from now
            min_datetime = timezone.now() + timedelta(days=2)

            if appointment_datetime < min_datetime:
                raise forms.ValidationError(
                    "Appointments must be booked at least 2 days in advance."
                )

        return cleaned_data
