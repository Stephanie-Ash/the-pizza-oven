from django.test import TestCase
from .models import Restaurant, Table


class TestModels(TestCase):
    def test_restaurant_string_method_returns_name(self):
        restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.assertEqual(str(restaurant), 'Test Restaurant')

    def test_table_string_method_returns_string_including_size(self):
        restaurant = Restaurant.objects.create(name='Test Restaurant')
        table = Table.objects.create(restaurant=restaurant, size=2)
        self.assertEqual(str(table), 'A table of 2 people size')
