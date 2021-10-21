""" Views for the bookings app """
from django.shortcuts import render
from restaurant.models import Restaurant
from .forms import BookingForm
from .check_availability import create_booking_slots


def make_booking(request):
    """
    Bring up the booking form and make a booking
    """
    restaurant = Restaurant.objects.get(name="The Pizza Oven")
    slots = create_booking_slots(
        restaurant.opening_time, restaurant.closing_time)

    booking_form = BookingForm(slots)

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'bookings/make_booking.html', context)
