""" Set up booking slots and check for available tables """
from datetime import datetime, date, timedelta
from itertools import combinations, chain
from restaurant.models import Table


def create_booking_slots(opening_time, closing_time):
    """
    Create a list of 15 minute interval booking slots
    for use in the booking form
    """
    current_slot = datetime.combine(date.today(), opening_time)
    final_slot = datetime.combine(date.today(), closing_time) - timedelta(
        minutes=59)
    slot_interval = timedelta(minutes=15)
    booking_slots = []

    while current_slot < final_slot:
        booking_slots.append(current_slot)
        current_slot += slot_interval

    return [(slot.time(), slot.strftime('%H:%M')) for slot in booking_slots]


def find_tables(date, time, end_time, party_size):
    """ Search for available tables on the date and time of the booking """

    # Exclude any tables whose bookings overlap
    # the start time of the required booking
    check1 = Table.objects.exclude(
        bookings__date=date,
        bookings__time__lt=time,
        bookings__end_time__gt=time)

    # Exclude any tables whose bookings overlap
    # the end time of the required booking
    check2 = check1.exclude(
        bookings__date=date,
        bookings__time__lt=end_time,
        bookings__end_time__gt=end_time)

    # Exclude any tables whose bookings span the required booking
    # booking length is fixed at 2 hours so there will be no bookings
    # within the time range
    available_tables = check2.exclude(
        bookings__date=date,
        bookings__time__lte=time,
        bookings__end_time__gte=end_time)

    # If there are any tables left after the checks
    # we need to select one or more for the booking
    if available_tables:
        return select_single_table(available_tables, party_size)
