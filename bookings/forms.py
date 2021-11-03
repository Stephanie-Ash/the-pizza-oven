""" Forms for making or updating bookings """
import datetime
from django import forms

from .models import Booking
from .check_availability import find_tables


class BookingForm(forms.ModelForm):
    """ The form for making or updating a booking """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'party_size',
                  'name', 'email', 'phone_number', 'special_requirements')

    def __init__(self, slots, booking_id, *args, **kwargs):
        # Get the id for the original booking for use in the table search
        # If a booking is being made not updated the id will be an empty string
        self.form_booking_id = booking_id

        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.Select(choices=slots)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['special_requirements'].widget.attrs['placeholder'] = (
            'Let us know of any special dietary or other requirements.')

    # Check for available tables in form validation
    def clean(self):
        cleaned_data = super().clean()
        planned_date = cleaned_data.get('date')
        planned_time = cleaned_data.get('time')
        planned_party_size = cleaned_data.get('party_size')
        current_booking_id = self.form_booking_id

        end = datetime.datetime.combine(
            datetime.date.today(), planned_time) + datetime.timedelta(hours=2)
        booking_end = end.time()

        tables = find_tables(
            planned_date, planned_time, booking_end, planned_party_size,
            current_booking_id)

        # Make the selected table(s) available to the view or
        # raise a validation error if none available
        if tables:
            cleaned_data['tables'] = tables
        else:
            raise forms.ValidationError(
                "Sorry no tables available at that time!"
            )

        return cleaned_data
