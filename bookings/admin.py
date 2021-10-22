""" Admin set-up for the bookings app"""
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Admin options for the Booking model """
    list_display = ('date', 'time', 'end_time', 'party_size')
