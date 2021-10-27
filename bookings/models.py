""" models for the bookings app """
from datetime import datetime, date, time, timedelta
from django.db import models

from restaurant.models import Table


class Booking(models.Model):
    """ Bookings model to book tables in the restaurant"""

    # Limit maximum bookings to 8 people.
    # Larger bookings can be handled in person with the restaurant.
    PARTY_SIZE_CHOICES = [
        (1, '1 person'),
        (2, '2 people'),
        (3, '3 people'),
        (4, '4 people'),
        (5, '5 people'),
        (6, '6 people'),
        (7, '7 people'),
        (8, '8 people'),
    ]

    date = models.DateField(
        auto_now=False, auto_now_add=False, default=date.today)
    time = models.TimeField(
        auto_now=False, auto_now_add=False, default=time(18, 00))
    end_time = models.TimeField(
        auto_now=False, auto_now_add=False, editable=False)
    party_size = models.IntegerField(choices=PARTY_SIZE_CHOICES, default=2)
    tables = models.ManyToManyField(Table, related_name='bookings')
    table_numbers = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    special_requirements = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date', '-time']

    def _generate_end_time(self):
        end_time = (
            datetime.combine(date.today(), self.time)) + timedelta(hours=2)
        return end_time.time()

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = self._generate_end_time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"A table of {self.party_size} on {self.date}"
