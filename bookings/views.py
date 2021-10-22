""" Views for the bookings app """
from django.shortcuts import render, redirect
from django.contrib import messages
from restaurant.models import Restaurant
from .forms import BookingForm
from .check_availability import create_booking_slots, find_tables


def make_booking(request):
    """
    Bring up the booking form and make a booking
    """
    restaurant = Restaurant.objects.get(name="The Pizza Oven")
    slots = create_booking_slots(
        restaurant.opening_time, restaurant.closing_time)

    if request.method == 'POST':
        booking_form = BookingForm(slots, data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save()
            tables = find_tables(
                booking.date, booking.time, booking.end_time,
                booking.party_size
            )
            if isinstance(tables, list):
                booking.tables.set(tables)
                booking.save()
            else:
                booking.tables.add(tables)
                booking.save()
            messages.success(request, 'Booking successfully made!')
            return redirect('make_booking')
        else:
            messages.error(
                request, 'Failed to make booking. Pleas check the form.')
    else:
        booking_form = BookingForm(slots)

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'bookings/make_booking.html', context)
