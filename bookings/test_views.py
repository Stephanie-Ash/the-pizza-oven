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
        self.superuser = User.objects.create_superuser(
            'admin', 'admin@email.com', 'adminpassword')
        self.user = User.objects.create_user(
            'john', 'john@email.com', 'johnpassword')

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

    def test_can_delete_booking_user(self):
        """ Test that the delete booking view deletes a booking. """

        # Test for a standard user.
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(
            f'/bookings/delete_booking/{self.booking.id}')
        self.assertRedirects(response, '/bookings/my_bookings')
        existing_bookings = Booking.objects.filter(id=self.booking.id)
        self.assertEqual(len(existing_bookings), 0)

    def test_can_delete_booking_superuser(self):
        """ Test that the delete booking view redirects. """

        # Test the redirect for a superuser
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(
            f'/bookings/delete_booking/{self.booking.id}')
        self.assertRedirects(response, '/bookings/manage_bookings')

    def test_can_toggle_updated(self):
        """
        Test that the toggle updated view changes the value
        of the updated field.
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(
            f'/bookings/toggle_updated/{self.booking.id}')
        self.assertRedirects(response, '/bookings/manage_bookings')
        updated_booking = Booking.objects.get(id=self.booking.id)
        self.assertFalse(updated_booking.updated)

    def test_can_add_table_no(self):
        """
        Test that the add table no view sets the
        table numbers field.
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            f'/bookings/add_table_no/{self.booking.id}',
            {'table_numbers': '20'})
        self.assertRedirects(response, '/bookings/manage_bookings')
        updated_booking = Booking.objects.get(id=self.booking.id)
        self.assertEqual(updated_booking.table_numbers, '20')

    def test_the_restaurant_owner_areas_redirect_standard_users(self):
        """
        Test that views that only allow access by a superuser
        redirect a normal user to the homepage.
        """
        # From https://stackoverflow.com/questions/16143149/
        # manage bookings
        self.client.login(username='john', password='johnpassword')
        manage = self.client.get('/bookings/manage_bookings', follow=True)
        self.assertRedirects(manage, '/')
        msg_manage = list(manage.context.get('messages'))[0]
        self.assertEqual(
            msg_manage.message, 'Sorry this area is for the restaurant owner.')

        # booking detail
        detail = self.client.get(
            f'/bookings/booking_detail/{self.booking.id}', follow=True)
        self.assertRedirects(detail, '/')
        msg_detail = list(detail.context.get('messages'))[0]
        self.assertEqual(
            msg_detail.message, 'Sorry this area is for the restaurant owner.')

        # toggle updated
        toggle = self.client.get(
            f'/bookings/toggle_updated/{self.booking.id}', follow=True)
        self.assertRedirects(toggle, '/')
        msg_toggle = list(toggle.context.get('messages'))[0]
        self.assertEqual(
            msg_toggle.message, 'Sorry only the restaurant owner can do this.')

        add_no = self.client.post(
            f'/bookings/add_table_no/{self.booking.id}',
            {'table_numbers': '20'}, follow=True)
        self.assertRedirects(add_no, '/')
        msg_add_no = list(add_no.context.get('messages'))[0]
        self.assertEqual(
            msg_add_no.message, 'Sorry only the restaurant owner can do this.')
