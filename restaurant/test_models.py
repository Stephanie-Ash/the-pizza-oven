import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Restaurant, Table


class TestModels(TestCase):
    def test_restaurant_string_method_returns_name(self):
        restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.assertEqual(str(restaurant), 'Test Restaurant')

    def test_table_string_method_returns_string_including_size(self):
        restaurant = Restaurant.objects.create(name='Test Restaurant')
        table = Table.objects.create(restaurant=restaurant, size=2)
        self.assertEqual(str(table), 'A table of 2 people size')

    def test_restaurant_closing_time_must_be_later_than_opening_time(self):
        open_time = datetime.time(11, 00, 00)
        close_time = datetime.time(10, 00, 00)
        restaurant = Restaurant.objects.create(
            name='Test Restaurant', opening_time=open_time, closing_time=close_time)
        self.assertRaises(ValidationError, restaurant.clean)
