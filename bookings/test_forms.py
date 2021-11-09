""" Testcases for the bookings app forms. """
from django.test import TestCase
from restaurant.models import Restaurant
from .check_availability import create_booking_slots
from .forms import BookingForm


class TestBookingForm(TestCase):
    """ Tests for the booking form. """
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='The Pizza Oven')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Test to check the correct fields are listed in the form meta """
        slots = create_booking_slots(
            self.restaurant.opening_time, self.restaurant.closing_time)
        booking_id = ''
        form = BookingForm(slots, booking_id)
        self.assertEqual(
            form.Meta.fields,
            ('date', 'time', 'party_size', 'name', 'email',
             'phone_number', 'special_requirements'))
