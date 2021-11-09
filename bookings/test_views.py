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
        self.user = User.objects.create_superuser(
            'admin', 'admin@email.com', 'adminpassword')

        self.restaurant = Restaurant.objects.create(name='The Pizza Oven')
        self.table = Table.objects.create(restaurant=self.restaurant, size=2)
        self.booking = Booking.objects.create(
            name='Test Name', email='test@email.com',
            phone_number='01234567890')
        self.booking.tables.add(self.table)

    def test_get_make_booking_page(self):
        """ Test the get make booking page view. """
        response = self.client.get('/bookings/make_booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/make_booking.html')

    def test_get_booking_confirmed_page(self):
        """ Test the get booking confirmed page view. """
        response = self.client.get(
            f'/bookings/booking_confirmed/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_confirmed.html')

    def test_get_manage_bookings_page(self):
        """ Test the get manage bookings page view. """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get('/bookings/manage_bookings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/manage_bookings.html')

    def test_get_booking_detail_page(self):
        """ Test the get booking detail page view. """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(
            f'/bookings/booking_detail/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_detail.html')

    def test_get_my_bookings_page(self):
        """ Test the get booking my bookings page view. """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get('/bookings/my_bookings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')

    def test_get_update_booking_page(self):
        """ Test the get update booking page view. """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(
            f'/bookings/update_booking/{self.booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/update_booking.html')
