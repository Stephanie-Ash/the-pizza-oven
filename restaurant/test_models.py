""" Testcases for the restaurant app models. """
import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Restaurant, Table


class TestModels(TestCase):
    """ Tests for the models. """
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')

    def test_restaurant_string_method_returns_name(self):
        """ Test the Restaurant model string method. """
        self.assertEqual(str(self.restaurant), 'Test Restaurant')

    def test_table_string_method_returns_string_including_size(self):
        """ Test the Table model string method. """
        table = Table.objects.create(restaurant=self.restaurant, size=2)
        self.assertEqual(str(table), 'A table of 2 people size')

    def test_restaurant_closing_time_must_be_later_than_opening_time(self):
        """ Test the restaurant model custom clean method. """
        open_time = datetime.time(11, 00, 00)
        close_time = datetime.time(10, 00, 00)
        self.restaurant.opening_time = open_time
        self.restaurant.closing_time = close_time
        self.assertRaises(ValidationError, self.restaurant.clean)
