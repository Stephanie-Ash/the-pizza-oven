""" Forms for bookings """
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """ The booking form """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'party_size',
                  'name', 'email', 'phone_number', 'special_requirements')

    def __init__(self, slots, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.Select(choices=slots)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['special_requirements'].widget.attrs['placeholder'] = (
            'Let us know of any special dietary or other requirements.')
