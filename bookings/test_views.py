""" Testcases for the restaurant app views. """
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from restaurant.models import Restaurant, Table
from .models import Booking


class TestViews(TestCase):
    """ Tests for the views. """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin', 'admin@email.com', 'adminpassword')

    def test_get_make_booking_page(self):
        """ Test the get make booking page view. """
        Restaurant.objects.create(name='The Pizza Oven')
        response = self.client.get('/bookings/make_booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/make_booking.html')

    def test_get_booking_confirmed_page(self):
        """ Test the get booking confirmed page view. """
        restaurant = Restaurant.objects.create(name='The Pizza Oven')
        table = Table.objects.create(restaurant=restaurant, size=2)
        booking = Booking.objects.create(
            name='Test Name', email='test@email.com',
            phone_number='01234567890')
        booking.tables.add(table)
        response = self.client.get(f'/bookings/booking_confirmed/{booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_confirmed.html')

    def test_get_manage_bookings_page(self):
        """ Test the get manage bookings page view. """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get('/bookings/manage_bookings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/manage_bookings.html')
