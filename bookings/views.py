""" Views for the bookings app """
import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from restaurant.models import Restaurant
from .models import Booking
from .forms import BookingForm, UpdateBookingForm
from .check_availability import create_booking_slots, find_tables


def make_booking(request):
    """
    Display the booking form and make a booking
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
            if request.user.is_authenticated:
                booking.customer = request.user
                booking.save()
            messages.success(request, 'Booking successfully made!')
            if request.user.is_superuser:
                return redirect(reverse('manage_bookings'))
            else:
                return redirect(reverse(
                    'booking_confirmed', args=[booking.id]))
        else:
            messages.error(
                request, 'Failed to make the booking. Please check the form.')
    else:
        booking_form = BookingForm(slots)

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'bookings/make_booking.html', context)


def booking_confirmed(request, booking_id):
    """
    Confirm a successful booking
    """
    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/booking_confirmed.html', context)


def manage_bookings(request):
    """
    Owner review and manage bookings
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this area is for the restaurant owner.')
        return redirect('home')

    bookings = Booking.objects.filter(date__gte=datetime.date.today())
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/manage_bookings.html', context)


def booking_detail(request, booking_id):
    """ A view to show individual booking details for the restaurant owner """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this area is for the restaurant owner.')
        return redirect('home')

    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/booking_detail.html', context)


def add_table_no(request, booking_id):
    """
    Add table numbers to the saved bookings
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only the restaurant owner can do this.')
        return redirect('home')

    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        table_numbers = request.POST.get('table_numbers')
        booking.table_numbers = table_numbers
        booking.save()
        return redirect(reverse('manage_bookings'))


def my_bookings(request):
    """
    Customer review and manage bookings
    """
    customer_bookings = Booking.objects.filter(
        customer__isnull=False, customer=request.user.id)
    bookings = customer_bookings.filter(date__gte=datetime.date.today())

    context = {
        'bookings': bookings
    }

    return render(request, 'bookings/my_bookings.html', context)


def update_booking(request, booking_id):
    restaurant = Restaurant.objects.get(name="The Pizza Oven")
    slots = create_booking_slots(
        restaurant.opening_time, restaurant.closing_time)

    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking_form = UpdateBookingForm(
            slots, data=request.POST, instance=booking)
        if booking_form.is_valid():
            if ('date' not in booking_form.changed_data and
                    'time' not in booking_form.changed_data and
                    'party_size' not in booking_form.changed_data):
                booking_form.save()
                messages.success(request, 'Booking successfully updated.')
                return redirect('manage_bookings')
            else:
                updated_data = booking_form.cleaned_data
                tables = find_tables(
                    updated_data['date'], updated_data['time'],
                    updated_data['booking_end'], updated_data['party_size'],
                    booking_id)
            if tables:
                booking.tables.clear()
                booking.table_numbers = ''
                if isinstance(tables, list):
                    booking_form.save()
                    booking.tables.set(tables)
                else:
                    booking_form.save()
                    booking.tables.add(tables)
                messages.success(request, 'Booking successfully updated.')
                return redirect('manage_bookings')
            else:
                messages.error(
                    request, 'Sorry no tables available at that time!')
        else:
            messages.error(
                request,
                'Failed to update the booking. Please check the form.')
    else:
        booking_form = BookingForm(slots, instance=booking)

    context = {
        'booking_form': booking_form,
        'booking': booking
    }
    return render(request, 'bookings/update_booking.html', context)


def delete_booking(request, booking_id):
    """
    Cancel a booking
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, 'Booking cancelled!')
    return redirect(reverse('manage_bookings'))
