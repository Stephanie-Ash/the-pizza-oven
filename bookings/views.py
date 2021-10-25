""" Views for the bookings app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from restaurant.models import Restaurant
from .models import Booking
from .forms import BookingForm
from .check_availability import create_booking_slots


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
            tables = booking_form.cleaned_data['tables']
            booking = booking_form.save()
            if isinstance(tables, list):
                booking.tables.set(tables)
            else:
                booking.tables.add(tables)
            messages.success(request, 'Booking successfully made!')
            return redirect(reverse('booking_confirmed', args=[booking.id]))
        else:
            messages.error(
                request, 'Failed to make booking. Please check the form.')
    else:
        booking_form = BookingForm(slots)

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'bookings/make_booking.html', context)


def booking_confirmed(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/booking_confirmed.html', context)
