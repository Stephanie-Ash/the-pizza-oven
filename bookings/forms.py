""" Forms for bookings """
import datetime
from django import forms

from .models import Booking
from .check_availability import find_tables


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

    def clean(self):
        cleaned_data = super().clean()
        planned_date = cleaned_data.get('date')
        planned_time = cleaned_data.get('time')
        planned_party_size = cleaned_data.get('party_size')

        end = datetime.datetime.combine(
            datetime.date.today(), planned_time) + datetime.timedelta(hours=2)
        booking_end = end.time()

        current_booking_id = ''

        tables = find_tables(
            planned_date, planned_time, booking_end, planned_party_size, current_booking_id)

        if tables:
            cleaned_data['tables'] = tables
        else:
            raise forms.ValidationError(
                "Sorry no tables available at that time!"
            )

        return cleaned_data


class UpdateBookingForm(forms.ModelForm):
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

    def clean(self):
        cleaned_data = super().clean()
        planned_time = cleaned_data.get('time')

        end = datetime.datetime.combine(
            datetime.date.today(), planned_time) + datetime.timedelta(hours=2)
        booking_end = end.time()

        cleaned_data['booking_end'] = booking_end

        return cleaned_data
