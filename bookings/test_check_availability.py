""" Testcases for the check availability functions """
import datetime
from django.test import TestCase
from restaurant.models import Restaurant, Table
from .models import Booking
from .check_availability import find_tables


class TestCheckAvailability(TestCase):
    """ Tests for the available table searches. """
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='The Pizza Oven')
        self.table1 = Table.objects.create(restaurant=self.restaurant, size=2)
        self.table2 = Table.objects.create(restaurant=self.restaurant, size=4)
        self.table3 = Table.objects.create(restaurant=self.restaurant, size=2)
        self.table4 = Table.objects.create(restaurant=self.restaurant, size=4)
        self.table5 = Table.objects.create(restaurant=self.restaurant, size=2)
        self.table6 = Table.objects.create(restaurant=self.restaurant, size=4)
        self.table7 = Table.objects.create(restaurant=self.restaurant, size=2)
        self.table8 = Table.objects.create(restaurant=self.restaurant, size=4)

    def test_smallest_single_table_chosen(self):
        """
        Test that the smallest available table is chosen when no table
        combination is required.
        """
        selected_table1 = find_tables(
            datetime.date.today(), datetime.time(18, 00),
            datetime.time(20, 00), 1, '')
        self.assertEqual(selected_table1.size, 2)

        selected_table2 = find_tables(
            datetime.date.today(), datetime.time(18, 00),
            datetime.time(20, 00), 2, '')
        self.assertEqual(selected_table2.size, 2)

        selected_table3 = find_tables(
            datetime.date.today(), datetime.time(18, 00),
            datetime.time(20, 00), 3, '')
        self.assertEqual(selected_table3.size, 4)

        selected_table4 = find_tables(
            datetime.date.today(), datetime.time(18, 00),
            datetime.time(20, 00), 4, '')
        self.assertEqual(selected_table4.size, 4)

    def test_smallest_table_combination_chosen(self):
        """
        Test that when the tables are combined the smallest number
        of tables are used and that the combined tables have the
        smallest amount of leftover space.
        """
        selected_tables1 = find_tables(
            datetime.date.today(), datetime.time(18, 00),
            datetime.time(20, 00), 5, '')
        tables1_sizes = [table.size for table in selected_tables1]
        self.assertEqual(tables1_sizes, [2, 4])

        selected_tables2 = find_tables(
            datetime.date.today(), datetime.time(18, 00),
            datetime.time(20, 00), 7, '')
        tables2_sizes = [table.size for table in selected_tables2]
        self.assertEqual(tables2_sizes, [4, 4])
