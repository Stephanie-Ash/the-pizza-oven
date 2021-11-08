import datetime
from django.test import TestCase
from .models import Booking


class TestModels(TestCase):
    def test_booking_string_method_includes_date_and_party_suze(self):
        booking = Booking.objects.create(
            date=datetime.date(2021, 11, 8), time=datetime.time(12, 00),
            party_size=4, name='Test Name', email='test@email.com',
            phone_number='01234567890')
        self.assertEqual(str(booking), 'A table of 4 on 08-11-2021')

    def test_booking_end_time_generated_on_save(self):
        booking = Booking.objects.create(
            date=datetime.date(2021, 11, 8), time=datetime.time(12, 00),
            party_size=4, name='Test Name', email='test@email.com',
            phone_number='01234567890')
        self.assertEqual(booking.end_time, datetime.time(14, 00))
