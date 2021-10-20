""" Set up booking slots and check for available tables """
from datetime import datetime, date, timedelta


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
