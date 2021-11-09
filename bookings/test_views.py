""" Testcases for the restaurant app views. """
from django.test import TestCase
from restaurant.models import Restaurant


class TestViews(TestCase):
    """ Tests for the views. """
    def test_get_make_booking_page(self):
        """ Test the get make booking page view. """
        Restaurant.objects.create(name='The Pizza Oven')
        response = self.client.get('/bookings/make_booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/make_booking.html')
